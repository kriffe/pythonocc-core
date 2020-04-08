from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.IMeshData import *
from OCC.Core.gp import *
from OCC.Core.GeomAbs import *
from OCC.Core.Message import *
from OCC.Core.TopoDS import *


class IMeshTools_Context(IMeshData_Shape):
	def __init__(self) -> None: ...
	def BuildModel(self) -> bool: ...
	def ChangeParameters(self) -> IMeshTools_Parameters: ...
	def Clean(self) -> None: ...
	def DiscretizeEdges(self) -> bool: ...
	def DiscretizeFaces(self) -> bool: ...
	def GetFaceDiscret(self) -> IMeshTools_ModelAlgo: ...
	def GetModelHealer(self) -> IMeshTools_ModelAlgo: ...
	def GetParameters(self) -> IMeshTools_Parameters: ...
	def GetPostProcessor(self) -> IMeshTools_ModelAlgo: ...
	def GetPreProcessor(self) -> IMeshTools_ModelAlgo: ...
	def HealModel(self) -> bool: ...
	def PostProcessModel(self) -> bool: ...
	def PreProcessModel(self) -> bool: ...
	def SetEdgeDiscret(self, theEdgeDiscret: IMeshTools_ModelAlgo) -> None: ...
	def SetFaceDiscret(self, theFaceDiscret: IMeshTools_ModelAlgo) -> None: ...
	def SetModelBuilder(self, theBuilder: IMeshTools_ModelBuilder) -> None: ...
	def SetModelHealer(self, theModelHealer: IMeshTools_ModelAlgo) -> None: ...
	def SetPostProcessor(self, thePostProcessor: IMeshTools_ModelAlgo) -> None: ...
	def SetPreProcessor(self, thePreProcessor: IMeshTools_ModelAlgo) -> None: ...

class IMeshTools_CurveTessellator(Standard_Transient):
	def PointsNb(self) -> int: ...
	def Value(self, theIndex: int, thePoint: gp_Pnt) -> Tuple[bool, float]: ...

class IMeshTools_MeshAlgo(Standard_Transient):
	pass

class IMeshTools_MeshAlgoFactory(Standard_Transient):
	def GetAlgo(self, theSurfaceType: GeomAbs_SurfaceType, theParameters: IMeshTools_Parameters) -> IMeshTools_MeshAlgo: ...

class IMeshTools_MeshBuilder(Message_Algorithm):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theContext: IMeshTools_Context) -> None: ...
	def Perform(self) -> None: ...
	def SetContext(self, theContext: IMeshTools_Context) -> None: ...

class IMeshTools_ModelAlgo(Standard_Transient):
	def Perform(self, theModel: IMeshData_Model, theParameters: IMeshTools_Parameters) -> bool: ...

class IMeshTools_ModelBuilder(Message_Algorithm):
	pass

class IMeshTools_Parameters:
	def __init__(self) -> None: ...
	@staticmethod
	def RelMinSize(self) -> float: ...

class IMeshTools_ShapeExplorer(IMeshData_Shape):
	def __init__(self, theShape: TopoDS_Shape) -> None: ...
	def Accept(self, theVisitor: IMeshTools_ShapeVisitor) -> None: ...

class IMeshTools_ShapeVisitor(Standard_Transient):
	@overload
	def Visit(self, theFace: TopoDS_Face) -> None: ...
	@overload
	def Visit(self, theEdge: TopoDS_Edge) -> None: ...
