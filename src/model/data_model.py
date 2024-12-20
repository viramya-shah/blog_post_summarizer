from pydantic import BaseModel
from dataclasses import dataclass


@dataclass
class Document:
    """
    
    """
    id: str
    url: str
    content: str
    title: str = None
    short_summary: str = None
    long_summary: str = None


class ShortSummaryDataModel(BaseModel):
    """
    
    """
    title: str
    summary: str


class LongSummaryDataModel(BaseModel):
    """
    
    """
    title: str
    summary: str
