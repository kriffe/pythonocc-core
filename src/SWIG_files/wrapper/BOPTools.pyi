from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.IntTools import *
from OCC.Core.gp import *
from OCC.Core.TopAbs import *
from OCC.Core.TopTools import *
from OCC.Core.Message import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.BRepAdaptor import *

#the following typedef cannot be wrapped as is
BOPTools_Box2dPairSelector = NewType('BOPTools_Box2dPairSelector', Any)
#the following typedef cannot be wrapped as is
BOPTools_Box2dTree = NewType('BOPTools_Box2dTree', Any)
#the following typedef cannot be wrapped as is
BOPTools_Box2dTreeSelector = NewType('BOPTools_Box2dTreeSelector', Any)
#the following typedef cannot be wrapped as is
BOPTools_BoxPairSelector = NewType('BOPTools_BoxPairSelector', Any)
#the following typedef cannot be wrapped as is
BOPTools_BoxTree = NewType('BOPTools_BoxTree', Any)
#the following typedef cannot be wrapped as is
BOPTools_BoxTreeSelector = NewType('BOPTools_BoxTreeSelector', Any)
#the following typedef cannot be wrapped as is
BOPTools_IndexedDataMapOfSetShape = NewType('BOPTools_IndexedDataMapOfSetShape', Any)
#the following typedef cannot be wrapped as is
BOPTools_ListIteratorOfListOfConnexityBlock = NewType('BOPTools_ListIteratorOfListOfConnexityBlock', Any)
#the following typedef cannot be wrapped as is
BOPTools_ListIteratorOfListOfCoupleOfShape = NewType('BOPTools_ListIteratorOfListOfCoupleOfShape', Any)
#the following typedef cannot be wrapped as is
BOPTools_ListOfConnexityBlock = NewType('BOPTools_ListOfConnexityBlock', Any)
#the following typedef cannot be wrapped as is
BOPTools_ListOfCoupleOfShape = NewType('BOPTools_ListOfCoupleOfShape', Any)
#the following typedef cannot be wrapped as is
BOPTools_MapIteratorOfMapOfSet = NewType('BOPTools_MapIteratorOfMapOfSet', Any)
#the following typedef cannot be wrapped as is
BOPTools_MapOfSet = NewType('BOPTools_MapOfSet', Any)

class BOPTools_AlgoTools:
	@staticmethod
	def AreFacesSameDomain(self, theF1: TopoDS_Face, theF2: TopoDS_Face, theContext: IntTools_Context, theFuzz: Optional[float]) -> bool: ...
	@overload
	@staticmethod
	def ComputeState(self, thePoint: gp_Pnt, theSolid: TopoDS_Solid, theTol: float, theContext: IntTools_Context) -> TopAbs_State: ...
	@overload
	@staticmethod
	def ComputeState(self, theVertex: TopoDS_Vertex, theSolid: TopoDS_Solid, theTol: float, theContext: IntTools_Context) -> TopAbs_State: ...
	@overload
	@staticmethod
	def ComputeState(self, theEdge: TopoDS_Edge, theSolid: TopoDS_Solid, theTol: float, theContext: IntTools_Context) -> TopAbs_State: ...
	@overload
	@staticmethod
	def ComputeState(self, theFace: TopoDS_Face, theSolid: TopoDS_Solid, theTol: float, theBounds: TopTools_IndexedMapOfShape, theContext: IntTools_Context) -> TopAbs_State: ...
	@staticmethod
	def ComputeStateByOnePoint(self, theShape: TopoDS_Shape, theSolid: TopoDS_Solid, theTol: float, theContext: IntTools_Context) -> TopAbs_State: ...
	@staticmethod
	def ComputeTolerance(self, theFace: TopoDS_Face, theEdge: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	@overload
	@staticmethod
	def ComputeVV(self, theV: TopoDS_Vertex, theP: gp_Pnt, theTolP: float) -> int: ...
	@overload
	@staticmethod
	def ComputeVV(self, theV1: TopoDS_Vertex, theV2: TopoDS_Vertex, theFuzz: Optional[float]) -> int: ...
	@staticmethod
	def CopyEdge(self, theEdge: TopoDS_Edge) -> TopoDS_Edge: ...
	@staticmethod
	def CorrectCurveOnSurface(self, theS: TopoDS_Shape, theMapToAvoid: TopTools_IndexedMapOfShape, theTolMax: Optional[float], theRunParallel: Optional[bool]) -> None: ...
	@staticmethod
	def CorrectPointOnCurve(self, theS: TopoDS_Shape, theMapToAvoid: TopTools_IndexedMapOfShape, theTolMax: Optional[float], theRunParallel: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def CorrectRange(self, aE1: TopoDS_Edge, aE2: TopoDS_Edge, aSR: IntTools_Range, aNewSR: IntTools_Range) -> None: ...
	@overload
	@staticmethod
	def CorrectRange(self, aE: TopoDS_Edge, aF: TopoDS_Face, aSR: IntTools_Range, aNewSR: IntTools_Range) -> None: ...
	@staticmethod
	def CorrectShapeTolerances(self, theS: TopoDS_Shape, theMapToAvoid: TopTools_IndexedMapOfShape, theRunParallel: Optional[bool]) -> None: ...
	@staticmethod
	def CorrectTolerances(self, theS: TopoDS_Shape, theMapToAvoid: TopTools_IndexedMapOfShape, theTolMax: Optional[float], theRunParallel: Optional[bool]) -> None: ...
	@staticmethod
	def Dimension(self, theS: TopoDS_Shape) -> int: ...
	@staticmethod
	def GetEdgeOff(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face, theEdgeOff: TopoDS_Edge) -> bool: ...
	@staticmethod
	def GetEdgeOnFace(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face, theEdgeOnF: TopoDS_Edge) -> bool: ...
	@staticmethod
	def GetFaceOff(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face, theLCEF: BOPTools_ListOfCoupleOfShape, theFaceOff: TopoDS_Face, theContext: IntTools_Context) -> bool: ...
	@staticmethod
	def IsBlockInOnFace(self, aShR: IntTools_Range, aF: TopoDS_Face, aE: TopoDS_Edge, aContext: IntTools_Context) -> bool: ...
	@staticmethod
	def IsHole(self, theW: TopoDS_Shape, theF: TopoDS_Shape) -> bool: ...
	@overload
	@staticmethod
	def IsInternalFace(self, theFace: TopoDS_Face, theEdge: TopoDS_Edge, theFace1: TopoDS_Face, theFace2: TopoDS_Face, theContext: IntTools_Context) -> int: ...
	@overload
	@staticmethod
	def IsInternalFace(self, theFace: TopoDS_Face, theEdge: TopoDS_Edge, theLF: TopTools_ListOfShape, theContext: IntTools_Context) -> int: ...
	@overload
	@staticmethod
	def IsInternalFace(self, theFace: TopoDS_Face, theSolid: TopoDS_Solid, theMEF: TopTools_IndexedDataMapOfShapeListOfShape, theTol: float, theContext: IntTools_Context) -> bool: ...
	@staticmethod
	def IsInvertedSolid(self, theSolid: TopoDS_Solid) -> bool: ...
	@staticmethod
	def IsMicroEdge(self, theEdge: TopoDS_Edge, theContext: IntTools_Context, theCheckSplittable: Optional[bool]) -> bool: ...
	@staticmethod
	def IsOpenShell(self, theShell: TopoDS_Shell) -> bool: ...
	@overload
	@staticmethod
	def IsSplitToReverse(self, theSplit: TopoDS_Shape, theShape: TopoDS_Shape, theContext: IntTools_Context, theError: Optional[int]) -> bool: ...
	@overload
	@staticmethod
	def IsSplitToReverse(self, theSplit: TopoDS_Face, theShape: TopoDS_Face, theContext: IntTools_Context, theError: Optional[int]) -> bool: ...
	@overload
	@staticmethod
	def IsSplitToReverse(self, theSplit: TopoDS_Edge, theShape: TopoDS_Edge, theContext: IntTools_Context, theError: Optional[int]) -> bool: ...
	@staticmethod
	def IsSplitToReverseWithWarn(self, theSplit: TopoDS_Shape, theShape: TopoDS_Shape, theContext: IntTools_Context, theReport: Optional[Message_Report]) -> bool: ...
	@staticmethod
	def MakeConnexityBlock(self, theLS: TopTools_ListOfShape, theMapAvoid: TopTools_IndexedMapOfShape, theLSCB: TopTools_ListOfShape, theAllocator: NCollection_BaseAllocator) -> None: ...
	@overload
	@staticmethod
	def MakeConnexityBlocks(self, theS: TopoDS_Shape, theConnectionType: TopAbs_ShapeEnum, theElementType: TopAbs_ShapeEnum, theLCB: TopTools_ListOfShape) -> None: ...
	@overload
	@staticmethod
	def MakeConnexityBlocks(self, theS: TopoDS_Shape, theConnectionType: TopAbs_ShapeEnum, theElementType: TopAbs_ShapeEnum, theLCB: TopTools_ListOfListOfShape, theConnectionMap: TopTools_IndexedDataMapOfShapeListOfShape) -> None: ...
	@overload
	@staticmethod
	def MakeConnexityBlocks(self, theLS: TopTools_ListOfShape, theConnectionType: TopAbs_ShapeEnum, theElementType: TopAbs_ShapeEnum, theLCB: BOPTools_ListOfConnexityBlock) -> None: ...
	@staticmethod
	def MakeContainer(self, theType: TopAbs_ShapeEnum, theShape: TopoDS_Shape) -> None: ...
	@staticmethod
	def MakeEdge(self, theCurve: IntTools_Curve, theV1: TopoDS_Vertex, theT1: float, theV2: TopoDS_Vertex, theT2: float, theTolR3D: float, theE: TopoDS_Edge) -> None: ...
	@overload
	@staticmethod
	def MakeNewVertex(self, aP1: gp_Pnt, aTol: float, aNewVertex: TopoDS_Vertex) -> None: ...
	@overload
	@staticmethod
	def MakeNewVertex(self, aV1: TopoDS_Vertex, aV2: TopoDS_Vertex, aNewVertex: TopoDS_Vertex) -> None: ...
	@overload
	@staticmethod
	def MakeNewVertex(self, aE1: TopoDS_Edge, aP1: float, aE2: TopoDS_Edge, aP2: float, aNewVertex: TopoDS_Vertex) -> None: ...
	@overload
	@staticmethod
	def MakeNewVertex(self, aE1: TopoDS_Edge, aP1: float, aF2: TopoDS_Face, aNewVertex: TopoDS_Vertex) -> None: ...
	@staticmethod
	def MakePCurve(self, theE: TopoDS_Edge, theF1: TopoDS_Face, theF2: TopoDS_Face, theCurve: IntTools_Curve, thePC1: bool, thePC2: bool, theContext: Optional[IntTools_Context]) -> None: ...
	@staticmethod
	def MakeSectEdge(self, aIC: IntTools_Curve, aV1: TopoDS_Vertex, aP1: float, aV2: TopoDS_Vertex, aP2: float, aNewEdge: TopoDS_Edge) -> None: ...
	@staticmethod
	def MakeSplitEdge(self, aE1: TopoDS_Edge, aV1: TopoDS_Vertex, aP1: float, aV2: TopoDS_Vertex, aP2: float, aNewEdge: TopoDS_Edge) -> None: ...
	@staticmethod
	def MakeVertex(self, theLV: TopTools_ListOfShape, theV: TopoDS_Vertex) -> None: ...
	@staticmethod
	def OrientEdgesOnWire(self, theWire: TopoDS_Shape) -> None: ...
	@staticmethod
	def OrientFacesOnShell(self, theShell: TopoDS_Shape) -> None: ...
	@staticmethod
	def PointOnEdge(self, aEdge: TopoDS_Edge, aPrm: float, aP: gp_Pnt) -> None: ...
	@staticmethod
	def Sense(self, theF1: TopoDS_Face, theF2: TopoDS_Face, theContext: IntTools_Context) -> int: ...
	@overload
	@staticmethod
	def UpdateVertex(self, aIC: IntTools_Curve, aT: float, aV: TopoDS_Vertex) -> None: ...
	@overload
	@staticmethod
	def UpdateVertex(self, aE: TopoDS_Edge, aT: float, aV: TopoDS_Vertex) -> None: ...
	@overload
	@staticmethod
	def UpdateVertex(self, aVF: TopoDS_Vertex, aVN: TopoDS_Vertex) -> None: ...

class BOPTools_AlgoTools2D:
	@overload
	@staticmethod
	def AdjustPCurveOnFace(self, theF: TopoDS_Face, theC3D: Geom_Curve, theC2D: Geom2d_Curve, theC2DA: Geom2d_Curve, theContext: Optional[IntTools_Context]) -> None: ...
	@overload
	@staticmethod
	def AdjustPCurveOnFace(self, theF: TopoDS_Face, theFirst: float, theLast: float, theC2D: Geom2d_Curve, theC2DA: Geom2d_Curve, theContext: Optional[IntTools_Context]) -> None: ...
	@staticmethod
	def AdjustPCurveOnSurf(self, aF: BRepAdaptor_Surface, aT1: float, aT2: float, aC2D: Geom2d_Curve, aC2DA: Geom2d_Curve) -> None: ...
	@staticmethod
	def AttachExistingPCurve(self, aEold: TopoDS_Edge, aEnew: TopoDS_Edge, aF: TopoDS_Face, aCtx: IntTools_Context) -> int: ...
	@staticmethod
	def BuildPCurveForEdgeOnFace(self, aE: TopoDS_Edge, aF: TopoDS_Face, theContext: Optional[IntTools_Context]) -> None: ...
	@overload
	@staticmethod
	def CurveOnSurface(self, aE: TopoDS_Edge, aF: TopoDS_Face, aC: Geom2d_Curve, theContext: Optional[IntTools_Context]) -> float: ...
	@overload
	@staticmethod
	def CurveOnSurface(self, aE: TopoDS_Edge, aF: TopoDS_Face, aC: Geom2d_Curve, theContext: Optional[IntTools_Context]) -> Tuple[float, float, float]: ...
	@staticmethod
	def EdgeTangent(self, anE: TopoDS_Edge, aT: float, Tau: gp_Vec) -> bool: ...
	@overload
	@staticmethod
	def HasCurveOnSurface(self, aE: TopoDS_Edge, aF: TopoDS_Face, aC: Geom2d_Curve) -> Tuple[bool, float, float, float]: ...
	@overload
	@staticmethod
	def HasCurveOnSurface(self, aE: TopoDS_Edge, aF: TopoDS_Face) -> bool: ...
	@overload
	@staticmethod
	def IntermediatePoint(self, aFirst: float, aLast: float) -> float: ...
	@overload
	@staticmethod
	def IntermediatePoint(self, anE: TopoDS_Edge) -> float: ...
	@staticmethod
	def IsEdgeIsoline(self, theE: TopoDS_Edge, theF: TopoDS_Face) -> Tuple[bool, bool]: ...
	@staticmethod
	def Make2D(self, aE: TopoDS_Edge, aF: TopoDS_Face, aC: Geom2d_Curve, theContext: Optional[IntTools_Context]) -> Tuple[float, float, float]: ...
	@overload
	@staticmethod
	def MakePCurveOnFace(self, aF: TopoDS_Face, C3D: Geom_Curve, aC: Geom2d_Curve, theContext: Optional[IntTools_Context]) -> float: ...
	@overload
	@staticmethod
	def MakePCurveOnFace(self, aF: TopoDS_Face, C3D: Geom_Curve, aT1: float, aT2: float, aC: Geom2d_Curve, theContext: Optional[IntTools_Context]) -> float: ...
	@staticmethod
	def PointOnSurface(self, aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, theContext: Optional[IntTools_Context]) -> Tuple[float, float]: ...

class BOPTools_AlgoTools3D:
	@staticmethod
	def DoSplitSEAMOnFace(self, aSp: TopoDS_Edge, aF: TopoDS_Face) -> None: ...
	@overload
	@staticmethod
	def GetApproxNormalToFaceOnEdge(self, aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, aPx: gp_Pnt, aD: gp_Dir, theContext: IntTools_Context) -> bool: ...
	@overload
	@staticmethod
	def GetApproxNormalToFaceOnEdge(self, theE: TopoDS_Edge, theF: TopoDS_Face, aT: float, aP: gp_Pnt, aDNF: gp_Dir, aDt2D: float) -> bool: ...
	@overload
	@staticmethod
	def GetApproxNormalToFaceOnEdge(self, theE: TopoDS_Edge, theF: TopoDS_Face, aT: float, aDt2D: float, aP: gp_Pnt, aDNF: gp_Dir, theContext: IntTools_Context) -> bool: ...
	@overload
	@staticmethod
	def GetNormalToFaceOnEdge(self, aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, aD: gp_Dir, theContext: Optional[IntTools_Context]) -> None: ...
	@overload
	@staticmethod
	def GetNormalToFaceOnEdge(self, aE: TopoDS_Edge, aF: TopoDS_Face, aD: gp_Dir, theContext: Optional[IntTools_Context]) -> None: ...
	@staticmethod
	def GetNormalToSurface(self, aS: Geom_Surface, U: float, V: float, aD: gp_Dir) -> bool: ...
	@staticmethod
	def IsEmptyShape(self, aS: TopoDS_Shape) -> bool: ...
	@staticmethod
	def MinStepIn2d(self) -> float: ...
	@staticmethod
	def OrientEdgeOnFace(self, aE: TopoDS_Edge, aF: TopoDS_Face, aER: TopoDS_Edge) -> None: ...
	@overload
	@staticmethod
	def PointInFace(self, theF: TopoDS_Face, theP: gp_Pnt, theP2D: gp_Pnt2d, theContext: IntTools_Context) -> int: ...
	@overload
	@staticmethod
	def PointInFace(self, theF: TopoDS_Face, theE: TopoDS_Edge, theT: float, theDt2D: float, theP: gp_Pnt, theP2D: gp_Pnt2d, theContext: IntTools_Context) -> int: ...
	@overload
	@staticmethod
	def PointInFace(self, theF: TopoDS_Face, theL: Geom2d_Curve, theP: gp_Pnt, theP2D: gp_Pnt2d, theContext: IntTools_Context, theDt2D: Optional[float]) -> int: ...
	@overload
	@staticmethod
	def PointNearEdge(self, aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, aDt2D: float, aP2D: gp_Pnt2d, aPx: gp_Pnt, theContext: IntTools_Context) -> int: ...
	@overload
	@staticmethod
	def PointNearEdge(self, aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, aDt2D: float, aP2D: gp_Pnt2d, aPx: gp_Pnt) -> int: ...
	@overload
	@staticmethod
	def PointNearEdge(self, aE: TopoDS_Edge, aF: TopoDS_Face, aT: float, aP2D: gp_Pnt2d, aPx: gp_Pnt, theContext: IntTools_Context) -> int: ...
	@overload
	@staticmethod
	def PointNearEdge(self, aE: TopoDS_Edge, aF: TopoDS_Face, aP2D: gp_Pnt2d, aPx: gp_Pnt, theContext: IntTools_Context) -> int: ...
	@staticmethod
	def SenseFlag(self, aNF1: gp_Dir, aNF2: gp_Dir) -> int: ...

class BOPTools_ConnexityBlock:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def ChangeLoops(self) -> TopTools_ListOfShape: ...
	def ChangeShapes(self) -> TopTools_ListOfShape: ...
	def IsRegular(self) -> bool: ...
	def Loops(self) -> TopTools_ListOfShape: ...
	def SetRegular(self, theFlag: bool) -> None: ...
	def Shapes(self) -> TopTools_ListOfShape: ...

class BOPTools_CoupleOfShape:
	def __init__(self) -> None: ...
	def SetShape1(self, theShape: TopoDS_Shape) -> None: ...
	def SetShape2(self, theShape: TopoDS_Shape) -> None: ...
	def Shape1(self) -> TopoDS_Shape: ...
	def Shape2(self) -> TopoDS_Shape: ...

class BOPTools_Set:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def Add(self, theS: TopoDS_Shape, theType: TopAbs_ShapeEnum) -> None: ...
	def Assign(self, Other: BOPTools_Set) -> BOPTools_Set: ...
	def HashCode(self, theUpperBound: int) -> int: ...
	def IsEqual(self, aOther: BOPTools_Set) -> bool: ...
	def NbShapes(self) -> int: ...
	def Shape(self) -> TopoDS_Shape: ...

class BOPTools_SetMapHasher:
	@staticmethod
	def HashCode(self, theSet: BOPTools_Set, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(self, aSet1: BOPTools_Set, aSet2: BOPTools_Set) -> bool: ...

#classnotwrapped
class BOPTools_Parallel:
	pass

#classnotwrapped
class BOPTools_BoxSelector:
	pass

#classnotwrapped
class BOPTools_BoxSet:
	pass

#classnotwrapped
class BOPTools_PairSelector:
	pass
BOPTools_AlgoTools_AreFacesSameDomain = BOPTools_AlgoTools.AreFacesSameDomain
BOPTools_AlgoTools_ComputeState = BOPTools_AlgoTools.ComputeState
BOPTools_AlgoTools_ComputeState = BOPTools_AlgoTools.ComputeState
BOPTools_AlgoTools_ComputeState = BOPTools_AlgoTools.ComputeState
BOPTools_AlgoTools_ComputeState = BOPTools_AlgoTools.ComputeState
BOPTools_AlgoTools_ComputeStateByOnePoint = BOPTools_AlgoTools.ComputeStateByOnePoint
BOPTools_AlgoTools_ComputeTolerance = BOPTools_AlgoTools.ComputeTolerance
BOPTools_AlgoTools_ComputeVV = BOPTools_AlgoTools.ComputeVV
BOPTools_AlgoTools_ComputeVV = BOPTools_AlgoTools.ComputeVV
BOPTools_AlgoTools_CopyEdge = BOPTools_AlgoTools.CopyEdge
BOPTools_AlgoTools_CorrectCurveOnSurface = BOPTools_AlgoTools.CorrectCurveOnSurface
BOPTools_AlgoTools_CorrectPointOnCurve = BOPTools_AlgoTools.CorrectPointOnCurve
BOPTools_AlgoTools_CorrectRange = BOPTools_AlgoTools.CorrectRange
BOPTools_AlgoTools_CorrectRange = BOPTools_AlgoTools.CorrectRange
BOPTools_AlgoTools_CorrectShapeTolerances = BOPTools_AlgoTools.CorrectShapeTolerances
BOPTools_AlgoTools_CorrectTolerances = BOPTools_AlgoTools.CorrectTolerances
BOPTools_AlgoTools_Dimension = BOPTools_AlgoTools.Dimension
BOPTools_AlgoTools_GetEdgeOff = BOPTools_AlgoTools.GetEdgeOff
BOPTools_AlgoTools_GetEdgeOnFace = BOPTools_AlgoTools.GetEdgeOnFace
BOPTools_AlgoTools_GetFaceOff = BOPTools_AlgoTools.GetFaceOff
BOPTools_AlgoTools_IsBlockInOnFace = BOPTools_AlgoTools.IsBlockInOnFace
BOPTools_AlgoTools_IsHole = BOPTools_AlgoTools.IsHole
BOPTools_AlgoTools_IsInternalFace = BOPTools_AlgoTools.IsInternalFace
BOPTools_AlgoTools_IsInternalFace = BOPTools_AlgoTools.IsInternalFace
BOPTools_AlgoTools_IsInternalFace = BOPTools_AlgoTools.IsInternalFace
BOPTools_AlgoTools_IsInvertedSolid = BOPTools_AlgoTools.IsInvertedSolid
BOPTools_AlgoTools_IsMicroEdge = BOPTools_AlgoTools.IsMicroEdge
BOPTools_AlgoTools_IsOpenShell = BOPTools_AlgoTools.IsOpenShell
BOPTools_AlgoTools_IsSplitToReverse = BOPTools_AlgoTools.IsSplitToReverse
BOPTools_AlgoTools_IsSplitToReverse = BOPTools_AlgoTools.IsSplitToReverse
BOPTools_AlgoTools_IsSplitToReverse = BOPTools_AlgoTools.IsSplitToReverse
BOPTools_AlgoTools_IsSplitToReverseWithWarn = BOPTools_AlgoTools.IsSplitToReverseWithWarn
BOPTools_AlgoTools_MakeConnexityBlock = BOPTools_AlgoTools.MakeConnexityBlock
BOPTools_AlgoTools_MakeConnexityBlocks = BOPTools_AlgoTools.MakeConnexityBlocks
BOPTools_AlgoTools_MakeConnexityBlocks = BOPTools_AlgoTools.MakeConnexityBlocks
BOPTools_AlgoTools_MakeConnexityBlocks = BOPTools_AlgoTools.MakeConnexityBlocks
BOPTools_AlgoTools_MakeContainer = BOPTools_AlgoTools.MakeContainer
BOPTools_AlgoTools_MakeEdge = BOPTools_AlgoTools.MakeEdge
BOPTools_AlgoTools_MakeNewVertex = BOPTools_AlgoTools.MakeNewVertex
BOPTools_AlgoTools_MakeNewVertex = BOPTools_AlgoTools.MakeNewVertex
BOPTools_AlgoTools_MakeNewVertex = BOPTools_AlgoTools.MakeNewVertex
BOPTools_AlgoTools_MakeNewVertex = BOPTools_AlgoTools.MakeNewVertex
BOPTools_AlgoTools_MakePCurve = BOPTools_AlgoTools.MakePCurve
BOPTools_AlgoTools_MakeSectEdge = BOPTools_AlgoTools.MakeSectEdge
BOPTools_AlgoTools_MakeSplitEdge = BOPTools_AlgoTools.MakeSplitEdge
BOPTools_AlgoTools_MakeVertex = BOPTools_AlgoTools.MakeVertex
BOPTools_AlgoTools_OrientEdgesOnWire = BOPTools_AlgoTools.OrientEdgesOnWire
BOPTools_AlgoTools_OrientFacesOnShell = BOPTools_AlgoTools.OrientFacesOnShell
BOPTools_AlgoTools_PointOnEdge = BOPTools_AlgoTools.PointOnEdge
BOPTools_AlgoTools_Sense = BOPTools_AlgoTools.Sense
BOPTools_AlgoTools_UpdateVertex = BOPTools_AlgoTools.UpdateVertex
BOPTools_AlgoTools_UpdateVertex = BOPTools_AlgoTools.UpdateVertex
BOPTools_AlgoTools_UpdateVertex = BOPTools_AlgoTools.UpdateVertex
BOPTools_AlgoTools2D_AdjustPCurveOnFace = BOPTools_AlgoTools2D.AdjustPCurveOnFace
BOPTools_AlgoTools2D_AdjustPCurveOnFace = BOPTools_AlgoTools2D.AdjustPCurveOnFace
BOPTools_AlgoTools2D_AdjustPCurveOnSurf = BOPTools_AlgoTools2D.AdjustPCurveOnSurf
BOPTools_AlgoTools2D_AttachExistingPCurve = BOPTools_AlgoTools2D.AttachExistingPCurve
BOPTools_AlgoTools2D_BuildPCurveForEdgeOnFace = BOPTools_AlgoTools2D.BuildPCurveForEdgeOnFace
BOPTools_AlgoTools2D_CurveOnSurface = BOPTools_AlgoTools2D.CurveOnSurface
BOPTools_AlgoTools2D_CurveOnSurface = BOPTools_AlgoTools2D.CurveOnSurface
BOPTools_AlgoTools2D_EdgeTangent = BOPTools_AlgoTools2D.EdgeTangent
BOPTools_AlgoTools2D_HasCurveOnSurface = BOPTools_AlgoTools2D.HasCurveOnSurface
BOPTools_AlgoTools2D_HasCurveOnSurface = BOPTools_AlgoTools2D.HasCurveOnSurface
BOPTools_AlgoTools2D_IntermediatePoint = BOPTools_AlgoTools2D.IntermediatePoint
BOPTools_AlgoTools2D_IntermediatePoint = BOPTools_AlgoTools2D.IntermediatePoint
BOPTools_AlgoTools2D_IsEdgeIsoline = BOPTools_AlgoTools2D.IsEdgeIsoline
BOPTools_AlgoTools2D_Make2D = BOPTools_AlgoTools2D.Make2D
BOPTools_AlgoTools2D_MakePCurveOnFace = BOPTools_AlgoTools2D.MakePCurveOnFace
BOPTools_AlgoTools2D_MakePCurveOnFace = BOPTools_AlgoTools2D.MakePCurveOnFace
BOPTools_AlgoTools2D_PointOnSurface = BOPTools_AlgoTools2D.PointOnSurface
BOPTools_AlgoTools3D_DoSplitSEAMOnFace = BOPTools_AlgoTools3D.DoSplitSEAMOnFace
BOPTools_AlgoTools3D_GetApproxNormalToFaceOnEdge = BOPTools_AlgoTools3D.GetApproxNormalToFaceOnEdge
BOPTools_AlgoTools3D_GetApproxNormalToFaceOnEdge = BOPTools_AlgoTools3D.GetApproxNormalToFaceOnEdge
BOPTools_AlgoTools3D_GetApproxNormalToFaceOnEdge = BOPTools_AlgoTools3D.GetApproxNormalToFaceOnEdge
BOPTools_AlgoTools3D_GetNormalToFaceOnEdge = BOPTools_AlgoTools3D.GetNormalToFaceOnEdge
BOPTools_AlgoTools3D_GetNormalToFaceOnEdge = BOPTools_AlgoTools3D.GetNormalToFaceOnEdge
BOPTools_AlgoTools3D_GetNormalToSurface = BOPTools_AlgoTools3D.GetNormalToSurface
BOPTools_AlgoTools3D_IsEmptyShape = BOPTools_AlgoTools3D.IsEmptyShape
BOPTools_AlgoTools3D_MinStepIn2d = BOPTools_AlgoTools3D.MinStepIn2d
BOPTools_AlgoTools3D_OrientEdgeOnFace = BOPTools_AlgoTools3D.OrientEdgeOnFace
BOPTools_AlgoTools3D_PointInFace = BOPTools_AlgoTools3D.PointInFace
BOPTools_AlgoTools3D_PointInFace = BOPTools_AlgoTools3D.PointInFace
BOPTools_AlgoTools3D_PointInFace = BOPTools_AlgoTools3D.PointInFace
BOPTools_AlgoTools3D_PointNearEdge = BOPTools_AlgoTools3D.PointNearEdge
BOPTools_AlgoTools3D_PointNearEdge = BOPTools_AlgoTools3D.PointNearEdge
BOPTools_AlgoTools3D_PointNearEdge = BOPTools_AlgoTools3D.PointNearEdge
BOPTools_AlgoTools3D_PointNearEdge = BOPTools_AlgoTools3D.PointNearEdge
BOPTools_AlgoTools3D_SenseFlag = BOPTools_AlgoTools3D.SenseFlag
BOPTools_SetMapHasher_HashCode = BOPTools_SetMapHasher.HashCode
BOPTools_SetMapHasher_IsEqual = BOPTools_SetMapHasher.IsEqual
