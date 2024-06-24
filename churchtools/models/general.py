from datetime import date, datetime
from typing import Any, Dict, Generator, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel  # type: ignore

from . import EmptyStrToNone


class SearchResult(BaseModel):
    apiUrl: str
    domainIdentifier: str
    domainType: str
    frontendUrl: str
    icon: str
    imageUrl: Optional[str] = None
    title: str

    # TODO: domainAttributes

    def __repr__(self) -> str:
        return f"<SearchResult: {self.title} [{self.domainType}]>"


class VersionInfo(BaseModel):
    build: str
    version: str

    def __repr__(self) -> str:
        return f"<Version: {self.version} (build: {self.build})>"
