from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.ShapeFix import *


class ShapeAlgo:
	@staticmethod
	def AlgoContainer(self) -> ShapeAlgo_AlgoContainer: ...
	@staticmethod
	def Init(self) -> None: ...
	@staticmethod
	def SetAlgoContainer(self, aContainer: ShapeAlgo_AlgoContainer) -> None: ...

class ShapeAlgo_ToolContainer(Standard_Transient):
	def __init__(self) -> None: ...
	def EdgeProjAux(self) -> ShapeFix_EdgeProjAux: ...
	def FixShape(self) -> ShapeFix_Shape: ...

#classnotwrapped
class ShapeAlgo_AlgoContainer: ...

# harray1 classes
# harray2 classes
# hsequence classes

shapealgo_AlgoContainer = shapealgo.AlgoContainer
shapealgo_Init = shapealgo.Init
shapealgo_SetAlgoContainer = shapealgo.SetAlgoContainer
