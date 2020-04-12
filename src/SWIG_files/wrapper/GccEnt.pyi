from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *


class GccEnt_Array1OfPosition:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> GccEnt_Position: ...
    def __setitem__(self, index: int, value: GccEnt_Position) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[GccEnt_Position]:
    def next(self) -> GccEnt_Position: ...
    __next__ = next

class GccEnt_Position(IntEnum):
	GccEnt_unqualified: int = ...
	GccEnt_enclosing: int = ...
	GccEnt_enclosed: int = ...
	GccEnt_outside: int = ...
	GccEnt_noqualifier: int = ...
GccEnt_unqualified = GccEnt_Position.GccEnt_unqualified
GccEnt_enclosing = GccEnt_Position.GccEnt_enclosing
GccEnt_enclosed = GccEnt_Position.GccEnt_enclosed
GccEnt_outside = GccEnt_Position.GccEnt_outside
GccEnt_noqualifier = GccEnt_Position.GccEnt_noqualifier

class GccEnt:
	@overload
	@staticmethod
	def Enclosed(self, Obj: gp_Lin2d) -> GccEnt_QualifiedLin: ...
	@overload
	@staticmethod
	def Enclosed(self, Obj: gp_Circ2d) -> GccEnt_QualifiedCirc: ...
	@staticmethod
	def Enclosing(self, Obj: gp_Circ2d) -> GccEnt_QualifiedCirc: ...
	@overload
	@staticmethod
	def Outside(self, Obj: gp_Lin2d) -> GccEnt_QualifiedLin: ...
	@overload
	@staticmethod
	def Outside(self, Obj: gp_Circ2d) -> GccEnt_QualifiedCirc: ...
	@overload
	@staticmethod
	def PositionFromString(self, thePositionString: str) -> GccEnt_Position: ...
	@overload
	@staticmethod
	def PositionFromString(self, thePositionString: str, thePosition: GccEnt_Position) -> bool: ...
	@staticmethod
	def PositionToString(self, thePosition: GccEnt_Position) -> str: ...
	@overload
	@staticmethod
	def Unqualified(self, Obj: gp_Lin2d) -> GccEnt_QualifiedLin: ...
	@overload
	@staticmethod
	def Unqualified(self, Obj: gp_Circ2d) -> GccEnt_QualifiedCirc: ...

class GccEnt_QualifiedCirc:
	def __init__(self, Qualified: gp_Circ2d, Qualifier: GccEnt_Position) -> None: ...
	def IsEnclosed(self) -> bool: ...
	def IsEnclosing(self) -> bool: ...
	def IsOutside(self) -> bool: ...
	def IsUnqualified(self) -> bool: ...
	def Qualified(self) -> gp_Circ2d: ...
	def Qualifier(self) -> GccEnt_Position: ...

class GccEnt_QualifiedLin:
	def __init__(self, Qualified: gp_Lin2d, Qualifier: GccEnt_Position) -> None: ...
	def IsEnclosed(self) -> bool: ...
	def IsOutside(self) -> bool: ...
	def IsUnqualified(self) -> bool: ...
	def Qualified(self) -> gp_Lin2d: ...
	def Qualifier(self) -> GccEnt_Position: ...

# harray1 classes
# harray2 classes
# hsequence classes

gccent_Enclosed = gccent.Enclosed
gccent_Enclosed = gccent.Enclosed
gccent_Enclosing = gccent.Enclosing
gccent_Outside = gccent.Outside
gccent_Outside = gccent.Outside
gccent_PositionFromString = gccent.PositionFromString
gccent_PositionFromString = gccent.PositionFromString
gccent_PositionToString = gccent.PositionToString
gccent_Print = gccent.Print
gccent_Unqualified = gccent.Unqualified
gccent_Unqualified = gccent.Unqualified
