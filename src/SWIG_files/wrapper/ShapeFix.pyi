from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.ShapeBuild import *
from OCC.Core.Message import *
from OCC.Core.ShapeExtend import *
from OCC.Core.Geom import *
from OCC.Core.TopLoc import *
from OCC.Core.ShapeAnalysis import *
from OCC.Core.ShapeConstruct import *
from OCC.Core.Geom2d import *
from OCC.Core.TopAbs import *
from OCC.Core.TopTools import *

#the following typedef cannot be wrapped as is
ShapeFix_DataMapIteratorOfDataMapOfShapeBox2d = NewType('ShapeFix_DataMapIteratorOfDataMapOfShapeBox2d', Any)
#the following typedef cannot be wrapped as is
ShapeFix_DataMapOfShapeBox2d = NewType('ShapeFix_DataMapOfShapeBox2d', Any)
#the following typedef cannot be wrapped as is
ShapeFix_SequenceOfWireSegment = NewType('ShapeFix_SequenceOfWireSegment', Any)

class ShapeFix:
	@staticmethod
	def EncodeRegularity(self, shape: TopoDS_Shape, tolang: Optional[float]) -> None: ...
	@staticmethod
	def FixVertexPosition(self, theshape: TopoDS_Shape, theTolerance: float, thecontext: ShapeBuild_ReShape) -> bool: ...
	@staticmethod
	def LeastEdgeSize(self, theshape: TopoDS_Shape) -> float: ...
	@staticmethod
	def RemoveSmallEdges(self, shape: TopoDS_Shape, Tolerance: float, context: ShapeBuild_ReShape) -> TopoDS_Shape: ...
	@staticmethod
	def SameParameter(self, shape: TopoDS_Shape, enforce: bool, preci: Optional[float], theProgress: Optional[Message_ProgressIndicator], theMsgReg: Optional[ShapeExtend_BasicMsgRegistrator]) -> bool: ...

class ShapeFix_Edge(Standard_Transient):
	def __init__(self) -> None: ...
	def FixAddCurve3d(self, edge: TopoDS_Edge) -> bool: ...
	@overload
	def FixAddPCurve(self, edge: TopoDS_Edge, face: TopoDS_Face, isSeam: bool, prec: Optional[float]) -> bool: ...
	@overload
	def FixAddPCurve(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location, isSeam: bool, prec: Optional[float]) -> bool: ...
	@overload
	def FixAddPCurve(self, edge: TopoDS_Edge, face: TopoDS_Face, isSeam: bool, surfana: ShapeAnalysis_Surface, prec: Optional[float]) -> bool: ...
	@overload
	def FixAddPCurve(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location, isSeam: bool, surfana: ShapeAnalysis_Surface, prec: Optional[float]) -> bool: ...
	def FixRemoveCurve3d(self, edge: TopoDS_Edge) -> bool: ...
	@overload
	def FixRemovePCurve(self, edge: TopoDS_Edge, face: TopoDS_Face) -> bool: ...
	@overload
	def FixRemovePCurve(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location) -> bool: ...
	@overload
	def FixReversed2d(self, edge: TopoDS_Edge, face: TopoDS_Face) -> bool: ...
	@overload
	def FixReversed2d(self, edge: TopoDS_Edge, surface: Geom_Surface, location: TopLoc_Location) -> bool: ...
	@overload
	def FixSameParameter(self, edge: TopoDS_Edge, tolerance: Optional[float]) -> bool: ...
	@overload
	def FixSameParameter(self, edge: TopoDS_Edge, face: TopoDS_Face, tolerance: Optional[float]) -> bool: ...
	@overload
	def FixVertexTolerance(self, edge: TopoDS_Edge, face: TopoDS_Face) -> bool: ...
	@overload
	def FixVertexTolerance(self, edge: TopoDS_Edge) -> bool: ...
	def Projector(self) -> ShapeConstruct_ProjectCurveOnSurface: ...
	def SetContext(self, context: ShapeBuild_ReShape) -> None: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeFix_EdgeConnect:
	def __init__(self) -> None: ...
	@overload
	def Add(self, aFirst: TopoDS_Edge, aSecond: TopoDS_Edge) -> None: ...
	@overload
	def Add(self, aShape: TopoDS_Shape) -> None: ...
	def Build(self) -> None: ...
	def Clear(self) -> None: ...

class ShapeFix_EdgeProjAux(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, F: TopoDS_Face, E: TopoDS_Edge) -> None: ...
	def Compute(self, preci: float) -> None: ...
	def FirstParam(self) -> float: ...
	def Init(self, F: TopoDS_Face, E: TopoDS_Edge) -> None: ...
	def IsFirstDone(self) -> bool: ...
	def IsIso(self, C: Geom2d_Curve) -> bool: ...
	def IsLastDone(self) -> bool: ...
	def LastParam(self) -> float: ...

class ShapeFix_FaceConnect:
	def __init__(self) -> None: ...
	def Add(self, aFirst: TopoDS_Face, aSecond: TopoDS_Face) -> bool: ...
	def Build(self, shell: TopoDS_Shell, sewtoler: float, fixtoler: float) -> TopoDS_Shell: ...
	def Clear(self) -> None: ...

class ShapeFix_FreeBounds:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, shape: TopoDS_Shape, sewtoler: float, closetoler: float, splitclosed: bool, splitopen: bool) -> None: ...
	@overload
	def __init__(self, shape: TopoDS_Shape, closetoler: float, splitclosed: bool, splitopen: bool) -> None: ...
	def GetClosedWires(self) -> TopoDS_Compound: ...
	def GetOpenWires(self) -> TopoDS_Compound: ...
	def GetShape(self) -> TopoDS_Shape: ...

class ShapeFix_IntersectionTool:
	def __init__(self, context: ShapeBuild_ReShape, preci: float, maxtol: Optional[float]) -> None: ...
	def Context(self) -> ShapeBuild_ReShape: ...
	def CutEdge(self, edge: TopoDS_Edge, pend: float, cut: float, face: TopoDS_Face) -> Tuple[bool, bool]: ...
	def FixIntersectingWires(self, face: TopoDS_Face) -> bool: ...
	def FixSelfIntersectWire(self, sewd: ShapeExtend_WireData, face: TopoDS_Face) -> Tuple[bool, int, int, int]: ...
	def SplitEdge(self, edge: TopoDS_Edge, param: float, vert: TopoDS_Vertex, face: TopoDS_Face, newE1: TopoDS_Edge, newE2: TopoDS_Edge, preci: float) -> bool: ...

class ShapeFix_Root(Standard_Transient):
	def __init__(self) -> None: ...
	def Context(self) -> ShapeBuild_ReShape: ...
	def LimitTolerance(self, toler: float) -> float: ...
	def MaxTolerance(self) -> float: ...
	def MinTolerance(self) -> float: ...
	def MsgRegistrator(self) -> ShapeExtend_BasicMsgRegistrator: ...
	def Precision(self) -> float: ...
	@overload
	def SendFail(self, shape: TopoDS_Shape, message: Message_Msg) -> None: ...
	@overload
	def SendFail(self, message: Message_Msg) -> None: ...
	@overload
	def SendMsg(self, shape: TopoDS_Shape, message: Message_Msg, gravity: Optional[Message_Gravity]) -> None: ...
	@overload
	def SendMsg(self, message: Message_Msg, gravity: Optional[Message_Gravity]) -> None: ...
	@overload
	def SendWarning(self, shape: TopoDS_Shape, message: Message_Msg) -> None: ...
	@overload
	def SendWarning(self, message: Message_Msg) -> None: ...
	def Set(self, Root: ShapeFix_Root) -> None: ...
	def SetContext(self, context: ShapeBuild_ReShape) -> None: ...
	def SetMaxTolerance(self, maxtol: float) -> None: ...
	def SetMinTolerance(self, mintol: float) -> None: ...
	def SetMsgRegistrator(self, msgreg: ShapeExtend_BasicMsgRegistrator) -> None: ...
	def SetPrecision(self, preci: float) -> None: ...

class ShapeFix_ShapeTolerance:
	def __init__(self) -> None: ...
	def LimitTolerance(self, shape: TopoDS_Shape, tmin: float, tmax: Optional[float], styp: Optional[TopAbs_ShapeEnum]) -> bool: ...
	def SetTolerance(self, shape: TopoDS_Shape, preci: float, styp: Optional[TopAbs_ShapeEnum]) -> None: ...

class ShapeFix_SplitTool:
	def __init__(self) -> None: ...
	def CutEdge(self, edge: TopoDS_Edge, pend: float, cut: float, face: TopoDS_Face) -> Tuple[bool, bool]: ...
	@overload
	def SplitEdge(self, edge: TopoDS_Edge, param: float, vert: TopoDS_Vertex, face: TopoDS_Face, newE1: TopoDS_Edge, newE2: TopoDS_Edge, tol3d: float, tol2d: float) -> bool: ...
	@overload
	def SplitEdge(self, edge: TopoDS_Edge, param1: float, param2: float, vert: TopoDS_Vertex, face: TopoDS_Face, newE1: TopoDS_Edge, newE2: TopoDS_Edge, tol3d: float, tol2d: float) -> bool: ...
	@overload
	def SplitEdge(self, edge: TopoDS_Edge, fp: float, V1: TopoDS_Vertex, lp: float, V2: TopoDS_Vertex, face: TopoDS_Face, SeqE: TopTools_SequenceOfShape, context: ShapeBuild_ReShape, tol3d: float, tol2d: float) -> Tuple[bool, int]: ...

class ShapeFix_WireVertex:
	def __init__(self) -> None: ...
	def Analyzer(self) -> ShapeAnalysis_WireVertex: ...
	def Fix(self) -> int: ...
	def FixSame(self) -> int: ...
	@overload
	def Init(self, wire: TopoDS_Wire, preci: float) -> None: ...
	@overload
	def Init(self, sbwd: ShapeExtend_WireData, preci: float) -> None: ...
	@overload
	def Init(self, sawv: ShapeAnalysis_WireVertex) -> None: ...
	def Wire(self) -> TopoDS_Wire: ...
	def WireData(self) -> ShapeExtend_WireData: ...

class ShapeFix_ComposeShell(ShapeFix_Root):
	def __init__(self) -> None: ...
	def GetClosedMode(self) -> bool: ...
	def SetClosedMode(self, value: bool) -> None: ...
	def DispatchWires(self, faces: TopTools_SequenceOfShape, wires: ShapeFix_SequenceOfWireSegment) -> None: ...
	def GetTransferParamTool(self) -> ShapeAnalysis_TransferParameters: ...
	def Init(self, Grid: ShapeExtend_CompositeSurface, L: TopLoc_Location, Face: TopoDS_Face, Prec: float) -> None: ...
	def Perform(self) -> bool: ...
	def Result(self) -> TopoDS_Shape: ...
	def SetTransferParamTool(self, TransferParam: ShapeAnalysis_TransferParameters) -> None: ...
	def SplitEdges(self) -> None: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeFix_Face(ShapeFix_Root):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, face: TopoDS_Face) -> None: ...
	def Add(self, wire: TopoDS_Wire) -> None: ...
	def GetAutoCorrectPrecisionMode(self) -> int: ...
	def SetAutoCorrectPrecisionMode(self, value: int) -> None: ...
	def ClearModes(self) -> None: ...
	def Face(self) -> TopoDS_Face: ...
	def FixAddNaturalBound(self) -> bool: ...
	def GetFixAddNaturalBoundMode(self) -> int: ...
	def SetFixAddNaturalBoundMode(self, value: int) -> None: ...
	def FixIntersectingWires(self) -> bool: ...
	def GetFixIntersectingWiresMode(self) -> int: ...
	def SetFixIntersectingWiresMode(self, value: int) -> None: ...
	def FixLoopWire(self, aResWires: TopTools_SequenceOfShape) -> bool: ...
	def GetFixLoopWiresMode(self) -> int: ...
	def SetFixLoopWiresMode(self, value: int) -> None: ...
	def FixMissingSeam(self) -> bool: ...
	def GetFixMissingSeamMode(self) -> int: ...
	def SetFixMissingSeamMode(self, value: int) -> None: ...
	@overload
	def FixOrientation(self) -> bool: ...
	@overload
	def FixOrientation(self, MapWires: TopTools_DataMapOfShapeListOfShape) -> bool: ...
	def GetFixOrientationMode(self) -> int: ...
	def SetFixOrientationMode(self, value: int) -> None: ...
	def FixPeriodicDegenerated(self) -> bool: ...
	def GetFixPeriodicDegeneratedMode(self) -> int: ...
	def SetFixPeriodicDegeneratedMode(self, value: int) -> None: ...
	def FixSmallAreaWire(self, theIsRemoveSmallFace: bool) -> bool: ...
	def GetFixSmallAreaWireMode(self) -> int: ...
	def SetFixSmallAreaWireMode(self, value: int) -> None: ...
	def FixSplitFace(self, MapWires: TopTools_DataMapOfShapeListOfShape) -> bool: ...
	def GetFixSplitFaceMode(self) -> int: ...
	def SetFixSplitFaceMode(self, value: int) -> None: ...
	def GetFixWireMode(self) -> int: ...
	def SetFixWireMode(self, value: int) -> None: ...
	def FixWireTool(self) -> ShapeFix_Wire: ...
	def FixWiresTwoCoincEdges(self) -> bool: ...
	@overload
	def Init(self, face: TopoDS_Face) -> None: ...
	@overload
	def Init(self, surf: Geom_Surface, preci: float, fwd: Optional[bool]) -> None: ...
	@overload
	def Init(self, surf: ShapeAnalysis_Surface, preci: float, fwd: Optional[bool]) -> None: ...
	def Perform(self) -> bool: ...
	def GetRemoveSmallAreaFaceMode(self) -> int: ...
	def SetRemoveSmallAreaFaceMode(self, value: int) -> None: ...
	def Result(self) -> TopoDS_Shape: ...
	def SetMaxTolerance(self, maxtol: float) -> None: ...
	def SetMinTolerance(self, mintol: float) -> None: ...
	def SetMsgRegistrator(self, msgreg: ShapeExtend_BasicMsgRegistrator) -> None: ...
	def SetPrecision(self, preci: float) -> None: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeFix_FixSmallFace(ShapeFix_Root):
	def __init__(self) -> None: ...
	def ComputeSharedEdgeForStripFace(self, F: TopoDS_Face, E1: TopoDS_Edge, E2: TopoDS_Edge, F1: TopoDS_Face, tol: float) -> TopoDS_Edge: ...
	def FixFace(self, F: TopoDS_Face) -> TopoDS_Face: ...
	def FixPinFace(self, F: TopoDS_Face) -> bool: ...
	def FixShape(self) -> TopoDS_Shape: ...
	def FixSplitFace(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
	def FixSpotFace(self) -> TopoDS_Shape: ...
	def FixStripFace(self, wasdone: Optional[bool]) -> TopoDS_Shape: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def Perform(self) -> None: ...
	def RemoveFacesInCaseOfSpot(self, F: TopoDS_Face) -> bool: ...
	def RemoveFacesInCaseOfStrip(self, F: TopoDS_Face) -> bool: ...
	def ReplaceInCaseOfStrip(self, F: TopoDS_Face, E1: TopoDS_Edge, E2: TopoDS_Edge, tol: float) -> bool: ...
	def ReplaceVerticesInCaseOfSpot(self, F: TopoDS_Face, tol: float) -> bool: ...
	def Shape(self) -> TopoDS_Shape: ...
	def SplitOneFace(self, F: TopoDS_Face, theSplittedFaces: TopoDS_Compound) -> bool: ...

class ShapeFix_FixSmallSolid(ShapeFix_Root):
	def __init__(self) -> None: ...
	def Merge(self, theShape: TopoDS_Shape, theContext: ShapeBuild_ReShape) -> TopoDS_Shape: ...
	def Remove(self, theShape: TopoDS_Shape, theContext: ShapeBuild_ReShape) -> TopoDS_Shape: ...
	def SetFixMode(self, theMode: int) -> None: ...
	def SetVolumeThreshold(self, theThreshold: Optional[float]) -> None: ...
	def SetWidthFactorThreshold(self, theThreshold: Optional[float]) -> None: ...

class ShapeFix_Shape(ShapeFix_Root):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, shape: TopoDS_Shape) -> None: ...
	def FixEdgeTool(self) -> ShapeFix_Edge: ...
	def FixFaceTool(self) -> ShapeFix_Face: ...
	def GetFixFreeFaceMode(self) -> int: ...
	def SetFixFreeFaceMode(self, value: int) -> None: ...
	def GetFixFreeShellMode(self) -> int: ...
	def SetFixFreeShellMode(self, value: int) -> None: ...
	def GetFixFreeWireMode(self) -> int: ...
	def SetFixFreeWireMode(self, value: int) -> None: ...
	def GetFixSameParameterMode(self) -> int: ...
	def SetFixSameParameterMode(self, value: int) -> None: ...
	def FixShellTool(self) -> ShapeFix_Shell: ...
	def GetFixSolidMode(self) -> int: ...
	def SetFixSolidMode(self, value: int) -> None: ...
	def FixSolidTool(self) -> ShapeFix_Solid: ...
	def GetFixVertexPositionMode(self) -> int: ...
	def SetFixVertexPositionMode(self, value: int) -> None: ...
	def GetFixVertexTolMode(self) -> int: ...
	def SetFixVertexTolMode(self, value: int) -> None: ...
	def FixWireTool(self) -> ShapeFix_Wire: ...
	def Init(self, shape: TopoDS_Shape) -> None: ...
	def Perform(self, theProgress: Optional[Message_ProgressIndicator]) -> bool: ...
	def SetMaxTolerance(self, maxtol: float) -> None: ...
	def SetMinTolerance(self, mintol: float) -> None: ...
	def SetMsgRegistrator(self, msgreg: ShapeExtend_BasicMsgRegistrator) -> None: ...
	def SetPrecision(self, preci: float) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeFix_Shell(ShapeFix_Root):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, shape: TopoDS_Shell) -> None: ...
	def ErrorFaces(self) -> TopoDS_Compound: ...
	def GetFixFaceMode(self) -> int: ...
	def SetFixFaceMode(self, value: int) -> None: ...
	def FixFaceOrientation(self, shell: TopoDS_Shell, isAccountMultiConex: Optional[bool], NonManifold: Optional[bool]) -> bool: ...
	def FixFaceTool(self) -> ShapeFix_Face: ...
	def GetFixOrientationMode(self) -> int: ...
	def SetFixOrientationMode(self, value: int) -> None: ...
	def Init(self, shell: TopoDS_Shell) -> None: ...
	def NbShells(self) -> int: ...
	def Perform(self, theProgress: Optional[Message_ProgressIndicator]) -> bool: ...
	def SetMaxTolerance(self, maxtol: float) -> None: ...
	def SetMinTolerance(self, mintol: float) -> None: ...
	def SetMsgRegistrator(self, msgreg: ShapeExtend_BasicMsgRegistrator) -> None: ...
	def SetNonManifoldFlag(self, isNonManifold: bool) -> None: ...
	def SetPrecision(self, preci: float) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Shell(self) -> TopoDS_Shell: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeFix_Solid(ShapeFix_Root):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, solid: TopoDS_Solid) -> None: ...
	def GetCreateOpenSolidMode(self) -> bool: ...
	def SetCreateOpenSolidMode(self, value: bool) -> None: ...
	def GetFixShellMode(self) -> int: ...
	def SetFixShellMode(self, value: int) -> None: ...
	def GetFixShellOrientationMode(self) -> int: ...
	def SetFixShellOrientationMode(self, value: int) -> None: ...
	def FixShellTool(self) -> ShapeFix_Shell: ...
	def Init(self, solid: TopoDS_Solid) -> None: ...
	def Perform(self, theProgress: Optional[Message_ProgressIndicator]) -> bool: ...
	def SetMaxTolerance(self, maxtol: float) -> None: ...
	def SetMinTolerance(self, mintol: float) -> None: ...
	def SetMsgRegistrator(self, msgreg: ShapeExtend_BasicMsgRegistrator) -> None: ...
	def SetPrecision(self, preci: float) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def Solid(self) -> TopoDS_Shape: ...
	def SolidFromShell(self, shell: TopoDS_Shell) -> TopoDS_Solid: ...
	def Status(self, status: ShapeExtend_Status) -> bool: ...

class ShapeFix_SplitCommonVertex(ShapeFix_Root):
	def __init__(self) -> None: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def Perform(self) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class ShapeFix_Wire(ShapeFix_Root):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, wire: TopoDS_Wire, face: TopoDS_Face, prec: float) -> None: ...
	def Analyzer(self) -> ShapeAnalysis_Wire: ...
	def ClearModes(self) -> None: ...
	def ClearStatuses(self) -> None: ...
	def GetClosedWireMode(self) -> bool: ...
	def SetClosedWireMode(self, value: bool) -> None: ...
	def Face(self) -> TopoDS_Face: ...
	def GetFixAddCurve3dMode(self) -> int: ...
	def SetFixAddCurve3dMode(self, value: int) -> None: ...
	def GetFixAddPCurveMode(self) -> int: ...
	def SetFixAddPCurveMode(self, value: int) -> None: ...
	def FixClosed(self, prec: Optional[float]) -> bool: ...
	@overload
	def FixConnected(self, prec: Optional[float]) -> bool: ...
	@overload
	def FixConnected(self, num: int, prec: float) -> bool: ...
	def GetFixConnectedMode(self) -> int: ...
	def SetFixConnectedMode(self, value: int) -> None: ...
	@overload
	def FixDegenerated(self) -> bool: ...
	@overload
	def FixDegenerated(self, num: int) -> bool: ...
	def GetFixDegeneratedMode(self) -> int: ...
	def SetFixDegeneratedMode(self, value: int) -> None: ...
	def FixEdgeCurves(self) -> bool: ...
	def GetFixEdgeCurvesMode(self) -> int: ...
	def SetFixEdgeCurvesMode(self, value: int) -> None: ...
	def FixEdgeTool(self) -> ShapeFix_Edge: ...
	def FixGap2d(self, num: int, convert: Optional[bool]) -> bool: ...
	def FixGap3d(self, num: int, convert: Optional[bool]) -> bool: ...
	def FixGaps2d(self) -> bool: ...
	def GetFixGaps2dMode(self) -> int: ...
	def SetFixGaps2dMode(self, value: int) -> None: ...
	def FixGaps3d(self) -> bool: ...
	def GetFixGaps3dMode(self) -> int: ...
	def SetFixGaps3dMode(self, value: int) -> None: ...
	def GetFixGapsByRangesMode(self) -> bool: ...
	def SetFixGapsByRangesMode(self, value: bool) -> None: ...
	def GetFixIntersectingEdgesMode(self) -> int: ...
	def SetFixIntersectingEdgesMode(self, value: int) -> None: ...
	@overload
	def FixLacking(self, force: Optional[bool]) -> bool: ...
	@overload
	def FixLacking(self, num: int, force: Optional[bool]) -> bool: ...
	def GetFixLackingMode(self) -> int: ...
	def SetFixLackingMode(self, value: int) -> None: ...
	def GetFixNonAdjacentIntersectingEdgesMode(self) -> int: ...
	def SetFixNonAdjacentIntersectingEdgesMode(self, value: int) -> None: ...
	def FixNotchedEdges(self) -> bool: ...
	def GetFixNotchedEdgesMode(self) -> int: ...
	def SetFixNotchedEdgesMode(self, value: int) -> None: ...
	def GetFixRemoveCurve3dMode(self) -> int: ...
	def SetFixRemoveCurve3dMode(self, value: int) -> None: ...
	def GetFixRemovePCurveMode(self) -> int: ...
	def SetFixRemovePCurveMode(self, value: int) -> None: ...
	@overload
	def FixReorder(self) -> bool: ...
	@overload
	def FixReorder(self, wi: ShapeAnalysis_WireOrder) -> bool: ...
	def GetFixReorderMode(self) -> int: ...
	def SetFixReorderMode(self, value: int) -> None: ...
	def GetFixReversed2dMode(self) -> int: ...
	def SetFixReversed2dMode(self, value: int) -> None: ...
	def GetFixSameParameterMode(self) -> int: ...
	def SetFixSameParameterMode(self, value: int) -> None: ...
	def FixSeam(self, num: int) -> bool: ...
	def GetFixSeamMode(self) -> int: ...
	def SetFixSeamMode(self, value: int) -> None: ...
	def GetFixSelfIntersectingEdgeMode(self) -> int: ...
	def SetFixSelfIntersectingEdgeMode(self, value: int) -> None: ...
	def FixSelfIntersection(self) -> bool: ...
	def GetFixSelfIntersectionMode(self) -> int: ...
	def SetFixSelfIntersectionMode(self, value: int) -> None: ...
	def FixShifted(self) -> bool: ...
	def GetFixShiftedMode(self) -> int: ...
	def SetFixShiftedMode(self, value: int) -> None: ...
	@overload
	def FixSmall(self, lockvtx: bool, precsmall: Optional[float]) -> int: ...
	@overload
	def FixSmall(self, num: int, lockvtx: bool, precsmall: float) -> bool: ...
	def GetFixSmallMode(self) -> int: ...
	def SetFixSmallMode(self, value: int) -> None: ...
	def GetFixTailMode(self) -> int: ...
	def SetFixTailMode(self, value: int) -> None: ...
	def FixTails(self) -> bool: ...
	def GetFixVertexToleranceMode(self) -> int: ...
	def SetFixVertexToleranceMode(self, value: int) -> None: ...
	@overload
	def Init(self, wire: TopoDS_Wire, face: TopoDS_Face, prec: float) -> None: ...
	@overload
	def Init(self, saw: ShapeAnalysis_Wire) -> None: ...
	def IsLoaded(self) -> bool: ...
	def IsReady(self) -> bool: ...
	def LastFixStatus(self, status: ShapeExtend_Status) -> bool: ...
	@overload
	def Load(self, wire: TopoDS_Wire) -> None: ...
	@overload
	def Load(self, sbwd: ShapeExtend_WireData) -> None: ...
	def GetModifyGeometryMode(self) -> bool: ...
	def SetModifyGeometryMode(self, value: bool) -> None: ...
	def GetModifyRemoveLoopMode(self) -> int: ...
	def SetModifyRemoveLoopMode(self, value: int) -> None: ...
	def GetModifyTopologyMode(self) -> bool: ...
	def SetModifyTopologyMode(self, value: bool) -> None: ...
	def NbEdges(self) -> int: ...
	def Perform(self) -> bool: ...
	def GetPreferencePCurveMode(self) -> bool: ...
	def SetPreferencePCurveMode(self, value: bool) -> None: ...
	def SetFace(self, face: TopoDS_Face) -> None: ...
	def SetMaxTailAngle(self, theMaxTailAngle: float) -> None: ...
	def SetMaxTailWidth(self, theMaxTailWidth: float) -> None: ...
	def SetPrecision(self, prec: float) -> None: ...
	@overload
	def SetSurface(self, surf: Geom_Surface) -> None: ...
	@overload
	def SetSurface(self, surf: Geom_Surface, loc: TopLoc_Location) -> None: ...
	def StatusClosed(self, status: ShapeExtend_Status) -> bool: ...
	def StatusConnected(self, status: ShapeExtend_Status) -> bool: ...
	def StatusDegenerated(self, status: ShapeExtend_Status) -> bool: ...
	def StatusEdgeCurves(self, status: ShapeExtend_Status) -> bool: ...
	def StatusFixTails(self, status: ShapeExtend_Status) -> bool: ...
	def StatusGaps2d(self, status: ShapeExtend_Status) -> bool: ...
	def StatusGaps3d(self, status: ShapeExtend_Status) -> bool: ...
	def StatusLacking(self, status: ShapeExtend_Status) -> bool: ...
	def StatusNotches(self, status: ShapeExtend_Status) -> bool: ...
	def StatusRemovedSegment(self) -> bool: ...
	def StatusReorder(self, status: ShapeExtend_Status) -> bool: ...
	def StatusSelfIntersection(self, status: ShapeExtend_Status) -> bool: ...
	def StatusSmall(self, status: ShapeExtend_Status) -> bool: ...
	def Wire(self) -> TopoDS_Wire: ...
	def WireAPIMake(self) -> TopoDS_Wire: ...
	def WireData(self) -> ShapeExtend_WireData: ...

class ShapeFix_Wireframe(ShapeFix_Root):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, shape: TopoDS_Shape) -> None: ...
	def CheckSmallEdges(self, theSmallEdges: TopTools_MapOfShape, theEdgeToFaces: TopTools_DataMapOfShapeListOfShape, theFaceWithSmall: TopTools_DataMapOfShapeListOfShape, theMultyEdges: TopTools_MapOfShape) -> bool: ...
	def ClearStatuses(self) -> None: ...
	def FixSmallEdges(self) -> bool: ...
	def FixWireGaps(self) -> bool: ...
	def LimitAngle(self) -> float: ...
	def Load(self, shape: TopoDS_Shape) -> None: ...
	def MergeSmallEdges(self, theSmallEdges: TopTools_MapOfShape, theEdgeToFaces: TopTools_DataMapOfShapeListOfShape, theFaceWithSmall: TopTools_DataMapOfShapeListOfShape, theMultyEdges: TopTools_MapOfShape, theModeDrop: Optional[bool], theLimitAngle: Optional[float]) -> bool: ...
	def GetModeDropSmallEdges(self) -> bool: ...
	def SetModeDropSmallEdges(self, value: bool) -> None: ...
	def SetLimitAngle(self, theLimitAngle: float) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def StatusSmallEdges(self, status: ShapeExtend_Status) -> bool: ...
	def StatusWireGaps(self, status: ShapeExtend_Status) -> bool: ...

#classnotwrapped
class ShapeFix_WireSegment: ...

# harray1 classes
# harray2 classes
# hsequence classes

shapefix_EncodeRegularity = shapefix.EncodeRegularity
shapefix_FixVertexPosition = shapefix.FixVertexPosition
shapefix_LeastEdgeSize = shapefix.LeastEdgeSize
shapefix_RemoveSmallEdges = shapefix.RemoveSmallEdges
shapefix_SameParameter = shapefix.SameParameter
