from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Adaptor2d import *
from OCC.Core.GeomAbs import *
from OCC.Core.Geom2d import *
from OCC.Core.Geom import *
from OCC.Core.AppCont import *
from OCC.Core.AppParCurves import *
from OCC.Core.TColgp import *
from OCC.Core.gp import *

#the following typedef cannot be wrapped as is
Approx_SequenceOfHArray1OfReal = NewType('Approx_SequenceOfHArray1OfReal', Any)

class Approx_Array1OfAdHSurface:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> False: ...
    def __setitem__(self, index: int, value: False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[False]:
    def next(self) -> False: ...
    __next__ = next

class Approx_Array1OfGTrsf2d:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> gp_GTrsf2d: ...
    def __setitem__(self, index: int, value: gp_GTrsf2d) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[gp_GTrsf2d]:
    def next(self) -> gp_GTrsf2d: ...
    __next__ = next

class Approx_Status(IntEnum):
	Approx_PointsAdded: int = ...
	Approx_NoPointsAdded: int = ...
	Approx_NoApproximation: int = ...
Approx_PointsAdded = Approx_Status.Approx_PointsAdded
Approx_NoPointsAdded = Approx_Status.Approx_NoPointsAdded
Approx_NoApproximation = Approx_Status.Approx_NoApproximation

class Approx_ParametrizationType(IntEnum):
	Approx_ChordLength: int = ...
	Approx_Centripetal: int = ...
	Approx_IsoParametric: int = ...
Approx_ChordLength = Approx_ParametrizationType.Approx_ChordLength
Approx_Centripetal = Approx_ParametrizationType.Approx_Centripetal
Approx_IsoParametric = Approx_ParametrizationType.Approx_IsoParametric

class Approx_Curve2d:
	def __init__(self, C2D: Adaptor2d_HCurve2d, First: float, Last: float, TolU: float, TolV: float, Continuity: GeomAbs_Shape, MaxDegree: int, MaxSegments: int) -> None: ...
	def Curve(self) -> Geom2d_BSplineCurve: ...
	def HasResult(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def MaxError2dU(self) -> float: ...
	def MaxError2dV(self) -> float: ...

class Approx_Curve3d:
	def __init__(self, Curve: Adaptor3d_HCurve, Tol3d: float, Order: GeomAbs_Shape, MaxSegments: int, MaxDegree: int) -> None: ...
	def Curve(self) -> Geom_BSplineCurve: ...
	def HasResult(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def MaxError(self) -> float: ...

class Approx_CurveOnSurface:
	def __init__(self, C2D: Adaptor2d_HCurve2d, Surf: Adaptor3d_HSurface, First: float, Last: float, Tol: float, Continuity: GeomAbs_Shape, MaxDegree: int, MaxSegments: int, Only3d: Optional[bool], Only2d: Optional[bool]) -> None: ...
	def Curve2d(self) -> Geom2d_BSplineCurve: ...
	def Curve3d(self) -> Geom_BSplineCurve: ...
	def HasResult(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def MaxError2dU(self) -> float: ...
	def MaxError2dV(self) -> float: ...
	def MaxError3d(self) -> float: ...

class Approx_CurvilinearParameter:
	@overload
	def __init__(self, C3D: Adaptor3d_HCurve, Tol: float, Order: GeomAbs_Shape, MaxDegree: int, MaxSegments: int) -> None: ...
	@overload
	def __init__(self, C2D: Adaptor2d_HCurve2d, Surf: Adaptor3d_HSurface, Tol: float, Order: GeomAbs_Shape, MaxDegree: int, MaxSegments: int) -> None: ...
	@overload
	def __init__(self, C2D1: Adaptor2d_HCurve2d, Surf1: Adaptor3d_HSurface, C2D2: Adaptor2d_HCurve2d, Surf2: Adaptor3d_HSurface, Tol: float, Order: GeomAbs_Shape, MaxDegree: int, MaxSegments: int) -> None: ...
	def Curve2d1(self) -> Geom2d_BSplineCurve: ...
	def Curve2d2(self) -> Geom2d_BSplineCurve: ...
	def Curve3d(self) -> Geom_BSplineCurve: ...
	def HasResult(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def MaxError2d1(self) -> float: ...
	def MaxError2d2(self) -> float: ...
	def MaxError3d(self) -> float: ...

class Approx_CurvlinFunc(Standard_Transient):
	@overload
	def __init__(self, C: Adaptor3d_HCurve, Tol: float) -> None: ...
	@overload
	def __init__(self, C2D: Adaptor2d_HCurve2d, S: Adaptor3d_HSurface, Tol: float) -> None: ...
	@overload
	def __init__(self, C2D1: Adaptor2d_HCurve2d, C2D2: Adaptor2d_HCurve2d, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, Tol: float) -> None: ...
	def EvalCase1(self, S: float, Order: int, Result: TColStd_Array1OfReal) -> bool: ...
	def EvalCase2(self, S: float, Order: int, Result: TColStd_Array1OfReal) -> bool: ...
	def EvalCase3(self, S: float, Order: int, Result: TColStd_Array1OfReal) -> bool: ...
	def FirstParameter(self) -> float: ...
	def GetLength(self) -> float: ...
	def GetSParameter(self, U: float) -> float: ...
	def GetUParameter(self, C: Adaptor3d_Curve, S: float, NumberOfCurve: int) -> float: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def LastParameter(self) -> float: ...
	@overload
	def Length(self) -> None: ...
	@overload
	def Length(self, C: Adaptor3d_Curve, FirstU: float, LasrU: float) -> float: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def SetTol(self, Tol: float) -> None: ...
	def Trim(self, First: float, Last: float, Tol: float) -> None: ...

class Approx_FitAndDivide:
	@overload
	def __init__(self, Line: AppCont_Function, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], cutting: Optional[bool], FirstC: Optional[AppParCurves_Constraint], LastC: Optional[AppParCurves_Constraint]) -> None: ...
	@overload
	def __init__(self, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], cutting: Optional[bool], FirstC: Optional[AppParCurves_Constraint], LastC: Optional[AppParCurves_Constraint]) -> None: ...
	def Error(self, Index: int) -> Tuple[float, float]: ...
	def IsAllApproximated(self) -> bool: ...
	def IsToleranceReached(self) -> bool: ...
	def NbMultiCurves(self) -> int: ...
	def Parameters(self, Index: int) -> Tuple[float, float]: ...
	def Perform(self, Line: AppCont_Function) -> None: ...
	def SetConstraints(self, FirstC: AppParCurves_Constraint, LastC: AppParCurves_Constraint) -> None: ...
	def SetDegrees(self, degreemin: int, degreemax: int) -> None: ...
	def SetInvOrder(self, theInvOrder: bool) -> None: ...
	def SetMaxSegments(self, theMaxSegments: int) -> None: ...
	def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None: ...
	def Value(self, Index: Optional[int]) -> AppParCurves_MultiCurve: ...

class Approx_FitAndDivide2d:
	@overload
	def __init__(self, Line: AppCont_Function, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], cutting: Optional[bool], FirstC: Optional[AppParCurves_Constraint], LastC: Optional[AppParCurves_Constraint]) -> None: ...
	@overload
	def __init__(self, degreemin: Optional[int], degreemax: Optional[int], Tolerance3d: Optional[float], Tolerance2d: Optional[float], cutting: Optional[bool], FirstC: Optional[AppParCurves_Constraint], LastC: Optional[AppParCurves_Constraint]) -> None: ...
	def Error(self, Index: int) -> Tuple[float, float]: ...
	def IsAllApproximated(self) -> bool: ...
	def IsToleranceReached(self) -> bool: ...
	def NbMultiCurves(self) -> int: ...
	def Parameters(self, Index: int) -> Tuple[float, float]: ...
	def Perform(self, Line: AppCont_Function) -> None: ...
	def SetConstraints(self, FirstC: AppParCurves_Constraint, LastC: AppParCurves_Constraint) -> None: ...
	def SetDegrees(self, degreemin: int, degreemax: int) -> None: ...
	def SetInvOrder(self, theInvOrder: bool) -> None: ...
	def SetMaxSegments(self, theMaxSegments: int) -> None: ...
	def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None: ...
	def Value(self, Index: Optional[int]) -> AppParCurves_MultiCurve: ...

class Approx_MCurvesToBSpCurve:
	def __init__(self) -> None: ...
	def Append(self, MC: AppParCurves_MultiCurve) -> None: ...
	def ChangeValue(self) -> AppParCurves_MultiBSpCurve: ...
	@overload
	def Perform(self) -> None: ...
	@overload
	def Perform(self, TheSeq: AppParCurves_SequenceOfMultiCurve) -> None: ...
	def Reset(self) -> None: ...
	def Value(self) -> AppParCurves_MultiBSpCurve: ...

class Approx_SameParameter:
	@overload
	def __init__(self, C3D: Geom_Curve, C2D: Geom2d_Curve, S: Geom_Surface, Tol: float) -> None: ...
	@overload
	def __init__(self, C3D: Adaptor3d_HCurve, C2D: Geom2d_Curve, S: Adaptor3d_HSurface, Tol: float) -> None: ...
	@overload
	def __init__(self, C3D: Adaptor3d_HCurve, C2D: Adaptor2d_HCurve2d, S: Adaptor3d_HSurface, Tol: float) -> None: ...
	def Curve2d(self) -> Geom2d_BSplineCurve: ...
	def IsDone(self) -> bool: ...
	def IsSameParameter(self) -> bool: ...
	def TolReached(self) -> float: ...

class Approx_SweepApproximation:
	def __init__(self, Func: Approx_SweepFunction) -> None: ...
	def Average2dError(self, Index: int) -> float: ...
	def AverageErrorOnSurf(self) -> float: ...
	def Curve2d(self, Index: int, TPoles: TColgp_Array1OfPnt2d, TKnots: TColStd_Array1OfReal, TMults: TColStd_Array1OfInteger) -> None: ...
	def Curve2dPoles(self, Index: int) -> TColgp_Array1OfPnt2d: ...
	def Curves2dDegree(self) -> int: ...
	def Curves2dKnots(self) -> TColStd_Array1OfReal: ...
	def Curves2dMults(self) -> TColStd_Array1OfInteger: ...
	def Curves2dShape(self) -> Tuple[int, int, int]: ...
	def Eval(self, Parameter: float, DerivativeRequest: int, First: float, Last: float) -> Tuple[int, float]: ...
	def IsDone(self) -> bool: ...
	def Max2dError(self, Index: int) -> float: ...
	def MaxErrorOnSurf(self) -> float: ...
	def NbCurves2d(self) -> int: ...
	def Perform(self, First: float, Last: float, Tol3d: float, BoundTol: float, Tol2d: float, TolAngular: float, Continuity: Optional[GeomAbs_Shape], Degmax: Optional[int], Segmax: Optional[int]) -> None: ...
	def SurfPoles(self) -> TColgp_Array2OfPnt: ...
	def SurfShape(self) -> Tuple[int, int, int, int, int, int]: ...
	def SurfUKnots(self) -> TColStd_Array1OfReal: ...
	def SurfUMults(self) -> TColStd_Array1OfInteger: ...
	def SurfVKnots(self) -> TColStd_Array1OfReal: ...
	def SurfVMults(self) -> TColStd_Array1OfInteger: ...
	def SurfWeights(self) -> TColStd_Array2OfReal: ...
	def Surface(self, TPoles: TColgp_Array2OfPnt, TWeights: TColStd_Array2OfReal, TUKnots: TColStd_Array1OfReal, TVKnots: TColStd_Array1OfReal, TUMults: TColStd_Array1OfInteger, TVMults: TColStd_Array1OfInteger) -> None: ...
	def TolCurveOnSurf(self, Index: int) -> float: ...
	def UDegree(self) -> int: ...
	def VDegree(self) -> int: ...

class Approx_SweepFunction(Standard_Transient):
	def BarycentreOfSurf(self) -> gp_Pnt: ...
	def D0(self, Param: float, First: float, Last: float, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> bool: ...
	def D1(self, Param: float, First: float, Last: float, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	def D2(self, Param: float, First: float, Last: float, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: TColStd_Array1OfReal) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def MaximalSection(self) -> float: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def Nb2dCurves(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def Resolution(self, Index: int, Tol: float) -> Tuple[float, float]: ...
	def SectionShape(self) -> Tuple[int, int, int]: ...
	def SetInterval(self, First: float, Last: float) -> None: ...
	def SetTolerance(self, Tol3d: float, Tol2d: float) -> None: ...

# harray1 classes
class Approx_HArray1OfGTrsf2d(Approx_Array1OfGTrsf2d, Standard_Transient): ...

class Approx_HArray1OfAdHSurface(Approx_Array1OfAdHSurface, Standard_Transient): ...

# harray2 classes
# harray2 classes

