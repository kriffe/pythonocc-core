from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.TopTools import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.Adaptor3d import *
from OCC.Core.gp import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *


class BiTgte_ContactType(IntEnum):
	BiTgte_FaceFace: int = ...
	BiTgte_FaceEdge: int = ...
	BiTgte_FaceVertex: int = ...
	BiTgte_EdgeEdge: int = ...
	BiTgte_EdgeVertex: int = ...
	BiTgte_VertexVertex: int = ...
BiTgte_FaceFace = BiTgte_ContactType.BiTgte_FaceFace
BiTgte_FaceEdge = BiTgte_ContactType.BiTgte_FaceEdge
BiTgte_FaceVertex = BiTgte_ContactType.BiTgte_FaceVertex
BiTgte_EdgeEdge = BiTgte_ContactType.BiTgte_EdgeEdge
BiTgte_EdgeVertex = BiTgte_ContactType.BiTgte_EdgeVertex
BiTgte_VertexVertex = BiTgte_ContactType.BiTgte_VertexVertex

class BiTgte_Blend:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape, Radius: float, Tol: float, NUBS: bool) -> None: ...
	def CenterLines(self, LC: TopTools_ListOfShape) -> None: ...
	def Clear(self) -> None: ...
	def ComputeCenters(self) -> None: ...
	def ContactType(self, Index: int) -> BiTgte_ContactType: ...
	def CurveOnShape1(self, Index: int) -> Geom_Curve: ...
	def CurveOnShape2(self, Index: int) -> Geom_Curve: ...
	@overload
	def Face(self, Index: int) -> TopoDS_Face: ...
	@overload
	def Face(self, CenterLine: TopoDS_Shape) -> TopoDS_Face: ...
	def IndicesOfBranche(self, Index: int) -> Tuple[int, int]: ...
	def Init(self, S: TopoDS_Shape, Radius: float, Tol: float, NUBS: bool) -> None: ...
	def IsDone(self) -> bool: ...
	def NbBranches(self) -> int: ...
	def NbSurfaces(self) -> int: ...
	def PCurve1OnFillet(self, Index: int) -> Geom2d_Curve: ...
	def PCurve2OnFillet(self, Index: int) -> Geom2d_Curve: ...
	def PCurveOnFace1(self, Index: int) -> Geom2d_Curve: ...
	def PCurveOnFace2(self, Index: int) -> Geom2d_Curve: ...
	def Perform(self, BuildShape: Optional[bool]) -> None: ...
	def SetEdge(self, Edge: TopoDS_Edge) -> None: ...
	def SetFaces(self, F1: TopoDS_Face, F2: TopoDS_Face) -> None: ...
	def SetStoppingFace(self, Face: TopoDS_Face) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def SupportShape1(self, Index: int) -> TopoDS_Shape: ...
	def SupportShape2(self, Index: int) -> TopoDS_Shape: ...
	@overload
	def Surface(self, Index: int) -> Geom_Surface: ...
	@overload
	def Surface(self, CenterLine: TopoDS_Shape) -> Geom_Surface: ...

class BiTgte_CurveOnEdge(Adaptor3d_Curve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, EonF: TopoDS_Edge, Edge: TopoDS_Edge) -> None: ...
	def BSpline(self) -> Geom_BSplineCurve: ...
	def Bezier(self) -> Geom_BezierCurve: ...
	def Circle(self) -> gp_Circ: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D0(self, U: float, P: gp_Pnt) -> None: ...
	def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
	def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec: ...
	def Degree(self) -> int: ...
	def Ellipse(self) -> gp_Elips: ...
	def FirstParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr: ...
	def Init(self, EonF: TopoDS_Edge, Edge: TopoDS_Edge) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def Parabola(self) -> gp_Parab: ...
	def Period(self) -> float: ...
	def Resolution(self, R3d: float) -> float: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
	def Value(self, U: float) -> gp_Pnt: ...

class BiTgte_CurveOnVertex(Adaptor3d_Curve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, EonF: TopoDS_Edge, V: TopoDS_Vertex) -> None: ...
	def BSpline(self) -> Geom_BSplineCurve: ...
	def Bezier(self) -> Geom_BezierCurve: ...
	def Circle(self) -> gp_Circ: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D0(self, U: float, P: gp_Pnt) -> None: ...
	def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
	def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec: ...
	def Degree(self) -> int: ...
	def Ellipse(self) -> gp_Elips: ...
	def FirstParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr: ...
	def Init(self, EonF: TopoDS_Edge, V: TopoDS_Vertex) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def Parabola(self) -> gp_Parab: ...
	def Period(self) -> float: ...
	def Resolution(self, R3d: float) -> float: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
	def Value(self, U: float) -> gp_Pnt: ...

class BiTgte_HCurveOnEdge(Adaptor3d_HCurve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: BiTgte_CurveOnEdge) -> None: ...
	def ChangeCurve(self) -> BiTgte_CurveOnEdge: ...
	def Curve(self) -> Adaptor3d_Curve: ...
	def GetCurve(self) -> Adaptor3d_Curve: ...
	def Set(self, C: BiTgte_CurveOnEdge) -> None: ...

class BiTgte_HCurveOnVertex(Adaptor3d_HCurve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: BiTgte_CurveOnVertex) -> None: ...
	def ChangeCurve(self) -> BiTgte_CurveOnVertex: ...
	def Curve(self) -> Adaptor3d_Curve: ...
	def GetCurve(self) -> Adaptor3d_Curve: ...
	def Set(self, C: BiTgte_CurveOnVertex) -> None: ...
