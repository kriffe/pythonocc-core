from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.Resource import *
from OCC.Core.Message import *
from OCC.Core.TopoDS import *
from OCC.Core.BRepTools import *
from OCC.Core.TopTools import *
from OCC.Core.ShapeExtend import *
from OCC.Core.GeomAbs import *
from OCC.Core.TopAbs import *
from OCC.Core.ShapeBuild import *


class shapeprocess:
	@staticmethod
	def FindOperator(name: str, op: ShapeProcess_Operator) -> bool: ...
	@staticmethod
	def Perform(context: ShapeProcess_Context, seq: str) -> bool: ...
	@staticmethod
	def RegisterOperator(name: str, op: ShapeProcess_Operator) -> bool: ...

class ShapeProcess_Context(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, file: str, scope: Optional[str]) -> None: ...
	def BooleanVal(self, param: str, def_: bool) -> bool: ...
	def GetBoolean(self, param: str) -> Tuple[bool, bool]: ...
	def GetInteger(self, param: str) -> Tuple[bool, int]: ...
	def GetReal(self, param: str) -> Tuple[bool, float]: ...
	def GetString(self, param: str, val: TCollection_AsciiString) -> bool: ...
	def Init(self, file: str, scope: Optional[str]) -> bool: ...
	def IntegerVal(self, param: str, def_: int) -> int: ...
	def IsParamSet(self, param: str) -> bool: ...
	def LoadResourceManager(self, file: str) -> Resource_Manager: ...
	def Messenger(self) -> Message_Messenger: ...
	def Progress(self) -> Message_ProgressIndicator: ...
	def RealVal(self, param: str, def_: float) -> float: ...
	def ResourceManager(self) -> Resource_Manager: ...
	def SetMessenger(self, messenger: Message_Messenger) -> None: ...
	def SetProgress(self, theProgress: Message_ProgressIndicator) -> None: ...
	def SetScope(self, scope: str) -> None: ...
	def SetTraceLevel(self, tracelev: int) -> None: ...
	def StringVal(self, param: str, def_: str) -> str: ...
	def TraceLevel(self) -> int: ...
	def UnSetScope(self) -> None: ...

class ShapeProcess_OperLibrary:
	@staticmethod
	def ApplyModifier(S: TopoDS_Shape, context: ShapeProcess_ShapeContext, M: BRepTools_Modification, map: TopTools_DataMapOfShapeShape, msg: Optional[ShapeExtend_MsgRegistrator], theMutableInput: Optional[bool]) -> TopoDS_Shape: ...
	@staticmethod
	def Init() -> None: ...

class ShapeProcess_Operator(Standard_Transient):
	def Perform(self, context: ShapeProcess_Context) -> bool: ...

class ShapeProcess_ShapeContext(ShapeProcess_Context):
	@overload
	def __init__(self, file: str, seq: Optional[str]) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape, file: str, seq: Optional[str]) -> None: ...
	def AddMessage(self, S: TopoDS_Shape, msg: Message_Msg, gravity: Optional[Message_Gravity]) -> None: ...
	def ContinuityVal(self, param: str, def_: GeomAbs_Shape) -> GeomAbs_Shape: ...
	def GetContinuity(self, param: str, val: GeomAbs_Shape) -> bool: ...
	def GetDetalisation(self) -> TopAbs_ShapeEnum: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def IsNonManifold(self) -> bool: ...
	def Map(self) -> TopTools_DataMapOfShapeShape: ...
	@overload
	def Messages(self) -> ShapeExtend_MsgRegistrator: ...
	@overload
	def Messages(self) -> ShapeExtend_MsgRegistrator: ...
	def PrintStatistics(self) -> None: ...
	@overload
	def RecordModification(self, repl: TopTools_DataMapOfShapeShape, msg: Optional[ShapeExtend_MsgRegistrator]) -> None: ...
	@overload
	def RecordModification(self, repl: ShapeBuild_ReShape, msg: ShapeExtend_MsgRegistrator) -> None: ...
	@overload
	def RecordModification(self, repl: ShapeBuild_ReShape) -> None: ...
	@overload
	def RecordModification(self, sh: TopoDS_Shape, repl: BRepTools_Modifier, msg: Optional[ShapeExtend_MsgRegistrator]) -> None: ...
	def Result(self) -> TopoDS_Shape: ...
	def SetDetalisation(self, level: TopAbs_ShapeEnum) -> None: ...
	def SetNonManifold(self, theNonManifold: bool) -> None: ...
	def SetResult(self, S: TopoDS_Shape) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class ShapeProcess_UOperator(ShapeProcess_Operator):
	def __init__(self, func: ShapeProcess_OperFunc) -> None: ...
	def Perform(self, context: ShapeProcess_Context) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes

shapeprocess_FindOperator = shapeprocess.FindOperator
shapeprocess_Perform = shapeprocess.Perform
shapeprocess_RegisterOperator = shapeprocess.RegisterOperator
ShapeProcess_OperLibrary_ApplyModifier = ShapeProcess_OperLibrary.ApplyModifier
ShapeProcess_OperLibrary_Init = ShapeProcess_OperLibrary.Init
