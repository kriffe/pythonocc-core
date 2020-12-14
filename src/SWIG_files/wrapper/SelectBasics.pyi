from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *


class selectbasics:
	@staticmethod
	def MaxOwnerPriority() -> int: ...
	@staticmethod
	def MinOwnerPriority() -> int: ...

class SelectBasics_PickResult:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theDepth: float, theDistToCenter: float, theObjPickedPnt: gp_Pnt) -> None: ...
	def Depth(self) -> float: ...
	def DistToGeomCenter(self) -> float: ...
	def HasPickedPoint(self) -> bool: ...
	def Invalidate(self) -> None: ...
	def IsValid(self) -> bool: ...
	@staticmethod
	def Min(thePickResult1: SelectBasics_PickResult, thePickResult2: SelectBasics_PickResult) -> SelectBasics_PickResult: ...
	def PickedPoint(self) -> gp_Pnt: ...
	def SetDepth(self, theDepth: float) -> None: ...
	def SetDistToGeomCenter(self, theDistToCenter: float) -> None: ...
	def SetPickedPoint(self, theObjPickedPnt: gp_Pnt) -> None: ...
	@overload
	def SetSurfaceNormal(self, theNormal: gp_Vec) -> None: ...
	def SurfaceNormal(self) -> False: ...

class SelectBasics_SelectingVolumeManager:
	def DetectedPoint(self, theDepth: float) -> gp_Pnt: ...
	def DistToGeometryCenter(self, theCOG: gp_Pnt) -> float: ...
	def GetActiveSelectionType(self) -> int: ...
	def GetFarPickedPnt(self) -> gp_Pnt: ...
	def GetMousePosition(self) -> gp_Pnt2d: ...
	def GetNearPickedPnt(self) -> gp_Pnt: ...
	def IsOverlapAllowed(self) -> bool: ...
	@overload
	def Overlaps(self, thePnt: gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool: ...
	@overload
	def Overlaps(self, thePnt: gp_Pnt) -> bool: ...
	@overload
	def Overlaps(self, theArrayOfPts: TColgp_HArray1OfPnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...
	@overload
	def Overlaps(self, theArrayOfPts: TColgp_Array1OfPnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...
	@overload
	def Overlaps(self, thePt1: gp_Pnt, thePt2: gp_Pnt, thePickResult: SelectBasics_PickResult) -> bool: ...
	@overload
	def Overlaps(self, thePt1: gp_Pnt, thePt2: gp_Pnt, thePt3: gp_Pnt, theSensType: int, thePickResult: SelectBasics_PickResult) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes

selectbasics_MaxOwnerPriority = selectbasics.MaxOwnerPriority
selectbasics_MinOwnerPriority = selectbasics.MinOwnerPriority
SelectBasics_PickResult_Min = SelectBasics_PickResult.Min
