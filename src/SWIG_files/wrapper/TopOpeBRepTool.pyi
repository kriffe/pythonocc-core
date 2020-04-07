from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRepClass3d import *
from OCC.Core.TopTools import *
from OCC.Core.TopoDS import *
from OCC.Core.TopAbs import *
from OCC.Core.Bnd import *
from OCC.Core.TColStd import *
from OCC.Core.Geom2d import *
from OCC.Core.GeomAdaptor import *
from OCC.Core.Geom import *
from OCC.Core.TColgp import *
from OCC.Core.gp import *
from OCC.Core.TopExp import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.TCollection import *
from OCC.Core.GeomAbs import *
from OCC.Core.Extrema import *

TopOpeBRepTool_PShapeClassifier = NewType('TopOpeBRepTool_PShapeClassifier', TopOpeBRepTool_ShapeClassifier)
TopOpeBRepTool_PSoClassif = NewType('TopOpeBRepTool_PSoClassif', BRepClass3d_SolidClassifier)
TopOpeBRepTool_Plos = NewType('TopOpeBRepTool_Plos', TopTools_ListOfShape)

class TopOpeBRepTool_OutCurveType:
	TopOpeBRepTool_BSPLINE1: int = ...
	TopOpeBRepTool_APPROX: int = ...
	TopOpeBRepTool_INTERPOL: int = ...

class TopOpeBRepTool:
	@staticmethod
	def CorrectONUVISO(self, F: TopoDS_Face, Fsp: TopoDS_Face) -> bool: ...
	@staticmethod
	def MakeFaces(self, F: TopoDS_Face, LOF: TopTools_ListOfShape, MshNOK: TopTools_IndexedMapOfOrientedShape, LOFF: TopTools_ListOfShape) -> bool: ...
	@staticmethod
	def PurgeClosingEdges(self, F: TopoDS_Face, FF: TopoDS_Face, MWisOld: TopTools_DataMapOfShapeInteger, MshNOK: TopTools_IndexedMapOfOrientedShape) -> bool: ...
	@staticmethod
	def PurgeClosingEdges(self, F: TopoDS_Face, LOF: TopTools_ListOfShape, MWisOld: TopTools_DataMapOfShapeInteger, MshNOK: TopTools_IndexedMapOfOrientedShape) -> bool: ...
	@staticmethod
	def Regularize(self, aFace: TopoDS_Face, aListOfFaces: TopTools_ListOfShape, ESplits: TopTools_DataMapOfShapeListOfShape) -> bool: ...
	@staticmethod
	def RegularizeFace(self, aFace: TopoDS_Face, OldWiresnewWires: TopTools_DataMapOfShapeListOfShape, aListOfFaces: TopTools_ListOfShape) -> bool: ...
	@staticmethod
	def RegularizeShells(self, aSolid: TopoDS_Solid, OldSheNewShe: TopTools_DataMapOfShapeListOfShape, FSplits: TopTools_DataMapOfShapeListOfShape) -> bool: ...
	@staticmethod
	def RegularizeWires(self, aFace: TopoDS_Face, OldWiresNewWires: TopTools_DataMapOfShapeListOfShape, ESplits: TopTools_DataMapOfShapeListOfShape) -> bool: ...

class TopOpeBRepTool_AncestorsTool:
	@staticmethod
	def MakeAncestors(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: TopAbs_ShapeEnum, M: TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...

class TopOpeBRepTool_BoxSort:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, T: TopOpeBRepTool_HBoxTool) -> None: ...
	def AddBoxes(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum]) -> None: ...
	def AddBoxesMakeCOB(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum]) -> None: ...
	def Box(self, S: TopoDS_Shape) -> Bnd_Box: ...
	def Clear(self) -> None: ...
	def Compare(self, S: TopoDS_Shape) -> TColStd_ListIteratorOfListOfInteger: ...
	def HAB(self) -> Bnd_HArray1OfBox: ...
	def HABShape(self, I: int) -> TopoDS_Shape: ...
	def HBoxTool(self) -> TopOpeBRepTool_HBoxTool: ...
	def MakeCOB(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum]) -> None: ...
	def MakeHAB(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum]) -> None: ...
	@staticmethod
	def MakeHABCOB(self, HAB: Bnd_HArray1OfBox, COB: Bnd_Box) -> None: ...
	def SetHBoxTool(self, T: TopOpeBRepTool_HBoxTool) -> None: ...
	def TouchedShape(self, I: TColStd_ListIteratorOfListOfInteger) -> TopoDS_Shape: ...

class TopOpeBRepTool_C2DF:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, PC: Geom2d_Curve, f2d: float, l2d: float, tol: float, F: TopoDS_Face) -> None: ...
	def Face(self) -> TopoDS_Face: ...
	def IsFace(self, F: TopoDS_Face) -> bool: ...
	def IsPC(self, PC: Geom2d_Curve) -> bool: ...
	def PC(self) -> Tuple[Geom2d_Curve, float, float, float]: ...
	def SetFace(self, F: TopoDS_Face) -> None: ...
	def SetPC(self, PC: Geom2d_Curve, f2d: float, l2d: float, tol: float) -> None: ...

class TopOpeBRepTool_CLASSI:
	def __init__(self) -> None: ...
	def Add2d(self, S: TopoDS_Shape) -> bool: ...
	def ClassiBnd2d(self, S1: TopoDS_Shape, S2: TopoDS_Shape, tol: float, checklarge: bool) -> int: ...
	def Classilist(self, lS: TopTools_ListOfShape, mapgreasma: TopTools_DataMapOfShapeListOfShape) -> bool: ...
	def Classip2d(self, S1: TopoDS_Shape, S2: TopoDS_Shape, stabnd2d12: int) -> int: ...
	def GetBox2d(self, S: TopoDS_Shape, Box2d: Bnd_Box2d) -> bool: ...
	def Getface(self, S: TopoDS_Shape, fa: TopOpeBRepTool_face) -> bool: ...
	def HasInit2d(self) -> bool: ...
	def Init2d(self, Fref: TopoDS_Face) -> None: ...

class TopOpeBRepTool_CORRISO:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, FRef: TopoDS_Face) -> None: ...
	def AddNewConnexity(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> bool: ...
	def Connexity(self, V: TopoDS_Vertex, Eds: TopTools_ListOfShape) -> bool: ...
	def EdgeOUTofBoundsUV(self, E: TopoDS_Edge, onU: bool, tolx: float) -> Tuple[int, float]: ...
	def EdgeWithFaultyUV(self, E: TopoDS_Edge) -> Tuple[bool, int]: ...
	def EdgeWithFaultyUV(self, EdsToCheck: TopTools_ListOfShape, nfybounds: int, fyE: TopoDS_Shape) -> Tuple[bool, int]: ...
	def EdgesOUTofBoundsUV(self, EdsToCheck: TopTools_ListOfShape, onU: bool, tolx: float, FyEds: TopTools_DataMapOfOrientedShapeInteger) -> bool: ...
	def EdgesWithFaultyUV(self, EdsToCheck: TopTools_ListOfShape, nfybounds: int, FyEds: TopTools_DataMapOfOrientedShapeInteger, stopatfirst: Optional[bool]) -> bool: ...
	def Eds(self) -> TopTools_ListOfShape: ...
	def Fref(self) -> TopoDS_Face: ...
	def GASref(self) -> GeomAdaptor_Surface: ...
	def GetnewS(self, newS: TopoDS_Face) -> bool: ...
	def Init(self, S: TopoDS_Shape) -> bool: ...
	def PurgeFyClosingE(self, ClEds: TopTools_ListOfShape, fyClEds: TopTools_ListOfShape) -> bool: ...
	def Refclosed(self, x: int) -> Tuple[bool, float]: ...
	def RemoveOldConnexity(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> bool: ...
	def S(self) -> TopoDS_Shape: ...
	def SetConnexity(self, V: TopoDS_Vertex, Eds: TopTools_ListOfShape) -> bool: ...
	def SetUVRep(self, E: TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF) -> bool: ...
	def Tol(self, I: int, tol3d: float) -> float: ...
	def TrslUV(self, onU: bool, FyEds: TopTools_DataMapOfOrientedShapeInteger) -> bool: ...
	def UVClosed(self) -> bool: ...
	def UVRep(self, E: TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF) -> bool: ...

class TopOpeBRepTool_CurveTool:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, OCT: TopOpeBRepTool_OutCurveType) -> None: ...
	@overload
	def __init__(self, GT: TopOpeBRepTool_GeomTool) -> None: ...
	def ChangeGeomTool(self) -> TopOpeBRepTool_GeomTool: ...
	def GetGeomTool(self) -> TopOpeBRepTool_GeomTool: ...
	@staticmethod
	def IsProjectable(self, S: TopoDS_Shape, C: Geom_Curve) -> bool: ...
	@staticmethod
	def MakeBSpline1fromPnt(self, P: TColgp_Array1OfPnt) -> Geom_Curve: ...
	@staticmethod
	def MakeBSpline1fromPnt2d(self, P: TColgp_Array1OfPnt2d) -> Geom2d_Curve: ...
	def MakeCurves(self, min: float, max: float, C3D: Geom_Curve, PC1: Geom2d_Curve, PC2: Geom2d_Curve, S1: TopoDS_Shape, S2: TopoDS_Shape, C3DN: Geom_Curve, PC1N: Geom2d_Curve, PC2N: Geom2d_Curve) -> Tuple[bool, float, float]: ...
	@staticmethod
	def MakePCurveOnFace(self, S: TopoDS_Shape, C: Geom_Curve, first: Optional[float], last: Optional[float]) -> Tuple[Geom2d_Curve, float]: ...
	def SetGeomTool(self, GT: TopOpeBRepTool_GeomTool) -> None: ...

class TopOpeBRepTool_FuseEdges:
	def __init__(self, theShape: TopoDS_Shape, PerformNow: Optional[bool]) -> None: ...
	def AvoidEdges(self, theMapEdg: TopTools_IndexedMapOfShape) -> None: ...
	def Edges(self, theMapLstEdg: TopTools_DataMapOfIntegerListOfShape) -> None: ...
	def Faces(self, theMapFac: TopTools_DataMapOfShapeShape) -> None: ...
	def NbVertices(self) -> int: ...
	def Perform(self) -> None: ...
	def ResultEdges(self, theMapEdg: TopTools_DataMapOfIntegerShape) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class TopOpeBRepTool_GeomTool:
	def __init__(self, TypeC3D: Optional[TopOpeBRepTool_OutCurveType], CompC3D: Optional[bool], CompPC1: Optional[bool], CompPC2: Optional[bool]) -> None: ...
	def CompC3D(self) -> bool: ...
	def CompPC1(self) -> bool: ...
	def CompPC2(self) -> bool: ...
	def Define(self, TypeC3D: TopOpeBRepTool_OutCurveType, CompC3D: bool, CompPC1: bool, CompPC2: bool) -> None: ...
	def Define(self, TypeC3D: TopOpeBRepTool_OutCurveType) -> None: ...
	def Define(self, GT: TopOpeBRepTool_GeomTool) -> None: ...
	def DefineCurves(self, CompC3D: bool) -> None: ...
	def DefinePCurves1(self, CompPC1: bool) -> None: ...
	def DefinePCurves2(self, CompPC2: bool) -> None: ...
	def GetTolerances(self) -> Tuple[float, float]: ...
	def NbPntMax(self) -> int: ...
	def SetNbPntMax(self, NbPntMax: int) -> None: ...
	def SetTolerances(self, tol3d: float, tol2d: float) -> None: ...
	def TypeC3D(self) -> TopOpeBRepTool_OutCurveType: ...

class TopOpeBRepTool_HBoxTool(Standard_Transient):
	def __init__(self) -> None: ...
	def AddBox(self, S: TopoDS_Shape) -> None: ...
	def AddBoxes(self, S: TopoDS_Shape, TS: TopAbs_ShapeEnum, TA: Optional[TopAbs_ShapeEnum]) -> None: ...
	def Box(self, S: TopoDS_Shape) -> Bnd_Box: ...
	def Box(self, I: int) -> Bnd_Box: ...
	def ChangeIMS(self) -> TopOpeBRepTool_IndexedDataMapOfShapeBox: ...
	def Clear(self) -> None: ...
	@staticmethod
	def ComputeBox(self, S: TopoDS_Shape, B: Bnd_Box) -> None: ...
	@staticmethod
	def ComputeBoxOnVertices(self, S: TopoDS_Shape, B: Bnd_Box) -> None: ...
	@staticmethod
	def DumpB(self, B: Bnd_Box) -> None: ...
	def Extent(self) -> int: ...
	def HasBox(self, S: TopoDS_Shape) -> bool: ...
	def IMS(self) -> TopOpeBRepTool_IndexedDataMapOfShapeBox: ...
	def Index(self, S: TopoDS_Shape) -> int: ...
	def Shape(self, I: int) -> TopoDS_Shape: ...

class TopOpeBRepTool_PurgeInternalEdges:
	def __init__(self, theShape: TopoDS_Shape, PerformNow: Optional[bool]) -> None: ...
	def Faces(self, theMapFacLstEdg: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def IsDone(self) -> bool: ...
	def NbEdges(self) -> int: ...
	def Perform(self) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class TopOpeBRepTool_REGUS:
	def __init__(self) -> None: ...
	def GetFsplits(self, Fsplits: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def GetOshNsh(self, OshNsh: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def InitBlock(self) -> bool: ...
	def MapS(self) -> bool: ...
	def NearestF(self, e: TopoDS_Edge, lof: TopTools_ListOfShape, ffound: TopoDS_Face) -> bool: ...
	def NextinBlock(self) -> bool: ...
	def REGU(self) -> bool: ...
	def S(self) -> TopoDS_Shape: ...
	def SetFsplits(self, Fsplits: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def SetOshNsh(self, OshNsh: TopTools_DataMapOfShapeListOfShape) -> None: ...
	@staticmethod
	def SplitF(self, Fanc: TopoDS_Face, FSplits: TopTools_ListOfShape) -> bool: ...
	def SplitFaces(self) -> bool: ...
	@staticmethod
	def WireToFace(self, Fanc: TopoDS_Face, nWs: TopTools_ListOfShape, nFs: TopTools_ListOfShape) -> bool: ...

class TopOpeBRepTool_REGUW:
	def __init__(self, FRef: TopoDS_Face) -> None: ...
	def AddNewConnexity(self, v: TopoDS_Vertex, OriKey: int, e: TopoDS_Edge) -> bool: ...
	def Connexity(self, v: TopoDS_Vertex, co: TopOpeBRepTool_connexity) -> bool: ...
	def Fref(self) -> TopoDS_Face: ...
	def GetEsplits(self, Esplits: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def GetOwNw(self, OwNw: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def GetSplits(self, Splits: TopTools_ListOfShape) -> bool: ...
	def HasInit(self) -> bool: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def InitBlock(self) -> bool: ...
	def MapS(self) -> bool: ...
	def NearestE(self, loe: TopTools_ListOfShape, efound: TopoDS_Edge) -> bool: ...
	def NextinBlock(self) -> bool: ...
	def REGU(self, istep: int, Scur: TopoDS_Shape, Splits: TopTools_ListOfShape) -> bool: ...
	def REGU(self) -> bool: ...
	def RemoveOldConnexity(self, v: TopoDS_Vertex, OriKey: int, e: TopoDS_Edge) -> bool: ...
	def S(self) -> TopoDS_Shape: ...
	def SetEsplits(self, Esplits: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def SetOwNw(self, OwNw: TopTools_DataMapOfShapeListOfShape) -> None: ...
	def SplitEds(self) -> bool: ...
	def UpdateMultiple(self, v: TopoDS_Vertex) -> bool: ...

class TopOpeBRepTool_ShapeClassifier:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, SRef: TopoDS_Shape) -> None: ...
	def ChangeSolidClassifier(self) -> TopOpeBRepTool_SolidClassifier: ...
	def ClearAll(self) -> None: ...
	def ClearCurrent(self) -> None: ...
	def P2D(self) -> gp_Pnt2d: ...
	def P3D(self) -> gp_Pnt: ...
	def SameDomain(self) -> int: ...
	def SameDomain(self, samedomain: int) -> None: ...
	def SetReference(self, SRef: TopoDS_Shape) -> None: ...
	def State(self) -> TopAbs_State: ...
	def StateP2DReference(self, P2D: gp_Pnt2d) -> None: ...
	def StateP3DReference(self, P3D: gp_Pnt) -> None: ...
	def StateShapeReference(self, S: TopoDS_Shape, AvoidS: TopoDS_Shape) -> TopAbs_State: ...
	def StateShapeReference(self, S: TopoDS_Shape, LAvoidS: TopTools_ListOfShape) -> TopAbs_State: ...
	def StateShapeShape(self, S: TopoDS_Shape, SRef: TopoDS_Shape, samedomain: Optional[int]) -> TopAbs_State: ...
	def StateShapeShape(self, S: TopoDS_Shape, AvoidS: TopoDS_Shape, SRef: TopoDS_Shape) -> TopAbs_State: ...
	def StateShapeShape(self, S: TopoDS_Shape, LAvoidS: TopTools_ListOfShape, SRef: TopoDS_Shape) -> TopAbs_State: ...

class TopOpeBRepTool_ShapeExplorer(TopExp_Explorer):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape, ToFind: TopAbs_ShapeEnum, ToAvoid: Optional[TopAbs_ShapeEnum]) -> None: ...
	def Index(self) -> int: ...
	def Init(self, S: TopoDS_Shape, ToFind: TopAbs_ShapeEnum, ToAvoid: Optional[TopAbs_ShapeEnum]) -> None: ...
	def Next(self) -> None: ...

class TopOpeBRepTool_ShapeTool:
	@staticmethod
	def AdjustOnPeriodic(self, S: TopoDS_Shape) -> Tuple[float, float]: ...
	@staticmethod
	def BASISCURVE(self, C: Geom_Curve) -> Geom_Curve: ...
	@staticmethod
	def BASISCURVE(self, E: TopoDS_Edge) -> Geom_Curve: ...
	@staticmethod
	def BASISSURFACE(self, S: Geom_Surface) -> Geom_Surface: ...
	@staticmethod
	def BASISSURFACE(self, F: TopoDS_Face) -> Geom_Surface: ...
	@staticmethod
	def Closed(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> bool: ...
	@staticmethod
	def CurvesSameOriented(self, C1: BRepAdaptor_Curve, C2: BRepAdaptor_Curve) -> bool: ...
	@staticmethod
	def EdgeData(self, BRAC: BRepAdaptor_Curve, P: float, T: gp_Dir, N: gp_Dir) -> Tuple[float, float]: ...
	@staticmethod
	def EdgeData(self, E: TopoDS_Shape, P: float, T: gp_Dir, N: gp_Dir) -> Tuple[float, float]: ...
	@staticmethod
	def EdgesSameOriented(self, E1: TopoDS_Shape, E2: TopoDS_Shape) -> bool: ...
	@staticmethod
	def FacesSameOriented(self, F1: TopoDS_Shape, F2: TopoDS_Shape) -> bool: ...
	@staticmethod
	def PeriodizeParameter(self, par: float, EE: TopoDS_Shape, FF: TopoDS_Shape) -> float: ...
	@staticmethod
	def Pnt(self, S: TopoDS_Shape) -> gp_Pnt: ...
	@staticmethod
	def Resolution3d(self, SU: Geom_Surface, Tol2d: float) -> float: ...
	@staticmethod
	def Resolution3d(self, F: TopoDS_Face, Tol2d: float) -> float: ...
	@staticmethod
	def Resolution3dU(self, SU: Geom_Surface, Tol2d: float) -> float: ...
	@staticmethod
	def Resolution3dV(self, SU: Geom_Surface, Tol2d: float) -> float: ...
	@staticmethod
	def ShapesSameOriented(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> bool: ...
	@staticmethod
	def SurfacesSameOriented(self, S1: BRepAdaptor_Surface, S2: BRepAdaptor_Surface) -> bool: ...
	@staticmethod
	def Tolerance(self, S: TopoDS_Shape) -> float: ...
	@staticmethod
	def UVBOUNDS(self, S: Geom_Surface) -> Tuple[bool, bool, float, float, float, float]: ...
	@staticmethod
	def UVBOUNDS(self, F: TopoDS_Face) -> Tuple[bool, bool, float, float, float, float]: ...

class TopOpeBRepTool_SolidClassifier:
	def __init__(self) -> None: ...
	def Classify(self, S: TopoDS_Solid, P: gp_Pnt, Tol: float) -> TopAbs_State: ...
	def Classify(self, S: TopoDS_Shell, P: gp_Pnt, Tol: float) -> TopAbs_State: ...
	def Clear(self) -> None: ...
	def LoadShell(self, S: TopoDS_Shell) -> None: ...
	def LoadSolid(self, S: TopoDS_Solid) -> None: ...
	def State(self) -> TopAbs_State: ...

class TopOpeBRepTool_TOOL:
	@staticmethod
	def ClosedE(self, E: TopoDS_Edge, vclo: TopoDS_Vertex) -> bool: ...
	@staticmethod
	def ClosedS(self, F: TopoDS_Face) -> bool: ...
	@staticmethod
	def CurvE(self, E: TopoDS_Edge, par: float, tg0: gp_Dir) -> Tuple[bool, float]: ...
	@staticmethod
	def CurvF(self, F: TopoDS_Face, uv: gp_Pnt2d, tg0: gp_Dir) -> Tuple[bool, float, bool]: ...
	@staticmethod
	def EdgeONFace(self, par: float, ed: TopoDS_Edge, uv: gp_Pnt2d, fa: TopoDS_Face) -> Tuple[bool, bool]: ...
	@staticmethod
	def Getduv(self, f: TopoDS_Face, uv: gp_Pnt2d, dir: gp_Vec, factor: float, duv: gp_Dir2d) -> bool: ...
	@staticmethod
	def Getstp3dF(self, p: gp_Pnt, f: TopoDS_Face, uv: gp_Pnt2d, st: TopAbs_State) -> bool: ...
	@staticmethod
	def IsClosingE(self, E: TopoDS_Edge, F: TopoDS_Face) -> bool: ...
	@staticmethod
	def IsClosingE(self, E: TopoDS_Edge, W: TopoDS_Shape, F: TopoDS_Face) -> bool: ...
	@staticmethod
	def IsQuad(self, E: TopoDS_Edge) -> bool: ...
	@staticmethod
	def IsQuad(self, F: TopoDS_Face) -> bool: ...
	@staticmethod
	def IsonCLO(self, PC: Geom2d_Curve, onU: bool, xfirst: float, xperiod: float, xtol: float) -> bool: ...
	@staticmethod
	def IsonCLO(self, C2DF: TopOpeBRepTool_C2DF, onU: bool, xfirst: float, xperiod: float, xtol: float) -> bool: ...
	@staticmethod
	def Matter(self, d1: gp_Vec, d2: gp_Vec, ref: gp_Vec) -> float: ...
	@staticmethod
	def Matter(self, d1: gp_Vec2d, d2: gp_Vec2d) -> float: ...
	@staticmethod
	def Matter(self, xx1: gp_Dir, nt1: gp_Dir, xx2: gp_Dir, nt2: gp_Dir, tola: float) -> Tuple[bool, float]: ...
	@staticmethod
	def Matter(self, f1: TopoDS_Face, f2: TopoDS_Face, e: TopoDS_Edge, pare: float, tola: float) -> Tuple[bool, float]: ...
	@staticmethod
	def MatterKPtg(self, f1: TopoDS_Face, f2: TopoDS_Face, e: TopoDS_Edge) -> Tuple[bool, float]: ...
	@staticmethod
	def MkShell(self, lF: TopTools_ListOfShape, She: TopoDS_Shape) -> None: ...
	@staticmethod
	def NgApp(self, par: float, E: TopoDS_Edge, F: TopoDS_Face, tola: float, ngApp: gp_Dir) -> bool: ...
	@staticmethod
	def NggeomF(self, uv: gp_Pnt2d, F: TopoDS_Face, ng: gp_Vec) -> bool: ...
	@staticmethod
	def Nt(self, uv: gp_Pnt2d, f: TopoDS_Face, normt: gp_Dir) -> bool: ...
	@staticmethod
	def OnBoundary(self, par: float, E: TopoDS_Edge) -> int: ...
	@staticmethod
	def OriinSor(self, sub: TopoDS_Shape, S: TopoDS_Shape, checkclo: Optional[bool]) -> int: ...
	@staticmethod
	def OriinSorclosed(self, sub: TopoDS_Shape, S: TopoDS_Shape) -> int: ...
	@staticmethod
	def ParE(self, Iv: int, E: TopoDS_Edge) -> float: ...
	@staticmethod
	def ParE2d(self, p2d: gp_Pnt2d, e: TopoDS_Edge, f: TopoDS_Face) -> Tuple[bool, float, float]: ...
	@staticmethod
	def ParISO(self, p2d: gp_Pnt2d, e: TopoDS_Edge, f: TopoDS_Face) -> Tuple[bool, float]: ...
	@staticmethod
	def Remove(self, loS: TopTools_ListOfShape, toremove: TopoDS_Shape) -> bool: ...
	@staticmethod
	def SplitE(self, Eanc: TopoDS_Edge, Splits: TopTools_ListOfShape) -> bool: ...
	@staticmethod
	def Tg2d(self, iv: int, E: TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF) -> gp_Vec2d: ...
	@staticmethod
	def Tg2dApp(self, iv: int, E: TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF, factor: float) -> gp_Vec2d: ...
	@staticmethod
	def TgINSIDE(self, v: TopoDS_Vertex, E: TopoDS_Edge, Tg: gp_Vec) -> Tuple[bool, int]: ...
	@staticmethod
	def TggeomE(self, par: float, BC: BRepAdaptor_Curve, Tg: gp_Vec) -> bool: ...
	@staticmethod
	def TggeomE(self, par: float, E: TopoDS_Edge, Tg: gp_Vec) -> bool: ...
	@staticmethod
	def TolP(self, E: TopoDS_Edge, F: TopoDS_Face) -> float: ...
	@staticmethod
	def TolUV(self, F: TopoDS_Face, tol3d: float) -> float: ...
	@staticmethod
	def TrslUV(self, t2d: gp_Vec2d, C2DF: TopOpeBRepTool_C2DF) -> None: ...
	@staticmethod
	def TrslUVModifE(self, t2d: gp_Vec2d, F: TopoDS_Face, E: TopoDS_Edge) -> bool: ...
	@staticmethod
	def UVF(self, par: float, C2DF: TopOpeBRepTool_C2DF) -> gp_Pnt2d: ...
	@staticmethod
	def UVISO(self, PC: Geom2d_Curve, d2d: gp_Dir2d, o2d: gp_Pnt2d) -> Tuple[bool, bool, bool]: ...
	@staticmethod
	def UVISO(self, C2DF: TopOpeBRepTool_C2DF, d2d: gp_Dir2d, o2d: gp_Pnt2d) -> Tuple[bool, bool, bool]: ...
	@staticmethod
	def UVISO(self, E: TopoDS_Edge, F: TopoDS_Face, d2d: gp_Dir2d, o2d: gp_Pnt2d) -> Tuple[bool, bool, bool]: ...
	@staticmethod
	def Vertex(self, Iv: int, E: TopoDS_Edge) -> TopoDS_Vertex: ...
	@staticmethod
	def Vertices(self, E: TopoDS_Edge, Vces: TopTools_Array1OfShape) -> None: ...
	@staticmethod
	def WireToFace(self, Fref: TopoDS_Face, mapWlow: TopTools_DataMapOfShapeListOfShape, lFs: TopTools_ListOfShape) -> bool: ...
	@staticmethod
	def XX(self, uv: gp_Pnt2d, f: TopoDS_Face, par: float, e: TopoDS_Edge, xx: gp_Dir) -> bool: ...
	@staticmethod
	def minDUV(self, F: TopoDS_Face) -> float: ...
	@staticmethod
	def outUVbounds(self, uv: gp_Pnt2d, F: TopoDS_Face) -> bool: ...
	@staticmethod
	def stuvF(self, uv: gp_Pnt2d, F: TopoDS_Face) -> Tuple[int, int]: ...
	@staticmethod
	def tryNgApp(self, par: float, E: TopoDS_Edge, F: TopoDS_Face, tola: float, ng: gp_Dir) -> bool: ...
	@staticmethod
	def tryOriEinF(self, par: float, E: TopoDS_Edge, F: TopoDS_Face) -> int: ...
	@staticmethod
	def tryTg2dApp(self, iv: int, E: TopoDS_Edge, C2DF: TopOpeBRepTool_C2DF, factor: float) -> gp_Vec2d: ...
	@staticmethod
	def uvApp(self, f: TopoDS_Face, e: TopoDS_Edge, par: float, eps: float, uvapp: gp_Pnt2d) -> bool: ...

class TopOpeBRepTool_connexity:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Key: TopoDS_Shape) -> None: ...
	def AddItem(self, OriKey: int, Item: TopTools_ListOfShape) -> None: ...
	def AddItem(self, OriKey: int, Item: TopoDS_Shape) -> None: ...
	def AllItems(self, Item: TopTools_ListOfShape) -> int: ...
	def ChangeItem(self, OriKey: int) -> TopTools_ListOfShape: ...
	def IsFaulty(self) -> bool: ...
	def IsInternal(self, Item: TopTools_ListOfShape) -> int: ...
	def IsMultiple(self) -> bool: ...
	def Item(self, OriKey: int, Item: TopTools_ListOfShape) -> int: ...
	def Key(self) -> TopoDS_Shape: ...
	def RemoveItem(self, OriKey: int, Item: TopoDS_Shape) -> bool: ...
	def RemoveItem(self, Item: TopoDS_Shape) -> bool: ...
	def SetKey(self, Key: TopoDS_Shape) -> None: ...

class TopOpeBRepTool_face:
	def __init__(self) -> None: ...
	def Ffinite(self) -> TopoDS_Face: ...
	def Finite(self) -> bool: ...
	def Init(self, W: TopoDS_Wire, Fref: TopoDS_Face) -> bool: ...
	def IsDone(self) -> bool: ...
	def RealF(self) -> TopoDS_Face: ...
	def W(self) -> TopoDS_Wire: ...

class TopOpeBRepTool_makeTransition:
	def __init__(self) -> None: ...
	def Getfactor(self) -> float: ...
	def HasRest(self) -> bool: ...
	def Initialize(self, E: TopoDS_Edge, pbef: float, paft: float, parE: float, FS: TopoDS_Face, uv: gp_Pnt2d, factor: float) -> bool: ...
	def IsT2d(self) -> bool: ...
	def MkT2donE(self, stb: TopAbs_State, sta: TopAbs_State) -> bool: ...
	def MkT3dproj(self, stb: TopAbs_State, sta: TopAbs_State) -> bool: ...
	def MkT3onE(self, stb: TopAbs_State, sta: TopAbs_State) -> bool: ...
	def MkTonE(self, stb: TopAbs_State, sta: TopAbs_State) -> bool: ...
	def SetRest(self, ES: TopoDS_Edge, parES: float) -> bool: ...
	def Setfactor(self, factor: float) -> None: ...

#classnotwrapped
class TopOpeBRepTool_STATE:
	pass

#classnotwrapped
class TopOpeBRepTool_mkTondgE:
	pass
