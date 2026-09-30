# FollowUp AI

Phase 1 project skeleton for a lightweight AI follow-up assistant for small sales teams.

## Product direction

FollowUp AI is taking an evidence-first path. The first MVP will prove the manual follow-up workflow before adding Gmail OAuth, Gmail sync, AI draft generation, or automatic sending.

- Evidence log: `docs/evidence.md`
- MVP scope: `docs/mvp-scope.md`
- Demo data: `docs/demo-data.md`
- GitHub issue template: `.github/ISSUE_TEMPLATE/mvp-validation.md`

## Architecture

- `frontend/` — Next.js App Router, TypeScript, and a minimal follow-up inbox UI.
- `backend/` — FastAPI service with versioned health routes and a SQLAlchemy/PostgreSQL connection foundation.
- `db` — PostgreSQL 16 via Docker Compose.
- `backend/migrations/` — checked-in migration location for future schema changes.

OAuth, Gmail sync, AI analysis, sending, and reply detection are intentionally not implemented in Phase 1.

## Run the manual MVP locally

The manual follow-up API can run before Docker and PostgreSQL are installed. In that mode, `/api/health` and `/api/follow-ups` work, while `/api/health/db` returns `{"status":"unavailable"}` until the database is running.

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open <http://localhost:8000/api/follow-ups> to view the demo follow-up candidates.

## Run locally with PostgreSQL

1. Copy `.env.example` to `.env`.
2. Start PostgreSQL: `docker compose up -d db`.
3. Start the backend:

   ```powershell
   cd backend
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 8000
   ```

4. In a second terminal, start the frontend:

   ```powershell
   cd frontend
   npm install
   npm run dev
   ```

Open <http://localhost:3000>. Backend health is available at <http://localhost:8000/api/health> and database health at <http://localhost:8000/api/health/db>.

The manual MVP follow-up API is available at <http://localhost:8000/api/follow-ups>.

## Run the full stack with Docker

```powershell
docker compose up --build
```


