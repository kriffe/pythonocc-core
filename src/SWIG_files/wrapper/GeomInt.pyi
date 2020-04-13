from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.math import *
from OCC.Core.AppParCurves import *
from OCC.Core.TColStd import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.IntPatch import *
from OCC.Core.GeomAdaptor import *
from OCC.Core.gp import *
from OCC.Core.Bnd import *
from OCC.Core.Adaptor3d import *
from OCC.Core.TopAbs import *
from OCC.Core.Approx import *
from OCC.Core.IntImp import *
from OCC.Core.ApproxInt import *
from OCC.Core.IntSurf import *
from OCC.Core.TColgp import *

#the following typedef cannot be wrapped as is
GeomInt_SequenceOfParameterAndOrientation = NewType('GeomInt_SequenceOfParameterAndOrientation', Any)
#the following typedef cannot be wrapped as is
GeomInt_VectorOfReal = NewType('GeomInt_VectorOfReal', Any)

class geomint:
	@staticmethod
	def AdjustPeriodic(self, thePar: float, theParMin: float, theParMax: float, thePeriod: float, theEps: Optional[float]) -> Tuple[bool, float, float]: ...

class GeomInt_BSpGradient_BFGSOfMyBSplGradientOfTheComputeLineOfWLApprox(math_BFGS):
	def __init__(self, F: math_MultipleVarFunctionWithGradient, StartingPoint: math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: Optional[int]) -> None: ...
	def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool: ...

class GeomInt_BSpParFunctionOfMyBSplGradientOfTheComputeLineOfWLApprox(math_MultipleVarFunctionWithGradient):
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, NbPol: int) -> None: ...
	def CurveValue(self) -> AppParCurves_MultiBSpCurve: ...
	def DerivativeFunctionMatrix(self) -> math_Matrix: ...
	def Error(self, IPoint: int, CurveIndex: int) -> float: ...
	def FirstConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, FirstPoint: int) -> AppParCurves_Constraint: ...
	def FunctionMatrix(self) -> math_Matrix: ...
	def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
	def Index(self) -> math_IntegerVector: ...
	def LastConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, LastPoint: int) -> AppParCurves_Constraint: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def NbVariables(self) -> int: ...
	def NewParameters(self) -> math_Vector: ...
	def SetFirstLambda(self, l1: float) -> None: ...
	def SetLastLambda(self, l2: float) -> None: ...
	def Value(self, X: math_Vector) -> Tuple[bool, float]: ...
	def Values(self, X: math_Vector, G: math_Vector) -> Tuple[bool, float]: ...

class GeomInt_BSpParLeastSquareOfMyBSplGradientOfTheComputeLineOfWLApprox:
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	def BSplineValue(self) -> AppParCurves_MultiBSpCurve: ...
	def BezierValue(self) -> AppParCurves_MultiCurve: ...
	def DerivativeFunctionMatrix(self) -> math_Matrix: ...
	def Distance(self) -> math_Matrix: ...
	def Error(self) -> Tuple[float, float, float]: ...
	def ErrorGradient(self, Grad: math_Vector) -> Tuple[float, float, float]: ...
	def FirstLambda(self) -> float: ...
	def FunctionMatrix(self) -> math_Matrix: ...
	def IsDone(self) -> bool: ...
	def KIndex(self) -> math_IntegerVector: ...
	def LastLambda(self) -> float: ...
	@overload
	def Perform(self, Parameters: math_Vector) -> None: ...
	@overload
	def Perform(self, Parameters: math_Vector, l1: float, l2: float) -> None: ...
	@overload
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, l1: float, l2: float) -> None: ...
	@overload
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, V1c: math_Vector, V2c: math_Vector, l1: float, l2: float) -> None: ...
	def Points(self) -> math_Matrix: ...
	def Poles(self) -> math_Matrix: ...

class GeomInt_Gradient_BFGSOfMyGradientOfTheComputeLineBezierOfWLApprox(math_BFGS):
	def __init__(self, F: math_MultipleVarFunctionWithGradient, StartingPoint: math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: Optional[int]) -> None: ...
	def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool: ...

class GeomInt_Gradient_BFGSOfMyGradientbisOfTheComputeLineOfWLApprox(math_BFGS):
	def __init__(self, F: math_MultipleVarFunctionWithGradient, StartingPoint: math_Vector, Tolerance3d: float, Tolerance2d: float, Eps: float, NbIterations: Optional[int]) -> None: ...
	def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool: ...

class GeomInt_IntSS:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S1: Geom_Surface, S2: Geom_Surface, Tol: float, Approx: Optional[bool], ApproxS1: Optional[bool], ApproxS2: Optional[bool]) -> None: ...
	def Boundary(self, Index: int) -> Geom_Curve: ...
	@staticmethod
	def BuildPCurves(self, f: float, l: float, S: Geom_Surface, C: Geom_Curve, C2d: Geom2d_Curve) -> float: ...
	def HasLineOnS1(self, Index: int) -> bool: ...
	def HasLineOnS2(self, Index: int) -> bool: ...
	def IsDone(self) -> bool: ...
	def Line(self, Index: int) -> Geom_Curve: ...
	def LineOnS1(self, Index: int) -> Geom2d_Curve: ...
	def LineOnS2(self, Index: int) -> Geom2d_Curve: ...
	@staticmethod
	def MakeBSpline(self, WL: IntPatch_WLine, ideb: int, ifin: int) -> Geom_Curve: ...
	@staticmethod
	def MakeBSpline2d(self, theWLine: IntPatch_WLine, ideb: int, ifin: int, onFirst: bool) -> Geom2d_BSplineCurve: ...
	def NbBoundaries(self) -> int: ...
	def NbLines(self) -> int: ...
	def NbPoints(self) -> int: ...
	@overload
	def Perform(self, S1: Geom_Surface, S2: Geom_Surface, Tol: float, Approx: Optional[bool], ApproxS1: Optional[bool], ApproxS2: Optional[bool]) -> None: ...
	@overload
	def Perform(self, HS1: GeomAdaptor_HSurface, HS2: GeomAdaptor_HSurface, Tol: float, Approx: Optional[bool], ApproxS1: Optional[bool], ApproxS2: Optional[bool]) -> None: ...
	@overload
	def Perform(self, S1: Geom_Surface, S2: Geom_Surface, Tol: float, U1: float, V1: float, U2: float, V2: float, Approx: Optional[bool], ApproxS1: Optional[bool], ApproxS2: Optional[bool]) -> None: ...
	@overload
	def Perform(self, HS1: GeomAdaptor_HSurface, HS2: GeomAdaptor_HSurface, Tol: float, U1: float, V1: float, U2: float, V2: float, Approx: Optional[bool], ApproxS1: Optional[bool], ApproxS2: Optional[bool]) -> None: ...
	def Pnt2d(self, Index: int, OnFirst: bool) -> gp_Pnt2d: ...
	def Point(self, Index: int) -> gp_Pnt: ...
	def TolReached2d(self) -> float: ...
	def TolReached3d(self) -> float: ...
	@staticmethod
	def TreatRLine(self, theRL: IntPatch_RLine, theHS1: GeomAdaptor_HSurface, theHS2: GeomAdaptor_HSurface, theC3d: Geom_Curve, theC2d1: Geom2d_Curve, theC2d2: Geom2d_Curve) -> float: ...
	@staticmethod
	def TrimILineOnSurfBoundaries(self, theC2d1: Geom2d_Curve, theC2d2: Geom2d_Curve, theBound1: Bnd_Box2d, theBound2: Bnd_Box2d, theArrayOfParameters: GeomInt_VectorOfReal) -> None: ...

class GeomInt_LineConstructor:
	def __init__(self) -> None: ...
	def IsDone(self) -> bool: ...
	def Load(self, D1: Adaptor3d_TopolTool, D2: Adaptor3d_TopolTool, S1: GeomAdaptor_HSurface, S2: GeomAdaptor_HSurface) -> None: ...
	def NbParts(self) -> int: ...
	def Part(self, I: int) -> Tuple[float, float]: ...
	def Perform(self, L: IntPatch_Line) -> None: ...

class GeomInt_LineTool:
	@staticmethod
	def DecompositionOfWLine(self, theWLine: IntPatch_WLine, theSurface1: GeomAdaptor_HSurface, theSurface2: GeomAdaptor_HSurface, aTolSum: float, theLConstructor: GeomInt_LineConstructor, theNewLines: IntPatch_SequenceOfLine) -> bool: ...
	@staticmethod
	def FirstParameter(self, L: IntPatch_Line) -> float: ...
	@staticmethod
	def LastParameter(self, L: IntPatch_Line) -> float: ...
	@staticmethod
	def NbVertex(self, L: IntPatch_Line) -> int: ...
	@staticmethod
	def Vertex(self, L: IntPatch_Line, I: int) -> IntPatch_Point: ...

class GeomInt_MyBSplGradientOfTheComputeLineOfWLApprox:
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, Deg: int, Tol3d: float, Tol2d: float, NbIterations: Optional[int]) -> None: ...
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, Deg: int, Tol3d: float, Tol2d: float, NbIterations: int, lambda1: float, lambda2: float) -> None: ...
	def AverageError(self) -> float: ...
	def Error(self, Index: int) -> float: ...
	def IsDone(self) -> bool: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def Value(self) -> AppParCurves_MultiBSpCurve: ...

class GeomInt_MyGradientOfTheComputeLineBezierOfWLApprox:
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Deg: int, Tol3d: float, Tol2d: float, NbIterations: Optional[int]) -> None: ...
	def AverageError(self) -> float: ...
	def Error(self, Index: int) -> float: ...
	def IsDone(self) -> bool: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def Value(self) -> AppParCurves_MultiCurve: ...

class GeomInt_MyGradientbisOfTheComputeLineOfWLApprox:
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Deg: int, Tol3d: float, Tol2d: float, NbIterations: Optional[int]) -> None: ...
	def AverageError(self) -> float: ...
	def Error(self, Index: int) -> float: ...
	def IsDone(self) -> bool: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def Value(self) -> AppParCurves_MultiCurve: ...

class GeomInt_ParFunctionOfMyGradientOfTheComputeLineBezierOfWLApprox(math_MultipleVarFunctionWithGradient):
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Deg: int) -> None: ...
	def CurveValue(self) -> AppParCurves_MultiCurve: ...
	def Error(self, IPoint: int, CurveIndex: int) -> float: ...
	def FirstConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, FirstPoint: int) -> AppParCurves_Constraint: ...
	def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
	def LastConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, LastPoint: int) -> AppParCurves_Constraint: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def NbVariables(self) -> int: ...
	def NewParameters(self) -> math_Vector: ...
	def Value(self, X: math_Vector) -> Tuple[bool, float]: ...
	def Values(self, X: math_Vector, G: math_Vector) -> Tuple[bool, float]: ...

class GeomInt_ParFunctionOfMyGradientbisOfTheComputeLineOfWLApprox(math_MultipleVarFunctionWithGradient):
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, TheConstraints: AppParCurves_HArray1OfConstraintCouple, Parameters: math_Vector, Deg: int) -> None: ...
	def CurveValue(self) -> AppParCurves_MultiCurve: ...
	def Error(self, IPoint: int, CurveIndex: int) -> float: ...
	def FirstConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, FirstPoint: int) -> AppParCurves_Constraint: ...
	def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
	def LastConstraint(self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, LastPoint: int) -> AppParCurves_Constraint: ...
	def MaxError2d(self) -> float: ...
	def MaxError3d(self) -> float: ...
	def NbVariables(self) -> int: ...
	def NewParameters(self) -> math_Vector: ...
	def Value(self, X: math_Vector) -> Tuple[bool, float]: ...
	def Values(self, X: math_Vector, G: math_Vector) -> Tuple[bool, float]: ...

class GeomInt_ParLeastSquareOfMyGradientOfTheComputeLineBezierOfWLApprox:
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	def BSplineValue(self) -> AppParCurves_MultiBSpCurve: ...
	def BezierValue(self) -> AppParCurves_MultiCurve: ...
	def DerivativeFunctionMatrix(self) -> math_Matrix: ...
	def Distance(self) -> math_Matrix: ...
	def Error(self) -> Tuple[float, float, float]: ...
	def ErrorGradient(self, Grad: math_Vector) -> Tuple[float, float, float]: ...
	def FirstLambda(self) -> float: ...
	def FunctionMatrix(self) -> math_Matrix: ...
	def IsDone(self) -> bool: ...
	def KIndex(self) -> math_IntegerVector: ...
	def LastLambda(self) -> float: ...
	@overload
	def Perform(self, Parameters: math_Vector) -> None: ...
	@overload
	def Perform(self, Parameters: math_Vector, l1: float, l2: float) -> None: ...
	@overload
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, l1: float, l2: float) -> None: ...
	@overload
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, V1c: math_Vector, V2c: math_Vector, l1: float, l2: float) -> None: ...
	def Points(self) -> math_Matrix: ...
	def Poles(self) -> math_Matrix: ...

class GeomInt_ParLeastSquareOfMyGradientbisOfTheComputeLineOfWLApprox:
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, Parameters: math_Vector, NbPol: int) -> None: ...
	@overload
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger, FirstPoint: int, LastPoint: int, FirstCons: AppParCurves_Constraint, LastCons: AppParCurves_Constraint, NbPol: int) -> None: ...
	def BSplineValue(self) -> AppParCurves_MultiBSpCurve: ...
	def BezierValue(self) -> AppParCurves_MultiCurve: ...
	def DerivativeFunctionMatrix(self) -> math_Matrix: ...
	def Distance(self) -> math_Matrix: ...
	def Error(self) -> Tuple[float, float, float]: ...
	def ErrorGradient(self, Grad: math_Vector) -> Tuple[float, float, float]: ...
	def FirstLambda(self) -> float: ...
	def FunctionMatrix(self) -> math_Matrix: ...
	def IsDone(self) -> bool: ...
	def KIndex(self) -> math_IntegerVector: ...
	def LastLambda(self) -> float: ...
	@overload
	def Perform(self, Parameters: math_Vector) -> None: ...
	@overload
	def Perform(self, Parameters: math_Vector, l1: float, l2: float) -> None: ...
	@overload
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, l1: float, l2: float) -> None: ...
	@overload
	def Perform(self, Parameters: math_Vector, V1t: math_Vector, V2t: math_Vector, V1c: math_Vector, V2c: math_Vector, l1: float, l2: float) -> None: ...
	def Points(self) -> math_Matrix: ...
	def Poles(self) -> math_Matrix: ...

class GeomInt_ParameterAndOrientation:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P: float, Or1: TopAbs_Orientation, Or2: TopAbs_Orientation) -> None: ...
	def Orientation1(self) -> TopAbs_Orientation: ...
	def Orientation2(self) -> TopAbs_Orientation: ...
	def Parameter(self) -> float: ...
	def SetOrientation1(self, Or: TopAbs_Orientation) -> None: ...
	def SetOrientation2(self, Or: TopAbs_Orientation) -> None: ...

class GeomInt_ResConstraintOfMyGradientOfTheComputeLineBezierOfWLApprox:
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, SCurv: AppParCurves_MultiCurve, FirstPoint: int, LastPoint: int, Constraints: AppParCurves_HArray1OfConstraintCouple, Bern: math_Matrix, DerivativeBern: math_Matrix, Tolerance: Optional[float]) -> None: ...
	def ConstraintDerivative(self, SSP: GeomInt_TheMultiLineOfWLApprox, Parameters: math_Vector, Deg: int, DA: math_Matrix) -> math_Matrix: ...
	def ConstraintMatrix(self) -> math_Matrix: ...
	def Duale(self) -> math_Vector: ...
	def InverseMatrix(self) -> math_Matrix: ...
	def IsDone(self) -> bool: ...

class GeomInt_ResConstraintOfMyGradientbisOfTheComputeLineOfWLApprox:
	def __init__(self, SSP: GeomInt_TheMultiLineOfWLApprox, SCurv: AppParCurves_MultiCurve, FirstPoint: int, LastPoint: int, Constraints: AppParCurves_HArray1OfConstraintCouple, Bern: math_Matrix, DerivativeBern: math_Matrix, Tolerance: Optional[float]) -> None: ...
	def ConstraintDerivative(self, SSP: GeomInt_TheMultiLineOfWLApprox, Parameters: math_Vector, Deg: int, DA: math_Matrix) -> math_Matrix: ...
	def ConstraintMatrix(self) -> math_Matrix: ...
	def Duale(self) -> math_Vector: ...
	def InverseMatrix(self) -> math_Matrix: ...
	def IsDone(self) -> bool: ...

class GeomInt_TheComputeLineBezierOfWLApprox:
	@overload
	def __init__(self, Line: GeomInt_TheMultiLineOfWLApprox, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	@overload
	def __init__(self, Line: GeomInt_TheMultiLineOfWLApprox, Parameters: math_Vector, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], Squares: Optional[bool]) -> None: ...
	@overload
	def __init__(self, Parameters: math_Vector, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], Squares: Optional[bool]) -> None: ...
	@overload
	def __init__(self, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	def ChangeValue(self, Index: Optional[int]) -> AppParCurves_MultiCurve: ...
	def Error(self, Index: int) -> Tuple[float, float]: ...
	def Init(self, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	def IsAllApproximated(self) -> bool: ...
	def IsToleranceReached(self) -> bool: ...
	def NbMultiCurves(self) -> int: ...
	def Parameters(self, Index: Optional[int]) -> TColStd_Array1OfReal: ...
	def Parametrization(self) -> Approx_ParametrizationType: ...
	def Perform(self, Line: GeomInt_TheMultiLineOfWLApprox) -> None: ...
	def SetConstraints(self, firstC: AppParCurves_Constraint, lastC: AppParCurves_Constraint) -> None: ...
	def SetDegrees(self, degreemin: int, degreemax: int) -> None: ...
	def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None: ...
	def SplineValue(self) -> AppParCurves_MultiBSpCurve: ...
	def Value(self, Index: Optional[int]) -> AppParCurves_MultiCurve: ...

class GeomInt_TheComputeLineOfWLApprox:
	@overload
	def __init__(self, Line: GeomInt_TheMultiLineOfWLApprox, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	@overload
	def __init__(self, Line: GeomInt_TheMultiLineOfWLApprox, Parameters: math_Vector, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], Squares: Optional[bool]) -> None: ...
	@overload
	def __init__(self, Parameters: math_Vector, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], Squares: Optional[bool]) -> None: ...
	@overload
	def __init__(self, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	def ChangeValue(self) -> AppParCurves_MultiBSpCurve: ...
	def Error(self) -> Tuple[float, float]: ...
	def Init(self, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], NbIterations: Optional[int], cutting: Optional[bool], parametrization: Optional[Approx_ParametrizationType], Squares: Optional[bool]) -> None: ...
	def Interpol(self, Line: GeomInt_TheMultiLineOfWLApprox) -> None: ...
	def IsAllApproximated(self) -> bool: ...
	def IsToleranceReached(self) -> bool: ...
	def Parameters(self) -> TColStd_Array1OfReal: ...
	def Perform(self, Line: GeomInt_TheMultiLineOfWLApprox) -> None: ...
	def SetConstraints(self, firstC: AppParCurves_Constraint, lastC: AppParCurves_Constraint) -> None: ...
	def SetContinuity(self, C: int) -> None: ...
	def SetDegrees(self, degreemin: int, degreemax: int) -> None: ...
	def SetKnots(self, Knots: TColStd_Array1OfReal) -> None: ...
	def SetKnotsAndMultiplicities(self, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger) -> None: ...
	def SetParameters(self, ThePar: math_Vector) -> None: ...
	def SetPeriodic(self, thePeriodic: bool) -> None: ...
	def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None: ...
	def Value(self) -> AppParCurves_MultiBSpCurve: ...

class GeomInt_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfWLApprox(math_FunctionSetWithDerivatives):
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

class GeomInt_TheImpPrmSvSurfacesOfWLApprox(ApproxInt_SvSurfaces):
	@overload
	def __init__(self, Surf1: Adaptor3d_HSurface, Surf2: IntSurf_Quadric) -> None: ...
	@overload
	def __init__(self, Surf1: IntSurf_Quadric, Surf2: Adaptor3d_HSurface) -> None: ...
	def Compute(self, Pt: gp_Pnt, Tg: gp_Vec, Tguv1: gp_Vec2d, Tguv2: gp_Vec2d) -> Tuple[bool, float, float, float, float]: ...
	def Pnt(self, u1: float, v1: float, u2: float, v2: float, P: gp_Pnt) -> None: ...
	def SeekPoint(self, u1: float, v1: float, u2: float, v2: float, Point: IntSurf_PntOn2S) -> bool: ...
	def Tangency(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec) -> bool: ...
	def TangencyOnSurf1(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d) -> bool: ...
	def TangencyOnSurf2(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d) -> bool: ...

class GeomInt_TheInt2SOfThePrmPrmSvSurfacesOfWLApprox:
	@overload
	def __init__(self, Param: TColStd_Array1OfReal, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, TolTangency: float) -> None: ...
	@overload
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, TolTangency: float) -> None: ...
	def ChangePoint(self) -> IntSurf_PntOn2S: ...
	def Direction(self) -> gp_Dir: ...
	def DirectionOnS1(self) -> gp_Dir2d: ...
	def DirectionOnS2(self) -> gp_Dir2d: ...
	def Function(self) -> GeomInt_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfWLApprox: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def IsTangent(self) -> bool: ...
	@overload
	def Perform(self, Param: TColStd_Array1OfReal, Rsnld: math_FunctionSetRoot) -> IntImp_ConstIsoparametric: ...
	@overload
	def Perform(self, Param: TColStd_Array1OfReal, Rsnld: math_FunctionSetRoot, ChoixIso: IntImp_ConstIsoparametric) -> IntImp_ConstIsoparametric: ...
	def Point(self) -> IntSurf_PntOn2S: ...

class GeomInt_TheMultiLineOfWLApprox:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, line: IntPatch_WLine, PtrSvSurfaces: None, NbP3d: int, NbP2d: int, ApproxU1V1: bool, ApproxU2V2: bool, xo: float, yo: float, zo: float, u1o: float, v1o: float, u2o: float, v2o: float, P2DOnFirst: bool, IndMin: Optional[int], IndMax: Optional[int]) -> None: ...
	@overload
	def __init__(self, line: IntPatch_WLine, NbP3d: int, NbP2d: int, ApproxU1V1: bool, ApproxU2V2: bool, xo: float, yo: float, zo: float, u1o: float, v1o: float, u2o: float, v2o: float, P2DOnFirst: bool, IndMin: Optional[int], IndMax: Optional[int]) -> None: ...
	def Dump(self) -> None: ...
	def FirstPoint(self) -> int: ...
	def LastPoint(self) -> int: ...
	def MakeMLBetween(self, Low: int, High: int, NbPointsToInsert: int) -> GeomInt_TheMultiLineOfWLApprox: ...
	def MakeMLOneMorePoint(self, Low: int, High: int, indbad: int, OtherLine: GeomInt_TheMultiLineOfWLApprox) -> bool: ...
	def NbP2d(self) -> int: ...
	def NbP3d(self) -> int: ...
	@overload
	def Tangency(self, MPointIndex: int, tabV: TColgp_Array1OfVec) -> bool: ...
	@overload
	def Tangency(self, MPointIndex: int, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	@overload
	def Tangency(self, MPointIndex: int, tabV: TColgp_Array1OfVec, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	@overload
	def Value(self, MPointIndex: int, tabPt: TColgp_Array1OfPnt) -> None: ...
	@overload
	def Value(self, MPointIndex: int, tabPt2d: TColgp_Array1OfPnt2d) -> None: ...
	@overload
	def Value(self, MPointIndex: int, tabPt: TColgp_Array1OfPnt, tabPt2d: TColgp_Array1OfPnt2d) -> None: ...
	def WhatStatus(self) -> Approx_Status: ...

class GeomInt_TheMultiLineToolOfWLApprox:
	@overload
	@staticmethod
	def Curvature(self, ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV: TColgp_Array1OfVec) -> bool: ...
	@overload
	@staticmethod
	def Curvature(self, ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	@overload
	@staticmethod
	def Curvature(self, ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV: TColgp_Array1OfVec, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	@staticmethod
	def Dump(self, ML: GeomInt_TheMultiLineOfWLApprox) -> None: ...
	@staticmethod
	def FirstPoint(self, ML: GeomInt_TheMultiLineOfWLApprox) -> int: ...
	@staticmethod
	def LastPoint(self, ML: GeomInt_TheMultiLineOfWLApprox) -> int: ...
	@staticmethod
	def MakeMLBetween(self, ML: GeomInt_TheMultiLineOfWLApprox, I1: int, I2: int, NbPMin: int) -> GeomInt_TheMultiLineOfWLApprox: ...
	@staticmethod
	def MakeMLOneMorePoint(self, ML: GeomInt_TheMultiLineOfWLApprox, I1: int, I2: int, indbad: int, OtherLine: GeomInt_TheMultiLineOfWLApprox) -> bool: ...
	@staticmethod
	def NbP2d(self, ML: GeomInt_TheMultiLineOfWLApprox) -> int: ...
	@staticmethod
	def NbP3d(self, ML: GeomInt_TheMultiLineOfWLApprox) -> int: ...
	@overload
	@staticmethod
	def Tangency(self, ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV: TColgp_Array1OfVec) -> bool: ...
	@overload
	@staticmethod
	def Tangency(self, ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	@overload
	@staticmethod
	def Tangency(self, ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabV: TColgp_Array1OfVec, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
	@overload
	@staticmethod
	def Value(self, ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabPt: TColgp_Array1OfPnt) -> None: ...
	@overload
	@staticmethod
	def Value(self, ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabPt2d: TColgp_Array1OfPnt2d) -> None: ...
	@overload
	@staticmethod
	def Value(self, ML: GeomInt_TheMultiLineOfWLApprox, MPointIndex: int, tabPt: TColgp_Array1OfPnt, tabPt2d: TColgp_Array1OfPnt2d) -> None: ...
	@staticmethod
	def WhatStatus(self, ML: GeomInt_TheMultiLineOfWLApprox, I1: int, I2: int) -> Approx_Status: ...

class GeomInt_ThePrmPrmSvSurfacesOfWLApprox(ApproxInt_SvSurfaces):
	def __init__(self, Surf1: Adaptor3d_HSurface, Surf2: Adaptor3d_HSurface) -> None: ...
	def Compute(self, Pt: gp_Pnt, Tg: gp_Vec, Tguv1: gp_Vec2d, Tguv2: gp_Vec2d) -> Tuple[bool, float, float, float, float]: ...
	def Pnt(self, u1: float, v1: float, u2: float, v2: float, P: gp_Pnt) -> None: ...
	def SeekPoint(self, u1: float, v1: float, u2: float, v2: float, Point: IntSurf_PntOn2S) -> bool: ...
	def Tangency(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec) -> bool: ...
	def TangencyOnSurf1(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d) -> bool: ...
	def TangencyOnSurf2(self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d) -> bool: ...

class GeomInt_TheZerImpFuncOfTheImpPrmSvSurfacesOfWLApprox(math_FunctionSetWithDerivatives):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, PS: Adaptor3d_HSurface, IS: IntSurf_Quadric) -> None: ...
	@overload
	def __init__(self, IS: IntSurf_Quadric) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def Direction2d(self) -> gp_Dir2d: ...
	def Direction3d(self) -> gp_Vec: ...
	def ISurface(self) -> IntSurf_Quadric: ...
	def IsTangent(self) -> bool: ...
	def NbEquations(self) -> int: ...
	def NbVariables(self) -> int: ...
	def PSurface(self) -> Adaptor3d_HSurface: ...
	def Point(self) -> gp_Pnt: ...
	def Root(self) -> float: ...
	@overload
	def Set(self, PS: Adaptor3d_HSurface) -> None: ...
	@overload
	def Set(self, Tolerance: float) -> None: ...
	def SetImplicitSurface(self, IS: IntSurf_Quadric) -> None: ...
	def Tolerance(self) -> float: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

#classnotwrapped
class GeomInt_WLApprox: ...

# harray1 classes
# harray2 classes
# hsequence classes

geomint_AdjustPeriodic = geomint.AdjustPeriodic
GeomInt_IntSS_BuildPCurves = GeomInt_IntSS.BuildPCurves
GeomInt_IntSS_MakeBSpline = GeomInt_IntSS.MakeBSpline
GeomInt_IntSS_MakeBSpline2d = GeomInt_IntSS.MakeBSpline2d
GeomInt_IntSS_TreatRLine = GeomInt_IntSS.TreatRLine
GeomInt_IntSS_TrimILineOnSurfBoundaries = GeomInt_IntSS.TrimILineOnSurfBoundaries
GeomInt_LineTool_DecompositionOfWLine = GeomInt_LineTool.DecompositionOfWLine
GeomInt_LineTool_FirstParameter = GeomInt_LineTool.FirstParameter
GeomInt_LineTool_LastParameter = GeomInt_LineTool.LastParameter
GeomInt_LineTool_NbVertex = GeomInt_LineTool.NbVertex
GeomInt_LineTool_Vertex = GeomInt_LineTool.Vertex
GeomInt_TheMultiLineToolOfWLApprox_Curvature = GeomInt_TheMultiLineToolOfWLApprox.Curvature
GeomInt_TheMultiLineToolOfWLApprox_Curvature = GeomInt_TheMultiLineToolOfWLApprox.Curvature
GeomInt_TheMultiLineToolOfWLApprox_Curvature = GeomInt_TheMultiLineToolOfWLApprox.Curvature
GeomInt_TheMultiLineToolOfWLApprox_Dump = GeomInt_TheMultiLineToolOfWLApprox.Dump
GeomInt_TheMultiLineToolOfWLApprox_FirstPoint = GeomInt_TheMultiLineToolOfWLApprox.FirstPoint
GeomInt_TheMultiLineToolOfWLApprox_LastPoint = GeomInt_TheMultiLineToolOfWLApprox.LastPoint
GeomInt_TheMultiLineToolOfWLApprox_MakeMLBetween = GeomInt_TheMultiLineToolOfWLApprox.MakeMLBetween
GeomInt_TheMultiLineToolOfWLApprox_MakeMLOneMorePoint = GeomInt_TheMultiLineToolOfWLApprox.MakeMLOneMorePoint
GeomInt_TheMultiLineToolOfWLApprox_NbP2d = GeomInt_TheMultiLineToolOfWLApprox.NbP2d
GeomInt_TheMultiLineToolOfWLApprox_NbP3d = GeomInt_TheMultiLineToolOfWLApprox.NbP3d
GeomInt_TheMultiLineToolOfWLApprox_Tangency = GeomInt_TheMultiLineToolOfWLApprox.Tangency
GeomInt_TheMultiLineToolOfWLApprox_Tangency = GeomInt_TheMultiLineToolOfWLApprox.Tangency
GeomInt_TheMultiLineToolOfWLApprox_Tangency = GeomInt_TheMultiLineToolOfWLApprox.Tangency
GeomInt_TheMultiLineToolOfWLApprox_Value = GeomInt_TheMultiLineToolOfWLApprox.Value
GeomInt_TheMultiLineToolOfWLApprox_Value = GeomInt_TheMultiLineToolOfWLApprox.Value
GeomInt_TheMultiLineToolOfWLApprox_Value = GeomInt_TheMultiLineToolOfWLApprox.Value
GeomInt_TheMultiLineToolOfWLApprox_WhatStatus = GeomInt_TheMultiLineToolOfWLApprox.WhatStatus
