from pydantic import BaseModel
from dataclasses import dataclass


@dataclass
class Document:
    """
    
    """
    id: str
    url: str
    content: str
    short_summary: str = None
    long_summary: str = None


class ShortSummaryDataModel(BaseModel):
    """
    
    """
    summary: str


class LongSummaryDataModel(BaseModel):
    """
    
    """
    summary: str
