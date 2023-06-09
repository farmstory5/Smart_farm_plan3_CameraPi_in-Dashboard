from _typeshed import Incomplete

from openpyxl.descriptors.serialisable import Serialisable as Serialisable

class ChartsheetProperties(Serialisable):
    tagname: str
    published: Incomplete
    codeName: Incomplete
    tabColor: Incomplete
    __elements__: Incomplete
    def __init__(
        self, published: Incomplete | None = None, codeName: Incomplete | None = None, tabColor: Incomplete | None = None
    ) -> None: ...
