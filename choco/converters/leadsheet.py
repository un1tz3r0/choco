from lark import Lark, Transformer
from .grammar.leadsheet import music21
from .parser import BaseParser

class Parser(BaseParser):
  def __init__(self, dialect: str):
    """Build parser with specified dialect

    Parameters
    ----------
    dialect : str
        Leadsheet dialect that needs to be used
    """
    DIALECT_MAP = {
      "music21": music21
    }

    super().__init__(DIALECT_MAP[dialect])