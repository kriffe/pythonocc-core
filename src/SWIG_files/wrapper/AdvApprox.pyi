from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColgp import *
from OCC.Core.PLib import *


class AdvApprox_ApproxAFunction:
	@overload
	def __init__(self, Num1DSS: int, Num2DSS: int, Num3DSS: int, OneDTol: TColStd_HArray1OfReal, TwoDTol: TColStd_HArray1OfReal, ThreeDTol: TColStd_HArray1OfReal, First: float, Last: float, Continuity: GeomAbs_Shape, MaxDeg: int, MaxSeg: int, Func: AdvApprox_EvaluatorFunction) -> None: ...
	@overload
	def __init__(self, Num1DSS: int, Num2DSS: int, Num3DSS: int, OneDTol: TColStd_HArray1OfReal, TwoDTol: TColStd_HArray1OfReal, ThreeDTol: TColStd_HArray1OfReal, First: float, Last: float, Continuity: GeomAbs_Shape, MaxDeg: int, MaxSeg: int, Func: AdvApprox_EvaluatorFunction, CutTool: AdvApprox_Cutting) -> None: ...
	@staticmethod
	def Approximation(self, TotalDimension: int, TotalNumSS: int, LocalDimension: TColStd_Array1OfInteger, First: float, Last: float, Evaluator: AdvApprox_EvaluatorFunction, CutTool: AdvApprox_Cutting, ContinuityOrder: int, NumMaxCoeffs: int, MaxSegments: int, TolerancesArray: TColStd_Array1OfReal, code_precis: int, NumCoeffPerCurveArray: TColStd_Array1OfInteger, LocalCoefficientArray: TColStd_Array1OfReal, IntervalsArray: TColStd_Array1OfReal, ErrorMaxArray: TColStd_Array1OfReal, AverageErrorArray: TColStd_Array1OfReal) -> Tuple[int, int]: ...
	@overload
	def AverageError(self, Dimension: int) -> TColStd_HArray1OfReal: ...
	@overload
	def AverageError(self, Dimension: int, Index: int) -> float: ...
	def Degree(self) -> int: ...
	def HasResult(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def Knots(self) -> TColStd_HArray1OfReal: ...
	@overload
	def MaxError(self, Dimension: int) -> TColStd_HArray1OfReal: ...
	@overload
	def MaxError(self, Dimension: int, Index: int) -> float: ...
	def Multiplicities(self) -> TColStd_HArray1OfInteger: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def NumSubSpaces(self, Dimension: int) -> int: ...
	@overload
	def Poles(self) -> TColgp_HArray2OfPnt: ...
	@overload
	def Poles(self, Index: int, P: TColgp_Array1OfPnt) -> None: ...
	@overload
	def Poles1d(self) -> TColStd_HArray2OfReal: ...
	@overload
	def Poles1d(self, Index: int, P: TColStd_Array1OfReal) -> None: ...
	@overload
	def Poles2d(self) -> TColgp_HArray2OfPnt2d: ...
	@overload
	def Poles2d(self, Index: int, P: TColgp_Array1OfPnt2d) -> None: ...

class AdvApprox_Cutting:
	def Value(self, a: float, b: float) -> Tuple[bool, float]: ...

class AdvApprox_SimpleApprox:
	def __init__(self, TotalDimension: int, TotalNumSS: int, Continuity: GeomAbs_Shape, WorkDegree: int, NbGaussPoints: int, JacobiBase: PLib_JacobiPolynomial, Func: AdvApprox_EvaluatorFunction) -> None: ...
	def AverageError(self, Index: int) -> float: ...
	def Coefficients(self) -> TColStd_HArray1OfReal: ...
	def Degree(self) -> int: ...
	def DifTab(self) -> TColStd_HArray1OfReal: ...
	def FirstConstr(self) -> TColStd_HArray2OfReal: ...
	def IsDone(self) -> bool: ...
	def LastConstr(self) -> TColStd_HArray2OfReal: ...
	def MaxError(self, Index: int) -> float: ...
	def Perform(self, LocalDimension: TColStd_Array1OfInteger, LocalTolerancesArray: TColStd_Array1OfReal, First: float, Last: float, MaxDegree: int) -> None: ...
	def SomTab(self) -> TColStd_HArray1OfReal: ...

class AdvApprox_DichoCutting(AdvApprox_Cutting):
	def __init__(self) -> None: ...
	def Value(self, a: float, b: float) -> Tuple[bool, float]: ...

class AdvApprox_PrefAndRec(AdvApprox_Cutting):
	def __init__(self, RecomendedCut: TColStd_Array1OfReal, PrefferedCut: TColStd_Array1OfReal, Weight: Optional[float]) -> None: ...
	def Value(self, a: float, b: float) -> Tuple[bool, float]: ...

class AdvApprox_PrefCutting(AdvApprox_Cutting):
	def __init__(self, CutPnts: TColStd_Array1OfReal) -> None: ...
	def Value(self, a: float, b: float) -> Tuple[bool, float]: ...

#classnotwrapped
class AdvApprox_EvaluatorFunction: ...

# harray1 classes
# harray2 classes
# harray2 classes

AdvApprox_ApproxAFunction_Approximation = AdvApprox_ApproxAFunction.Approximation
