from fastapi import FastAPI, Query
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./thor.db")
engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, future=True)
app = FastAPI(title="Thor Backend")

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/listings")
def listings(city: str | None = None, q: str | None = None, min_price: int | None = Query(default=None), max_price: int | None = Query(default=None)):
    sql = "SELECT id, title, city, price, rooms, area, source, url FROM listings WHERE 1=1"
    params = {}
    if city:
        sql += " AND lower(city) LIKE :city"
        params['city'] = f"%{city.lower()}%"
    if q:
        sql += " AND (lower(title) LIKE :q OR lower(source) LIKE :q)"
        params['q'] = f"%{q.lower()}%"
    if min_price is not None:
        sql += " AND price >= :min_price"
        params['min_price'] = min_price
    if max_price is not None:
        sql += " AND price <= :max_price"
        params['max_price'] = max_price
    with SessionLocal() as s:
        rows = s.execute(text(sql), params).mappings().all()
        return [dict(r) for r in rows]