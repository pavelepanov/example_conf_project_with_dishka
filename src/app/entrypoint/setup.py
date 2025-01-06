from typing import Iterable

from dishka import AsyncContainer, Provider, make_async_container
from fastapi import APIRouter, FastAPI

from app.entrypoint.config import Config, create_config


def create_app() -> FastAPI:
    app = FastAPI()

    return app


def create_async_container(providers: Iterable[Provider]) -> AsyncContainer:
    config = create_config()
    return make_async_container(*providers, context={Config: config})


def configure_app(app: FastAPI, root_router: APIRouter) -> None:
    app.include_router(root_router)
