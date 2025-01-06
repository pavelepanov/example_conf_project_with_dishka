from typing import Iterable

from dishka import Provider

from app.entrypoint.ioc.adapters import (
    AnswerProvider,
    ConfigProvider,
    SomeConfigProvider,
)
from app.entrypoint.ioc.interactors import InteractorProvider


def get_providers() -> Iterable[Provider]:
    return (
        InteractorProvider(),
        ConfigProvider(),
        SomeConfigProvider(),
        AnswerProvider(),
    )
