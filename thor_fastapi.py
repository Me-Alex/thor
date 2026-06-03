from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Thor API")

class Listing(BaseModel):
    id: int
    title: str
    city: str
    price: int
    rooms: int
    area: float
    source: str
    url: str

LISTINGS = [
    Listing(id=1, title="2-room apartment, Pipera", city="Bucharest", price=119000, rooms=2, area=58, source="Storia", url="https://example.com/1"),
    Listing(id=2, title="Villa with garden, Voluntari", city="Bucharest", price=345000, rooms=5, area=220, source="Imobiliare.ro", url="https://example.com/2"),
    Listing(id=3, title="Studio, Tineretului", city="Bucharest", price=73500, rooms=1, area=34, source="Publi24", url="https://example.com/3"),
]

@app.get('/health')
def health():
    return {"ok": True, "service": "Thor"}

@app.get('/listings', response_model=list[Listing])
def get_listings(city: Optional[str] = None, q: Optional[str] = None, min_price: Optional[int] = Query(default=None), max_price: Optional[int] = Query(default=None)):
    items = LISTINGS
    if city:
        items = [x for x in items if city.lower() in x.city.lower()]
    if q:
        ql = q.lower()
        items = [x for x in items if ql in x.title.lower() or ql in x.source.lower()]
    if min_price is not None:
        items = [x for x in items if x.price >= min_price]
    if max_price is not None:
        items = [x for x in items if x.price <= max_price]
    return items