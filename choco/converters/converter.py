from .parser import BaseParser
from .encoder import BaseEncoder


class Converter(object):
    def __init__(self, parser: BaseParser, encoder: BaseEncoder):
        """Builds a converter using the specified parser and encoder.

        Parameters
        ----------
        parser : BaseParser
            Parser to parse chord into grammar tree
        encoder : BaseEncoder
            Encoder to encode the grammar tree into a string
        """
        self.encoder = encoder
        self.parser = parser

    def convert(self, chord: str) -> str:
        """Convert chord into new encoding by parsing it and passing it to the encoder.

        Parameters
        ----------
        chord : str
            Chord initial encoding

        Returns
        -------
        str
            Chord final encoding
        """
        return self.encoder.encode(self.parser.parse(chord))
