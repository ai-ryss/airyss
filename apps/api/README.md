# AIryss API

FastAPI backend for the AIryss orchestration platform.

## Responsibility

This service is the HTTP boundary of the AIryss platform. It exposes
endpoints consumed by the web frontend and coordinates the three core
roles: Human, Iryss, and Aryss.

It does **not** execute workspace commands directly. That responsibility
belongs to the `workspace-runner` worker.

## Structure

```
src/
  main.py              # app factory (create_app)
  config/
    settings.py        # environment variable bindings (pydantic-settings)
  routers/
    health.py          # GET /health
    sessions.py        # GET /sessions
    workspaces.py      # GET /workspaces
    prompts.py         # GET /prompts  (placeholder)
    git.py             # GET /git/status  (placeholder)
    audit.py           # GET /audit  (placeholder)
  services/
    orchestrator/
      router.py        # routes tasks to Iryss or Aryss
      session_manager.py  # session lifecycle
    workspace/
      manager.py       # delegates provisioning to workspace-runner
    llm/
      iryss_adapter.py # Anthropic (Claude) API calls for Iryss
      aryss_adapter.py # OpenAI API calls for Aryss
    git/
      repository.py    # git operations within a workspace
  schemas/
    health.py
    session.py
    workspace.py
```

## Routes

| Method | Path            | Status      | Description                           |
|--------|-----------------|-------------|---------------------------------------|
| GET    | /health         | implemented | service health check                  |
| GET    | /sessions       | placeholder | list active development sessions      |
| GET    | /workspaces     | placeholder | list provisioned workspace containers |
| GET    | /prompts        | placeholder | list prompt templates                 |
| GET    | /git/status     | placeholder | git status for a workspace            |
| GET    | /audit          | placeholder | list audit events                     |

> nginx strips the `/api` prefix before forwarding to this service, so
> `GET /api/health` (external) maps to `GET /health` (internal).

## Local development

```bash
cd apps/api
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## Environment variables

| Variable          | Default   | Description               |
|-------------------|-----------|---------------------------|
| POSTGRES_HOST     | localhost |                           |
| POSTGRES_PORT     | 5432      |                           |
| POSTGRES_DB       | airyss    |                           |
| POSTGRES_USER     | airyss    |                           |
| POSTGRES_PASSWORD |           |                           |
| REDIS_HOST        | localhost |                           |
| REDIS_PORT        | 6379      |                           |
| ANTHROPIC_API_KEY |           | required for Iryss (Claude) |
| OPENAI_API_KEY    |           | required for Aryss          |
