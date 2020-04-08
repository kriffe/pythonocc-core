from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.Contap import *
from OCC.Core.BRepTopAdaptor import *
from OCC.Core.TopTools import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *
from OCC.Core.HLRAlgo import *


class HLRTopoBRep_DSFiller:
	@staticmethod
	def Insert(self, S: TopoDS_Shape, FO: Contap_Contour, DS: HLRTopoBRep_Data, MST: BRepTopAdaptor_MapOfShapeTool, nbIso: int) -> None: ...

class HLRTopoBRep_Data:
	def __init__(self) -> None: ...
	def AddIntL(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def AddIntV(self, V: TopoDS_Vertex) -> None: ...
	def AddIsoL(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def AddOldS(self, NewS: TopoDS_Shape, OldS: TopoDS_Shape) -> None: ...
	def AddOutL(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def AddOutV(self, V: TopoDS_Vertex) -> None: ...
	def AddSplE(self, E: TopoDS_Edge) -> TopTools_ListOfShape: ...
	def Append(self, V: TopoDS_Vertex, P: float) -> None: ...
	def Clean(self) -> None: ...
	def Clear(self) -> None: ...
	def Edge(self) -> TopoDS_Edge: ...
	def EdgeHasSplE(self, E: TopoDS_Edge) -> bool: ...
	def EdgeSplE(self, E: TopoDS_Edge) -> TopTools_ListOfShape: ...
	def FaceHasIntL(self, F: TopoDS_Face) -> bool: ...
	def FaceHasIsoL(self, F: TopoDS_Face) -> bool: ...
	def FaceHasOutL(self, F: TopoDS_Face) -> bool: ...
	def FaceIntL(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def FaceIsoL(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def FaceOutL(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def InitEdge(self) -> None: ...
	def InitVertex(self, E: TopoDS_Edge) -> None: ...
	def InsertBefore(self, V: TopoDS_Vertex, P: float) -> None: ...
	def IsIntLFaceEdge(self, F: TopoDS_Face, E: TopoDS_Edge) -> bool: ...
	def IsIntV(self, V: TopoDS_Vertex) -> bool: ...
	def IsIsoLFaceEdge(self, F: TopoDS_Face, E: TopoDS_Edge) -> bool: ...
	def IsOutLFaceEdge(self, F: TopoDS_Face, E: TopoDS_Edge) -> bool: ...
	def IsOutV(self, V: TopoDS_Vertex) -> bool: ...
	def IsSplEEdgeEdge(self, E1: TopoDS_Edge, E2: TopoDS_Edge) -> bool: ...
	def MoreEdge(self) -> bool: ...
	def MoreVertex(self) -> bool: ...
	def NewSOldS(self, New: TopoDS_Shape) -> TopoDS_Shape: ...
	def NextEdge(self) -> None: ...
	def NextVertex(self) -> None: ...
	def Parameter(self) -> float: ...
	def Vertex(self) -> TopoDS_Vertex: ...

class HLRTopoBRep_FaceData:
	def __init__(self) -> None: ...
	def AddIntL(self) -> TopTools_ListOfShape: ...
	def AddIsoL(self) -> TopTools_ListOfShape: ...
	def AddOutL(self) -> TopTools_ListOfShape: ...
	def FaceIntL(self) -> TopTools_ListOfShape: ...
	def FaceIsoL(self) -> TopTools_ListOfShape: ...
	def FaceOutL(self) -> TopTools_ListOfShape: ...

class HLRTopoBRep_FaceIsoLiner:
	@staticmethod
	def MakeIsoLine(self, F: TopoDS_Face, Iso: Geom2d_Line, V1: TopoDS_Vertex, V2: TopoDS_Vertex, U1: float, U2: float, Tol: float, DS: HLRTopoBRep_Data) -> None: ...
	@staticmethod
	def MakeVertex(self, E: TopoDS_Edge, P: gp_Pnt, Par: float, Tol: float, DS: HLRTopoBRep_Data) -> TopoDS_Vertex: ...
	@staticmethod
	def Perform(self, FI: int, F: TopoDS_Face, DS: HLRTopoBRep_Data, nbIsos: int) -> None: ...

class HLRTopoBRep_OutLiner(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, OriSh: TopoDS_Shape) -> None: ...
	@overload
	def __init__(self, OriS: TopoDS_Shape, OutS: TopoDS_Shape) -> None: ...
	def DataStructure(self) -> HLRTopoBRep_Data: ...
	def Fill(self, P: HLRAlgo_Projector, MST: BRepTopAdaptor_MapOfShapeTool, nbIso: int) -> None: ...
	@overload
	def OriginalShape(self, OriS: TopoDS_Shape) -> None: ...
	@overload
	def OriginalShape(self) -> TopoDS_Shape: ...
	@overload
	def OutLinedShape(self, OutS: TopoDS_Shape) -> None: ...
	@overload
	def OutLinedShape(self) -> TopoDS_Shape: ...

class HLRTopoBRep_VData:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P: float, V: TopoDS_Shape) -> None: ...
	def Parameter(self) -> float: ...
	def Vertex(self) -> TopoDS_Shape: ...
