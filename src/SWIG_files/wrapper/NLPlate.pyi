from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.Plate import *
from OCC.Core.Geom import *

#the following typedef cannot be wrapped as is
NLPlate_ListIteratorOfStackOfPlate = NewType('NLPlate_ListIteratorOfStackOfPlate', Any)
#the following typedef cannot be wrapped as is
NLPlate_SequenceOfHGPPConstraint = NewType('NLPlate_SequenceOfHGPPConstraint', Any)
#the following typedef cannot be wrapped as is
NLPlate_StackOfPlate = NewType('NLPlate_StackOfPlate', Any)

class NLPlate_HGPPConstraint(Standard_Transient):
	def ActiveOrder(self) -> int: ...
	def G0Criterion(self) -> float: ...
	def G0Target(self) -> gp_XYZ: ...
	def G1Criterion(self) -> float: ...
	def G1Target(self) -> Plate_D1: ...
	def G2Criterion(self) -> float: ...
	def G2Target(self) -> Plate_D2: ...
	def G3Criterion(self) -> float: ...
	def G3Target(self) -> Plate_D3: ...
	def IncrementalLoadAllowed(self) -> bool: ...
	def IsG0(self) -> bool: ...
	def Orientation(self) -> int: ...
	def SetActiveOrder(self, ActiveOrder: int) -> None: ...
	def SetG0Criterion(self, TolDist: float) -> None: ...
	def SetG1Criterion(self, TolAng: float) -> None: ...
	def SetG2Criterion(self, TolCurv: float) -> None: ...
	def SetG3Criterion(self, TolG3: float) -> None: ...
	def SetIncrementalLoadAllowed(self, ILA: bool) -> None: ...
	def SetOrientation(self, Orient: Optional[int]) -> None: ...
	def SetUV(self, UV: gp_XY) -> None: ...
	def SetUVFreeSliding(self, UVFree: bool) -> None: ...
	def UV(self) -> gp_XY: ...
	def UVFreeSliding(self) -> bool: ...

class NLPlate_NLPlate:
	def __init__(self, InitialSurface: Geom_Surface) -> None: ...
	def ConstraintsSliding(self, NbIterations: Optional[int]) -> None: ...
	def Continuity(self) -> int: ...
	def Evaluate(self, point2d: gp_XY) -> gp_XYZ: ...
	def EvaluateDerivative(self, point2d: gp_XY, iu: int, iv: int) -> gp_XYZ: ...
	def IncrementalSolve(self, ord: Optional[int], InitialConsraintOrder: Optional[int], NbIncrements: Optional[int], UVSliding: Optional[bool]) -> None: ...
	def Init(self) -> None: ...
	def IsDone(self) -> bool: ...
	def Load(self, GConst: NLPlate_HGPPConstraint) -> None: ...
	def MaxActiveConstraintOrder(self) -> int: ...
	def Solve(self, ord: Optional[int], InitialConsraintOrder: Optional[int]) -> None: ...
	def Solve2(self, ord: Optional[int], InitialConsraintOrder: Optional[int]) -> None: ...
	def destroy(self) -> None: ...

class NLPlate_HPG0Constraint(NLPlate_HGPPConstraint):
	def __init__(self, UV: gp_XY, Value: gp_XYZ) -> None: ...
	def ActiveOrder(self) -> int: ...
	def G0Target(self) -> gp_XYZ: ...
	def IncrementalLoadAllowed(self) -> bool: ...
	def IsG0(self) -> bool: ...
	def SetIncrementalLoadAllowed(self, ILA: bool) -> None: ...
	def SetUVFreeSliding(self, UVFree: bool) -> None: ...
	def UVFreeSliding(self) -> bool: ...

class NLPlate_HPG1Constraint(NLPlate_HGPPConstraint):
	def __init__(self, UV: gp_XY, D1T: Plate_D1) -> None: ...
	def ActiveOrder(self) -> int: ...
	def G1Target(self) -> Plate_D1: ...
	def IncrementalLoadAllowed(self) -> bool: ...
	def IsG0(self) -> bool: ...
	def Orientation(self) -> int: ...
	def SetIncrementalLoadAllowed(self, ILA: bool) -> None: ...
	def SetOrientation(self, Orient: Optional[int]) -> None: ...

class NLPlate_HPG0G1Constraint(NLPlate_HPG0Constraint):
	def __init__(self, UV: gp_XY, Value: gp_XYZ, D1T: Plate_D1) -> None: ...
	def ActiveOrder(self) -> int: ...
	def G1Target(self) -> Plate_D1: ...
	def Orientation(self) -> int: ...
	def SetOrientation(self, Orient: Optional[int]) -> None: ...

class NLPlate_HPG2Constraint(NLPlate_HPG1Constraint):
	def __init__(self, UV: gp_XY, D1T: Plate_D1, D2T: Plate_D2) -> None: ...
	def ActiveOrder(self) -> int: ...
	def G2Target(self) -> Plate_D2: ...

class NLPlate_HPG0G2Constraint(NLPlate_HPG0G1Constraint):
	def __init__(self, UV: gp_XY, Value: gp_XYZ, D1T: Plate_D1, D2T: Plate_D2) -> None: ...
	def ActiveOrder(self) -> int: ...
	def G2Target(self) -> Plate_D2: ...

class NLPlate_HPG3Constraint(NLPlate_HPG2Constraint):
	def __init__(self, UV: gp_XY, D1T: Plate_D1, D2T: Plate_D2, D3T: Plate_D3) -> None: ...
	def ActiveOrder(self) -> int: ...
	def G3Target(self) -> Plate_D3: ...

class NLPlate_HPG0G3Constraint(NLPlate_HPG0G2Constraint):
	def __init__(self, UV: gp_XY, Value: gp_XYZ, D1T: Plate_D1, D2T: Plate_D2, D3T: Plate_D3) -> None: ...
	def ActiveOrder(self) -> int: ...
	def G3Target(self) -> Plate_D3: ...
