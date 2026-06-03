# Thor

Romanian real-estate aggregator for listings from multiple sites into one interface.

## Included
- `thor_webapp.html` - UI prototype
- `thor_fastapi.py` - API prototype
- `thor_worker.py` - sync worker skeleton
- `thor_schema.sql` - database schema
- `thor_architecture.md` - system design
- `thor_utils.py` - normalization and dedupe helpers
- `thor_dedupe.py` - duplicate matcher
- `thor_publi24_pipeline.py` - first import pipeline
- `backend/` - Dockerized FastAPI backend
- `cloudflare_pages/` - Cloudflare Pages + Workers deploy bundle

## Quick start
```bash
docker compose up --build
```

## Deploy
1. Frontend: Cloudflare Pages
2. API: Cloudflare Workers or VPS
3. Database: PostgreSQL
