from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Adaptor3d import *
from OCC.Core.gp import *


class LProp3d_CLProps:
	@overload
	def __init__(self, C: Adaptor3d_HCurve, N: int, Resolution: float) -> None: ...
	@overload
	def __init__(self, C: Adaptor3d_HCurve, U: float, N: int, Resolution: float) -> None: ...
	@overload
	def __init__(self, N: int, Resolution: float) -> None: ...
	def CentreOfCurvature(self, P: gp_Pnt) -> None: ...
	def Curvature(self) -> float: ...
	def D1(self) -> gp_Vec: ...
	def D2(self) -> gp_Vec: ...
	def D3(self) -> gp_Vec: ...
	def IsTangentDefined(self) -> bool: ...
	def Normal(self, N: gp_Dir) -> None: ...
	def SetCurve(self, C: Adaptor3d_HCurve) -> None: ...
	def SetParameter(self, U: float) -> None: ...
	def Tangent(self, D: gp_Dir) -> None: ...
	def Value(self) -> gp_Pnt: ...

class LProp3d_CurveTool:
	@staticmethod
	def Continuity(self, C: Adaptor3d_HCurve) -> int: ...
	@staticmethod
	def D1(self, C: Adaptor3d_HCurve, U: float, P: gp_Pnt, V1: gp_Vec) -> None: ...
	@staticmethod
	def D2(self, C: Adaptor3d_HCurve, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	@staticmethod
	def D3(self, C: Adaptor3d_HCurve, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	@staticmethod
	def FirstParameter(self, C: Adaptor3d_HCurve) -> float: ...
	@staticmethod
	def LastParameter(self, C: Adaptor3d_HCurve) -> float: ...
	@staticmethod
	def Value(self, C: Adaptor3d_HCurve, U: float, P: gp_Pnt) -> None: ...

class LProp3d_SLProps:
	@overload
	def __init__(self, S: Adaptor3d_HSurface, U: float, V: float, N: int, Resolution: float) -> None: ...
	@overload
	def __init__(self, S: Adaptor3d_HSurface, N: int, Resolution: float) -> None: ...
	@overload
	def __init__(self, N: int, Resolution: float) -> None: ...
	def CurvatureDirections(self, MaxD: gp_Dir, MinD: gp_Dir) -> None: ...
	def D1U(self) -> gp_Vec: ...
	def D1V(self) -> gp_Vec: ...
	def D2U(self) -> gp_Vec: ...
	def D2V(self) -> gp_Vec: ...
	def DUV(self) -> gp_Vec: ...
	def GaussianCurvature(self) -> float: ...
	def IsCurvatureDefined(self) -> bool: ...
	def IsNormalDefined(self) -> bool: ...
	def IsTangentUDefined(self) -> bool: ...
	def IsTangentVDefined(self) -> bool: ...
	def IsUmbilic(self) -> bool: ...
	def MaxCurvature(self) -> float: ...
	def MeanCurvature(self) -> float: ...
	def MinCurvature(self) -> float: ...
	def Normal(self) -> gp_Dir: ...
	def SetParameters(self, U: float, V: float) -> None: ...
	def SetSurface(self, S: Adaptor3d_HSurface) -> None: ...
	def TangentU(self, D: gp_Dir) -> None: ...
	def TangentV(self, D: gp_Dir) -> None: ...
	def Value(self) -> gp_Pnt: ...

class LProp3d_SurfaceTool:
	@staticmethod
	def Bounds(self, S: Adaptor3d_HSurface) -> Tuple[float, float, float, float]: ...
	@staticmethod
	def Continuity(self, S: Adaptor3d_HSurface) -> int: ...
	@staticmethod
	def D1(self, S: Adaptor3d_HSurface, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec) -> None: ...
	@staticmethod
	def D2(self, S: Adaptor3d_HSurface, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, DUV: gp_Vec) -> None: ...
	@staticmethod
	def DN(self, S: Adaptor3d_HSurface, U: float, V: float, IU: int, IV: int) -> gp_Vec: ...
	@staticmethod
	def Value(self, S: Adaptor3d_HSurface, U: float, V: float, P: gp_Pnt) -> None: ...
