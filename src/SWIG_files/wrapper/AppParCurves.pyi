from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.math import *
from OCC.Core.TColgp import *
from OCC.Core.gp import *
from OCC.Core.TColStd import *

#the following typedef cannot be wrapped as is
AppParCurves_SequenceOfMultiBSpCurve = NewType('AppParCurves_SequenceOfMultiBSpCurve', Any)
#the following typedef cannot be wrapped as is
AppParCurves_SequenceOfMultiCurve = NewType('AppParCurves_SequenceOfMultiCurve', Any)

class AppParCurves_Array1OfConstraintCouple:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> AppParCurves_ConstraintCouple: ...
    def __setitem__(self, index: int, value: AppParCurves_ConstraintCouple) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[AppParCurves_ConstraintCouple]:
    def next(self) -> AppParCurves_ConstraintCouple: ...
    __next__ = next

class AppParCurves_Array1OfMultiBSpCurve:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> AppParCurves_MultiBSpCurve: ...
    def __setitem__(self, index: int, value: AppParCurves_MultiBSpCurve) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[AppParCurves_MultiBSpCurve]:
    def next(self) -> AppParCurves_MultiBSpCurve: ...
    __next__ = next

class AppParCurves_Array1OfMultiCurve:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> AppParCurves_MultiCurve: ...
    def __setitem__(self, index: int, value: AppParCurves_MultiCurve) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[AppParCurves_MultiCurve]:
    def next(self) -> AppParCurves_MultiCurve: ...
    __next__ = next

class AppParCurves_Array1OfMultiPoint:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> AppParCurves_MultiPoint: ...
    def __setitem__(self, index: int, value: AppParCurves_MultiPoint) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[AppParCurves_MultiPoint]:
    def next(self) -> AppParCurves_MultiPoint: ...
    __next__ = next

class AppParCurves_Constraint(IntEnum):
	AppParCurves_NoConstraint: int = ...
	AppParCurves_PassPoint: int = ...
	AppParCurves_TangencyPoint: int = ...
	AppParCurves_CurvaturePoint: int = ...
AppParCurves_NoConstraint = AppParCurves_Constraint.AppParCurves_NoConstraint
AppParCurves_PassPoint = AppParCurves_Constraint.AppParCurves_PassPoint
AppParCurves_TangencyPoint = AppParCurves_Constraint.AppParCurves_TangencyPoint
AppParCurves_CurvaturePoint = AppParCurves_Constraint.AppParCurves_CurvaturePoint

class AppParCurves:
	@staticmethod
	def Bernstein(self, NbPoles: int, U: math_Vector, A: math_Matrix, DA: math_Matrix) -> None: ...
	@staticmethod
	def BernsteinMatrix(self, NbPoles: int, U: math_Vector, A: math_Matrix) -> None: ...
	@staticmethod
	def SecondDerivativeBernstein(self, U: float, DDA: math_Vector) -> None: ...
	@staticmethod
	def SplineFunction(self, NbPoles: int, Degree: int, Parameters: math_Vector, FlatKnots: math_Vector, A: math_Matrix, DA: math_Matrix, Index: math_IntegerVector) -> None: ...

class AppParCurves_ConstraintCouple:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, TheIndex: int, Cons: AppParCurves_Constraint) -> None: ...
	def Constraint(self) -> AppParCurves_Constraint: ...
	def Index(self) -> int: ...
	def SetConstraint(self, Cons: AppParCurves_Constraint) -> None: ...
	def SetIndex(self, TheIndex: int) -> None: ...

class AppParCurves_MultiCurve:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, NbPol: int) -> None: ...
	@overload
	def __init__(self, tabMU: AppParCurves_Array1OfMultiPoint) -> None: ...
	@overload
	def Curve(self, CuIndex: int, TabPnt: TColgp_Array1OfPnt) -> None: ...
	@overload
	def Curve(self, CuIndex: int, TabPnt: TColgp_Array1OfPnt2d) -> None: ...
	@overload
	def D1(self, CuIndex: int, U: float, Pt: gp_Pnt, V1: gp_Vec) -> None: ...
	@overload
	def D1(self, CuIndex: int, U: float, Pt: gp_Pnt2d, V1: gp_Vec2d) -> None: ...
	@overload
	def D2(self, CuIndex: int, U: float, Pt: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	@overload
	def D2(self, CuIndex: int, U: float, Pt: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def Degree(self) -> int: ...
	def Dimension(self, CuIndex: int) -> int: ...
	def NbCurves(self) -> int: ...
	def NbPoles(self) -> int: ...
	def Pole(self, CuIndex: int, Nieme: int) -> gp_Pnt: ...
	def Pole2d(self, CuIndex: int, Nieme: int) -> gp_Pnt2d: ...
	def SetNbPoles(self, nbPoles: int) -> None: ...
	def SetValue(self, Index: int, MPoint: AppParCurves_MultiPoint) -> None: ...
	def Transform(self, CuIndex: int, x: float, dx: float, y: float, dy: float, z: float, dz: float) -> None: ...
	def Transform2d(self, CuIndex: int, x: float, dx: float, y: float, dy: float) -> None: ...
	@overload
	def Value(self, Index: int) -> AppParCurves_MultiPoint: ...
	@overload
	def Value(self, CuIndex: int, U: float, Pt: gp_Pnt) -> None: ...
	@overload
	def Value(self, CuIndex: int, U: float, Pt: gp_Pnt2d) -> None: ...

class AppParCurves_MultiPoint:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, NbPoints: int, NbPoints2d: int) -> None: ...
	@overload
	def __init__(self, tabP: TColgp_Array1OfPnt) -> None: ...
	@overload
	def __init__(self, tabP2d: TColgp_Array1OfPnt2d) -> None: ...
	@overload
	def __init__(self, tabP: TColgp_Array1OfPnt, tabP2d: TColgp_Array1OfPnt2d) -> None: ...
	def Dimension(self, Index: int) -> int: ...
	def NbPoints(self) -> int: ...
	def NbPoints2d(self) -> int: ...
	def Point(self, Index: int) -> gp_Pnt: ...
	def Point2d(self, Index: int) -> gp_Pnt2d: ...
	def SetPoint(self, Index: int, Point: gp_Pnt) -> None: ...
	def SetPoint2d(self, Index: int, Point: gp_Pnt2d) -> None: ...
	def Transform(self, CuIndex: int, x: float, dx: float, y: float, dy: float, z: float, dz: float) -> None: ...
	def Transform2d(self, CuIndex: int, x: float, dx: float, y: float, dy: float) -> None: ...

class AppParCurves_MultiBSpCurve(AppParCurves_MultiCurve):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, NbPol: int) -> None: ...
	@overload
	def __init__(self, tabMU: AppParCurves_Array1OfMultiPoint, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger) -> None: ...
	@overload
	def __init__(self, SC: AppParCurves_MultiCurve, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger) -> None: ...
	@overload
	def D1(self, CuIndex: int, U: float, Pt: gp_Pnt, V1: gp_Vec) -> None: ...
	@overload
	def D1(self, CuIndex: int, U: float, Pt: gp_Pnt2d, V1: gp_Vec2d) -> None: ...
	@overload
	def D2(self, CuIndex: int, U: float, Pt: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	@overload
	def D2(self, CuIndex: int, U: float, Pt: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
	def Degree(self) -> int: ...
	def Knots(self) -> TColStd_Array1OfReal: ...
	def Multiplicities(self) -> TColStd_Array1OfInteger: ...
	def SetKnots(self, theKnots: TColStd_Array1OfReal) -> None: ...
	def SetMultiplicities(self, theMults: TColStd_Array1OfInteger) -> None: ...
	@overload
	def Value(self, CuIndex: int, U: float, Pt: gp_Pnt) -> None: ...
	@overload
	def Value(self, CuIndex: int, U: float, Pt: gp_Pnt2d) -> None: ...

# harray1 classes

class AppParCurves_HArray1OfMultiCurve(AppParCurves_Array1OfMultiCurve, Standard_Transient):
    def AppParCurves_HArray1OfMultiCurve(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> AppParCurves_Array1OfMultiCurve: ...


class AppParCurves_HArray1OfConstraintCouple(AppParCurves_Array1OfConstraintCouple, Standard_Transient):
    def AppParCurves_HArray1OfConstraintCouple(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> AppParCurves_Array1OfConstraintCouple: ...


class AppParCurves_HArray1OfMultiPoint(AppParCurves_Array1OfMultiPoint, Standard_Transient):
    def AppParCurves_HArray1OfMultiPoint(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> AppParCurves_Array1OfMultiPoint: ...


class AppParCurves_HArray1OfMultiBSpCurve(AppParCurves_Array1OfMultiBSpCurve, Standard_Transient):
    def AppParCurves_HArray1OfMultiBSpCurve(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> AppParCurves_Array1OfMultiBSpCurve: ...

# harray2 classes
# hsequence classes

appparcurves_Bernstein = appparcurves.Bernstein
appparcurves_BernsteinMatrix = appparcurves.BernsteinMatrix
appparcurves_SecondDerivativeBernstein = appparcurves.SecondDerivativeBernstein
appparcurves_SplineFunction = appparcurves.SplineFunction
