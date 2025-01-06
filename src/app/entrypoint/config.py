from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class SomeConfig:
    some_string: str

    @staticmethod
    def from_env() -> "SomeConfig":
        some_string = getenv("SOME_STRING")

        return SomeConfig(some_string=some_string)


@dataclass(frozen=True)
class Config:
    some_config: SomeConfig


def create_config() -> Config:
    return Config(
        some_config=SomeConfig.from_env(),
    )
