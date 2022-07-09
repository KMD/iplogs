from abc import ABC, abstractmethod

from typing import List
from pydantic import BaseModel


class Response(BaseModel):
    action: str
    files: List[str]

    class Config:
        arbitrary_types_allowed = True


class ResponseIP(Response):
    ip: str


class ResponseEvents(Response):
    no_events: int


class ResponseBytes(Response):
    no_bytes: int


class Source(ABC):
    """
    Abstract Factory Pattern
    Abstract class, in case we will support more than one log type
    we want to be consistent.
    More info: https://en.wikipedia.org/wiki/Abstract_factory_pattern
    """

    @abstractmethod
    def most_frequent_IP(self) -> ResponseIP:
        ...

    @abstractmethod
    def least_frequent_IP(self) -> ResponseIP:
        ...

    @abstractmethod
    def events_per_second(self) -> ResponseEvents:
        ...

    @abstractmethod
    def total_amount_of_bytes_exchanged(self) -> ResponseBytes:
        ...
