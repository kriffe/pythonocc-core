from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *


class hermit:
	@overload
	@staticmethod
	def Solution(self, BS: Geom_BSplineCurve, TolPoles: Optional[float], TolKnots: Optional[float]) -> Geom2d_BSplineCurve: ...
	@overload
	@staticmethod
	def Solution(self, BS: Geom2d_BSplineCurve, TolPoles: Optional[float], TolKnots: Optional[float]) -> Geom2d_BSplineCurve: ...
	@staticmethod
	def Solutionbis(self, BS: Geom_BSplineCurve, TolPoles: Optional[float], TolKnots: Optional[float]) -> Tuple[float, float]: ...

# harray1 classes
# harray2 classes
# hsequence classes

hermit_Solution = hermit.Solution
hermit_Solution = hermit.Solution
hermit_Solutionbis = hermit.Solutionbis
