from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepGeom import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *


class StepToGeom:
	@staticmethod
	def MakeAxis1Placement(self, SA: StepGeom_Axis1Placement) -> Geom_Axis1Placement: ...
	@staticmethod
	def MakeAxis2Placement(self, SA: StepGeom_Axis2Placement3d) -> Geom_Axis2Placement: ...
	@staticmethod
	def MakeAxisPlacement(self, SA: StepGeom_Axis2Placement2d) -> Geom2d_AxisPlacement: ...
	@staticmethod
	def MakeBSplineCurve(self, SC: StepGeom_BSplineCurve) -> Geom_BSplineCurve: ...
	@staticmethod
	def MakeBSplineCurve2d(self, SC: StepGeom_BSplineCurve) -> Geom2d_BSplineCurve: ...
	@staticmethod
	def MakeBSplineSurface(self, SS: StepGeom_BSplineSurface) -> Geom_BSplineSurface: ...
	@staticmethod
	def MakeBoundedCurve(self, SC: StepGeom_BoundedCurve) -> Geom_BoundedCurve: ...
	@staticmethod
	def MakeBoundedCurve2d(self, SC: StepGeom_BoundedCurve) -> Geom2d_BoundedCurve: ...
	@staticmethod
	def MakeBoundedSurface(self, SS: StepGeom_BoundedSurface) -> Geom_BoundedSurface: ...
	@staticmethod
	def MakeCartesianPoint(self, SP: StepGeom_CartesianPoint) -> Geom_CartesianPoint: ...
	@staticmethod
	def MakeCartesianPoint2d(self, SP: StepGeom_CartesianPoint) -> Geom2d_CartesianPoint: ...
	@staticmethod
	def MakeCircle(self, SC: StepGeom_Circle) -> Geom_Circle: ...
	@staticmethod
	def MakeCircle2d(self, SC: StepGeom_Circle) -> Geom2d_Circle: ...
	@staticmethod
	def MakeConic(self, SC: StepGeom_Conic) -> Geom_Conic: ...
	@staticmethod
	def MakeConic2d(self, SC: StepGeom_Conic) -> Geom2d_Conic: ...
	@staticmethod
	def MakeConicalSurface(self, SS: StepGeom_ConicalSurface) -> Geom_ConicalSurface: ...
	@staticmethod
	def MakeCurve(self, SC: StepGeom_Curve) -> Geom_Curve: ...
	@staticmethod
	def MakeCurve2d(self, SC: StepGeom_Curve) -> Geom2d_Curve: ...
	@staticmethod
	def MakeCylindricalSurface(self, SS: StepGeom_CylindricalSurface) -> Geom_CylindricalSurface: ...
	@staticmethod
	def MakeDirection(self, SD: StepGeom_Direction) -> Geom_Direction: ...
	@staticmethod
	def MakeDirection2d(self, SD: StepGeom_Direction) -> Geom2d_Direction: ...
	@staticmethod
	def MakeElementarySurface(self, SS: StepGeom_ElementarySurface) -> Geom_ElementarySurface: ...
	@staticmethod
	def MakeEllipse(self, SC: StepGeom_Ellipse) -> Geom_Ellipse: ...
	@staticmethod
	def MakeEllipse2d(self, SC: StepGeom_Ellipse) -> Geom2d_Ellipse: ...
	@staticmethod
	def MakeHyperbola(self, SC: StepGeom_Hyperbola) -> Geom_Hyperbola: ...
	@staticmethod
	def MakeHyperbola2d(self, SC: StepGeom_Hyperbola) -> Geom2d_Hyperbola: ...
	@staticmethod
	def MakeLine(self, SC: StepGeom_Line) -> Geom_Line: ...
	@staticmethod
	def MakeLine2d(self, SC: StepGeom_Line) -> Geom2d_Line: ...
	@staticmethod
	def MakeParabola(self, SC: StepGeom_Parabola) -> Geom_Parabola: ...
	@staticmethod
	def MakeParabola2d(self, SC: StepGeom_Parabola) -> Geom2d_Parabola: ...
	@staticmethod
	def MakePlane(self, SP: StepGeom_Plane) -> Geom_Plane: ...
	@staticmethod
	def MakePolyline(self, SPL: StepGeom_Polyline) -> Geom_BSplineCurve: ...
	@staticmethod
	def MakePolyline2d(self, SPL: StepGeom_Polyline) -> Geom2d_BSplineCurve: ...
	@staticmethod
	def MakeRectangularTrimmedSurface(self, SS: StepGeom_RectangularTrimmedSurface) -> Geom_RectangularTrimmedSurface: ...
	@staticmethod
	def MakeSphericalSurface(self, SS: StepGeom_SphericalSurface) -> Geom_SphericalSurface: ...
	@staticmethod
	def MakeSurface(self, SS: StepGeom_Surface) -> Geom_Surface: ...
	@staticmethod
	def MakeSurfaceOfLinearExtrusion(self, SS: StepGeom_SurfaceOfLinearExtrusion) -> Geom_SurfaceOfLinearExtrusion: ...
	@staticmethod
	def MakeSurfaceOfRevolution(self, SS: StepGeom_SurfaceOfRevolution) -> Geom_SurfaceOfRevolution: ...
	@staticmethod
	def MakeSweptSurface(self, SS: StepGeom_SweptSurface) -> Geom_SweptSurface: ...
	@staticmethod
	def MakeToroidalSurface(self, SS: StepGeom_ToroidalSurface) -> Geom_ToroidalSurface: ...
	@staticmethod
	def MakeTransformation2d(self, SCTO: StepGeom_CartesianTransformationOperator2d, CT: gp_Trsf2d) -> bool: ...
	@staticmethod
	def MakeTransformation3d(self, SCTO: StepGeom_CartesianTransformationOperator3d, CT: gp_Trsf) -> bool: ...
	@staticmethod
	def MakeTrimmedCurve(self, SC: StepGeom_TrimmedCurve) -> Geom_TrimmedCurve: ...
	@staticmethod
	def MakeTrimmedCurve2d(self, SC: StepGeom_TrimmedCurve) -> Geom2d_BSplineCurve: ...
	@staticmethod
	def MakeVectorWithMagnitude(self, SV: StepGeom_Vector) -> Geom_VectorWithMagnitude: ...
	@staticmethod
	def MakeVectorWithMagnitude2d(self, SV: StepGeom_Vector) -> Geom2d_VectorWithMagnitude: ...
steptogeom_MakeAxis1Placement = steptogeom.MakeAxis1Placement
steptogeom_MakeAxis2Placement = steptogeom.MakeAxis2Placement
steptogeom_MakeAxisPlacement = steptogeom.MakeAxisPlacement
steptogeom_MakeBSplineCurve = steptogeom.MakeBSplineCurve
steptogeom_MakeBSplineCurve2d = steptogeom.MakeBSplineCurve2d
steptogeom_MakeBSplineSurface = steptogeom.MakeBSplineSurface
steptogeom_MakeBoundedCurve = steptogeom.MakeBoundedCurve
steptogeom_MakeBoundedCurve2d = steptogeom.MakeBoundedCurve2d
steptogeom_MakeBoundedSurface = steptogeom.MakeBoundedSurface
steptogeom_MakeCartesianPoint = steptogeom.MakeCartesianPoint
steptogeom_MakeCartesianPoint2d = steptogeom.MakeCartesianPoint2d
steptogeom_MakeCircle = steptogeom.MakeCircle
steptogeom_MakeCircle2d = steptogeom.MakeCircle2d
steptogeom_MakeConic = steptogeom.MakeConic
steptogeom_MakeConic2d = steptogeom.MakeConic2d
steptogeom_MakeConicalSurface = steptogeom.MakeConicalSurface
steptogeom_MakeCurve = steptogeom.MakeCurve
steptogeom_MakeCurve2d = steptogeom.MakeCurve2d
steptogeom_MakeCylindricalSurface = steptogeom.MakeCylindricalSurface
steptogeom_MakeDirection = steptogeom.MakeDirection
steptogeom_MakeDirection2d = steptogeom.MakeDirection2d
steptogeom_MakeElementarySurface = steptogeom.MakeElementarySurface
steptogeom_MakeEllipse = steptogeom.MakeEllipse
steptogeom_MakeEllipse2d = steptogeom.MakeEllipse2d
steptogeom_MakeHyperbola = steptogeom.MakeHyperbola
steptogeom_MakeHyperbola2d = steptogeom.MakeHyperbola2d
steptogeom_MakeLine = steptogeom.MakeLine
steptogeom_MakeLine2d = steptogeom.MakeLine2d
steptogeom_MakeParabola = steptogeom.MakeParabola
steptogeom_MakeParabola2d = steptogeom.MakeParabola2d
steptogeom_MakePlane = steptogeom.MakePlane
steptogeom_MakePolyline = steptogeom.MakePolyline
steptogeom_MakePolyline2d = steptogeom.MakePolyline2d
steptogeom_MakeRectangularTrimmedSurface = steptogeom.MakeRectangularTrimmedSurface
steptogeom_MakeSphericalSurface = steptogeom.MakeSphericalSurface
steptogeom_MakeSurface = steptogeom.MakeSurface
steptogeom_MakeSurfaceOfLinearExtrusion = steptogeom.MakeSurfaceOfLinearExtrusion
steptogeom_MakeSurfaceOfRevolution = steptogeom.MakeSurfaceOfRevolution
steptogeom_MakeSweptSurface = steptogeom.MakeSweptSurface
steptogeom_MakeToroidalSurface = steptogeom.MakeToroidalSurface
steptogeom_MakeTransformation2d = steptogeom.MakeTransformation2d
steptogeom_MakeTransformation3d = steptogeom.MakeTransformation3d
steptogeom_MakeTrimmedCurve = steptogeom.MakeTrimmedCurve
steptogeom_MakeTrimmedCurve2d = steptogeom.MakeTrimmedCurve2d
steptogeom_MakeVectorWithMagnitude = steptogeom.MakeVectorWithMagnitude
steptogeom_MakeVectorWithMagnitude2d = steptogeom.MakeVectorWithMagnitude2d
