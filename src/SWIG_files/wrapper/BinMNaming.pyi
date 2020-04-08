from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BinMDF import *
from OCC.Core.Message import *
from OCC.Core.BinTools import *
from OCC.Core.TDF import *
from OCC.Core.BinObjMgt import *


class BinMNaming:
	@staticmethod
	def AddDrivers(self, theDriverTable: BinMDF_ADriverTable, aMsgDrv: Message_Messenger) -> None: ...

class BinMNaming_NamedShapeDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def Clear(self) -> None: ...
	def GetFormatNb(self) -> int: ...
	def GetShapesLocations(self) -> BinTools_LocationSet: ...
	def IsWithTriangles(self) -> bool: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	@overload
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	@overload
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...
	def SetFormatNb(self, theFormat: int) -> None: ...
	def SetWithTriangles(self, isWithTriangles: bool) -> None: ...

class BinMNaming_NamingDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	@overload
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	@overload
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...
