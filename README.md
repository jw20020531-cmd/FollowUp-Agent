# FollowUp AI

Evidence-first prototype for tracking email follow-ups in student groups and small teams.

## Product direction

FollowUp AI is taking an evidence-first path. The first MVP will prove the manual follow-up workflow before adding Gmail OAuth, Gmail sync, AI draft generation, or automatic sending.

- Evidence log: `docs/evidence.md`
- MVP scope: `docs/mvp-scope.md`
- Demo data: `docs/demo-data.md`
- GitHub issue template: `.github/ISSUE_TEMPLATE/mvp-validation.md`

## Architecture

- `frontend/` - Next.js App Router, TypeScript, and a read-only demo inbox.
- `backend/` - FastAPI service with persistent follow-up records. SQLite is the local default.
- `db` - optional PostgreSQL 16 via Docker Compose.
- `backend/migrations/` — checked-in migration location for future schema changes.

OAuth, Gmail sync, AI analysis, sending, and reply detection are intentionally not implemented in Phase 1.

## Run the manual MVP locally

The backend uses a local SQLite database by default. No Docker installation is needed for the API. The web page displays sample data; create and status updates are available through the API.

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open <http://localhost:8000/api/follow-ups> to view seeded demo candidates. The interactive API documentation is at <http://localhost:8000/docs>.

## Run locally with PostgreSQL

1. Start PostgreSQL: `docker compose up -d db`.
2. Set `DATABASE_URL` to `postgresql+psycopg://followup:followup@localhost:5432/followup` in the backend shell.
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

