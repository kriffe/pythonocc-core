from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *


class TopAbs_Orientation:
	TopAbs_FORWARD: int = ...
	TopAbs_REVERSED: int = ...
	TopAbs_INTERNAL: int = ...
	TopAbs_EXTERNAL: int = ...

class TopAbs_ShapeEnum:
	TopAbs_COMPOUND: int = ...
	TopAbs_COMPSOLID: int = ...
	TopAbs_SOLID: int = ...
	TopAbs_SHELL: int = ...
	TopAbs_FACE: int = ...
	TopAbs_WIRE: int = ...
	TopAbs_EDGE: int = ...
	TopAbs_VERTEX: int = ...
	TopAbs_SHAPE: int = ...

class TopAbs_State:
	TopAbs_IN: int = ...
	TopAbs_OUT: int = ...
	TopAbs_ON: int = ...
	TopAbs_UNKNOWN: int = ...

class TopAbs:
	@staticmethod
	def Complement(self, Or: TopAbs_Orientation) -> TopAbs_Orientation: ...
	@staticmethod
	def Compose(self, Or1: TopAbs_Orientation, Or2: TopAbs_Orientation) -> TopAbs_Orientation: ...
	@staticmethod
	def Reverse(self, Or: TopAbs_Orientation) -> TopAbs_Orientation: ...
	@staticmethod
	def ShapeOrientationFromString(self, theOrientationString: str) -> TopAbs_Orientation: ...
	@staticmethod
	def ShapeOrientationFromString(self, theOrientationString: str, theOrientation: TopAbs_Orientation) -> bool: ...
	@staticmethod
	def ShapeOrientationToString(self, theOrientation: TopAbs_Orientation) -> str: ...
	@staticmethod
	def ShapeTypeFromString(self, theTypeString: str) -> TopAbs_ShapeEnum: ...
	@staticmethod
	def ShapeTypeFromString(self, theTypeString: str, theType: TopAbs_ShapeEnum) -> bool: ...
	@staticmethod
	def ShapeTypeToString(self, theType: TopAbs_ShapeEnum) -> str: ...
