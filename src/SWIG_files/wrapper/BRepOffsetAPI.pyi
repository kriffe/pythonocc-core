from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRepBuilderAPI import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.TopTools import *
from OCC.Core.Draft import *
from OCC.Core.Geom import *
from OCC.Core.GeomAbs import *
from OCC.Core.BRepFill import *
from OCC.Core.BRepOffset import *
from OCC.Core.BRepPrimAPI import *
from OCC.Core.GeomFill import *
from OCC.Core.Law import *
from OCC.Core.Approx import *

BRepOffsetAPI_Sewing = NewType('BRepOffsetAPI_Sewing', BRepBuilderAPI_Sewing)

class BRepOffsetAPI_DraftAngle(BRepBuilderAPI_ModifyShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def Add(self, F: TopoDS_Face, Direction: gp_Dir, Angle: float, NeutralPlane: gp_Pln, Flag: Optional[bool]) -> None: ...
	def AddDone(self) -> bool: ...
	def Build(self) -> None: ...
	def Clear(self) -> None: ...
	def ConnectedFaces(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def CorrectWires(self) -> None: ...
	def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def Modified(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def ModifiedFaces(self) -> TopTools_ListOfShape: ...
	def ModifiedShape(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
	def ProblematicShape(self) -> TopoDS_Shape: ...
	def Remove(self, F: TopoDS_Face) -> None: ...
	def Status(self) -> Draft_ErrorStatus: ...

class BRepOffsetAPI_FindContigousEdges:
	def __init__(self, tolerance: Optional[float], option: Optional[bool]) -> None: ...
	def Add(self, shape: TopoDS_Shape) -> None: ...
	def ContigousEdge(self, index: int) -> TopoDS_Edge: ...
	def ContigousEdgeCouple(self, index: int) -> TopTools_ListOfShape: ...
	def DegeneratedShape(self, index: int) -> TopoDS_Shape: ...
	def Dump(self) -> None: ...
	def Init(self, tolerance: float, option: bool) -> None: ...
	def IsDegenerated(self, shape: TopoDS_Shape) -> bool: ...
	def IsModified(self, shape: TopoDS_Shape) -> bool: ...
	def Modified(self, shape: TopoDS_Shape) -> TopoDS_Shape: ...
	def NbContigousEdges(self) -> int: ...
	def NbDegeneratedShapes(self) -> int: ...
	def Perform(self) -> None: ...
	def SectionToBoundary(self, section: TopoDS_Edge) -> TopoDS_Edge: ...

class BRepOffsetAPI_MakeDraft(BRepBuilderAPI_MakeShape):
	def __init__(self, Shape: TopoDS_Shape, Dir: gp_Dir, Angle: float) -> None: ...
	def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	@overload
	def Perform(self, LengthMax: float) -> None: ...
	@overload
	def Perform(self, Surface: Geom_Surface, KeepInsideSurface: Optional[bool]) -> None: ...
	@overload
	def Perform(self, StopShape: TopoDS_Shape, KeepOutSide: Optional[bool]) -> None: ...
	def SetDraft(self, IsInternal: Optional[bool]) -> None: ...
	def SetOptions(self, Style: Optional[BRepBuilderAPI_TransitionMode], AngleMin: Optional[float], AngleMax: Optional[float]) -> None: ...
	def Shell(self) -> TopoDS_Shell: ...

class BRepOffsetAPI_MakeEvolved(BRepBuilderAPI_MakeShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theSpine: TopoDS_Shape, theProfile: TopoDS_Wire, theJoinType: Optional[GeomAbs_JoinType], theIsAxeProf: Optional[bool], theIsSolid: Optional[bool], theIsProfOnSpine: Optional[bool], theTol: Optional[float], theIsVolume: Optional[bool], theRunInParallel: Optional[bool]) -> None: ...
	def Bottom(self) -> TopoDS_Shape: ...
	def Build(self) -> None: ...
	def Evolved(self) -> BRepFill_Evolved: ...
	def GeneratedShapes(self, SpineShape: TopoDS_Shape, ProfShape: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Top(self) -> TopoDS_Shape: ...

class BRepOffsetAPI_MakeFilling(BRepBuilderAPI_MakeShape):
	def __init__(self, Degree: Optional[int], NbPtsOnCur: Optional[int], NbIter: Optional[int], Anisotropie: Optional[bool], Tol2d: Optional[float], Tol3d: Optional[float], TolAng: Optional[float], TolCurv: Optional[float], MaxDeg: Optional[int], MaxSegments: Optional[int]) -> None: ...
	@overload
	def Add(self, Constr: TopoDS_Edge, Order: GeomAbs_Shape, IsBound: Optional[bool]) -> int: ...
	@overload
	def Add(self, Constr: TopoDS_Edge, Support: TopoDS_Face, Order: GeomAbs_Shape, IsBound: Optional[bool]) -> int: ...
	@overload
	def Add(self, Support: TopoDS_Face, Order: GeomAbs_Shape) -> int: ...
	@overload
	def Add(self, Point: gp_Pnt) -> int: ...
	@overload
	def Add(self, U: float, V: float, Support: TopoDS_Face, Order: GeomAbs_Shape) -> int: ...
	def Build(self) -> None: ...
	@overload
	def G0Error(self) -> float: ...
	@overload
	def G0Error(self, Index: int) -> float: ...
	@overload
	def G1Error(self) -> float: ...
	@overload
	def G1Error(self, Index: int) -> float: ...
	@overload
	def G2Error(self) -> float: ...
	@overload
	def G2Error(self, Index: int) -> float: ...
	def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def IsDone(self) -> bool: ...
	def LoadInitSurface(self, Surf: TopoDS_Face) -> None: ...
	def SetApproxParam(self, MaxDeg: Optional[int], MaxSegments: Optional[int]) -> None: ...
	def SetConstrParam(self, Tol2d: Optional[float], Tol3d: Optional[float], TolAng: Optional[float], TolCurv: Optional[float]) -> None: ...
	def SetResolParam(self, Degree: Optional[int], NbPtsOnCur: Optional[int], NbIter: Optional[int], Anisotropie: Optional[bool]) -> None: ...

class BRepOffsetAPI_MakeOffset(BRepBuilderAPI_MakeShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Spine: TopoDS_Face, Join: Optional[GeomAbs_JoinType], IsOpenResult: Optional[bool]) -> None: ...
	@overload
	def __init__(self, Spine: TopoDS_Wire, Join: Optional[GeomAbs_JoinType], IsOpenResult: Optional[bool]) -> None: ...
	def AddWire(self, Spine: TopoDS_Wire) -> None: ...
	def Build(self) -> None: ...
	def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	@overload
	def Init(self, Spine: TopoDS_Face, Join: Optional[GeomAbs_JoinType], IsOpenResult: Optional[bool]) -> None: ...
	@overload
	def Init(self, Join: Optional[GeomAbs_JoinType], IsOpenResult: Optional[bool]) -> None: ...
	def Perform(self, Offset: float, Alt: Optional[float]) -> None: ...

class BRepOffsetAPI_MakeOffsetShape(BRepBuilderAPI_MakeShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape, Offset: float, Tol: float, Mode: Optional[BRepOffset_Mode], Intersection: Optional[bool], SelfInter: Optional[bool], Join: Optional[GeomAbs_JoinType], RemoveIntEdges: Optional[bool]) -> None: ...
	def Build(self) -> None: ...
	def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def GeneratedEdge(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def GetJoinType(self) -> GeomAbs_JoinType: ...
	def MakeOffset(self) -> BRepOffset_MakeOffset: ...
	def PerformByJoin(self, S: TopoDS_Shape, Offset: float, Tol: float, Mode: Optional[BRepOffset_Mode], Intersection: Optional[bool], SelfInter: Optional[bool], Join: Optional[GeomAbs_JoinType], RemoveIntEdges: Optional[bool]) -> None: ...
	def PerformBySimple(self, theS: TopoDS_Shape, theOffsetValue: float) -> None: ...

class BRepOffsetAPI_MakePipe(BRepPrimAPI_MakeSweep):
	@overload
	def __init__(self, Spine: TopoDS_Wire, Profile: TopoDS_Shape) -> None: ...
	@overload
	def __init__(self, Spine: TopoDS_Wire, Profile: TopoDS_Shape, aMode: GeomFill_Trihedron, ForceApproxC1: Optional[bool]) -> None: ...
	def Build(self) -> None: ...
	def ErrorOnSurface(self) -> float: ...
	def FirstShape(self) -> TopoDS_Shape: ...
	@overload
	def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	@overload
	def Generated(self, SSpine: TopoDS_Shape, SProfile: TopoDS_Shape) -> TopoDS_Shape: ...
	def LastShape(self) -> TopoDS_Shape: ...
	def Pipe(self) -> BRepFill_Pipe: ...

class BRepOffsetAPI_MakePipeShell(BRepPrimAPI_MakeSweep):
	def __init__(self, Spine: TopoDS_Wire) -> None: ...
	@overload
	def Add(self, Profile: TopoDS_Shape, WithContact: Optional[bool], WithCorrection: Optional[bool]) -> None: ...
	@overload
	def Add(self, Profile: TopoDS_Shape, Location: TopoDS_Vertex, WithContact: Optional[bool], WithCorrection: Optional[bool]) -> None: ...
	def Build(self) -> None: ...
	def Delete(self, Profile: TopoDS_Shape) -> None: ...
	def ErrorOnSurface(self) -> float: ...
	def FirstShape(self) -> TopoDS_Shape: ...
	def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def GetStatus(self) -> BRepBuilderAPI_PipeError: ...
	def IsReady(self) -> bool: ...
	def LastShape(self) -> TopoDS_Shape: ...
	def MakeSolid(self) -> bool: ...
	def Profiles(self, theProfiles: TopTools_ListOfShape) -> None: ...
	def SetDiscreteMode(self) -> None: ...
	def SetForceApproxC1(self, ForceApproxC1: bool) -> None: ...
	@overload
	def SetLaw(self, Profile: TopoDS_Shape, L: Law_Function, WithContact: Optional[bool], WithCorrection: Optional[bool]) -> None: ...
	@overload
	def SetLaw(self, Profile: TopoDS_Shape, L: Law_Function, Location: TopoDS_Vertex, WithContact: Optional[bool], WithCorrection: Optional[bool]) -> None: ...
	def SetMaxDegree(self, NewMaxDegree: int) -> None: ...
	def SetMaxSegments(self, NewMaxSegments: int) -> None: ...
	@overload
	def SetMode(self, IsFrenet: Optional[bool]) -> None: ...
	@overload
	def SetMode(self, Axe: gp_Ax2) -> None: ...
	@overload
	def SetMode(self, BiNormal: gp_Dir) -> None: ...
	@overload
	def SetMode(self, SpineSupport: TopoDS_Shape) -> bool: ...
	@overload
	def SetMode(self, AuxiliarySpine: TopoDS_Wire, CurvilinearEquivalence: bool, KeepContact: Optional[BRepFill_TypeOfContact]) -> None: ...
	def SetTolerance(self, Tol3d: Optional[float], BoundTol: Optional[float], TolAngular: Optional[float]) -> None: ...
	def SetTransitionMode(self, Mode: Optional[BRepBuilderAPI_TransitionMode]) -> None: ...
	def Simulate(self, NumberOfSection: int, Result: TopTools_ListOfShape) -> None: ...
	def Spine(self) -> TopoDS_Wire: ...

class BRepOffsetAPI_MiddlePath(BRepBuilderAPI_MakeShape):
	def __init__(self, aShape: TopoDS_Shape, StartShape: TopoDS_Shape, EndShape: TopoDS_Shape) -> None: ...
	def Build(self) -> None: ...

class BRepOffsetAPI_NormalProjection(BRepBuilderAPI_MakeShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def Add(self, ToProj: TopoDS_Shape) -> None: ...
	def Ancestor(self, E: TopoDS_Edge) -> TopoDS_Shape: ...
	def Build(self) -> None: ...
	def BuildWire(self, Liste: TopTools_ListOfShape) -> bool: ...
	def Compute3d(self, With3d: Optional[bool]) -> None: ...
	def Couple(self, E: TopoDS_Edge) -> TopoDS_Shape: ...
	def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def IsDone(self) -> bool: ...
	def Projection(self) -> TopoDS_Shape: ...
	def SetLimit(self, FaceBoundaries: Optional[bool]) -> None: ...
	def SetMaxDistance(self, MaxDist: float) -> None: ...
	def SetParams(self, Tol3D: float, Tol2D: float, InternalContinuity: GeomAbs_Shape, MaxDegree: int, MaxSeg: int) -> None: ...

class BRepOffsetAPI_ThruSections(BRepBuilderAPI_MakeShape):
	def __init__(self, isSolid: Optional[bool], ruled: Optional[bool], pres3d: Optional[float]) -> None: ...
	def AddVertex(self, aVertex: TopoDS_Vertex) -> None: ...
	def AddWire(self, wire: TopoDS_Wire) -> None: ...
	def Build(self) -> None: ...
	def CheckCompatibility(self, check: Optional[bool]) -> None: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def CriteriumWeight(self) -> Tuple[float, float, float]: ...
	def FirstShape(self) -> TopoDS_Shape: ...
	def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def GeneratedFace(self, Edge: TopoDS_Shape) -> TopoDS_Shape: ...
	def Init(self, isSolid: Optional[bool], ruled: Optional[bool], pres3d: Optional[float]) -> None: ...
	def LastShape(self) -> TopoDS_Shape: ...
	def MaxDegree(self) -> int: ...
	def ParType(self) -> Approx_ParametrizationType: ...
	def SetContinuity(self, C: GeomAbs_Shape) -> None: ...
	def SetCriteriumWeight(self, W1: float, W2: float, W3: float) -> None: ...
	def SetMaxDegree(self, MaxDeg: int) -> None: ...
	def SetParType(self, ParType: Approx_ParametrizationType) -> None: ...
	def SetSmoothing(self, UseSmoothing: bool) -> None: ...
	def UseSmoothing(self) -> bool: ...
	def Wires(self) -> TopTools_ListOfShape: ...

class BRepOffsetAPI_MakeThickSolid(BRepOffsetAPI_MakeOffsetShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape, ClosingFaces: TopTools_ListOfShape, Offset: float, Tol: float, Mode: Optional[BRepOffset_Mode], Intersection: Optional[bool], SelfInter: Optional[bool], Join: Optional[GeomAbs_JoinType], RemoveIntEdges: Optional[bool]) -> None: ...
	def Build(self) -> None: ...
	def MakeThickSolidByJoin(self, S: TopoDS_Shape, ClosingFaces: TopTools_ListOfShape, Offset: float, Tol: float, Mode: Optional[BRepOffset_Mode], Intersection: Optional[bool], SelfInter: Optional[bool], Join: Optional[GeomAbs_JoinType], RemoveIntEdges: Optional[bool]) -> None: ...
	def MakeThickSolidBySimple(self, theS: TopoDS_Shape, theOffsetValue: float) -> None: ...
	def Modified(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
