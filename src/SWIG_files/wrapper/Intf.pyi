from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.Bnd import *


class Intf_PIType(IntEnum):
	Intf_EXTERNAL: int = ...
	Intf_FACE: int = ...
	Intf_EDGE: int = ...
	Intf_VERTEX: int = ...
Intf_EXTERNAL = Intf_PIType.Intf_EXTERNAL
Intf_FACE = Intf_PIType.Intf_FACE
Intf_EDGE = Intf_PIType.Intf_EDGE
Intf_VERTEX = Intf_PIType.Intf_VERTEX

class Intf:
	@staticmethod
	def Contain(self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt, ThePnt: gp_Pnt) -> bool: ...
	@staticmethod
	def PlaneEquation(self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt, NormalVector: gp_XYZ) -> float: ...

class Intf_Interference:
	def Contains(self, ThePnt: Intf_SectionPoint) -> bool: ...
	def Dump(self) -> None: ...
	def GetTolerance(self) -> float: ...
	@overload
	def Insert(self, TheZone: Intf_TangentZone) -> bool: ...
	@overload
	def Insert(self, pdeb: Intf_SectionPoint, pfin: Intf_SectionPoint) -> None: ...
	def LineValue(self, Index: int) -> Intf_SectionLine: ...
	def NbSectionLines(self) -> int: ...
	def NbSectionPoints(self) -> int: ...
	def NbTangentZones(self) -> int: ...
	def PntValue(self, Index: int) -> Intf_SectionPoint: ...
	def ZoneValue(self, Index: int) -> Intf_TangentZone: ...

class Intf_Polygon2d:
	def Bounding(self) -> Bnd_Box2d: ...
	def Closed(self) -> bool: ...
	def DeflectionOverEstimation(self) -> float: ...
	def NbSegments(self) -> int: ...
	def Segment(self, theIndex: int, theBegin: gp_Pnt2d, theEnd: gp_Pnt2d) -> None: ...

class Intf_SectionLine:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Other: Intf_SectionLine) -> None: ...
	@overload
	def Append(self, Pi: Intf_SectionPoint) -> None: ...
	@overload
	def Append(self, LS: Intf_SectionLine) -> None: ...
	def Close(self) -> None: ...
	def Contains(self, ThePI: Intf_SectionPoint) -> bool: ...
	def Dump(self, Indent: int) -> None: ...
	def GetPoint(self, Index: int) -> Intf_SectionPoint: ...
	def IsClosed(self) -> bool: ...
	def IsEnd(self, ThePI: Intf_SectionPoint) -> int: ...
	def IsEqual(self, Other: Intf_SectionLine) -> bool: ...
	def NumberOfPoints(self) -> int: ...
	@overload
	def Prepend(self, Pi: Intf_SectionPoint) -> None: ...
	@overload
	def Prepend(self, LS: Intf_SectionLine) -> None: ...
	def Reverse(self) -> None: ...

class Intf_SectionPoint:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Where: gp_Pnt, DimeO: Intf_PIType, AddrO1: int, AddrO2: int, ParamO: float, DimeT: Intf_PIType, AddrT1: int, AddrT2: int, ParamT: float, Incid: float) -> None: ...
	@overload
	def __init__(self, Where: gp_Pnt2d, DimeO: Intf_PIType, AddrO1: int, ParamO: float, DimeT: Intf_PIType, AddrT1: int, ParamT: float, Incid: float) -> None: ...
	def Dump(self, Indent: int) -> None: ...
	def Incidence(self) -> float: ...
	@overload
	def InfoFirst(self, Dim: Intf_PIType) -> Tuple[int, int, float]: ...
	@overload
	def InfoFirst(self, Dim: Intf_PIType) -> Tuple[int, float]: ...
	@overload
	def InfoSecond(self, Dim: Intf_PIType) -> Tuple[int, int, float]: ...
	@overload
	def InfoSecond(self, Dim: Intf_PIType) -> Tuple[int, float]: ...
	def IsEqual(self, Other: Intf_SectionPoint) -> bool: ...
	def IsOnSameEdge(self, Other: Intf_SectionPoint) -> bool: ...
	def Merge(self, Other: Intf_SectionPoint) -> None: ...
	def ParamOnFirst(self) -> float: ...
	def ParamOnSecond(self) -> float: ...
	def Pnt(self) -> gp_Pnt: ...
	def TypeOnFirst(self) -> Intf_PIType: ...
	def TypeOnSecond(self) -> Intf_PIType: ...

class Intf_TangentZone:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Other: Intf_TangentZone) -> None: ...
	@overload
	def Append(self, Pi: Intf_SectionPoint) -> None: ...
	@overload
	def Append(self, Tzi: Intf_TangentZone) -> None: ...
	def Contains(self, ThePI: Intf_SectionPoint) -> bool: ...
	def Dump(self, Indent: int) -> None: ...
	def GetPoint(self, Index: int) -> Intf_SectionPoint: ...
	def HasCommonRange(self, Other: Intf_TangentZone) -> bool: ...
	def InfoFirst(self) -> Tuple[int, float, int, float]: ...
	def InfoSecond(self) -> Tuple[int, float, int, float]: ...
	def Insert(self, Pi: Intf_SectionPoint) -> bool: ...
	def InsertAfter(self, Index: int, Pi: Intf_SectionPoint) -> None: ...
	def InsertBefore(self, Index: int, Pi: Intf_SectionPoint) -> None: ...
	def IsEqual(self, Other: Intf_TangentZone) -> bool: ...
	def NumberOfPoints(self) -> int: ...
	def ParamOnFirst(self) -> Tuple[float, float]: ...
	def ParamOnSecond(self) -> Tuple[float, float]: ...
	def PolygonInsert(self, Pi: Intf_SectionPoint) -> None: ...
	def RangeContains(self, ThePI: Intf_SectionPoint) -> bool: ...

class Intf_Tool:
	def __init__(self) -> None: ...
	def BeginParam(self, SegmentNum: int) -> float: ...
	def EndParam(self, SegmentNum: int) -> float: ...
	def Hypr2dBox(self, theHypr2d: gp_Hypr2d, bounding: Bnd_Box2d, boxHypr: Bnd_Box2d) -> None: ...
	def HyprBox(self, theHypr: gp_Hypr, bounding: Bnd_Box, boxHypr: Bnd_Box) -> None: ...
	def Lin2dBox(self, theLin2d: gp_Lin2d, bounding: Bnd_Box2d, boxLin: Bnd_Box2d) -> None: ...
	def LinBox(self, theLin: gp_Lin, bounding: Bnd_Box, boxLin: Bnd_Box) -> None: ...
	def NbSegments(self) -> int: ...
	def Parab2dBox(self, theParab2d: gp_Parab2d, bounding: Bnd_Box2d, boxHypr: Bnd_Box2d) -> None: ...
	def ParabBox(self, theParab: gp_Parab, bounding: Bnd_Box, boxHypr: Bnd_Box) -> None: ...

class Intf_InterferencePolygon2d(Intf_Interference):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Obje1: Intf_Polygon2d, Obje2: Intf_Polygon2d) -> None: ...
	@overload
	def __init__(self, Obje: Intf_Polygon2d) -> None: ...
	@overload
	def Perform(self, Obje1: Intf_Polygon2d, Obje2: Intf_Polygon2d) -> None: ...
	@overload
	def Perform(self, Obje: Intf_Polygon2d) -> None: ...
	def Pnt2dValue(self, Index: int) -> gp_Pnt2d: ...
intf_Contain = intf.Contain
intf_PlaneEquation = intf.PlaneEquation
