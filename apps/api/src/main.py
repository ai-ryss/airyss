from fastapi import FastAPI

from src.routers import audit, git, health, prompts, sessions, workspaces


def create_app() -> FastAPI:
    app = FastAPI(
        title="AIryss API",
        description="Orchestration layer for AIryss human-governed AI development platform",
        version="0.1.0",
    )

    app.include_router(health.router)
    app.include_router(sessions.router)
    app.include_router(workspaces.router)
    app.include_router(prompts.router)
    app.include_router(git.router)
    app.include_router(audit.router)

    return app


app = create_app()
