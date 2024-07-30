from typing import Iterator
from htpy import Element

class HXMLElement(Element):
    def __iter__(self) -> Iterator[str]:
        yield "<!DOCTYPE hxml>"  # AFAICT I'm just making this up, and this doesn't matter?
        yield from super().__iter__()

hxml = HXMLElement("xml", {}, None)

view = Element("view", {}, None)
text = Element("text", {}, None)
