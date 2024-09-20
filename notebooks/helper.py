from pydantic import BaseModel, Field, HttpUrl
from typing import List, Dict

class BlogPost(BaseModel):
  url: HttpUrl
  filename: str = ""
  text: str = ""
  # text_short: str = ""
  markdown: str = "" # todo: convert markdown to plain text, store here
  # questions: List = []
  chunks: dict = {} # populated by different chunking strategies later

from llama_index.core import VectorStoreIndex

class Index(BaseModel):
  name: str
  index: VectorStoreIndex
  questions: list[Dict[str, str]] = [] # store q and a here

  class Config:
    arbitrary_types_allowed = True