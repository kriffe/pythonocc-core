from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Adaptor3d import *
from OCC.Core.gp import *
from OCC.Core.Convert import *
from OCC.Core.TColStd import *
from OCC.Core.GeomAbs import *
from OCC.Core.Blend import *
from OCC.Core.Law import *
from OCC.Core.math import *
from OCC.Core.TColgp import *
from OCC.Core.Adaptor2d import *


class BlendFunc_SectionShape(IntEnum):
	BlendFunc_Rational: int = ...
	BlendFunc_QuasiAngular: int = ...
	BlendFunc_Polynomial: int = ...
	BlendFunc_Linear: int = ...
BlendFunc_Rational = BlendFunc_SectionShape.BlendFunc_Rational
BlendFunc_QuasiAngular = BlendFunc_SectionShape.BlendFunc_QuasiAngular
BlendFunc_Polynomial = BlendFunc_SectionShape.BlendFunc_Polynomial
BlendFunc_Linear = BlendFunc_SectionShape.BlendFunc_Linear

class blendfunc:
	@staticmethod
	def ComputeDNormal(self, Surf: Adaptor3d_HSurface, p2d: gp_Pnt2d, Normal: gp_Vec, DNu: gp_Vec, DNv: gp_Vec) -> bool: ...
	@staticmethod
	def ComputeNormal(self, Surf: Adaptor3d_HSurface, p2d: gp_Pnt2d, Normal: gp_Vec) -> bool: ...
	@staticmethod
	def GetMinimalWeights(self, SectShape: BlendFunc_SectionShape, TConv: Convert_ParameterisationType, AngleMin: float, AngleMax: float, Weigths: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def GetShape(self, SectShape: BlendFunc_SectionShape, MaxAng: float, TypeConv: Convert_ParameterisationType) -> Tuple[int, int, int]: ...
	@staticmethod
	def NextShape(self, S: GeomAbs_Shape) -> GeomAbs_Shape: ...

class BlendFunc_CSCircular(Blend_CSFunction):
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve, CGuide: Adaptor3d_HCurve, L: Law_Function) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetSection(self, Param: float, U: float, V: float, W: float, tabP: TColgp_Array1OfPnt, tabV: TColgp_Array1OfVec) -> bool: ...
	def GetSectionSize(self) -> float: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	@overload
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	@overload
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbVariables(self) -> int: ...
	def ParameterOnC(self) -> float: ...
	def Pnt2d(self) -> gp_Pnt2d: ...
	def PointOnC(self) -> gp_Pnt: ...
	def PointOnS(self) -> gp_Pnt: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	@overload
	def Section(self, Param: float, U: float, V: float, W: float, C: gp_Circ) -> Tuple[float, float]: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	@overload
	def Set(self, Param: float) -> None: ...
	@overload
	def Set(self, First: float, Last: float) -> None: ...
	@overload
	def Set(self, Radius: float, Choix: int) -> None: ...
	@overload
	def Set(self, TypeSection: BlendFunc_SectionShape) -> None: ...
	def Tangent(self, U: float, V: float, TgS: gp_Vec, NormS: gp_Vec) -> None: ...
	def Tangent2d(self) -> gp_Vec2d: ...
	def TangentOnC(self) -> gp_Vec: ...
	def TangentOnS(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_CSConstRad(Blend_CSFunction):
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve, CGuide: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetSection(self, Param: float, U: float, V: float, W: float, tabP: TColgp_Array1OfPnt, tabV: TColgp_Array1OfVec) -> bool: ...
	def GetSectionSize(self) -> float: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	@overload
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	@overload
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def ParameterOnC(self) -> float: ...
	def Pnt2d(self) -> gp_Pnt2d: ...
	def PointOnC(self) -> gp_Pnt: ...
	def PointOnS(self) -> gp_Pnt: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	@overload
	def Section(self, Param: float, U: float, V: float, W: float, C: gp_Circ) -> Tuple[float, float]: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	@overload
	def Set(self, Param: float) -> None: ...
	@overload
	def Set(self, First: float, Last: float) -> None: ...
	@overload
	def Set(self, Radius: float, Choix: int) -> None: ...
	@overload
	def Set(self, TypeSection: BlendFunc_SectionShape) -> None: ...
	def Tangent(self, U: float, V: float, TgS: gp_Vec, NormS: gp_Vec) -> None: ...
	def Tangent2d(self) -> gp_Vec2d: ...
	def TangentOnC(self) -> gp_Vec: ...
	def TangentOnS(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_ChAsym(Blend_Function):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def ComputeValues(self, X: math_Vector, DegF: int, DegL: int) -> bool: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalDistance(self) -> float: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetSectionSize(self) -> float: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	@overload
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	@overload
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def PointOnS1(self) -> gp_Pnt: ...
	def PointOnS2(self) -> gp_Pnt: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	@overload
	def Section(self, Param: float, U1: float, V1: float, U2: float, V2: float, C: gp_Lin) -> Tuple[float, float]: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Set(self, Param: float) -> None: ...
	@overload
	def Set(self, First: float, Last: float) -> None: ...
	@overload
	def Set(self, Dist1: float, Angle: float, Choix: int) -> None: ...
	def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: gp_Vec, TgLast: gp_Vec, NormFirst: gp_Vec, NormLast: gp_Vec) -> None: ...
	def Tangent2dOnS1(self) -> gp_Vec2d: ...
	def Tangent2dOnS2(self) -> gp_Vec2d: ...
	def TangentOnS1(self) -> gp_Vec: ...
	def TangentOnS2(self) -> gp_Vec: ...
	def TwistOnS1(self) -> bool: ...
	def TwistOnS2(self) -> bool: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_ChAsymInv(Blend_FuncInv):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def ComputeValues(self, X: math_Vector, DegF: int, DegL: int) -> bool: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def NbEquations(self) -> int: ...
	@overload
	def Set(self, OnFirst: bool, COnSurf: Adaptor2d_HCurve2d) -> None: ...
	@overload
	def Set(self, Dist1: float, Angle: float, Choix: int) -> None: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_ConstRad(Blend_Function):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def AxeRot(self, Prm: float) -> gp_Ax1: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalDistance(self) -> float: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetSectionSize(self) -> float: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	@overload
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	@overload
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def PointOnS1(self) -> gp_Pnt: ...
	def PointOnS2(self) -> gp_Pnt: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	@overload
	def Section(self, Param: float, U1: float, V1: float, U2: float, V2: float, C: gp_Circ) -> Tuple[float, float]: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	@overload
	def Set(self, Param: float) -> None: ...
	@overload
	def Set(self, First: float, Last: float) -> None: ...
	@overload
	def Set(self, Radius: float, Choix: int) -> None: ...
	@overload
	def Set(self, TypeSection: BlendFunc_SectionShape) -> None: ...
	def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: gp_Vec, TgLast: gp_Vec, NormFirst: gp_Vec, NormLast: gp_Vec) -> None: ...
	def Tangent2dOnS1(self) -> gp_Vec2d: ...
	def Tangent2dOnS2(self) -> gp_Vec2d: ...
	def TangentOnS1(self) -> gp_Vec: ...
	def TangentOnS2(self) -> gp_Vec: ...
	def TwistOnS1(self) -> bool: ...
	def TwistOnS2(self) -> bool: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_ConstRadInv(Blend_FuncInv):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def NbEquations(self) -> int: ...
	@overload
	def Set(self, OnFirst: bool, COnSurf: Adaptor2d_HCurve2d) -> None: ...
	@overload
	def Set(self, R: float, Choix: int) -> None: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_Corde:
	def __init__(self, S: Adaptor3d_HSurface, CGuide: Adaptor3d_HCurve) -> None: ...
	def DerFguide(self, Sol: math_Vector, DerF: gp_Vec2d) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def NPlan(self) -> gp_Vec: ...
	def PointOnGuide(self) -> gp_Pnt: ...
	def PointOnS(self) -> gp_Pnt: ...
	def SetDist(self, Dist: float) -> None: ...
	def SetParam(self, Param: float) -> None: ...
	def Tangent2dOnS(self) -> gp_Vec2d: ...
	def TangentOnS(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...

class BlendFunc_EvolRad(Blend_Function):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve, Law: Law_Function) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalDistance(self) -> float: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetSectionSize(self) -> float: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	@overload
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	@overload
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def PointOnS1(self) -> gp_Pnt: ...
	def PointOnS2(self) -> gp_Pnt: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	@overload
	def Section(self, Param: float, U1: float, V1: float, U2: float, V2: float, C: gp_Circ) -> Tuple[float, float]: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	@overload
	def Set(self, Param: float) -> None: ...
	@overload
	def Set(self, First: float, Last: float) -> None: ...
	@overload
	def Set(self, Choix: int) -> None: ...
	@overload
	def Set(self, TypeSection: BlendFunc_SectionShape) -> None: ...
	def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: gp_Vec, TgLast: gp_Vec, NormFirst: gp_Vec, NormLast: gp_Vec) -> None: ...
	def Tangent2dOnS1(self) -> gp_Vec2d: ...
	def Tangent2dOnS2(self) -> gp_Vec2d: ...
	def TangentOnS1(self) -> gp_Vec: ...
	def TangentOnS2(self) -> gp_Vec: ...
	def TwistOnS1(self) -> bool: ...
	def TwistOnS2(self) -> bool: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_EvolRadInv(Blend_FuncInv):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve, Law: Law_Function) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def NbEquations(self) -> int: ...
	@overload
	def Set(self, OnFirst: bool, COnSurf: Adaptor2d_HCurve2d) -> None: ...
	@overload
	def Set(self, Choix: int) -> None: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_GenChamfInv(Blend_FuncInv):
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def NbEquations(self) -> int: ...
	@overload
	def Set(self, OnFirst: bool, COnSurf: Adaptor2d_HCurve2d) -> None: ...
	@overload
	def Set(self, Dist1: float, Dist2: float, Choix: int) -> None: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_GenChamfer(Blend_Function):
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalDistance(self) -> float: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	@overload
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	@overload
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	@overload
	def Section(self, Param: float, U1: float, V1: float, U2: float, V2: float, C: gp_Lin) -> Tuple[float, float]: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	@overload
	def Set(self, Param: float) -> None: ...
	@overload
	def Set(self, First: float, Last: float) -> None: ...
	@overload
	def Set(self, Dist1: float, Dist2: float, Choix: int) -> None: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_Ruled(Blend_Function):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def AxeRot(self, Prm: float) -> gp_Ax1: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalDistance(self) -> float: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetSection(self, Param: float, U1: float, V1: float, U2: float, V2: float, tabP: TColgp_Array1OfPnt, tabV: TColgp_Array1OfVec) -> bool: ...
	def GetSectionSize(self) -> float: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	@overload
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	@overload
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def PointOnS1(self) -> gp_Pnt: ...
	def PointOnS2(self) -> gp_Pnt: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	@overload
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	@overload
	def Set(self, Param: float) -> None: ...
	@overload
	def Set(self, First: float, Last: float) -> None: ...
	def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: gp_Vec, TgLast: gp_Vec, NormFirst: gp_Vec, NormLast: gp_Vec) -> None: ...
	def Tangent2dOnS1(self) -> gp_Vec2d: ...
	def Tangent2dOnS2(self) -> gp_Vec2d: ...
	def TangentOnS1(self) -> gp_Vec: ...
	def TangentOnS2(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_RuledInv(Blend_FuncInv):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def NbEquations(self) -> int: ...
	def Set(self, OnFirst: bool, COnSurf: Adaptor2d_HCurve2d) -> None: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BlendFunc_Tensor:
	def __init__(self, NbRow: int, NbCol: int, NbMat: int) -> None: ...
	def GetChangeValue(self, Row: int, Col: int, Mat: int) -> float: ...
	def SetChangeValue(self, Row: int, Col: int, Mat: int, value: float) -> None: ...
	def Init(self, InitialValue: float) -> None: ...
	def Multiply(self, Right: math_Vector, Product: math_Matrix) -> None: ...
	def Value(self, Row: int, Col: int, Mat: int) -> float: ...

class BlendFunc_ChamfInv(BlendFunc_GenChamfInv):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def Set(self, Dist1: float, Dist2: float, Choix: int) -> None: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...

class BlendFunc_Chamfer(BlendFunc_GenChamfer):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, CG: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetSectionSize(self) -> float: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def PointOnS1(self) -> gp_Pnt: ...
	def PointOnS2(self) -> gp_Pnt: ...
	@overload
	def Set(self, Param: float) -> None: ...
	@overload
	def Set(self, Dist1: float, Dist2: float, Choix: int) -> None: ...
	def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: gp_Vec, TgLast: gp_Vec, NormFirst: gp_Vec, NormLast: gp_Vec) -> None: ...
	def Tangent2dOnS1(self) -> gp_Vec2d: ...
	def Tangent2dOnS2(self) -> gp_Vec2d: ...
	def TangentOnS1(self) -> gp_Vec: ...
	def TangentOnS2(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...

class BlendFunc_ConstThroat(BlendFunc_GenChamfer):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetSectionSize(self) -> float: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def PointOnS1(self) -> gp_Pnt: ...
	def PointOnS2(self) -> gp_Pnt: ...
	@overload
	def Set(self, Param: float) -> None: ...
	def Tangent(self, U1: float, V1: float, U2: float, V2: float, TgFirst: gp_Vec, TgLast: gp_Vec, NormFirst: gp_Vec, NormLast: gp_Vec) -> None: ...
	def Tangent2dOnS1(self) -> gp_Vec2d: ...
	def Tangent2dOnS2(self) -> gp_Vec2d: ...
	def TangentOnS1(self) -> gp_Vec: ...
	def TangentOnS2(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...

class BlendFunc_ConstThroatInv(BlendFunc_GenChamfInv):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...

class BlendFunc_ConstThroatWithPenetration(BlendFunc_ConstThroat):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetSectionSize(self) -> float: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def Tangent2dOnS1(self) -> gp_Vec2d: ...
	def Tangent2dOnS2(self) -> gp_Vec2d: ...
	def TangentOnS1(self) -> gp_Vec: ...
	def TangentOnS2(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...

class BlendFunc_ConstThroatWithPenetrationInv(BlendFunc_ConstThroatInv):
	def __init__(self, S1: Adaptor3d_HSurface, S2: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes

blendfunc_ComputeDNormal = blendfunc.ComputeDNormal
blendfunc_ComputeNormal = blendfunc.ComputeNormal
blendfunc_GetMinimalWeights = blendfunc.GetMinimalWeights
blendfunc_GetShape = blendfunc.GetShape
blendfunc_NextShape = blendfunc.NextShape
