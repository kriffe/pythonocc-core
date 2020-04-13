from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Quantity import *
from OCC.Core.IGESControl import *
from OCC.Core.XSControl import *
from OCC.Core.TCollection import *
from OCC.Core.TDocStd import *
from OCC.Core.TDF import *


class igescafcontrol:
	@staticmethod
	def DecodeColor(self, col: int) -> Quantity_Color: ...
	@staticmethod
	def EncodeColor(self, col: Quantity_Color) -> int: ...

class IGESCAFControl_Reader(IGESControl_Reader):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theWS: XSControl_WorkSession, FromScratch: Optional[bool]) -> None: ...
	def GetColorMode(self) -> bool: ...
	def GetLayerMode(self) -> bool: ...
	def GetNameMode(self) -> bool: ...
	@overload
	def Perform(self, theFileName: TCollection_AsciiString, theDoc: TDocStd_Document) -> bool: ...
	@overload
	def Perform(self, theFileName: str, theDoc: TDocStd_Document) -> bool: ...
	def SetColorMode(self, theMode: bool) -> None: ...
	def SetLayerMode(self, theMode: bool) -> None: ...
	def SetNameMode(self, theMode: bool) -> None: ...
	def Transfer(self, theDoc: TDocStd_Document) -> bool: ...

class IGESCAFControl_Writer(IGESControl_Writer):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, WS: XSControl_WorkSession, scratch: Optional[bool]) -> None: ...
	def GetColorMode(self) -> bool: ...
	def GetLayerMode(self) -> bool: ...
	def GetNameMode(self) -> bool: ...
	@overload
	def Perform(self, doc: TDocStd_Document, filename: TCollection_AsciiString) -> bool: ...
	@overload
	def Perform(self, doc: TDocStd_Document, filename: str) -> bool: ...
	def SetColorMode(self, colormode: bool) -> None: ...
	def SetLayerMode(self, layermode: bool) -> None: ...
	def SetNameMode(self, namemode: bool) -> None: ...
	@overload
	def Transfer(self, doc: TDocStd_Document) -> bool: ...
	@overload
	def Transfer(self, labels: TDF_LabelSequence) -> bool: ...
	@overload
	def Transfer(self, label: TDF_Label) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes

igescafcontrol_DecodeColor = igescafcontrol.DecodeColor
igescafcontrol_EncodeColor = igescafcontrol.EncodeColor
