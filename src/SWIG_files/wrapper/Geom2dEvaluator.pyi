from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.Geom2d import *
from OCC.Core.Geom2dAdaptor import *


class Geom2dEvaluator_Curve(Standard_Transient):
	def D0(self, theU: float, theValue: gp_Pnt2d) -> None: ...
	def D1(self, theU: float, theValue: gp_Pnt2d, theD1: gp_Vec2d) -> None: ...
	def D2(self, theU: float, theValue: gp_Pnt2d, theD1: gp_Vec2d, theD2: gp_Vec2d) -> None: ...
	def D3(self, theU: float, theValue: gp_Pnt2d, theD1: gp_Vec2d, theD2: gp_Vec2d, theD3: gp_Vec2d) -> None: ...
	def DN(self, theU: float, theDerU: int) -> gp_Vec2d: ...

class Geom2dEvaluator_OffsetCurve(Geom2dEvaluator_Curve):
	@overload
	def __init__(self, theBase: Geom2d_Curve, theOffset: float) -> None: ...
	@overload
	def __init__(self, theBase: Geom2dAdaptor_HCurve, theOffset: float) -> None: ...
	def D0(self, theU: float, theValue: gp_Pnt2d) -> None: ...
	def D1(self, theU: float, theValue: gp_Pnt2d, theD1: gp_Vec2d) -> None: ...
	def D2(self, theU: float, theValue: gp_Pnt2d, theD1: gp_Vec2d, theD2: gp_Vec2d) -> None: ...
	def D3(self, theU: float, theValue: gp_Pnt2d, theD1: gp_Vec2d, theD2: gp_Vec2d, theD3: gp_Vec2d) -> None: ...
	def DN(self, theU: float, theDeriv: int) -> gp_Vec2d: ...
	def SetOffsetValue(self, theOffset: float) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

