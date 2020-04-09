from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *


class Precision:
	@staticmethod
	def Angular(self) -> float: ...
	@staticmethod
	def Approximation(self) -> float: ...
	@staticmethod
	def Confusion(self) -> float: ...
	@staticmethod
	def Infinite(self) -> float: ...
	@staticmethod
	def Intersection(self) -> float: ...
	@staticmethod
	def IsInfinite(self, R: float) -> bool: ...
	@staticmethod
	def IsNegativeInfinite(self, R: float) -> bool: ...
	@staticmethod
	def IsPositiveInfinite(self, R: float) -> bool: ...
	@overload
	@staticmethod
	def PApproximation(self, T: float) -> float: ...
	@overload
	@staticmethod
	def PApproximation(self) -> float: ...
	@overload
	@staticmethod
	def PConfusion(self, T: float) -> float: ...
	@overload
	@staticmethod
	def PConfusion(self) -> float: ...
	@overload
	@staticmethod
	def PIntersection(self, T: float) -> float: ...
	@overload
	@staticmethod
	def PIntersection(self) -> float: ...
	@overload
	@staticmethod
	def Parametric(self, P: float, T: float) -> float: ...
	@overload
	@staticmethod
	def Parametric(self, P: float) -> float: ...
	@staticmethod
	def SquareConfusion(self) -> float: ...
	@staticmethod
	def SquarePConfusion(self) -> float: ...

# harray1 classes
# harray2 classes
# harray2 classes

precision_Angular = precision.Angular
precision_Approximation = precision.Approximation
precision_Confusion = precision.Confusion
precision_Infinite = precision.Infinite
precision_Intersection = precision.Intersection
precision_IsInfinite = precision.IsInfinite
precision_IsNegativeInfinite = precision.IsNegativeInfinite
precision_IsPositiveInfinite = precision.IsPositiveInfinite
precision_PApproximation = precision.PApproximation
precision_PApproximation = precision.PApproximation
precision_PConfusion = precision.PConfusion
precision_PConfusion = precision.PConfusion
precision_PIntersection = precision.PIntersection
precision_PIntersection = precision.PIntersection
precision_Parametric = precision.Parametric
precision_Parametric = precision.Parametric
precision_SquareConfusion = precision.SquareConfusion
precision_SquarePConfusion = precision.SquarePConfusion
