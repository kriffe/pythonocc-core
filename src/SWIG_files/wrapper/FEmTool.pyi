from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.math import *
from OCC.Core.PLib import *
from OCC.Core.GeomAbs import *

#the following typedef cannot be wrapped as is
FEmTool_AssemblyTable = NewType('FEmTool_AssemblyTable', Any)
#the following typedef cannot be wrapped as is
FEmTool_ListIteratorOfListOfVectors = NewType('FEmTool_ListIteratorOfListOfVectors', Any)
#the following typedef cannot be wrapped as is
FEmTool_ListOfVectors = NewType('FEmTool_ListOfVectors', Any)
#the following typedef cannot be wrapped as is
FEmTool_SeqOfLinConstr = NewType('FEmTool_SeqOfLinConstr', Any)

class FEmTool_Assembly:
	def __init__(self, Dependence: TColStd_Array2OfInteger, Table: FEmTool_HAssemblyTable) -> None: ...
	def AddConstraint(self, IndexofConstraint: int, Element: int, Dimension: int, LinearForm: math_Vector, Value: float) -> None: ...
	def AddMatrix(self, Element: int, Dimension1: int, Dimension2: int, Mat: math_Matrix) -> None: ...
	def AddVector(self, Element: int, Dimension: int, Vec: math_Vector) -> None: ...
	def GetAssemblyTable(self, AssTable: FEmTool_HAssemblyTable) -> None: ...
	def NbGlobVar(self) -> int: ...
	def NullifyConstraint(self) -> None: ...
	def NullifyMatrix(self) -> None: ...
	def NullifyVector(self) -> None: ...
	def ResetConstraint(self) -> None: ...
	def Solution(self, Solution: math_Vector) -> None: ...
	def Solve(self) -> bool: ...

class FEmTool_Curve(Standard_Transient):
	def __init__(self, Dimension: int, NbElements: int, TheBase: PLib_Base, Tolerance: float) -> None: ...
	def Base(self) -> PLib_Base: ...
	def D0(self, U: float, Pnt: TColStd_Array1OfReal) -> None: ...
	def D1(self, U: float, Vec: TColStd_Array1OfReal) -> None: ...
	def D2(self, U: float, Vec: TColStd_Array1OfReal) -> None: ...
	def Degree(self, IndexOfElement: int) -> int: ...
	def Dimension(self) -> int: ...
	def GetElement(self, IndexOfElement: int, Coeffs: TColStd_Array2OfReal) -> None: ...
	def GetPolynom(self, Coeffs: TColStd_Array1OfReal) -> None: ...
	def Knots(self) -> TColStd_Array1OfReal: ...
	def Length(self, FirstU: float, LastU: float) -> float: ...
	def NbElements(self) -> int: ...
	def ReduceDegree(self, IndexOfElement: int, Tol: float) -> Tuple[int, float]: ...
	def SetDegree(self, IndexOfElement: int, Degree: int) -> None: ...
	def SetElement(self, IndexOfElement: int, Coeffs: TColStd_Array2OfReal) -> None: ...

class FEmTool_ElementaryCriterion(Standard_Transient):
	def DependenceTable(self) -> TColStd_HArray2OfInteger: ...
	def Gradient(self, Dim: int, G: math_Vector) -> None: ...
	def Hessian(self, Dim1: int, Dim2: int, H: math_Matrix) -> None: ...
	@overload
	def Set(self, Coeff: TColStd_HArray2OfReal) -> None: ...
	@overload
	def Set(self, FirstKnot: float, LastKnot: float) -> None: ...
	def Value(self) -> float: ...

class FEmTool_ElementsOfRefMatrix(math_FunctionSet):
	def __init__(self, TheBase: PLib_Base, DerOrder: int) -> None: ...
	def NbEquations(self) -> int: ...
	def NbVariables(self) -> int: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...

class FEmTool_SparseMatrix(Standard_Transient):
	def ChangeValue(self, I: int, J: int) -> float: ...
	def ColNumber(self) -> int: ...
	def Decompose(self) -> bool: ...
	def Init(self, Value: float) -> None: ...
	def Multiplied(self, X: math_Vector, MX: math_Vector) -> None: ...
	def Prepare(self) -> bool: ...
	def RowNumber(self) -> int: ...
	@overload
	def Solve(self, B: math_Vector, X: math_Vector) -> None: ...
	@overload
	def Solve(self, B: math_Vector, Init: math_Vector, X: math_Vector, Residual: math_Vector, Tolerance: Optional[float], NbIterations: Optional[int]) -> None: ...

class FEmTool_LinearFlexion(FEmTool_ElementaryCriterion):
	def __init__(self, WorkDegree: int, ConstraintOrder: GeomAbs_Shape) -> None: ...
	def DependenceTable(self) -> TColStd_HArray2OfInteger: ...
	def Gradient(self, Dimension: int, G: math_Vector) -> None: ...
	def Hessian(self, Dimension1: int, Dimension2: int, H: math_Matrix) -> None: ...
	def Value(self) -> float: ...

class FEmTool_LinearJerk(FEmTool_ElementaryCriterion):
	def __init__(self, WorkDegree: int, ConstraintOrder: GeomAbs_Shape) -> None: ...
	def DependenceTable(self) -> TColStd_HArray2OfInteger: ...
	def Gradient(self, Dimension: int, G: math_Vector) -> None: ...
	def Hessian(self, Dimension1: int, Dimension2: int, H: math_Matrix) -> None: ...
	def Value(self) -> float: ...

class FEmTool_LinearTension(FEmTool_ElementaryCriterion):
	def __init__(self, WorkDegree: int, ConstraintOrder: GeomAbs_Shape) -> None: ...
	def DependenceTable(self) -> TColStd_HArray2OfInteger: ...
	def Gradient(self, Dimension: int, G: math_Vector) -> None: ...
	def Hessian(self, Dimension1: int, Dimension2: int, H: math_Matrix) -> None: ...
	def Value(self) -> float: ...

class FEmTool_ProfileMatrix(FEmTool_SparseMatrix):
	def __init__(self, FirstIndexes: TColStd_Array1OfInteger) -> None: ...
	def GetChangeValue(self, I: int, J: int) -> float: ...
	def SetChangeValue(self, I: int, J: int, value: float) -> None: ...
	def ColNumber(self) -> int: ...
	def Decompose(self) -> bool: ...
	def Init(self, Value: float) -> None: ...
	def IsInProfile(self, i: int, j: int) -> bool: ...
	def Multiplied(self, X: math_Vector, MX: math_Vector) -> None: ...
	def OutM(self) -> None: ...
	def OutS(self) -> None: ...
	def Prepare(self) -> bool: ...
	def RowNumber(self) -> int: ...
	@overload
	def Solve(self, B: math_Vector, X: math_Vector) -> None: ...
	@overload
	def Solve(self, B: math_Vector, Init: math_Vector, X: math_Vector, Residual: math_Vector, Tolerance: Optional[float], NbIterations: Optional[int]) -> None: ...

# harray1 classes
# harray2 classes

class FEmTool_HAssemblyTable(FEmTool_AssemblyTable, Standard_Transient):
    def FEmTool_HAssemblyTable(self, theRowLow: int, theRowUpp: int, theColLow: int, theColUpp: int) -> None: ...
    def FEmTool_HAssemblyTable(self, theOther: FEmTool_AssemblyTable) -> None: ...
    def Array2(self) -> FEmTool_AssemblyTable: ...

# hsequence classes

