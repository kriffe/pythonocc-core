from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopAbs import *
from OCC.Core.IntRes2d import *

#the following typedef cannot be wrapped as is
HatchGen_Domains = NewType('HatchGen_Domains', Any)
#the following typedef cannot be wrapped as is
HatchGen_PointsOnElement = NewType('HatchGen_PointsOnElement', Any)
#the following typedef cannot be wrapped as is
HatchGen_PointsOnHatching = NewType('HatchGen_PointsOnHatching', Any)

class HatchGen_ErrorStatus(IntEnum):
	HatchGen_NoProblem: int = ...
	HatchGen_TrimFailure: int = ...
	HatchGen_TransitionFailure: int = ...
	HatchGen_IncoherentParity: int = ...
	HatchGen_IncompatibleStates: int = ...
HatchGen_NoProblem = HatchGen_ErrorStatus.HatchGen_NoProblem
HatchGen_TrimFailure = HatchGen_ErrorStatus.HatchGen_TrimFailure
HatchGen_TransitionFailure = HatchGen_ErrorStatus.HatchGen_TransitionFailure
HatchGen_IncoherentParity = HatchGen_ErrorStatus.HatchGen_IncoherentParity
HatchGen_IncompatibleStates = HatchGen_ErrorStatus.HatchGen_IncompatibleStates

class HatchGen_IntersectionType(IntEnum):
	HatchGen_TRUE: int = ...
	HatchGen_TOUCH: int = ...
	HatchGen_TANGENT: int = ...
	HatchGen_UNDETERMINED: int = ...
HatchGen_TRUE = HatchGen_IntersectionType.HatchGen_TRUE
HatchGen_TOUCH = HatchGen_IntersectionType.HatchGen_TOUCH
HatchGen_TANGENT = HatchGen_IntersectionType.HatchGen_TANGENT
HatchGen_UNDETERMINED = HatchGen_IntersectionType.HatchGen_UNDETERMINED

class HatchGen_Domain:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P1: HatchGen_PointOnHatching, P2: HatchGen_PointOnHatching) -> None: ...
	@overload
	def __init__(self, P: HatchGen_PointOnHatching, First: bool) -> None: ...
	def Dump(self, Index: Optional[int]) -> None: ...
	def FirstPoint(self) -> HatchGen_PointOnHatching: ...
	def HasFirstPoint(self) -> bool: ...
	def HasSecondPoint(self) -> bool: ...
	def SecondPoint(self) -> HatchGen_PointOnHatching: ...
	@overload
	def SetFirstPoint(self, P: HatchGen_PointOnHatching) -> None: ...
	@overload
	def SetFirstPoint(self) -> None: ...
	@overload
	def SetPoints(self, P1: HatchGen_PointOnHatching, P2: HatchGen_PointOnHatching) -> None: ...
	@overload
	def SetPoints(self) -> None: ...
	@overload
	def SetSecondPoint(self, P: HatchGen_PointOnHatching) -> None: ...
	@overload
	def SetSecondPoint(self) -> None: ...

class HatchGen_IntersectionPoint:
	def Dump(self, Index: Optional[int]) -> None: ...
	def Index(self) -> int: ...
	def Parameter(self) -> float: ...
	def Position(self) -> TopAbs_Orientation: ...
	def SegmentBeginning(self) -> bool: ...
	def SegmentEnd(self) -> bool: ...
	def SetIndex(self, Index: int) -> None: ...
	def SetParameter(self, Parameter: float) -> None: ...
	def SetPosition(self, Position: TopAbs_Orientation) -> None: ...
	def SetSegmentBeginning(self, State: Optional[bool]) -> None: ...
	def SetSegmentEnd(self, State: Optional[bool]) -> None: ...
	def SetStateAfter(self, State: TopAbs_State) -> None: ...
	def SetStateBefore(self, State: TopAbs_State) -> None: ...
	def StateAfter(self) -> TopAbs_State: ...
	def StateBefore(self) -> TopAbs_State: ...

class HatchGen_PointOnElement(HatchGen_IntersectionPoint):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Point: HatchGen_PointOnElement) -> None: ...
	@overload
	def __init__(self, Point: IntRes2d_IntersectionPoint) -> None: ...
	def Dump(self, Index: Optional[int]) -> None: ...
	def IntersectionType(self) -> HatchGen_IntersectionType: ...
	def IsDifferent(self, Point: HatchGen_PointOnElement, Confusion: float) -> bool: ...
	def IsIdentical(self, Point: HatchGen_PointOnElement, Confusion: float) -> bool: ...
	def SetIntersectionType(self, Type: HatchGen_IntersectionType) -> None: ...

class HatchGen_PointOnHatching(HatchGen_IntersectionPoint):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Point: HatchGen_PointOnHatching) -> None: ...
	@overload
	def __init__(self, Point: IntRes2d_IntersectionPoint) -> None: ...
	def AddPoint(self, Point: HatchGen_PointOnElement, Confusion: float) -> None: ...
	def ClrPoints(self) -> None: ...
	def Dump(self, Index: Optional[int]) -> None: ...
	def IsEqual(self, Point: HatchGen_PointOnHatching, Confusion: float) -> bool: ...
	def IsGreater(self, Point: HatchGen_PointOnHatching, Confusion: float) -> bool: ...
	def IsLower(self, Point: HatchGen_PointOnHatching, Confusion: float) -> bool: ...
	def NbPoints(self) -> int: ...
	def Point(self, Index: int) -> HatchGen_PointOnElement: ...
	def RemPoint(self, Index: int) -> None: ...

# harray1 classes
# harray2 classes
# harray2 classes

