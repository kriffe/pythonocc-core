from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.TColGeom import *
from OCC.Core.TColStd import *
from OCC.Core.Convert import *
from OCC.Core.GeomAbs import *
from OCC.Core.Adaptor3d import *
from OCC.Core.TColgp import *


class GeomConvert:
	@overload
	@staticmethod
	def C0BSplineToArrayOfC1BSplineCurve(self, BS: Geom_BSplineCurve, tabBS: TColGeom_HArray1OfBSplineCurve, tolerance: float) -> None: ...
	@overload
	@staticmethod
	def C0BSplineToArrayOfC1BSplineCurve(self, BS: Geom_BSplineCurve, tabBS: TColGeom_HArray1OfBSplineCurve, AngularTolerance: float, tolerance: float) -> None: ...
	@staticmethod
	def C0BSplineToC1BSplineCurve(self, BS: Geom_BSplineCurve, tolerance: float, AngularTolerance: Optional[float]) -> None: ...
	@overload
	@staticmethod
	def ConcatC1(self, ArrayOfCurves: TColGeom_Array1OfBSplineCurve, ArrayOfToler: TColStd_Array1OfReal, ArrayOfIndices: TColStd_HArray1OfInteger, ArrayOfConcatenated: TColGeom_HArray1OfBSplineCurve, ClosedTolerance: float) -> bool: ...
	@overload
	@staticmethod
	def ConcatC1(self, ArrayOfCurves: TColGeom_Array1OfBSplineCurve, ArrayOfToler: TColStd_Array1OfReal, ArrayOfIndices: TColStd_HArray1OfInteger, ArrayOfConcatenated: TColGeom_HArray1OfBSplineCurve, ClosedTolerance: float, AngularTolerance: float) -> bool: ...
	@staticmethod
	def ConcatG1(self, ArrayOfCurves: TColGeom_Array1OfBSplineCurve, ArrayOfToler: TColStd_Array1OfReal, ArrayOfConcatenated: TColGeom_HArray1OfBSplineCurve, ClosedTolerance: float) -> bool: ...
	@staticmethod
	def CurveToBSplineCurve(self, C: Geom_Curve, Parameterisation: Optional[Convert_ParameterisationType]) -> Geom_BSplineCurve: ...
	@overload
	@staticmethod
	def SplitBSplineCurve(self, C: Geom_BSplineCurve, FromK1: int, ToK2: int, SameOrientation: Optional[bool]) -> Geom_BSplineCurve: ...
	@overload
	@staticmethod
	def SplitBSplineCurve(self, C: Geom_BSplineCurve, FromU1: float, ToU2: float, ParametricTolerance: float, SameOrientation: Optional[bool]) -> Geom_BSplineCurve: ...
	@overload
	@staticmethod
	def SplitBSplineSurface(self, S: Geom_BSplineSurface, FromUK1: int, ToUK2: int, FromVK1: int, ToVK2: int, SameUOrientation: Optional[bool], SameVOrientation: Optional[bool]) -> Geom_BSplineSurface: ...
	@overload
	@staticmethod
	def SplitBSplineSurface(self, S: Geom_BSplineSurface, FromK1: int, ToK2: int, USplit: bool, SameOrientation: Optional[bool]) -> Geom_BSplineSurface: ...
	@overload
	@staticmethod
	def SplitBSplineSurface(self, S: Geom_BSplineSurface, FromU1: float, ToU2: float, FromV1: float, ToV2: float, ParametricTolerance: float, SameUOrientation: Optional[bool], SameVOrientation: Optional[bool]) -> Geom_BSplineSurface: ...
	@overload
	@staticmethod
	def SplitBSplineSurface(self, S: Geom_BSplineSurface, FromParam1: float, ToParam2: float, USplit: bool, ParametricTolerance: float, SameOrientation: Optional[bool]) -> Geom_BSplineSurface: ...
	@staticmethod
	def SurfaceToBSplineSurface(self, S: Geom_Surface) -> Geom_BSplineSurface: ...

class GeomConvert_ApproxCurve:
	@overload
	def __init__(self, Curve: Geom_Curve, Tol3d: float, Order: GeomAbs_Shape, MaxSegments: int, MaxDegree: int) -> None: ...
	@overload
	def __init__(self, Curve: Adaptor3d_HCurve, Tol3d: float, Order: GeomAbs_Shape, MaxSegments: int, MaxDegree: int) -> None: ...
	def Curve(self) -> Geom_BSplineCurve: ...
	def HasResult(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def MaxError(self) -> float: ...

class GeomConvert_ApproxSurface:
	@overload
	def __init__(self, Surf: Geom_Surface, Tol3d: float, UContinuity: GeomAbs_Shape, VContinuity: GeomAbs_Shape, MaxDegU: int, MaxDegV: int, MaxSegments: int, PrecisCode: int) -> None: ...
	@overload
	def __init__(self, Surf: Adaptor3d_HSurface, Tol3d: float, UContinuity: GeomAbs_Shape, VContinuity: GeomAbs_Shape, MaxDegU: int, MaxDegV: int, MaxSegments: int, PrecisCode: int) -> None: ...
	def HasResult(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def MaxError(self) -> float: ...
	def Surface(self) -> Geom_BSplineSurface: ...

class GeomConvert_BSplineCurveKnotSplitting:
	def __init__(self, BasisCurve: Geom_BSplineCurve, ContinuityRange: int) -> None: ...
	def NbSplits(self) -> int: ...
	def SplitValue(self, Index: int) -> int: ...
	def Splitting(self, SplitValues: TColStd_Array1OfInteger) -> None: ...

class GeomConvert_BSplineCurveToBezierCurve:
	@overload
	def __init__(self, BasisCurve: Geom_BSplineCurve) -> None: ...
	@overload
	def __init__(self, BasisCurve: Geom_BSplineCurve, U1: float, U2: float, ParametricTolerance: float) -> None: ...
	def Arc(self, Index: int) -> Geom_BezierCurve: ...
	def Arcs(self, Curves: TColGeom_Array1OfBezierCurve) -> None: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def NbArcs(self) -> int: ...

class GeomConvert_BSplineSurfaceKnotSplitting:
	def __init__(self, BasisSurface: Geom_BSplineSurface, UContinuityRange: int, VContinuityRange: int) -> None: ...
	def NbUSplits(self) -> int: ...
	def NbVSplits(self) -> int: ...
	def Splitting(self, USplit: TColStd_Array1OfInteger, VSplit: TColStd_Array1OfInteger) -> None: ...
	def USplitValue(self, UIndex: int) -> int: ...
	def VSplitValue(self, VIndex: int) -> int: ...

class GeomConvert_BSplineSurfaceToBezierSurface:
	@overload
	def __init__(self, BasisSurface: Geom_BSplineSurface) -> None: ...
	@overload
	def __init__(self, BasisSurface: Geom_BSplineSurface, U1: float, U2: float, V1: float, V2: float, ParametricTolerance: float) -> None: ...
	def NbUPatches(self) -> int: ...
	def NbVPatches(self) -> int: ...
	def Patch(self, UIndex: int, VIndex: int) -> Geom_BezierSurface: ...
	def Patches(self, Surfaces: TColGeom_Array2OfBezierSurface) -> None: ...
	def UKnots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def VKnots(self, TKnots: TColStd_Array1OfReal) -> None: ...

class GeomConvert_CompBezierSurfacesToBSplineSurface:
	@overload
	def __init__(self, Beziers: TColGeom_Array2OfBezierSurface) -> None: ...
	@overload
	def __init__(self, Beziers: TColGeom_Array2OfBezierSurface, Tolerance: float, RemoveKnots: Optional[bool]) -> None: ...
	@overload
	def __init__(self, Beziers: TColGeom_Array2OfBezierSurface, UKnots: TColStd_Array1OfReal, VKnots: TColStd_Array1OfReal, UContinuity: Optional[GeomAbs_Shape], VContinuity: Optional[GeomAbs_Shape], Tolerance: Optional[float]) -> None: ...
	def IsDone(self) -> bool: ...
	def NbUKnots(self) -> int: ...
	def NbUPoles(self) -> int: ...
	def NbVKnots(self) -> int: ...
	def NbVPoles(self) -> int: ...
	def Poles(self) -> TColgp_HArray2OfPnt: ...
	def UDegree(self) -> int: ...
	def UKnots(self) -> TColStd_HArray1OfReal: ...
	def UMultiplicities(self) -> TColStd_HArray1OfInteger: ...
	def VDegree(self) -> int: ...
	def VKnots(self) -> TColStd_HArray1OfReal: ...
	def VMultiplicities(self) -> TColStd_HArray1OfInteger: ...

class GeomConvert_CompCurveToBSplineCurve:
	@overload
	def __init__(self, Parameterisation: Optional[Convert_ParameterisationType]) -> None: ...
	@overload
	def __init__(self, BasisCurve: Geom_BoundedCurve, Parameterisation: Optional[Convert_ParameterisationType]) -> None: ...
	def Add(self, NewCurve: Geom_BoundedCurve, Tolerance: float, After: Optional[bool], WithRatio: Optional[bool], MinM: Optional[int]) -> bool: ...
	def BSplineCurve(self) -> Geom_BSplineCurve: ...
