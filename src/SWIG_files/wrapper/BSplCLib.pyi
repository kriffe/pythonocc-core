from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.math import *
from OCC.Core.TColgp import *
from OCC.Core.gp import *
from OCC.Core.GeomAbs import *


class BSplCLib_MultDistribution(IntEnum):
	BSplCLib_NonConstant: int = ...
	BSplCLib_Constant: int = ...
	BSplCLib_QuasiConstant: int = ...
BSplCLib_NonConstant = BSplCLib_MultDistribution.BSplCLib_NonConstant
BSplCLib_Constant = BSplCLib_MultDistribution.BSplCLib_Constant
BSplCLib_QuasiConstant = BSplCLib_MultDistribution.BSplCLib_QuasiConstant

class BSplCLib_KnotDistribution(IntEnum):
	BSplCLib_NonUniform: int = ...
	BSplCLib_Uniform: int = ...
BSplCLib_NonUniform = BSplCLib_KnotDistribution.BSplCLib_NonUniform
BSplCLib_Uniform = BSplCLib_KnotDistribution.BSplCLib_Uniform

class bsplclib:
	@staticmethod
	def AntiBoorScheme(self, U: float, Degree: int, Dimension: int, Depth: int, Length: int, Tolerance: float) -> Tuple[bool, float, float]: ...
	@staticmethod
	def Bohm(self, U: float, Degree: int, N: int, Dimension: int) -> Tuple[float, float]: ...
	@staticmethod
	def BoorIndex(self, Index: int, Length: int, Depth: int) -> int: ...
	@staticmethod
	def BoorScheme(self, U: float, Degree: int, Dimension: int, Depth: int, Length: int) -> Tuple[float, float]: ...
	@staticmethod
	def BuildBSpMatrix(self, Parameters: TColStd_Array1OfReal, OrderArray: TColStd_Array1OfInteger, FlatKnots: TColStd_Array1OfReal, Degree: int, Matrix: math_Matrix) -> Tuple[int, int, int]: ...
	@staticmethod
	def BuildBoor(self, Index: int, Length: int, Dimension: int, Poles: TColStd_Array1OfReal) -> float: ...
	@overload
	@staticmethod
	def BuildCache(self, U: float, InverseOfSpanDomain: float, PeriodicFlag: bool, Degree: int, FlatKnots: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, CachePoles: TColgp_Array1OfPnt, CacheWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def BuildCache(self, U: float, InverseOfSpanDomain: float, PeriodicFlag: bool, Degree: int, FlatKnots: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, CachePoles: TColgp_Array1OfPnt2d, CacheWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def BuildCache(self, theParameter: float, theSpanDomain: float, thePeriodicFlag: bool, theDegree: int, theSpanIndex: int, theFlatKnots: TColStd_Array1OfReal, thePoles: TColgp_Array1OfPnt, theWeights: TColStd_Array1OfReal, theCacheArray: TColStd_Array2OfReal) -> None: ...
	@overload
	@staticmethod
	def BuildCache(self, theParameter: float, theSpanDomain: float, thePeriodicFlag: bool, theDegree: int, theSpanIndex: int, theFlatKnots: TColStd_Array1OfReal, thePoles: TColgp_Array1OfPnt2d, theWeights: TColStd_Array1OfReal, theCacheArray: TColStd_Array2OfReal) -> None: ...
	@overload
	@staticmethod
	def BuildEval(self, Degree: int, Index: int, Poles: TColStd_Array1OfReal, Weights: TColStd_Array1OfReal) -> float: ...
	@overload
	@staticmethod
	def BuildEval(self, Degree: int, Index: int, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal) -> float: ...
	@overload
	@staticmethod
	def BuildEval(self, Degree: int, Index: int, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal) -> float: ...
	@staticmethod
	def BuildKnots(self, Degree: int, Index: int, Periodic: bool, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger) -> float: ...
	@staticmethod
	def BuildSchoenbergPoints(self, Degree: int, FlatKnots: TColStd_Array1OfReal, Parameters: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def CacheD0(self, U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Point: gp_Pnt) -> None: ...
	@overload
	@staticmethod
	def CacheD0(self, U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Point: gp_Pnt2d) -> None: ...
	@overload
	@staticmethod
	def CacheD1(self, U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Point: gp_Pnt, Vec: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def CacheD1(self, U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Point: gp_Pnt2d, Vec: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def CacheD2(self, U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Point: gp_Pnt, Vec1: gp_Vec, Vec2: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def CacheD2(self, U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Point: gp_Pnt2d, Vec1: gp_Vec2d, Vec2: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def CacheD3(self, U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Point: gp_Pnt, Vec1: gp_Vec, Vec2: gp_Vec, Vec3: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def CacheD3(self, U: float, Degree: int, CacheParameter: float, SpanLenght: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Point: gp_Pnt2d, Vec1: gp_Vec2d, Vec2: gp_Vec2d, Vec3: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def CoefsD0(self, U: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Point: gp_Pnt) -> None: ...
	@overload
	@staticmethod
	def CoefsD0(self, U: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Point: gp_Pnt2d) -> None: ...
	@overload
	@staticmethod
	def CoefsD1(self, U: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Point: gp_Pnt, Vec: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def CoefsD1(self, U: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Point: gp_Pnt2d, Vec: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def CoefsD2(self, U: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Point: gp_Pnt, Vec1: gp_Vec, Vec2: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def CoefsD2(self, U: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Point: gp_Pnt2d, Vec1: gp_Vec2d, Vec2: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def CoefsD3(self, U: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Point: gp_Pnt, Vec1: gp_Vec, Vec2: gp_Vec, Vec3: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def CoefsD3(self, U: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Point: gp_Pnt2d, Vec1: gp_Vec2d, Vec2: gp_Vec2d, Vec3: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def D0(self, U: float, Index: int, Degree: int, Periodic: bool, Poles: TColStd_Array1OfReal, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger) -> float: ...
	@overload
	@staticmethod
	def D0(self, U: float, Index: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, P: gp_Pnt) -> None: ...
	@overload
	@staticmethod
	def D0(self, U: float, UIndex: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, P: gp_Pnt2d) -> None: ...
	@overload
	@staticmethod
	def D0(self, U: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, P: gp_Pnt) -> None: ...
	@overload
	@staticmethod
	def D0(self, U: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, P: gp_Pnt2d) -> None: ...
	@overload
	@staticmethod
	def D1(self, U: float, Index: int, Degree: int, Periodic: bool, Poles: TColStd_Array1OfReal, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger) -> Tuple[float, float]: ...
	@overload
	@staticmethod
	def D1(self, U: float, Index: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, P: gp_Pnt, V: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def D1(self, U: float, UIndex: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def D1(self, U: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, P: gp_Pnt, V: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def D1(self, U: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def D2(self, U: float, Index: int, Degree: int, Periodic: bool, Poles: TColStd_Array1OfReal, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger) -> Tuple[float, float, float]: ...
	@overload
	@staticmethod
	def D2(self, U: float, Index: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def D2(self, U: float, UIndex: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def D2(self, U: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def D2(self, U: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def D3(self, U: float, Index: int, Degree: int, Periodic: bool, Poles: TColStd_Array1OfReal, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger) -> Tuple[float, float, float, float]: ...
	@overload
	@staticmethod
	def D3(self, U: float, Index: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def D3(self, U: float, UIndex: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	@overload
	@staticmethod
	def D3(self, U: float, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	@overload
	@staticmethod
	def D3(self, U: float, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d) -> None: ...
	@staticmethod
	def Derivative(self, Degree: int, Dimension: int, Length: int, Order: int) -> Tuple[float, float]: ...
	@overload
	@staticmethod
	def Eval(self, U: float, Degree: int, Dimension: int) -> Tuple[float, float]: ...
	@overload
	@staticmethod
	def Eval(self, U: float, PeriodicFlag: bool, DerivativeRequest: int, Degree: int, FlatKnots: TColStd_Array1OfReal, ArrayDimension: int) -> Tuple[int, float, float]: ...
	@overload
	@staticmethod
	def Eval(self, U: float, PeriodicFlag: bool, DerivativeRequest: int, Degree: int, FlatKnots: TColStd_Array1OfReal, ArrayDimension: int) -> Tuple[int, float, float, float, float]: ...
	@overload
	@staticmethod
	def Eval(self, U: float, PeriodicFlag: bool, HomogeneousFlag: bool, Degree: int, FlatKnots: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Point: gp_Pnt) -> Tuple[int, float]: ...
	@overload
	@staticmethod
	def Eval(self, U: float, PeriodicFlag: bool, HomogeneousFlag: bool, Degree: int, FlatKnots: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Point: gp_Pnt2d) -> Tuple[int, float]: ...
	@staticmethod
	def EvalBsplineBasis(self, DerivativeOrder: int, Order: int, FlatKnots: TColStd_Array1OfReal, Parameter: float, BsplineBasis: math_Matrix, isPeriodic: Optional[bool]) -> Tuple[int, int]: ...
	@staticmethod
	def FactorBandedMatrix(self, Matrix: math_Matrix, UpperBandWidth: int, LowerBandWidth: int) -> Tuple[int, int]: ...
	@staticmethod
	def FirstUKnotIndex(self, Degree: int, Mults: TColStd_Array1OfInteger) -> int: ...
	@staticmethod
	def FlatBezierKnots(self, Degree: int) -> float: ...
	@staticmethod
	def FlatIndex(self, Degree: int, Index: int, Mults: TColStd_Array1OfInteger, Periodic: bool) -> int: ...
	@overload
	@staticmethod
	def FunctionMultiply(self, Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: TColStd_Array1OfReal, PolesDimension: int, FlatKnots: TColStd_Array1OfReal, NewDegree: int) -> Tuple[float, float, int]: ...
	@overload
	@staticmethod
	def FunctionMultiply(self, Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: TColStd_Array1OfReal, Poles: TColStd_Array1OfReal, FlatKnots: TColStd_Array1OfReal, NewDegree: int, NewPoles: TColStd_Array1OfReal) -> int: ...
	@overload
	@staticmethod
	def FunctionMultiply(self, Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt2d, FlatKnots: TColStd_Array1OfReal, NewDegree: int, NewPoles: TColgp_Array1OfPnt2d) -> int: ...
	@overload
	@staticmethod
	def FunctionMultiply(self, Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt, FlatKnots: TColStd_Array1OfReal, NewDegree: int, NewPoles: TColgp_Array1OfPnt) -> int: ...
	@overload
	@staticmethod
	def FunctionReparameterise(self, Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: TColStd_Array1OfReal, PolesDimension: int, FlatKnots: TColStd_Array1OfReal, NewDegree: int) -> Tuple[float, float, int]: ...
	@overload
	@staticmethod
	def FunctionReparameterise(self, Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: TColStd_Array1OfReal, Poles: TColStd_Array1OfReal, FlatKnots: TColStd_Array1OfReal, NewDegree: int, NewPoles: TColStd_Array1OfReal) -> int: ...
	@overload
	@staticmethod
	def FunctionReparameterise(self, Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt, FlatKnots: TColStd_Array1OfReal, NewDegree: int, NewPoles: TColgp_Array1OfPnt) -> int: ...
	@overload
	@staticmethod
	def FunctionReparameterise(self, Function: BSplCLib_EvaluatorFunction, BSplineDegree: int, BSplineFlatKnots: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt2d, FlatKnots: TColStd_Array1OfReal, NewDegree: int, NewPoles: TColgp_Array1OfPnt2d) -> int: ...
	@staticmethod
	def GetPole(self, Index: int, Length: int, Depth: int, Dimension: int, Pole: TColStd_Array1OfReal) -> Tuple[float, int]: ...
	@staticmethod
	def Hunt(self, theArray: TColStd_Array1OfReal, theX: float) -> int: ...
	@overload
	@staticmethod
	def IncreaseDegree(self, Degree: int, NewDegree: int, Periodic: bool, Dimension: int, Poles: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NewPoles: TColStd_Array1OfReal, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger) -> None: ...
	@overload
	@staticmethod
	def IncreaseDegree(self, Degree: int, NewDegree: int, Periodic: bool, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt, NewWeights: TColStd_Array1OfReal, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger) -> None: ...
	@overload
	@staticmethod
	def IncreaseDegree(self, Degree: int, NewDegree: int, Periodic: bool, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt2d, NewWeights: TColStd_Array1OfReal, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger) -> None: ...
	@overload
	@staticmethod
	def IncreaseDegree(self, NewDegree: int, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, NewPoles: TColgp_Array1OfPnt, NewWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def IncreaseDegree(self, NewDegree: int, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, NewPoles: TColgp_Array1OfPnt2d, NewWeights: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def IncreaseDegreeCountKnots(self, Degree: int, NewDegree: int, Periodic: bool, Mults: TColStd_Array1OfInteger) -> int: ...
	@overload
	@staticmethod
	def InsertKnot(self, UIndex: int, U: float, UMult: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt, NewWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def InsertKnot(self, UIndex: int, U: float, UMult: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt2d, NewWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def InsertKnots(self, Degree: int, Periodic: bool, Dimension: int, Poles: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, AddKnots: TColStd_Array1OfReal, AddMults: TColStd_Array1OfInteger, NewPoles: TColStd_Array1OfReal, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, Epsilon: float, Add: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def InsertKnots(self, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, AddKnots: TColStd_Array1OfReal, AddMults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt, NewWeights: TColStd_Array1OfReal, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, Epsilon: float, Add: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def InsertKnots(self, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, AddKnots: TColStd_Array1OfReal, AddMults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt2d, NewWeights: TColStd_Array1OfReal, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, Epsilon: float, Add: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def Interpolate(self, Degree: int, FlatKnots: TColStd_Array1OfReal, Parameters: TColStd_Array1OfReal, ContactOrderArray: TColStd_Array1OfInteger, Poles: TColgp_Array1OfPnt) -> int: ...
	@overload
	@staticmethod
	def Interpolate(self, Degree: int, FlatKnots: TColStd_Array1OfReal, Parameters: TColStd_Array1OfReal, ContactOrderArray: TColStd_Array1OfInteger, Poles: TColgp_Array1OfPnt2d) -> int: ...
	@overload
	@staticmethod
	def Interpolate(self, Degree: int, FlatKnots: TColStd_Array1OfReal, Parameters: TColStd_Array1OfReal, ContactOrderArray: TColStd_Array1OfInteger, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal) -> int: ...
	@overload
	@staticmethod
	def Interpolate(self, Degree: int, FlatKnots: TColStd_Array1OfReal, Parameters: TColStd_Array1OfReal, ContactOrderArray: TColStd_Array1OfInteger, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal) -> int: ...
	@overload
	@staticmethod
	def Interpolate(self, Degree: int, FlatKnots: TColStd_Array1OfReal, Parameters: TColStd_Array1OfReal, ContactOrderArray: TColStd_Array1OfInteger, ArrayDimension: int) -> Tuple[float, int]: ...
	@overload
	@staticmethod
	def Interpolate(self, Degree: int, FlatKnots: TColStd_Array1OfReal, Parameters: TColStd_Array1OfReal, ContactOrderArray: TColStd_Array1OfInteger, ArrayDimension: int) -> Tuple[float, float, int]: ...
	@staticmethod
	def IsRational(self, Weights: TColStd_Array1OfReal, I1: int, I2: int, Epsilon: Optional[float]) -> bool: ...
	@staticmethod
	def KnotAnalysis(self, Degree: int, Periodic: bool, CKnots: TColStd_Array1OfReal, CMults: TColStd_Array1OfInteger, KnotForm: GeomAbs_BSplKnotDistribution) -> int: ...
	@staticmethod
	def KnotForm(self, Knots: TColStd_Array1OfReal, FromK1: int, ToK2: int) -> BSplCLib_KnotDistribution: ...
	@overload
	@staticmethod
	def KnotSequence(self, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, KnotSeq: TColStd_Array1OfReal, Periodic: Optional[bool]) -> None: ...
	@overload
	@staticmethod
	def KnotSequence(self, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, Degree: int, Periodic: bool, KnotSeq: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def KnotSequenceLength(self, Mults: TColStd_Array1OfInteger, Degree: int, Periodic: bool) -> int: ...
	@staticmethod
	def Knots(self, KnotSeq: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, Periodic: Optional[bool]) -> None: ...
	@staticmethod
	def KnotsLength(self, KnotSeq: TColStd_Array1OfReal, Periodic: Optional[bool]) -> int: ...
	@staticmethod
	def LastUKnotIndex(self, Degree: int, Mults: TColStd_Array1OfInteger) -> int: ...
	@overload
	@staticmethod
	def LocateParameter(self, Degree: int, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, U: float, IsPeriodic: bool, FromK1: int, ToK2: int) -> Tuple[int, float]: ...
	@overload
	@staticmethod
	def LocateParameter(self, Degree: int, Knots: TColStd_Array1OfReal, U: float, IsPeriodic: bool, FromK1: int, ToK2: int) -> Tuple[int, float]: ...
	@overload
	@staticmethod
	def LocateParameter(self, Degree: int, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, U: float, Periodic: bool) -> Tuple[int, float]: ...
	@staticmethod
	def MaxDegree(self) -> int: ...
	@staticmethod
	def MaxKnotMult(self, Mults: TColStd_Array1OfInteger, K1: int, K2: int) -> int: ...
	@staticmethod
	def MergeBSplineKnots(self, Tolerance: float, StartValue: float, EndValue: float, Degree1: int, Knots1: TColStd_Array1OfReal, Mults1: TColStd_Array1OfInteger, Degree2: int, Knots2: TColStd_Array1OfReal, Mults2: TColStd_Array1OfInteger, NewKnots: TColStd_HArray1OfReal, NewMults: TColStd_HArray1OfInteger) -> int: ...
	@staticmethod
	def MinKnotMult(self, Mults: TColStd_Array1OfInteger, K1: int, K2: int) -> int: ...
	@overload
	@staticmethod
	def MovePoint(self, U: float, Displ: gp_Vec2d, Index1: int, Index2: int, Degree: int, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, FlatKnots: TColStd_Array1OfReal, NewPoles: TColgp_Array1OfPnt2d) -> Tuple[int, int]: ...
	@overload
	@staticmethod
	def MovePoint(self, U: float, Displ: gp_Vec, Index1: int, Index2: int, Degree: int, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, FlatKnots: TColStd_Array1OfReal, NewPoles: TColgp_Array1OfPnt) -> Tuple[int, int]: ...
	@overload
	@staticmethod
	def MovePointAndTangent(self, U: float, ArrayDimension: int, Tolerance: float, Degree: int, StartingCondition: int, EndingCondition: int, Weights: TColStd_Array1OfReal, FlatKnots: TColStd_Array1OfReal) -> Tuple[float, float, float, float, int]: ...
	@overload
	@staticmethod
	def MovePointAndTangent(self, U: float, Delta: gp_Vec, DeltaDerivative: gp_Vec, Tolerance: float, Degree: int, StartingCondition: int, EndingCondition: int, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, FlatKnots: TColStd_Array1OfReal, NewPoles: TColgp_Array1OfPnt) -> int: ...
	@overload
	@staticmethod
	def MovePointAndTangent(self, U: float, Delta: gp_Vec2d, DeltaDerivative: gp_Vec2d, Tolerance: float, Degree: int, StartingCondition: int, EndingCondition: int, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, FlatKnots: TColStd_Array1OfReal, NewPoles: TColgp_Array1OfPnt2d) -> int: ...
	@staticmethod
	def MultForm(self, Mults: TColStd_Array1OfInteger, FromK1: int, ToK2: int) -> BSplCLib_MultDistribution: ...
	@staticmethod
	def NbPoles(self, Degree: int, Periodic: bool, Mults: TColStd_Array1OfInteger) -> int: ...
	@staticmethod
	def NoMults(self) -> TColStd_Array1OfInteger: ...
	@staticmethod
	def NoWeights(self) -> TColStd_Array1OfReal: ...
	@staticmethod
	def PoleIndex(self, Degree: int, Index: int, Periodic: bool, Mults: TColStd_Array1OfInteger) -> int: ...
	@overload
	@staticmethod
	def PolesCoefficients(self, Poles: TColgp_Array1OfPnt2d, CachePoles: TColgp_Array1OfPnt2d) -> None: ...
	@overload
	@staticmethod
	def PolesCoefficients(self, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, CachePoles: TColgp_Array1OfPnt2d, CacheWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def PolesCoefficients(self, Poles: TColgp_Array1OfPnt, CachePoles: TColgp_Array1OfPnt) -> None: ...
	@overload
	@staticmethod
	def PolesCoefficients(self, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, CachePoles: TColgp_Array1OfPnt, CacheWeights: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def PrepareInsertKnots(self, Degree: int, Periodic: bool, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, AddKnots: TColStd_Array1OfReal, AddMults: TColStd_Array1OfInteger, Epsilon: float, Add: Optional[bool]) -> Tuple[bool, int, int]: ...
	@staticmethod
	def PrepareTrimming(self, Degree: int, Periodic: bool, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, U1: float, U2: float) -> Tuple[int, int]: ...
	@staticmethod
	def PrepareUnperiodize(self, Degree: int, Mults: TColStd_Array1OfInteger) -> Tuple[int, int]: ...
	@overload
	@staticmethod
	def RaiseMultiplicity(self, KnotIndex: int, Mult: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt, NewWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def RaiseMultiplicity(self, KnotIndex: int, Mult: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt2d, NewWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def RemoveKnot(self, Index: int, Mult: int, Degree: int, Periodic: bool, Dimension: int, Poles: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NewPoles: TColStd_Array1OfReal, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, Tolerance: float) -> bool: ...
	@overload
	@staticmethod
	def RemoveKnot(self, Index: int, Mult: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt, NewWeights: TColStd_Array1OfReal, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, Tolerance: float) -> bool: ...
	@overload
	@staticmethod
	def RemoveKnot(self, Index: int, Mult: int, Degree: int, Periodic: bool, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt2d, NewWeights: TColStd_Array1OfReal, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, Tolerance: float) -> bool: ...
	@staticmethod
	def Reparametrize(self, U1: float, U2: float, Knots: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def Resolution(self, ArrayDimension: int, NumPoles: int, Weights: TColStd_Array1OfReal, FlatKnots: TColStd_Array1OfReal, Degree: int, Tolerance3D: float) -> Tuple[float, float]: ...
	@overload
	@staticmethod
	def Resolution(self, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, NumPoles: int, FlatKnots: TColStd_Array1OfReal, Degree: int, Tolerance3D: float) -> float: ...
	@overload
	@staticmethod
	def Resolution(self, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, NumPoles: int, FlatKnots: TColStd_Array1OfReal, Degree: int, Tolerance3D: float) -> float: ...
	@overload
	@staticmethod
	def Reverse(self, Knots: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def Reverse(self, Mults: TColStd_Array1OfInteger) -> None: ...
	@overload
	@staticmethod
	def Reverse(self, Poles: TColgp_Array1OfPnt, Last: int) -> None: ...
	@overload
	@staticmethod
	def Reverse(self, Poles: TColgp_Array1OfPnt2d, Last: int) -> None: ...
	@overload
	@staticmethod
	def Reverse(self, Weights: TColStd_Array1OfReal, Last: int) -> None: ...
	@overload
	@staticmethod
	def SolveBandedSystem(self, Matrix: math_Matrix, UpperBandWidth: int, LowerBandWidth: int, ArrayDimension: int) -> Tuple[int, float]: ...
	@overload
	@staticmethod
	def SolveBandedSystem(self, Matrix: math_Matrix, UpperBandWidth: int, LowerBandWidth: int, Array: TColgp_Array1OfPnt2d) -> int: ...
	@overload
	@staticmethod
	def SolveBandedSystem(self, Matrix: math_Matrix, UpperBandWidth: int, LowerBandWidth: int, Array: TColgp_Array1OfPnt) -> int: ...
	@overload
	@staticmethod
	def SolveBandedSystem(self, Matrix: math_Matrix, UpperBandWidth: int, LowerBandWidth: int, HomogenousFlag: bool, ArrayDimension: int) -> Tuple[int, float, float]: ...
	@overload
	@staticmethod
	def SolveBandedSystem(self, Matrix: math_Matrix, UpperBandWidth: int, LowerBandWidth: int, HomogenousFlag: bool, Array: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal) -> int: ...
	@overload
	@staticmethod
	def SolveBandedSystem(self, Matrix: math_Matrix, UpperBandWidth: int, LowerBandWidth: int, HomogeneousFlag: bool, Array: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal) -> int: ...
	@staticmethod
	def TangExtendToConstraint(self, FlatKnots: TColStd_Array1OfReal, C1Coefficient: float, NumPoles: int, Dimension: int, Degree: int, ConstraintPoint: TColStd_Array1OfReal, Continuity: int, After: bool) -> Tuple[float, int, int, float, float]: ...
	@overload
	@staticmethod
	def Trimming(self, Degree: int, Periodic: bool, Dimension: int, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, Poles: TColStd_Array1OfReal, U1: float, U2: float, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, NewPoles: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def Trimming(self, Degree: int, Periodic: bool, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, U1: float, U2: float, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt, NewWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def Trimming(self, Degree: int, Periodic: bool, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, U1: float, U2: float, NewKnots: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, NewPoles: TColgp_Array1OfPnt2d, NewWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def Unperiodize(self, Degree: int, Dimension: int, Mults: TColStd_Array1OfInteger, Knots: TColStd_Array1OfReal, Poles: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, NewKnots: TColStd_Array1OfReal, NewPoles: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def Unperiodize(self, Degree: int, Mults: TColStd_Array1OfInteger, Knots: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, NewKnots: TColStd_Array1OfReal, NewPoles: TColgp_Array1OfPnt, NewWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	@staticmethod
	def Unperiodize(self, Degree: int, Mults: TColStd_Array1OfInteger, Knots: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, NewMults: TColStd_Array1OfInteger, NewKnots: TColStd_Array1OfReal, NewPoles: TColgp_Array1OfPnt2d, NewWeights: TColStd_Array1OfReal) -> None: ...

class BSplCLib_Cache(Standard_Transient):
	@overload
	def __init__(self, theDegree: int, thePeriodic: bool, theFlatKnots: TColStd_Array1OfReal, thePoles2d: TColgp_Array1OfPnt2d, theWeights: Optional[TColStd_Array1OfReal]) -> None: ...
	@overload
	def __init__(self, theDegree: int, thePeriodic: bool, theFlatKnots: TColStd_Array1OfReal, thePoles: TColgp_Array1OfPnt, theWeights: Optional[TColStd_Array1OfReal]) -> None: ...
	@overload
	def BuildCache(self, theParameter: float, theFlatKnots: TColStd_Array1OfReal, thePoles2d: TColgp_Array1OfPnt2d, theWeights: TColStd_Array1OfReal) -> None: ...
	@overload
	def BuildCache(self, theParameter: float, theFlatKnots: TColStd_Array1OfReal, thePoles: TColgp_Array1OfPnt, theWeights: Optional[TColStd_Array1OfReal]) -> None: ...
	@overload
	def D0(self, theParameter: float, thePoint: gp_Pnt2d) -> None: ...
	@overload
	def D0(self, theParameter: float, thePoint: gp_Pnt) -> None: ...
	@overload
	def D1(self, theParameter: float, thePoint: gp_Pnt2d, theTangent: gp_Vec2d) -> None: ...
	@overload
	def D1(self, theParameter: float, thePoint: gp_Pnt, theTangent: gp_Vec) -> None: ...
	@overload
	def D2(self, theParameter: float, thePoint: gp_Pnt2d, theTangent: gp_Vec2d, theCurvature: gp_Vec2d) -> None: ...
	@overload
	def D2(self, theParameter: float, thePoint: gp_Pnt, theTangent: gp_Vec, theCurvature: gp_Vec) -> None: ...
	@overload
	def D3(self, theParameter: float, thePoint: gp_Pnt2d, theTangent: gp_Vec2d, theCurvature: gp_Vec2d, theTorsion: gp_Vec2d) -> None: ...
	@overload
	def D3(self, theParameter: float, thePoint: gp_Pnt, theTangent: gp_Vec, theCurvature: gp_Vec, theTorsion: gp_Vec) -> None: ...
	def IsCacheValid(self, theParameter: float) -> bool: ...

class BSplCLib_CacheParams:
	def __init__(self, theDegree: int, thePeriodic: bool, theFlatKnots: TColStd_Array1OfReal) -> None: ...
	def IsCacheValid(self, theParameter: float) -> bool: ...
	def LocateParameter(self, theFlatKnots: TColStd_Array1OfReal) -> float: ...
	def PeriodicNormalization(self, theParameter: float) -> float: ...

#classnotwrapped
class BSplCLib_EvaluatorFunction: ...

# harray1 classes
# harray2 classes
# hsequence classes

bsplclib_AntiBoorScheme = bsplclib.AntiBoorScheme
bsplclib_Bohm = bsplclib.Bohm
bsplclib_BoorIndex = bsplclib.BoorIndex
bsplclib_BoorScheme = bsplclib.BoorScheme
bsplclib_BuildBSpMatrix = bsplclib.BuildBSpMatrix
bsplclib_BuildBoor = bsplclib.BuildBoor
bsplclib_BuildCache = bsplclib.BuildCache
bsplclib_BuildCache = bsplclib.BuildCache
bsplclib_BuildCache = bsplclib.BuildCache
bsplclib_BuildCache = bsplclib.BuildCache
bsplclib_BuildEval = bsplclib.BuildEval
bsplclib_BuildEval = bsplclib.BuildEval
bsplclib_BuildEval = bsplclib.BuildEval
bsplclib_BuildKnots = bsplclib.BuildKnots
bsplclib_BuildSchoenbergPoints = bsplclib.BuildSchoenbergPoints
bsplclib_CacheD0 = bsplclib.CacheD0
bsplclib_CacheD0 = bsplclib.CacheD0
bsplclib_CacheD1 = bsplclib.CacheD1
bsplclib_CacheD1 = bsplclib.CacheD1
bsplclib_CacheD2 = bsplclib.CacheD2
bsplclib_CacheD2 = bsplclib.CacheD2
bsplclib_CacheD3 = bsplclib.CacheD3
bsplclib_CacheD3 = bsplclib.CacheD3
bsplclib_CoefsD0 = bsplclib.CoefsD0
bsplclib_CoefsD0 = bsplclib.CoefsD0
bsplclib_CoefsD1 = bsplclib.CoefsD1
bsplclib_CoefsD1 = bsplclib.CoefsD1
bsplclib_CoefsD2 = bsplclib.CoefsD2
bsplclib_CoefsD2 = bsplclib.CoefsD2
bsplclib_CoefsD3 = bsplclib.CoefsD3
bsplclib_CoefsD3 = bsplclib.CoefsD3
bsplclib_D0 = bsplclib.D0
bsplclib_D0 = bsplclib.D0
bsplclib_D0 = bsplclib.D0
bsplclib_D0 = bsplclib.D0
bsplclib_D0 = bsplclib.D0
bsplclib_D1 = bsplclib.D1
bsplclib_D1 = bsplclib.D1
bsplclib_D1 = bsplclib.D1
bsplclib_D1 = bsplclib.D1
bsplclib_D1 = bsplclib.D1
bsplclib_D2 = bsplclib.D2
bsplclib_D2 = bsplclib.D2
bsplclib_D2 = bsplclib.D2
bsplclib_D2 = bsplclib.D2
bsplclib_D2 = bsplclib.D2
bsplclib_D3 = bsplclib.D3
bsplclib_D3 = bsplclib.D3
bsplclib_D3 = bsplclib.D3
bsplclib_D3 = bsplclib.D3
bsplclib_D3 = bsplclib.D3
bsplclib_Derivative = bsplclib.Derivative
bsplclib_Eval = bsplclib.Eval
bsplclib_Eval = bsplclib.Eval
bsplclib_Eval = bsplclib.Eval
bsplclib_Eval = bsplclib.Eval
bsplclib_Eval = bsplclib.Eval
bsplclib_EvalBsplineBasis = bsplclib.EvalBsplineBasis
bsplclib_FactorBandedMatrix = bsplclib.FactorBandedMatrix
bsplclib_FirstUKnotIndex = bsplclib.FirstUKnotIndex
bsplclib_FlatBezierKnots = bsplclib.FlatBezierKnots
bsplclib_FlatIndex = bsplclib.FlatIndex
bsplclib_FunctionMultiply = bsplclib.FunctionMultiply
bsplclib_FunctionMultiply = bsplclib.FunctionMultiply
bsplclib_FunctionMultiply = bsplclib.FunctionMultiply
bsplclib_FunctionMultiply = bsplclib.FunctionMultiply
bsplclib_FunctionReparameterise = bsplclib.FunctionReparameterise
bsplclib_FunctionReparameterise = bsplclib.FunctionReparameterise
bsplclib_FunctionReparameterise = bsplclib.FunctionReparameterise
bsplclib_FunctionReparameterise = bsplclib.FunctionReparameterise
bsplclib_GetPole = bsplclib.GetPole
bsplclib_Hunt = bsplclib.Hunt
bsplclib_IncreaseDegree = bsplclib.IncreaseDegree
bsplclib_IncreaseDegree = bsplclib.IncreaseDegree
bsplclib_IncreaseDegree = bsplclib.IncreaseDegree
bsplclib_IncreaseDegree = bsplclib.IncreaseDegree
bsplclib_IncreaseDegree = bsplclib.IncreaseDegree
bsplclib_IncreaseDegreeCountKnots = bsplclib.IncreaseDegreeCountKnots
bsplclib_InsertKnot = bsplclib.InsertKnot
bsplclib_InsertKnot = bsplclib.InsertKnot
bsplclib_InsertKnots = bsplclib.InsertKnots
bsplclib_InsertKnots = bsplclib.InsertKnots
bsplclib_InsertKnots = bsplclib.InsertKnots
bsplclib_Interpolate = bsplclib.Interpolate
bsplclib_Interpolate = bsplclib.Interpolate
bsplclib_Interpolate = bsplclib.Interpolate
bsplclib_Interpolate = bsplclib.Interpolate
bsplclib_Interpolate = bsplclib.Interpolate
bsplclib_Interpolate = bsplclib.Interpolate
bsplclib_IsRational = bsplclib.IsRational
bsplclib_KnotAnalysis = bsplclib.KnotAnalysis
bsplclib_KnotForm = bsplclib.KnotForm
bsplclib_KnotSequence = bsplclib.KnotSequence
bsplclib_KnotSequence = bsplclib.KnotSequence
bsplclib_KnotSequenceLength = bsplclib.KnotSequenceLength
bsplclib_Knots = bsplclib.Knots
bsplclib_KnotsLength = bsplclib.KnotsLength
bsplclib_LastUKnotIndex = bsplclib.LastUKnotIndex
bsplclib_LocateParameter = bsplclib.LocateParameter
bsplclib_LocateParameter = bsplclib.LocateParameter
bsplclib_LocateParameter = bsplclib.LocateParameter
bsplclib_MaxDegree = bsplclib.MaxDegree
bsplclib_MaxKnotMult = bsplclib.MaxKnotMult
bsplclib_MergeBSplineKnots = bsplclib.MergeBSplineKnots
bsplclib_MinKnotMult = bsplclib.MinKnotMult
bsplclib_MovePoint = bsplclib.MovePoint
bsplclib_MovePoint = bsplclib.MovePoint
bsplclib_MovePointAndTangent = bsplclib.MovePointAndTangent
bsplclib_MovePointAndTangent = bsplclib.MovePointAndTangent
bsplclib_MovePointAndTangent = bsplclib.MovePointAndTangent
bsplclib_MultForm = bsplclib.MultForm
bsplclib_NbPoles = bsplclib.NbPoles
bsplclib_NoMults = bsplclib.NoMults
bsplclib_NoWeights = bsplclib.NoWeights
bsplclib_PoleIndex = bsplclib.PoleIndex
bsplclib_PolesCoefficients = bsplclib.PolesCoefficients
bsplclib_PolesCoefficients = bsplclib.PolesCoefficients
bsplclib_PolesCoefficients = bsplclib.PolesCoefficients
bsplclib_PolesCoefficients = bsplclib.PolesCoefficients
bsplclib_PrepareInsertKnots = bsplclib.PrepareInsertKnots
bsplclib_PrepareTrimming = bsplclib.PrepareTrimming
bsplclib_PrepareUnperiodize = bsplclib.PrepareUnperiodize
bsplclib_RaiseMultiplicity = bsplclib.RaiseMultiplicity
bsplclib_RaiseMultiplicity = bsplclib.RaiseMultiplicity
bsplclib_RemoveKnot = bsplclib.RemoveKnot
bsplclib_RemoveKnot = bsplclib.RemoveKnot
bsplclib_RemoveKnot = bsplclib.RemoveKnot
bsplclib_Reparametrize = bsplclib.Reparametrize
bsplclib_Resolution = bsplclib.Resolution
bsplclib_Resolution = bsplclib.Resolution
bsplclib_Resolution = bsplclib.Resolution
bsplclib_Reverse = bsplclib.Reverse
bsplclib_Reverse = bsplclib.Reverse
bsplclib_Reverse = bsplclib.Reverse
bsplclib_Reverse = bsplclib.Reverse
bsplclib_Reverse = bsplclib.Reverse
bsplclib_SolveBandedSystem = bsplclib.SolveBandedSystem
bsplclib_SolveBandedSystem = bsplclib.SolveBandedSystem
bsplclib_SolveBandedSystem = bsplclib.SolveBandedSystem
bsplclib_SolveBandedSystem = bsplclib.SolveBandedSystem
bsplclib_SolveBandedSystem = bsplclib.SolveBandedSystem
bsplclib_SolveBandedSystem = bsplclib.SolveBandedSystem
bsplclib_TangExtendToConstraint = bsplclib.TangExtendToConstraint
bsplclib_Trimming = bsplclib.Trimming
bsplclib_Trimming = bsplclib.Trimming
bsplclib_Trimming = bsplclib.Trimming
bsplclib_Unperiodize = bsplclib.Unperiodize
bsplclib_Unperiodize = bsplclib.Unperiodize
bsplclib_Unperiodize = bsplclib.Unperiodize
