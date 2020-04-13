from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *
from OCC.Core.TColStd import *


class GProp_EquaType(IntEnum):
	GProp_Plane: int = ...
	GProp_Line: int = ...
	GProp_Point: int = ...
	GProp_Space: int = ...
	GProp_None: int = ...
GProp_Plane = GProp_EquaType.GProp_Plane
GProp_Line = GProp_EquaType.GProp_Line
GProp_Point = GProp_EquaType.GProp_Point
GProp_Space = GProp_EquaType.GProp_Space
GProp_None = GProp_EquaType.GProp_None

class GProp_ValueType(IntEnum):
	GProp_Mass: int = ...
	GProp_CenterMassX: int = ...
	GProp_CenterMassY: int = ...
	GProp_CenterMassZ: int = ...
	GProp_InertiaXX: int = ...
	GProp_InertiaYY: int = ...
	GProp_InertiaZZ: int = ...
	GProp_InertiaXY: int = ...
	GProp_InertiaXZ: int = ...
	GProp_InertiaYZ: int = ...
	GProp_Unknown: int = ...
GProp_Mass = GProp_ValueType.GProp_Mass
GProp_CenterMassX = GProp_ValueType.GProp_CenterMassX
GProp_CenterMassY = GProp_ValueType.GProp_CenterMassY
GProp_CenterMassZ = GProp_ValueType.GProp_CenterMassZ
GProp_InertiaXX = GProp_ValueType.GProp_InertiaXX
GProp_InertiaYY = GProp_ValueType.GProp_InertiaYY
GProp_InertiaZZ = GProp_ValueType.GProp_InertiaZZ
GProp_InertiaXY = GProp_ValueType.GProp_InertiaXY
GProp_InertiaXZ = GProp_ValueType.GProp_InertiaXZ
GProp_InertiaYZ = GProp_ValueType.GProp_InertiaYZ
GProp_Unknown = GProp_ValueType.GProp_Unknown

class gprop:
	@staticmethod
	def HOperator(G: gp_Pnt, Q: gp_Pnt, Mass: float, Operator: gp_Mat) -> None: ...

class GProp_GProps:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, SystemLocation: gp_Pnt) -> None: ...
	def Add(self, Item: GProp_GProps, Density: Optional[float]) -> None: ...
	def CentreOfMass(self) -> gp_Pnt: ...
	def Mass(self) -> float: ...
	def MatrixOfInertia(self) -> gp_Mat: ...
	def MomentOfInertia(self, A: gp_Ax1) -> float: ...
	def PrincipalProperties(self) -> GProp_PrincipalProps: ...
	def RadiusOfGyration(self, A: gp_Ax1) -> float: ...
	def StaticMoments(self) -> Tuple[float, float, float]: ...

class GProp_PEquation:
	def __init__(self, Pnts: TColgp_Array1OfPnt, Tol: float) -> None: ...
	def Box(self, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	def IsLinear(self) -> bool: ...
	def IsPlanar(self) -> bool: ...
	def IsPoint(self) -> bool: ...
	def IsSpace(self) -> bool: ...
	def Line(self) -> gp_Lin: ...
	def Plane(self) -> gp_Pln: ...
	def Point(self) -> gp_Pnt: ...

class GProp_PrincipalProps:
	def __init__(self) -> None: ...
	def FirstAxisOfInertia(self) -> gp_Vec: ...
	@overload
	def HasSymmetryAxis(self) -> bool: ...
	@overload
	def HasSymmetryAxis(self, aTol: float) -> bool: ...
	@overload
	def HasSymmetryPoint(self) -> bool: ...
	@overload
	def HasSymmetryPoint(self, aTol: float) -> bool: ...
	def Moments(self) -> Tuple[float, float, float]: ...
	def RadiusOfGyration(self) -> Tuple[float, float, float]: ...
	def SecondAxisOfInertia(self) -> gp_Vec: ...
	def ThirdAxisOfInertia(self) -> gp_Vec: ...

class GProp_CelGProps(GProp_GProps):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, C: gp_Circ, CLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, C: gp_Circ, U1: float, U2: float, CLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, C: gp_Lin, U1: float, U2: float, CLocation: gp_Pnt) -> None: ...
	@overload
	def Perform(self, C: gp_Circ, U1: float, U2: float) -> None: ...
	@overload
	def Perform(self, C: gp_Lin, U1: float, U2: float) -> None: ...
	def SetLocation(self, CLocation: gp_Pnt) -> None: ...

class GProp_PGProps(GProp_GProps):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Pnts: TColgp_Array1OfPnt) -> None: ...
	@overload
	def __init__(self, Pnts: TColgp_Array2OfPnt) -> None: ...
	@overload
	def __init__(self, Pnts: TColgp_Array1OfPnt, Density: TColStd_Array1OfReal) -> None: ...
	@overload
	def __init__(self, Pnts: TColgp_Array2OfPnt, Density: TColStd_Array2OfReal) -> None: ...
	@overload
	def AddPoint(self, P: gp_Pnt) -> None: ...
	@overload
	def AddPoint(self, P: gp_Pnt, Density: float) -> None: ...
	@overload
	@staticmethod
	def Barycentre(Pnts: TColgp_Array1OfPnt) -> gp_Pnt: ...
	@overload
	@staticmethod
	def Barycentre(Pnts: TColgp_Array2OfPnt) -> gp_Pnt: ...
	@overload
	@staticmethod
	def Barycentre(Pnts: TColgp_Array1OfPnt, Density: TColStd_Array1OfReal, G: gp_Pnt) -> float: ...
	@overload
	@staticmethod
	def Barycentre(Pnts: TColgp_Array2OfPnt, Density: TColStd_Array2OfReal, G: gp_Pnt) -> float: ...

class GProp_SelGProps(GProp_GProps):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: gp_Cylinder, Alpha1: float, Alpha2: float, Z1: float, Z2: float, SLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: gp_Cone, Alpha1: float, Alpha2: float, Z1: float, Z2: float, SLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: gp_Sphere, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float, SLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: gp_Torus, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float, SLocation: gp_Pnt) -> None: ...
	@overload
	def Perform(self, S: gp_Cylinder, Alpha1: float, Alpha2: float, Z1: float, Z2: float) -> None: ...
	@overload
	def Perform(self, S: gp_Cone, Alpha1: float, Alpha2: float, Z1: float, Z2: float) -> None: ...
	@overload
	def Perform(self, S: gp_Sphere, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float) -> None: ...
	@overload
	def Perform(self, S: gp_Torus, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float) -> None: ...
	def SetLocation(self, SLocation: gp_Pnt) -> None: ...

class GProp_VelGProps(GProp_GProps):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: gp_Cylinder, Alpha1: float, Alpha2: float, Z1: float, Z2: float, VLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: gp_Cone, Alpha1: float, Alpha2: float, Z1: float, Z2: float, VLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: gp_Sphere, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float, VLocation: gp_Pnt) -> None: ...
	@overload
	def __init__(self, S: gp_Torus, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float, VLocation: gp_Pnt) -> None: ...
	@overload
	def Perform(self, S: gp_Cylinder, Alpha1: float, Alpha2: float, Z1: float, Z2: float) -> None: ...
	@overload
	def Perform(self, S: gp_Cone, Alpha1: float, Alpha2: float, Z1: float, Z2: float) -> None: ...
	@overload
	def Perform(self, S: gp_Sphere, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float) -> None: ...
	@overload
	def Perform(self, S: gp_Torus, Teta1: float, Teta2: float, Alpha1: float, Alpha2: float) -> None: ...
	def SetLocation(self, VLocation: gp_Pnt) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

gprop_HOperator = gprop.HOperator
GProp_PGProps_Barycentre = GProp_PGProps.Barycentre
GProp_PGProps_Barycentre = GProp_PGProps.Barycentre
GProp_PGProps_Barycentre = GProp_PGProps.Barycentre
GProp_PGProps_Barycentre = GProp_PGProps.Barycentre
