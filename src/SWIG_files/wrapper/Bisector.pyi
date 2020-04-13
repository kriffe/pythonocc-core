from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *
from OCC.Core.GeomAbs import *
from OCC.Core.math import *
from OCC.Core.IntRes2d import *


class bisector:
	@staticmethod
	def IsConvex(self, Cu: Geom2d_Curve, Sign: float) -> bool: ...

class Bisector_Bisec:
	def __init__(self) -> None: ...
	def ChangeValue(self) -> Geom2d_TrimmedCurve: ...
	@overload
	def Perform(self, Cu1: Geom2d_Curve, Cu2: Geom2d_Curve, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, Sense: float, ajointype: GeomAbs_JoinType, Tolerance: float, oncurve: Optional[bool]) -> None: ...
	@overload
	def Perform(self, Cu: Geom2d_Curve, Pnt: Geom2d_Point, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, Sense: float, Tolerance: float, oncurve: Optional[bool]) -> None: ...
	@overload
	def Perform(self, Pnt: Geom2d_Point, Cu: Geom2d_Curve, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, Sense: float, Tolerance: float, oncurve: Optional[bool]) -> None: ...
	@overload
	def Perform(self, Pnt1: Geom2d_Point, Pnt2: Geom2d_Point, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, Sense: float, Tolerance: Optional[float], oncurve: Optional[bool]) -> None: ...
	def Value(self) -> Geom2d_TrimmedCurve: ...

class Bisector_Curve(Geom2d_Curve):
	def IntervalFirst(self, Index: int) -> float: ...
	def IntervalLast(self, Index: int) -> float: ...
	def IsExtendAtEnd(self) -> bool: ...
	def IsExtendAtStart(self) -> bool: ...
	def NbIntervals(self) -> int: ...
	def Parameter(self, P: gp_Pnt2d) -> float: ...

class Bisector_FunctionH(math_FunctionWithDerivative):
	def __init__(self, C2: Geom2d_Curve, P1: gp_Pnt2d, T1: gp_Vec2d) -> None: ...
	def Derivative(self, X: float) -> Tuple[bool, float]: ...
	def Value(self, X: float) -> Tuple[bool, float]: ...
	def Values(self, X: float) -> Tuple[bool, float, float]: ...

class Bisector_FunctionInter(math_FunctionWithDerivative):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Geom2d_Curve, Bis1: Bisector_Curve, Bis2: Bisector_Curve) -> None: ...
	def Derivative(self, X: float) -> Tuple[bool, float]: ...
	def Perform(self, C: Geom2d_Curve, Bis1: Bisector_Curve, Bis2: Bisector_Curve) -> None: ...
	def Value(self, X: float) -> Tuple[bool, float]: ...
	def Values(self, X: float) -> Tuple[bool, float, float]: ...

class Bisector_Inter(IntRes2d_Intersection):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C1: Bisector_Bisec, D1: IntRes2d_Domain, C2: Bisector_Bisec, D2: IntRes2d_Domain, TolConf: float, Tol: float, ComunElement: bool) -> None: ...
	def Perform(self, C1: Bisector_Bisec, D1: IntRes2d_Domain, C2: Bisector_Bisec, D2: IntRes2d_Domain, TolConf: float, Tol: float, ComunElement: bool) -> None: ...

class Bisector_PointOnBis:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Param1: float, Param2: float, ParamBis: float, Distance: float, Point: gp_Pnt2d) -> None: ...
	@overload
	def Distance(self, Distance: float) -> None: ...
	@overload
	def Distance(self) -> float: ...
	def Dump(self) -> None: ...
	@overload
	def IsInfinite(self, Infinite: bool) -> None: ...
	@overload
	def IsInfinite(self) -> bool: ...
	@overload
	def ParamOnBis(self, Param: float) -> None: ...
	@overload
	def ParamOnBis(self) -> float: ...
	@overload
	def ParamOnC1(self, Param: float) -> None: ...
	@overload
	def ParamOnC1(self) -> float: ...
	@overload
	def ParamOnC2(self, Param: float) -> None: ...
	@overload
	def ParamOnC2(self) -> float: ...
	@overload
	def Point(self, P: gp_Pnt2d) -> None: ...
	@overload
	def Point(self) -> gp_Pnt2d: ...

class Bisector_PolyBis:
	def __init__(self) -> None: ...
	def Append(self, Point: Bisector_PointOnBis) -> None: ...
	def First(self) -> Bisector_PointOnBis: ...
	def Interval(self, U: float) -> int: ...
	def IsEmpty(self) -> bool: ...
	def Last(self) -> Bisector_PointOnBis: ...
	def Length(self) -> int: ...
	def Transform(self, T: gp_Trsf2d) -> None: ...
	def Value(self, Index: int) -> Bisector_PointOnBis: ...

class Bisector_BisecAna(Bisector_Curve):
	def __init__(self) -> None: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Copy(self) -> Geom2d_Geometry: ...
	def D0(self, U: float, P: gp_Pnt2d) -> None: ...
	def D1(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d) -> None: ...
	def D2(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def D3(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec2d: ...
	def Dump(self, Deep: Optional[int], Offset: Optional[int]) -> None: ...
	def FirstParameter(self) -> float: ...
	def Geom2dCurve(self) -> Geom2d_Curve: ...
	def Init(self, bisector: Geom2d_TrimmedCurve) -> None: ...
	def IntervalFirst(self, Index: int) -> float: ...
	def IntervalLast(self, Index: int) -> float: ...
	def IsCN(self, N: int) -> bool: ...
	def IsClosed(self) -> bool: ...
	def IsExtendAtEnd(self) -> bool: ...
	def IsExtendAtStart(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def NbIntervals(self) -> int: ...
	def Parameter(self, P: gp_Pnt2d) -> float: ...
	def ParameterOfEndPoint(self) -> float: ...
	def ParameterOfStartPoint(self) -> float: ...
	@overload
	def Perform(self, Cu1: Geom2d_Curve, Cu2: Geom2d_Curve, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, Sense: float, jointype: GeomAbs_JoinType, Tolerance: float, oncurve: Optional[bool]) -> None: ...
	@overload
	def Perform(self, Cu: Geom2d_Curve, Pnt: Geom2d_Point, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, Sense: float, Tolerance: float, oncurve: Optional[bool]) -> None: ...
	@overload
	def Perform(self, Pnt: Geom2d_Point, Cu: Geom2d_Curve, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, Sense: float, Tolerance: float, oncurve: Optional[bool]) -> None: ...
	@overload
	def Perform(self, Pnt1: Geom2d_Point, Pnt2: Geom2d_Point, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, Sense: float, Tolerance: Optional[float], oncurve: Optional[bool]) -> None: ...
	def Reverse(self) -> None: ...
	def ReversedParameter(self, U: float) -> float: ...
	@overload
	def SetTrim(self, Cu: Geom2d_Curve) -> None: ...
	@overload
	def SetTrim(self, uf: float, ul: float) -> None: ...
	def Transform(self, T: gp_Trsf2d) -> None: ...

class Bisector_BisecCC(Bisector_Curve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Cu1: Geom2d_Curve, Cu2: Geom2d_Curve, Side1: float, Side2: float, Origin: gp_Pnt2d, DistMax: Optional[float]) -> None: ...
	def ChangeGuide(self) -> Bisector_BisecCC: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Copy(self) -> Geom2d_Geometry: ...
	def Curve(self, IndCurve: int) -> Geom2d_Curve: ...
	def D0(self, U: float, P: gp_Pnt2d) -> None: ...
	def D1(self, U: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	def D2(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def D3(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec2d: ...
	def Dump(self, Deep: Optional[int], Offset: Optional[int]) -> None: ...
	def FirstParameter(self) -> float: ...
	def IntervalContinuity(self) -> GeomAbs_Shape: ...
	def IntervalFirst(self, Index: int) -> float: ...
	def IntervalLast(self, Index: int) -> float: ...
	def IsCN(self, N: int) -> bool: ...
	def IsClosed(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def IsExtendAtEnd(self) -> bool: ...
	def IsExtendAtStart(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def LinkBisCurve(self, U: float) -> float: ...
	def LinkCurveBis(self, U: float) -> float: ...
	def NbIntervals(self) -> int: ...
	def Parameter(self, P: gp_Pnt2d) -> float: ...
	def Perform(self, Cu1: Geom2d_Curve, Cu2: Geom2d_Curve, Side1: float, Side2: float, Origin: gp_Pnt2d, DistMax: Optional[float]) -> None: ...
	def Polygon(self) -> Bisector_PolyBis: ...
	def Reverse(self) -> None: ...
	def ReversedParameter(self, U: float) -> float: ...
	def Transform(self, T: gp_Trsf2d) -> None: ...
	def ValueAndDist(self, U: float) -> Tuple[gp_Pnt2d, float, float, float]: ...
	def ValueByInt(self, U: float) -> Tuple[gp_Pnt2d, float, float, float]: ...

class Bisector_BisecPC(Bisector_Curve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Cu: Geom2d_Curve, P: gp_Pnt2d, Side: float, DistMax: Optional[float]) -> None: ...
	@overload
	def __init__(self, Cu: Geom2d_Curve, P: gp_Pnt2d, Side: float, UMin: float, UMax: float) -> None: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Copy(self) -> Geom2d_Geometry: ...
	def D0(self, U: float, P: gp_Pnt2d) -> None: ...
	def D1(self, U: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	def D2(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def D3(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec2d: ...
	def Distance(self, U: float) -> float: ...
	def Dump(self, Deep: Optional[int], Offset: Optional[int]) -> None: ...
	def FirstParameter(self) -> float: ...
	def IntervalContinuity(self) -> GeomAbs_Shape: ...
	def IntervalFirst(self, Index: int) -> float: ...
	def IntervalLast(self, Index: int) -> float: ...
	def IsCN(self, N: int) -> bool: ...
	def IsClosed(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def IsExtendAtEnd(self) -> bool: ...
	def IsExtendAtStart(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def LinkBisCurve(self, U: float) -> float: ...
	def LinkCurveBis(self, U: float) -> float: ...
	def NbIntervals(self) -> int: ...
	def Parameter(self, P: gp_Pnt2d) -> float: ...
	def Perform(self, Cu: Geom2d_Curve, P: gp_Pnt2d, Side: float, DistMax: Optional[float]) -> None: ...
	def Reverse(self) -> None: ...
	def ReversedParameter(self, U: float) -> float: ...
	def Transform(self, T: gp_Trsf2d) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

bisector_IsConvex = bisector.IsConvex
