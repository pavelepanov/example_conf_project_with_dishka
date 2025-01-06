from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol

from app.entrypoint.config import Config


@dataclass
class Dependency:
    some_string: str


class Port(Protocol):
    @abstractmethod
    def method(self) -> str: ...


class Adapter(Port):
    def __init__(
        self,
        config: Config,
    ):
        self._config = config

    def method(self) -> str:
        return self._config.some_config.some_string
