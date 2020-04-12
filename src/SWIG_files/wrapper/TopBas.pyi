from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopAbs import *

#the following typedef cannot be wrapped as is
TopBas_ListIteratorOfListOfTestInterference = NewType('TopBas_ListIteratorOfListOfTestInterference', Any)
#the following typedef cannot be wrapped as is
TopBas_ListOfTestInterference = NewType('TopBas_ListOfTestInterference', Any)

class TopBas_TestInterference:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Inters: float, Bound: int, Orient: TopAbs_Orientation, Trans: TopAbs_Orientation, BTrans: TopAbs_Orientation) -> None: ...
	@overload
	def Boundary(self, B: int) -> None: ...
	@overload
	def Boundary(self) -> int: ...
	@overload
	def BoundaryTransition(self, BTr: TopAbs_Orientation) -> None: ...
	@overload
	def BoundaryTransition(self) -> TopAbs_Orientation: ...
	def GetChangeBoundary(self) -> int: ...
	def SetChangeBoundary(self, value: int) -> None: ...
	def GetChangeIntersection(self) -> float: ...
	def SetChangeIntersection(self, value: float) -> None: ...
	@overload
	def Intersection(self, I: float) -> None: ...
	@overload
	def Intersection(self) -> float: ...
	@overload
	def Orientation(self, O: TopAbs_Orientation) -> None: ...
	@overload
	def Orientation(self) -> TopAbs_Orientation: ...
	@overload
	def Transition(self, Tr: TopAbs_Orientation) -> None: ...
	@overload
	def Transition(self) -> TopAbs_Orientation: ...

# harray1 classes
# harray2 classes
# hsequence classes

