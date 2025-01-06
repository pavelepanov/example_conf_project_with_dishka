from dishka import AsyncContainer, Provider
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.entrypoint.ioc.registry import get_providers
from app.entrypoint.setup import configure_app, create_app, create_async_container
from app.http.root_router import root_router


def make_app(*di_providers: Provider) -> FastAPI:
    app: FastAPI = create_app()
    configure_app(app=app, root_router=root_router)
    async_container: AsyncContainer = create_async_container(
        providers=(*get_providers(), *di_providers)
    )

    setup_dishka(container=async_container, app=app)

    return app
