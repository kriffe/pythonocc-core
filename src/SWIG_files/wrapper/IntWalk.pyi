from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.math import *
from OCC.Core.Adaptor3d import *
from OCC.Core.IntImp import *
from OCC.Core.TColStd import *
from OCC.Core.gp import *
from OCC.Core.IntSurf import *


class IntWalk_StatusDeflection(IntEnum):
	IntWalk_PasTropGrand: int = ...
	IntWalk_StepTooSmall: int = ...
	IntWalk_PointConfondu: int = ...
	IntWalk_ArretSurPointPrecedent: int = ...
	IntWalk_ArretSurPoint: int = ...
	IntWalk_OK: int = ...
IntWalk_PasTropGrand = IntWalk_StatusDeflection.IntWalk_PasTropGrand
IntWalk_StepTooSmall = IntWalk_StatusDeflection.IntWalk_StepTooSmall
IntWalk_PointConfondu = IntWalk_StatusDeflection.IntWalk_PointConfondu
IntWalk_ArretSurPointPrecedent = IntWalk_StatusDeflection.IntWalk_ArretSurPointPrecedent
IntWalk_ArretSurPoint = IntWalk_StatusDeflection.IntWalk_ArretSurPoint
IntWalk_OK = IntWalk_StatusDeflection.IntWalk_OK

class IntWalk_TheFunctionOfTheInt2S(math_FunctionSetWithDerivatives):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface) -> None: ...
	def AuxillarSurface1(self) -> Adaptor3d_HSurface: ...
	def AuxillarSurface2(self) -> Adaptor3d_HSurface: ...
	def ComputeParameters(self, ChoixIso: IntImp_ConstIsoparametric, Param: TColStd_Array1OfReal, UVap: math_Vector, BornInf: math_Vector, BornSup: math_Vector, Tolerance: math_Vector) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def Direction(self) -> gp_Dir: ...
	def DirectionOnS1(self) -> gp_Dir2d: ...
	def DirectionOnS2(self) -> gp_Dir2d: ...
	def IsTangent(self, UVap: math_Vector, Param: TColStd_Array1OfReal, BestChoix: IntImp_ConstIsoparametric) -> bool: ...
	def NbEquations(self) -> int: ...
	def NbVariables(self) -> int: ...
	def Point(self) -> gp_Pnt: ...
	def Root(self) -> float: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class IntWalk_TheInt2S:
	@overload
	def __init__(self, Param: TColStd_Array1OfReal, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, TolTangency: float) -> None: ...
	@overload
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, TolTangency: float) -> None: ...
	def ChangePoint(self) -> IntSurf_PntOn2S: ...
	def Direction(self) -> gp_Dir: ...
	def DirectionOnS1(self) -> gp_Dir2d: ...
	def DirectionOnS2(self) -> gp_Dir2d: ...
	def Function(self) -> IntWalk_TheFunctionOfTheInt2S: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def IsTangent(self) -> bool: ...
	@overload
	def Perform(self, Param: TColStd_Array1OfReal, Rsnld: math_FunctionSetRoot) -> IntImp_ConstIsoparametric: ...
	@overload
	def Perform(self, Param: TColStd_Array1OfReal, Rsnld: math_FunctionSetRoot, ChoixIso: IntImp_ConstIsoparametric) -> IntImp_ConstIsoparametric: ...
	def Point(self) -> IntSurf_PntOn2S: ...

class IntWalk_WalkingData:
	pass

# harray1 classes
# harray2 classes
# hsequence classes

