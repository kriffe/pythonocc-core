from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.TopTools import *


class ChFi2d_ConstructionError(IntEnum):
	ChFi2d_NotPlanar: int = ...
	ChFi2d_NoFace: int = ...
	ChFi2d_InitialisationError: int = ...
	ChFi2d_ParametersError: int = ...
	ChFi2d_Ready: int = ...
	ChFi2d_IsDone: int = ...
	ChFi2d_ComputationError: int = ...
	ChFi2d_ConnexionError: int = ...
	ChFi2d_TangencyError: int = ...
	ChFi2d_FirstEdgeDegenerated: int = ...
	ChFi2d_LastEdgeDegenerated: int = ...
	ChFi2d_BothEdgesDegenerated: int = ...
	ChFi2d_NotAuthorized: int = ...
ChFi2d_NotPlanar = ChFi2d_ConstructionError.ChFi2d_NotPlanar
ChFi2d_NoFace = ChFi2d_ConstructionError.ChFi2d_NoFace
ChFi2d_InitialisationError = ChFi2d_ConstructionError.ChFi2d_InitialisationError
ChFi2d_ParametersError = ChFi2d_ConstructionError.ChFi2d_ParametersError
ChFi2d_Ready = ChFi2d_ConstructionError.ChFi2d_Ready
ChFi2d_IsDone = ChFi2d_ConstructionError.ChFi2d_IsDone
ChFi2d_ComputationError = ChFi2d_ConstructionError.ChFi2d_ComputationError
ChFi2d_ConnexionError = ChFi2d_ConstructionError.ChFi2d_ConnexionError
ChFi2d_TangencyError = ChFi2d_ConstructionError.ChFi2d_TangencyError
ChFi2d_FirstEdgeDegenerated = ChFi2d_ConstructionError.ChFi2d_FirstEdgeDegenerated
ChFi2d_LastEdgeDegenerated = ChFi2d_ConstructionError.ChFi2d_LastEdgeDegenerated
ChFi2d_BothEdgesDegenerated = ChFi2d_ConstructionError.ChFi2d_BothEdgesDegenerated
ChFi2d_NotAuthorized = ChFi2d_ConstructionError.ChFi2d_NotAuthorized

class ChFi2d:
	pass

class ChFi2d_AnaFilletAlgo:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theWire: TopoDS_Wire, thePlane: gp_Pln) -> None: ...
	@overload
	def __init__(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, thePlane: gp_Pln) -> None: ...
	@overload
	def Init(self, theWire: TopoDS_Wire, thePlane: gp_Pln) -> None: ...
	@overload
	def Init(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, thePlane: gp_Pln) -> None: ...
	def Perform(self, radius: float) -> bool: ...
	def Result(self, e1: TopoDS_Edge, e2: TopoDS_Edge) -> TopoDS_Edge: ...

class ChFi2d_Builder:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, F: TopoDS_Face) -> None: ...
	@overload
	def AddChamfer(self, E1: TopoDS_Edge, E2: TopoDS_Edge, D1: float, D2: float) -> TopoDS_Edge: ...
	@overload
	def AddChamfer(self, E: TopoDS_Edge, V: TopoDS_Vertex, D: float, Ang: float) -> TopoDS_Edge: ...
	def AddFillet(self, V: TopoDS_Vertex, Radius: float) -> TopoDS_Edge: ...
	def BasisEdge(self, E: TopoDS_Edge) -> TopoDS_Edge: ...
	def ChamferEdges(self) -> TopTools_SequenceOfShape: ...
	def DescendantEdge(self, E: TopoDS_Edge) -> TopoDS_Edge: ...
	def FilletEdges(self) -> TopTools_SequenceOfShape: ...
	def HasDescendant(self, E: TopoDS_Edge) -> bool: ...
	@overload
	def Init(self, F: TopoDS_Face) -> None: ...
	@overload
	def Init(self, RefFace: TopoDS_Face, ModFace: TopoDS_Face) -> None: ...
	def IsModified(self, E: TopoDS_Edge) -> bool: ...
	@overload
	def ModifyChamfer(self, Chamfer: TopoDS_Edge, E1: TopoDS_Edge, E2: TopoDS_Edge, D1: float, D2: float) -> TopoDS_Edge: ...
	@overload
	def ModifyChamfer(self, Chamfer: TopoDS_Edge, E: TopoDS_Edge, D: float, Ang: float) -> TopoDS_Edge: ...
	def ModifyFillet(self, Fillet: TopoDS_Edge, Radius: float) -> TopoDS_Edge: ...
	def NbChamfer(self) -> int: ...
	def NbFillet(self) -> int: ...
	def RemoveChamfer(self, Chamfer: TopoDS_Edge) -> TopoDS_Vertex: ...
	def RemoveFillet(self, Fillet: TopoDS_Edge) -> TopoDS_Vertex: ...
	def Result(self) -> TopoDS_Face: ...
	def Status(self) -> ChFi2d_ConstructionError: ...

class ChFi2d_ChamferAPI:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theWire: TopoDS_Wire) -> None: ...
	@overload
	def __init__(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge) -> None: ...
	@overload
	def Init(self, theWire: TopoDS_Wire) -> None: ...
	@overload
	def Init(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge) -> None: ...
	def Perform(self) -> bool: ...
	def Result(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, theLength1: float, theLength2: float) -> TopoDS_Edge: ...

class ChFi2d_FilletAPI:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theWire: TopoDS_Wire, thePlane: gp_Pln) -> None: ...
	@overload
	def __init__(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, thePlane: gp_Pln) -> None: ...
	@overload
	def Init(self, theWire: TopoDS_Wire, thePlane: gp_Pln) -> None: ...
	@overload
	def Init(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, thePlane: gp_Pln) -> None: ...
	def NbResults(self, thePoint: gp_Pnt) -> int: ...
	def Perform(self, theRadius: float) -> bool: ...
	def Result(self, thePoint: gp_Pnt, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, iSolution: Optional[int]) -> TopoDS_Edge: ...

class ChFi2d_FilletAlgo:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theWire: TopoDS_Wire, thePlane: gp_Pln) -> None: ...
	@overload
	def __init__(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, thePlane: gp_Pln) -> None: ...
	@overload
	def Init(self, theWire: TopoDS_Wire, thePlane: gp_Pln) -> None: ...
	@overload
	def Init(self, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, thePlane: gp_Pln) -> None: ...
	def NbResults(self, thePoint: gp_Pnt) -> int: ...
	def Perform(self, theRadius: float) -> bool: ...
	def Result(self, thePoint: gp_Pnt, theEdge1: TopoDS_Edge, theEdge2: TopoDS_Edge, iSolution: Optional[int]) -> TopoDS_Edge: ...

# harray1 classes
# harray2 classes
# harray2 classes

