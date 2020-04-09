from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *


class Adaptor2d_Curve2d:
	def BSpline(self) -> Geom2d_BSplineCurve: ...
	def Bezier(self) -> Geom2d_BezierCurve: ...
	def Circle(self) -> gp_Circ2d: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D0(self, U: float, P: gp_Pnt2d) -> None: ...
	def D1(self, U: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	def D2(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def D3(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec2d: ...
	def Degree(self) -> int: ...
	def Ellipse(self) -> gp_Elips2d: ...
	def FirstParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr2d: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin2d: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def NbSamples(self) -> int: ...
	def Parabola(self) -> gp_Parab2d: ...
	def Period(self) -> float: ...
	def Resolution(self, R3d: float) -> float: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor2d_HCurve2d: ...
	def Value(self, U: float) -> gp_Pnt2d: ...

class Adaptor2d_HCurve2d(Standard_Transient):
	def BSpline(self) -> Geom2d_BSplineCurve: ...
	def Bezier(self) -> Geom2d_BezierCurve: ...
	def Circle(self) -> gp_Circ2d: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Curve2d(self) -> Adaptor2d_Curve2d: ...
	def D0(self, U: float, P: gp_Pnt2d) -> None: ...
	def D1(self, U: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	def D2(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def D3(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec2d: ...
	def Degree(self) -> int: ...
	def Ellipse(self) -> gp_Elips2d: ...
	def FirstParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr2d: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin2d: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def Parabola(self) -> gp_Parab2d: ...
	def Period(self) -> float: ...
	def Resolution(self, R3d: float) -> float: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor2d_HCurve2d: ...
	def Value(self, U: float) -> gp_Pnt2d: ...

class Adaptor2d_HLine2d(Adaptor2d_HCurve2d):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_Line2d) -> None: ...
	def ChangeCurve2d(self) -> Adaptor2d_Line2d: ...
	def Curve2d(self) -> Adaptor2d_Curve2d: ...
	def Set(self, C: Adaptor2d_Line2d) -> None: ...

class Adaptor2d_HOffsetCurve(Adaptor2d_HCurve2d):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_OffsetCurve) -> None: ...
	def ChangeCurve2d(self) -> Adaptor2d_OffsetCurve: ...
	def Curve2d(self) -> Adaptor2d_Curve2d: ...
	def Set(self, C: Adaptor2d_OffsetCurve) -> None: ...

class Adaptor2d_Line2d(Adaptor2d_Curve2d):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P: gp_Pnt2d, D: gp_Dir2d, UFirst: float, ULast: float) -> None: ...
	def BSpline(self) -> Geom2d_BSplineCurve: ...
	def Bezier(self) -> Geom2d_BezierCurve: ...
	def Circle(self) -> gp_Circ2d: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D0(self, X: float, P: gp_Pnt2d) -> None: ...
	def D1(self, X: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	def D2(self, X: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def D3(self, X: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec2d: ...
	def Degree(self) -> int: ...
	def Ellipse(self) -> gp_Elips2d: ...
	def FirstParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr2d: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin2d: ...
	@overload
	def Load(self, L: gp_Lin2d) -> None: ...
	@overload
	def Load(self, L: gp_Lin2d, UFirst: float, ULast: float) -> None: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def Parabola(self) -> gp_Parab2d: ...
	def Period(self) -> float: ...
	def Resolution(self, R3d: float) -> float: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor2d_HCurve2d: ...
	def Value(self, X: float) -> gp_Pnt2d: ...

class Adaptor2d_OffsetCurve(Adaptor2d_Curve2d):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_HCurve2d) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_HCurve2d, Offset: float) -> None: ...
	@overload
	def __init__(self, C: Adaptor2d_HCurve2d, Offset: float, WFirst: float, WLast: float) -> None: ...
	def BSpline(self) -> Geom2d_BSplineCurve: ...
	def Bezier(self) -> Geom2d_BezierCurve: ...
	def Circle(self) -> gp_Circ2d: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Curve(self) -> Adaptor2d_HCurve2d: ...
	def D0(self, U: float, P: gp_Pnt2d) -> None: ...
	def D1(self, U: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	def D2(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def D3(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec2d: ...
	def Degree(self) -> int: ...
	def Ellipse(self) -> gp_Elips2d: ...
	def FirstParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr2d: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin2d: ...
	@overload
	def Load(self, S: Adaptor2d_HCurve2d) -> None: ...
	@overload
	def Load(self, Offset: float) -> None: ...
	@overload
	def Load(self, Offset: float, WFirst: float, WLast: float) -> None: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def NbSamples(self) -> int: ...
	def Offset(self) -> float: ...
	def Parabola(self) -> gp_Parab2d: ...
	def Period(self) -> float: ...
	def Resolution(self, R3d: float) -> float: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor2d_HCurve2d: ...
	def Value(self, U: float) -> gp_Pnt2d: ...

# harray1 classes
# harray2 classes
# harray2 classes

