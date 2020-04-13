from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.Bnd import *


class brepbndlib:
	@staticmethod
	def Add(S: TopoDS_Shape, B: Bnd_Box, useTriangulation: Optional[bool]) -> None: ...
	@staticmethod
	def AddClose(S: TopoDS_Shape, B: Bnd_Box) -> None: ...
	@staticmethod
	def AddOBB(theS: TopoDS_Shape, theOBB: Bnd_OBB, theIsTriangulationUsed: Optional[bool], theIsOptimal: Optional[bool], theIsShapeToleranceUsed: Optional[bool]) -> None: ...
	@staticmethod
	def AddOptimal(S: TopoDS_Shape, B: Bnd_Box, useTriangulation: Optional[bool], useShapeTolerance: Optional[bool]) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

brepbndlib_Add = brepbndlib.Add
brepbndlib_AddClose = brepbndlib.AddClose
brepbndlib_AddOBB = brepbndlib.AddOBB
brepbndlib_AddOptimal = brepbndlib.AddOptimal
