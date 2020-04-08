from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Graphic3d import *
from OCC.Core.gp import *
from OCC.Core.Quantity import *
from OCC.Core.Aspect import *
from OCC.Core.TColStd import *
from OCC.Core.Bnd import *
from OCC.Core.TCollection import *
from OCC.Core.Image import *

Handle_V3d_Light = NewType('Handle_V3d_Light', Handle_Graphic3d_CLight)
V3d_Coordinate = NewType('V3d_Coordinate', Standard_Real)
V3d_Light = NewType('V3d_Light', Graphic3d_CLight)
#the following typedef cannot be wrapped as is
V3d_ListOfLight = NewType('V3d_ListOfLight', Any)
#the following typedef cannot be wrapped as is
V3d_ListOfLightIterator = NewType('V3d_ListOfLightIterator', Any)
#the following typedef cannot be wrapped as is
V3d_ListOfView = NewType('V3d_ListOfView', Any)
#the following typedef cannot be wrapped as is
V3d_ListOfViewIterator = NewType('V3d_ListOfViewIterator', Any)
V3d_Parameter = NewType('V3d_Parameter', Standard_Real)
V3d_TypeOfLight = NewType('V3d_TypeOfLight', Graphic3d_TypeOfLightSource)
V3d_TypeOfShadingModel = NewType('V3d_TypeOfShadingModel', Graphic3d_TypeOfShadingModel)
V3d_ViewPointer = NewType('V3d_ViewPointer', V3d_View)
V3d_ViewerPointer = NewType('V3d_ViewerPointer', V3d_Viewer)

class V3d_TypeOfPickCamera(IntEnum):
	V3d_POSITIONCAMERA: int = ...
	V3d_SPACECAMERA: int = ...
	V3d_RADIUSTEXTCAMERA: int = ...
	V3d_ExtRADIUSCAMERA: int = ...
	V3d_IntRADIUSCAMERA: int = ...
	V3d_NOTHINGCAMERA: int = ...
V3d_POSITIONCAMERA = V3d_TypeOfPickCamera.V3d_POSITIONCAMERA
V3d_SPACECAMERA = V3d_TypeOfPickCamera.V3d_SPACECAMERA
V3d_RADIUSTEXTCAMERA = V3d_TypeOfPickCamera.V3d_RADIUSTEXTCAMERA
V3d_ExtRADIUSCAMERA = V3d_TypeOfPickCamera.V3d_ExtRADIUSCAMERA
V3d_IntRADIUSCAMERA = V3d_TypeOfPickCamera.V3d_IntRADIUSCAMERA
V3d_NOTHINGCAMERA = V3d_TypeOfPickCamera.V3d_NOTHINGCAMERA

class V3d_TypeOfVisualization(IntEnum):
	V3d_WIREFRAME: int = ...
	V3d_ZBUFFER: int = ...
V3d_WIREFRAME = V3d_TypeOfVisualization.V3d_WIREFRAME
V3d_ZBUFFER = V3d_TypeOfVisualization.V3d_ZBUFFER

class V3d_TypeOfView(IntEnum):
	V3d_ORTHOGRAPHIC: int = ...
	V3d_PERSPECTIVE: int = ...
V3d_ORTHOGRAPHIC = V3d_TypeOfView.V3d_ORTHOGRAPHIC
V3d_PERSPECTIVE = V3d_TypeOfView.V3d_PERSPECTIVE

class V3d_StereoDumpOptions(IntEnum):
	V3d_SDO_MONO: int = ...
	V3d_SDO_LEFT_EYE: int = ...
	V3d_SDO_RIGHT_EYE: int = ...
	V3d_SDO_BLENDED: int = ...
V3d_SDO_MONO = V3d_StereoDumpOptions.V3d_SDO_MONO
V3d_SDO_LEFT_EYE = V3d_StereoDumpOptions.V3d_SDO_LEFT_EYE
V3d_SDO_RIGHT_EYE = V3d_StereoDumpOptions.V3d_SDO_RIGHT_EYE
V3d_SDO_BLENDED = V3d_StereoDumpOptions.V3d_SDO_BLENDED

class V3d_TypeOfOrientation(IntEnum):
	V3d_Xpos: int = ...
	V3d_Ypos: int = ...
	V3d_Zpos: int = ...
	V3d_Xneg: int = ...
	V3d_Yneg: int = ...
	V3d_Zneg: int = ...
	V3d_XposYpos: int = ...
	V3d_XposZpos: int = ...
	V3d_YposZpos: int = ...
	V3d_XnegYneg: int = ...
	V3d_XnegYpos: int = ...
	V3d_XnegZneg: int = ...
	V3d_XnegZpos: int = ...
	V3d_YnegZneg: int = ...
	V3d_YnegZpos: int = ...
	V3d_XposYneg: int = ...
	V3d_XposZneg: int = ...
	V3d_YposZneg: int = ...
	V3d_XposYposZpos: int = ...
	V3d_XposYnegZpos: int = ...
	V3d_XposYposZneg: int = ...
	V3d_XnegYposZpos: int = ...
	V3d_XposYnegZneg: int = ...
	V3d_XnegYposZneg: int = ...
	V3d_XnegYnegZpos: int = ...
	V3d_XnegYnegZneg: int = ...
	V3d_TypeOfOrientation_Zup_AxoLeft: int = ...
	V3d_TypeOfOrientation_Zup_AxoRight: int = ...
	V3d_TypeOfOrientation_Zup_Front: int = ...
	V3d_TypeOfOrientation_Zup_Back: int = ...
	V3d_TypeOfOrientation_Zup_Top: int = ...
	V3d_TypeOfOrientation_Zup_Bottom: int = ...
	V3d_TypeOfOrientation_Zup_Left: int = ...
	V3d_TypeOfOrientation_Zup_Right: int = ...
	V3d_TypeOfOrientation_Yup_AxoLeft: int = ...
	V3d_TypeOfOrientation_Yup_AxoRight: int = ...
	V3d_TypeOfOrientation_Yup_Front: int = ...
	V3d_TypeOfOrientation_Yup_Back: int = ...
	V3d_TypeOfOrientation_Yup_Top: int = ...
	V3d_TypeOfOrientation_Yup_Bottom: int = ...
	V3d_TypeOfOrientation_Yup_Left: int = ...
	V3d_TypeOfOrientation_Yup_Right: int = ...
V3d_Xpos = V3d_TypeOfOrientation.V3d_Xpos
V3d_Ypos = V3d_TypeOfOrientation.V3d_Ypos
V3d_Zpos = V3d_TypeOfOrientation.V3d_Zpos
V3d_Xneg = V3d_TypeOfOrientation.V3d_Xneg
V3d_Yneg = V3d_TypeOfOrientation.V3d_Yneg
V3d_Zneg = V3d_TypeOfOrientation.V3d_Zneg
V3d_XposYpos = V3d_TypeOfOrientation.V3d_XposYpos
V3d_XposZpos = V3d_TypeOfOrientation.V3d_XposZpos
V3d_YposZpos = V3d_TypeOfOrientation.V3d_YposZpos
V3d_XnegYneg = V3d_TypeOfOrientation.V3d_XnegYneg
V3d_XnegYpos = V3d_TypeOfOrientation.V3d_XnegYpos
V3d_XnegZneg = V3d_TypeOfOrientation.V3d_XnegZneg
V3d_XnegZpos = V3d_TypeOfOrientation.V3d_XnegZpos
V3d_YnegZneg = V3d_TypeOfOrientation.V3d_YnegZneg
V3d_YnegZpos = V3d_TypeOfOrientation.V3d_YnegZpos
V3d_XposYneg = V3d_TypeOfOrientation.V3d_XposYneg
V3d_XposZneg = V3d_TypeOfOrientation.V3d_XposZneg
V3d_YposZneg = V3d_TypeOfOrientation.V3d_YposZneg
V3d_XposYposZpos = V3d_TypeOfOrientation.V3d_XposYposZpos
V3d_XposYnegZpos = V3d_TypeOfOrientation.V3d_XposYnegZpos
V3d_XposYposZneg = V3d_TypeOfOrientation.V3d_XposYposZneg
V3d_XnegYposZpos = V3d_TypeOfOrientation.V3d_XnegYposZpos
V3d_XposYnegZneg = V3d_TypeOfOrientation.V3d_XposYnegZneg
V3d_XnegYposZneg = V3d_TypeOfOrientation.V3d_XnegYposZneg
V3d_XnegYnegZpos = V3d_TypeOfOrientation.V3d_XnegYnegZpos
V3d_XnegYnegZneg = V3d_TypeOfOrientation.V3d_XnegYnegZneg
V3d_TypeOfOrientation_Zup_AxoLeft = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_AxoLeft
V3d_TypeOfOrientation_Zup_AxoRight = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_AxoRight
V3d_TypeOfOrientation_Zup_Front = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Front
V3d_TypeOfOrientation_Zup_Back = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Back
V3d_TypeOfOrientation_Zup_Top = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Top
V3d_TypeOfOrientation_Zup_Bottom = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Bottom
V3d_TypeOfOrientation_Zup_Left = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Left
V3d_TypeOfOrientation_Zup_Right = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Zup_Right
V3d_TypeOfOrientation_Yup_AxoLeft = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_AxoLeft
V3d_TypeOfOrientation_Yup_AxoRight = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_AxoRight
V3d_TypeOfOrientation_Yup_Front = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Front
V3d_TypeOfOrientation_Yup_Back = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Back
V3d_TypeOfOrientation_Yup_Top = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Top
V3d_TypeOfOrientation_Yup_Bottom = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Bottom
V3d_TypeOfOrientation_Yup_Left = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Left
V3d_TypeOfOrientation_Yup_Right = V3d_TypeOfOrientation.V3d_TypeOfOrientation_Yup_Right

class V3d_TypeOfAxe(IntEnum):
	V3d_X: int = ...
	V3d_Y: int = ...
	V3d_Z: int = ...
V3d_X = V3d_TypeOfAxe.V3d_X
V3d_Y = V3d_TypeOfAxe.V3d_Y
V3d_Z = V3d_TypeOfAxe.V3d_Z

class V3d_TypeOfRepresentation(IntEnum):
	V3d_SIMPLE: int = ...
	V3d_COMPLETE: int = ...
	V3d_PARTIAL: int = ...
	V3d_SAMELAST: int = ...
V3d_SIMPLE = V3d_TypeOfRepresentation.V3d_SIMPLE
V3d_COMPLETE = V3d_TypeOfRepresentation.V3d_COMPLETE
V3d_PARTIAL = V3d_TypeOfRepresentation.V3d_PARTIAL
V3d_SAMELAST = V3d_TypeOfRepresentation.V3d_SAMELAST

class V3d_TypeOfBackfacingModel(IntEnum):
	V3d_TOBM_AUTOMATIC: int = ...
	V3d_TOBM_ALWAYS_DISPLAYED: int = ...
	V3d_TOBM_NEVER_DISPLAYED: int = ...
V3d_TOBM_AUTOMATIC = V3d_TypeOfBackfacingModel.V3d_TOBM_AUTOMATIC
V3d_TOBM_ALWAYS_DISPLAYED = V3d_TypeOfBackfacingModel.V3d_TOBM_ALWAYS_DISPLAYED
V3d_TOBM_NEVER_DISPLAYED = V3d_TypeOfBackfacingModel.V3d_TOBM_NEVER_DISPLAYED

class V3d_TypeOfPickLight(IntEnum):
	V3d_POSITIONLIGHT: int = ...
	V3d_SPACELIGHT: int = ...
	V3d_RADIUSTEXTLIGHT: int = ...
	V3d_ExtRADIUSLIGHT: int = ...
	V3d_IntRADIUSLIGHT: int = ...
	V3d_NOTHING: int = ...
V3d_POSITIONLIGHT = V3d_TypeOfPickLight.V3d_POSITIONLIGHT
V3d_SPACELIGHT = V3d_TypeOfPickLight.V3d_SPACELIGHT
V3d_RADIUSTEXTLIGHT = V3d_TypeOfPickLight.V3d_RADIUSTEXTLIGHT
V3d_ExtRADIUSLIGHT = V3d_TypeOfPickLight.V3d_ExtRADIUSLIGHT
V3d_IntRADIUSLIGHT = V3d_TypeOfPickLight.V3d_IntRADIUSLIGHT
V3d_NOTHING = V3d_TypeOfPickLight.V3d_NOTHING

class V3d:
	@staticmethod
	def ArrowOfRadius(self, garrow: Graphic3d_Group, X0: float, Y0: float, Z0: float, DX: float, DY: float, DZ: float, Alpha: float, Lng: float) -> None: ...
	@staticmethod
	def CircleInPlane(self, gcircle: Graphic3d_Group, X0: float, Y0: float, Z0: float, VX: float, VY: float, VZ: float, Radius: float) -> None: ...
	@staticmethod
	def GetProjAxis(self, theOrientation: V3d_TypeOfOrientation) -> gp_Dir: ...
	@staticmethod
	def SwitchViewsinWindow(self, aPreviousView: V3d_View, aNextView: V3d_View) -> None: ...
	@overload
	@staticmethod
	def TypeOfOrientationFromString(self, theTypeString: str) -> V3d_TypeOfOrientation: ...
	@overload
	@staticmethod
	def TypeOfOrientationFromString(self, theTypeString: str, theType: V3d_TypeOfOrientation) -> bool: ...
	@staticmethod
	def TypeOfOrientationToString(self, theType: V3d_TypeOfOrientation) -> str: ...

class V3d_AmbientLight(Graphic3d_CLight):
	@overload
	def __init__(self, theColor: Optional[Quantity_Color]) -> None: ...
	@overload
	def __init__(self, theViewer: V3d_Viewer, theColor: Optional[Quantity_Color]) -> None: ...

class V3d_CircularGrid(Aspect_CircularGrid):
	def __init__(self, aViewer: V3d_ViewerPointer, aColor: Quantity_Color, aTenthColor: Quantity_Color) -> None: ...
	def Display(self) -> None: ...
	def Erase(self) -> None: ...
	def GraphicValues(self) -> Tuple[float, float]: ...
	def IsDisplayed(self) -> bool: ...
	def SetColors(self, aColor: Quantity_Color, aTenthColor: Quantity_Color) -> None: ...
	def SetGraphicValues(self, Radius: float, OffSet: float) -> None: ...

class V3d_ImageDumpOptions:
	def __init__(self) -> None: ...

class V3d_Plane(Standard_Transient):
	def __init__(self, theA: Optional[float], theB: Optional[float], theC: Optional[float], theD: Optional[float]) -> None: ...
	def ClipPlane(self) -> Graphic3d_ClipPlane: ...
	def Display(self, theView: V3d_View, theColor: Optional[Quantity_Color]) -> None: ...
	def Erase(self) -> None: ...
	def IsDisplayed(self) -> bool: ...
	def Plane(self) -> Tuple[float, float, float, float]: ...
	def SetPlane(self, theA: float, theB: float, theC: float, theD: float) -> None: ...

class V3d_PositionLight(Graphic3d_CLight):
	pass

class V3d_RectangularGrid(Aspect_RectangularGrid):
	def __init__(self, aViewer: V3d_ViewerPointer, aColor: Quantity_Color, aTenthColor: Quantity_Color) -> None: ...
	def Display(self) -> None: ...
	def Erase(self) -> None: ...
	def GraphicValues(self) -> Tuple[float, float, float]: ...
	def IsDisplayed(self) -> bool: ...
	def SetColors(self, aColor: Quantity_Color, aTenthColor: Quantity_Color) -> None: ...
	def SetGraphicValues(self, XSize: float, YSize: float, OffSet: float) -> None: ...

class V3d_Trihedron(Standard_Transient):
	def __init__(self) -> None: ...
	def Display(self, theView: V3d_View) -> None: ...
	def Erase(self) -> None: ...
	def SetArrowDiameter(self, theDiam: float) -> None: ...
	def SetArrowsColor(self, theXColor: Quantity_Color, theYColor: Quantity_Color, theZColor: Quantity_Color) -> None: ...
	def SetLabelsColor(self, theColor: Quantity_Color) -> None: ...
	def SetNbFacets(self, theNbFacets: int) -> None: ...
	def SetPosition(self, thePosition: Aspect_TypeOfTriedronPosition) -> None: ...
	def SetScale(self, theScale: float) -> None: ...
	def SetSizeRatio(self, theRatio: float) -> None: ...
	def SetWireframe(self, theAsWireframe: bool) -> None: ...

class V3d_View(Standard_Transient):
	@overload
	def __init__(self, theViewer: V3d_Viewer, theType: Optional[V3d_TypeOfView]) -> None: ...
	@overload
	def __init__(self, theViewer: V3d_Viewer, theView: V3d_View) -> None: ...
	def ActiveLight(self) -> V3d_Light: ...
	def ActiveLightIterator(self) -> V3d_ListOfLightIterator: ...
	def AddClipPlane(self, thePlane: Graphic3d_ClipPlane) -> None: ...
	def At(self) -> Tuple[float, float, float]: ...
	def AutoZFit(self) -> None: ...
	def AutoZFitMode(self) -> bool: ...
	def AutoZFitScaleFactor(self) -> float: ...
	@overload
	def AxialScale(self) -> Tuple[float, float, float]: ...
	@overload
	def AxialScale(self, Dx: int, Dy: int, Axis: V3d_TypeOfAxe) -> None: ...
	def BackFacingModel(self) -> V3d_TypeOfBackfacingModel: ...
	@overload
	def BackgroundColor(self, Type: Quantity_TypeOfColor) -> Tuple[float, float, float]: ...
	@overload
	def BackgroundColor(self) -> Quantity_Color: ...
	def Camera(self) -> Graphic3d_Camera: ...
	def ChangeRenderingParams(self) -> Graphic3d_RenderingParams: ...
	def ClipPlanes(self) -> Graphic3d_SequenceOfHClipPlane: ...
	def ComputedMode(self) -> bool: ...
	@overload
	def Convert(self, Vp: int) -> float: ...
	@overload
	def Convert(self, Xp: int, Yp: int) -> Tuple[float, float]: ...
	@overload
	def Convert(self, Vv: float) -> int: ...
	@overload
	def Convert(self, Xv: float, Yv: float) -> Tuple[int, int]: ...
	@overload
	def Convert(self, Xp: int, Yp: int) -> Tuple[float, float, float]: ...
	@overload
	def Convert(self, X: float, Y: float, Z: float) -> Tuple[int, int]: ...
	@overload
	def ConvertToGrid(self, Xp: int, Yp: int) -> Tuple[float, float, float]: ...
	@overload
	def ConvertToGrid(self, X: float, Y: float, Z: float) -> Tuple[float, float, float]: ...
	def ConvertWithProj(self, Xp: int, Yp: int) -> Tuple[float, float, float, float, float, float]: ...
	def DefaultCamera(self) -> Graphic3d_Camera: ...
	def Depth(self) -> float: ...
	def DepthFitAll(self, Aspect: Optional[float], Margin: Optional[float]) -> None: ...
	def DiagnosticInformation(self, theDict: TColStd_IndexedDataMapOfStringString, theFlags: Graphic3d_DiagnosticInfo) -> None: ...
	def DoMapping(self) -> None: ...
	def Dump(self, theFile: str, theBufferType: Optional[Graphic3d_BufferType]) -> bool: ...
	def Eye(self) -> Tuple[float, float, float]: ...
	@overload
	def FitAll(self, theMargin: Optional[float], theToUpdate: Optional[bool]) -> None: ...
	@overload
	def FitAll(self, theBox: Bnd_Box, theMargin: Optional[float], theToUpdate: Optional[bool]) -> None: ...
	@overload
	def FitAll(self, theMinXv: float, theMinYv: float, theMaxXv: float, theMaxYv: float) -> None: ...
	def FitMinMax(self, theCamera: Graphic3d_Camera, theBox: Bnd_Box, theMargin: float, theResolution: Optional[float], theToEnlargeIfLine: Optional[bool]) -> bool: ...
	def FocalReferencePoint(self) -> Tuple[float, float, float]: ...
	def Focale(self) -> float: ...
	def GetGraduatedTrihedron(self) -> Graphic3d_GraduatedTrihedron: ...
	def GradientBackground(self) -> Aspect_GradientBackground: ...
	def GradientBackgroundColors(self, theColor1: Quantity_Color, theColor2: Quantity_Color) -> None: ...
	def GraduatedTrihedronDisplay(self, theTrihedronData: Graphic3d_GraduatedTrihedron) -> None: ...
	def GraduatedTrihedronErase(self) -> None: ...
	def GravityPoint(self) -> gp_Pnt: ...
	def IfMoreLights(self) -> bool: ...
	def IfWindow(self) -> bool: ...
	def InitActiveLights(self) -> None: ...
	def Invalidate(self) -> None: ...
	def InvalidateImmediate(self) -> None: ...
	def IsActiveLight(self, theLight: V3d_Light) -> bool: ...
	def IsCullingEnabled(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def IsInvalidated(self) -> bool: ...
	def IsInvalidatedImmediate(self) -> bool: ...
	def LightLimit(self) -> int: ...
	def MoreActiveLights(self) -> bool: ...
	@overload
	def Move(self, Dx: float, Dy: float, Dz: float, Start: Optional[bool]) -> None: ...
	@overload
	def Move(self, Axe: V3d_TypeOfAxe, Length: float, Start: Optional[bool]) -> None: ...
	@overload
	def Move(self, Length: float, Start: Optional[bool]) -> None: ...
	def MustBeResized(self) -> None: ...
	def NextActiveLights(self) -> None: ...
	def Pan(self, theDXp: int, theDYp: int, theZoomFactor: Optional[float], theToStart: Optional[bool]) -> None: ...
	def Panning(self, theDXv: float, theDYv: float, theZoomFactor: Optional[float], theToStart: Optional[bool]) -> None: ...
	def Place(self, theXp: int, theYp: int, theZoomFactor: Optional[float]) -> None: ...
	def PlaneLimit(self) -> int: ...
	def Proj(self) -> Tuple[float, float, float]: ...
	def ProjReferenceAxe(self, Xpix: int, Ypix: int) -> Tuple[float, float, float, float, float, float]: ...
	@overload
	def Project(self, theX: float, theY: float, theZ: float) -> Tuple[float, float]: ...
	@overload
	def Project(self, theX: float, theY: float, theZ: float) -> Tuple[float, float, float]: ...
	def Redraw(self) -> None: ...
	def RedrawImmediate(self) -> None: ...
	def Remove(self) -> None: ...
	def RemoveClipPlane(self, thePlane: Graphic3d_ClipPlane) -> None: ...
	def RenderingParams(self) -> Graphic3d_RenderingParams: ...
	def Reset(self, theToUpdate: Optional[bool]) -> None: ...
	def ResetViewMapping(self) -> None: ...
	def ResetViewOrientation(self) -> None: ...
	@overload
	def Rotate(self, Ax: float, Ay: float, Az: float, Start: Optional[bool]) -> None: ...
	@overload
	def Rotate(self, Ax: float, Ay: float, Az: float, X: float, Y: float, Z: float, Start: Optional[bool]) -> None: ...
	@overload
	def Rotate(self, Axe: V3d_TypeOfAxe, Angle: float, X: float, Y: float, Z: float, Start: Optional[bool]) -> None: ...
	@overload
	def Rotate(self, Axe: V3d_TypeOfAxe, Angle: float, Start: Optional[bool]) -> None: ...
	@overload
	def Rotate(self, Angle: float, Start: Optional[bool]) -> None: ...
	def Rotation(self, X: int, Y: int) -> None: ...
	def Scale(self) -> float: ...
	def SetAt(self, X: float, Y: float, Z: float) -> None: ...
	def SetAutoZFitMode(self, theIsOn: bool, theScaleFactor: Optional[float]) -> None: ...
	def SetAxialScale(self, Sx: float, Sy: float, Sz: float) -> None: ...
	def SetAxis(self, X: float, Y: float, Z: float, Vx: float, Vy: float, Vz: float) -> None: ...
	def SetBackFacingModel(self, theModel: Optional[V3d_TypeOfBackfacingModel]) -> None: ...
	@overload
	def SetBackgroundColor(self, theType: Quantity_TypeOfColor, theV1: float, theV2: float, theV3: float) -> None: ...
	@overload
	def SetBackgroundColor(self, theColor: Quantity_Color) -> None: ...
	def SetBackgroundCubeMap(self, theCubeMap: Graphic3d_CubeMap, theToUpdate: Optional[bool]) -> None: ...
	def SetBackgroundImage(self, theFileName: str, theFillStyle: Optional[Aspect_FillMethod], theToUpdate: Optional[bool]) -> None: ...
	def SetBgGradientColors(self, theColor1: Quantity_Color, theColor2: Quantity_Color, theFillStyle: Optional[Aspect_GradientFillMethod], theToUpdate: Optional[bool]) -> None: ...
	def SetBgGradientStyle(self, theMethod: Optional[Aspect_GradientFillMethod], theToUpdate: Optional[bool]) -> None: ...
	def SetBgImageStyle(self, theFillStyle: Aspect_FillMethod, theToUpdate: Optional[bool]) -> None: ...
	def SetCamera(self, theCamera: Graphic3d_Camera) -> None: ...
	def SetCenter(self, theXp: int, theYp: int) -> None: ...
	@overload
	def SetClipPlanes(self, thePlanes: Graphic3d_SequenceOfHClipPlane) -> None: ...
	@overload
	def SetClipPlanes(self, thePlanes: Graphic3d_SequenceOfHClipPlane) -> None: ...
	def SetComputedMode(self, theMode: bool) -> None: ...
	def SetDepth(self, Depth: float) -> None: ...
	def SetEye(self, X: float, Y: float, Z: float) -> None: ...
	def SetFocale(self, Focale: float) -> None: ...
	def SetFront(self) -> None: ...
	def SetFrustumCulling(self, theMode: bool) -> None: ...
	def SetGrid(self, aPlane: gp_Ax3, aGrid: Aspect_Grid) -> None: ...
	def SetGridActivity(self, aFlag: bool) -> None: ...
	def SetImmediateUpdate(self, theImmediateUpdate: bool) -> bool: ...
	@overload
	def SetLightOff(self, theLight: V3d_Light) -> None: ...
	@overload
	def SetLightOff(self) -> None: ...
	@overload
	def SetLightOn(self, theLight: V3d_Light) -> None: ...
	@overload
	def SetLightOn(self) -> None: ...
	def SetMagnify(self, theWindow: Aspect_Window, thePreviousView: V3d_View, theX1: int, theY1: int, theX2: int, theY2: int) -> None: ...
	@overload
	def SetProj(self, Vx: float, Vy: float, Vz: float) -> None: ...
	@overload
	def SetProj(self, theOrientation: V3d_TypeOfOrientation, theIsYup: Optional[bool]) -> None: ...
	def SetScale(self, Coef: float) -> None: ...
	def SetShadingModel(self, theShadingModel: Graphic3d_TypeOfShadingModel) -> None: ...
	def SetSize(self, theSize: float) -> None: ...
	def SetTextureEnv(self, theTexture: Graphic3d_TextureEnv) -> None: ...
	def SetTwist(self, Angle: float) -> None: ...
	@overload
	def SetUp(self, Vx: float, Vy: float, Vz: float) -> None: ...
	@overload
	def SetUp(self, Orientation: V3d_TypeOfOrientation) -> None: ...
	def SetViewMappingDefault(self) -> None: ...
	def SetViewOrientationDefault(self) -> None: ...
	def SetVisualization(self, theType: V3d_TypeOfVisualization) -> None: ...
	def SetWindow(self, theWindow: Aspect_Window, theContext: Optional[Aspect_RenderingContext]) -> None: ...
	def SetZSize(self, SetZSize: float) -> None: ...
	def SetZoom(self, Coef: float, Start: Optional[bool]) -> None: ...
	def ShadingModel(self) -> Graphic3d_TypeOfShadingModel: ...
	def Size(self) -> Tuple[float, float]: ...
	def StartRotation(self, X: int, Y: int, zRotationThreshold: Optional[float]) -> None: ...
	def StartZoomAtPoint(self, theXp: int, theYp: int) -> None: ...
	@overload
	def StatisticInformation(self) -> TCollection_AsciiString: ...
	@overload
	def StatisticInformation(self, theDict: TColStd_IndexedDataMapOfStringString) -> None: ...
	def TextureEnv(self) -> Graphic3d_TextureEnv: ...
	@overload
	def ToPixMap(self, theImage: Image_PixMap, theParams: V3d_ImageDumpOptions) -> bool: ...
	@overload
	def ToPixMap(self, theImage: Image_PixMap, theWidth: int, theHeight: int, theBufferType: Optional[Graphic3d_BufferType], theToAdjustAspect: Optional[bool], theStereoOptions: Optional[V3d_StereoDumpOptions]) -> bool: ...
	@overload
	def Translate(self, Dx: float, Dy: float, Dz: float, Start: Optional[bool]) -> None: ...
	@overload
	def Translate(self, Axe: V3d_TypeOfAxe, Length: float, Start: Optional[bool]) -> None: ...
	@overload
	def Translate(self, Length: float, Start: Optional[bool]) -> None: ...
	def TriedronDisplay(self, thePosition: Optional[Aspect_TypeOfTriedronPosition], theColor: Optional[Quantity_Color], theScale: Optional[float], theMode: Optional[V3d_TypeOfVisualization]) -> None: ...
	def TriedronErase(self) -> None: ...
	@overload
	def Turn(self, Ax: float, Ay: float, Az: float, Start: Optional[bool]) -> None: ...
	@overload
	def Turn(self, Axe: V3d_TypeOfAxe, Angle: float, Start: Optional[bool]) -> None: ...
	@overload
	def Turn(self, Angle: float, Start: Optional[bool]) -> None: ...
	def Twist(self) -> float: ...
	def Type(self) -> V3d_TypeOfView: ...
	def Up(self) -> Tuple[float, float, float]: ...
	def Update(self) -> None: ...
	def UpdateLights(self) -> None: ...
	def View(self) -> Graphic3d_CView: ...
	def Viewer(self) -> V3d_Viewer: ...
	def Visualization(self) -> V3d_TypeOfVisualization: ...
	def Window(self) -> Aspect_Window: ...
	def WindowFit(self, theMinXp: int, theMinYp: int, theMaxXp: int, theMaxYp: int) -> None: ...
	def WindowFitAll(self, Xmin: int, Ymin: int, Xmax: int, Ymax: int) -> None: ...
	def ZBufferTriedronSetup(self, theXColor: Optional[Quantity_Color], theYColor: Optional[Quantity_Color], theZColor: Optional[Quantity_Color], theSizeRatio: Optional[float], theAxisDiametr: Optional[float], theNbFacettes: Optional[int]) -> None: ...
	def ZFitAll(self, theScaleFactor: Optional[float]) -> None: ...
	def ZSize(self) -> float: ...
	def Zoom(self, theXp1: int, theYp1: int, theXp2: int, theYp2: int) -> None: ...
	def ZoomAtPoint(self, theMouseStartX: int, theMouseStartY: int, theMouseEndX: int, theMouseEndY: int) -> None: ...

class V3d_Viewer(Standard_Transient):
	@overload
	def __init__(self, theDriver: Graphic3d_GraphicDriver) -> None: ...
	@overload
	def __init__(self, theDriver: Graphic3d_GraphicDriver, theName: Standard_ExtString, theDomain: Optional[str], theViewSize: Optional[float], theViewProj: Optional[V3d_TypeOfOrientation], theViewBackground: Optional[Quantity_Color], theVisualization: Optional[V3d_TypeOfVisualization], theShadingModel: Optional[Graphic3d_TypeOfShadingModel], theComputedMode: Optional[bool], theDefaultComputedMode: Optional[bool]) -> None: ...
	def ActivateGrid(self, aGridType: Aspect_GridType, aGridDrawMode: Aspect_GridDrawMode) -> None: ...
	def ActiveLight(self) -> V3d_Light: ...
	def ActiveLightIterator(self) -> V3d_ListOfLightIterator: ...
	def ActiveView(self) -> V3d_View: ...
	def ActiveViewIterator(self) -> V3d_ListOfViewIterator: ...
	def AddLight(self, theLight: V3d_Light) -> None: ...
	def AddZLayer(self, theSettings: Optional[Graphic3d_ZLayerSettings]) -> Tuple[bool, int]: ...
	def CircularGridGraphicValues(self) -> Tuple[float, float]: ...
	def CircularGridValues(self) -> Tuple[float, float, float, int, float]: ...
	def ComputedMode(self) -> bool: ...
	def CreateView(self) -> V3d_View: ...
	def DeactivateGrid(self) -> None: ...
	@overload
	def DefaultBackgroundColor(self) -> Quantity_Color: ...
	@overload
	def DefaultBackgroundColor(self, theType: Quantity_TypeOfColor) -> Tuple[float, float, float]: ...
	def DefaultBgGradientColors(self, theColor1: Quantity_Color, theColor2: Quantity_Color) -> None: ...
	def DefaultComputedMode(self) -> bool: ...
	def DefaultRenderingParams(self) -> Graphic3d_RenderingParams: ...
	def DefaultShadingModel(self) -> Graphic3d_TypeOfShadingModel: ...
	def DefaultTypeOfView(self) -> V3d_TypeOfView: ...
	def DefaultViewProj(self) -> V3d_TypeOfOrientation: ...
	def DefaultViewSize(self) -> float: ...
	def DefaultVisualization(self) -> V3d_TypeOfVisualization: ...
	def DefinedLight(self) -> V3d_Light: ...
	def DefinedLightIterator(self) -> V3d_ListOfLightIterator: ...
	def DefinedView(self) -> V3d_View: ...
	def DefinedViewIterator(self) -> V3d_ListOfViewIterator: ...
	def DelLight(self, theLight: V3d_Light) -> None: ...
	def DisplayPrivilegedPlane(self, theOnOff: bool, theSize: Optional[float]) -> None: ...
	def Driver(self) -> Graphic3d_GraphicDriver: ...
	def Erase(self) -> None: ...
	def GetAllZLayers(self, theLayerSeq: TColStd_SequenceOfInteger) -> None: ...
	def GetGradientBackground(self) -> Aspect_GradientBackground: ...
	def Grid(self) -> Aspect_Grid: ...
	def GridDrawMode(self) -> Aspect_GridDrawMode: ...
	def GridEcho(self) -> bool: ...
	def GridType(self) -> Aspect_GridType: ...
	def HideGridEcho(self, theView: V3d_View) -> None: ...
	def IfMoreViews(self) -> bool: ...
	def InitActiveLights(self) -> None: ...
	def InitActiveViews(self) -> None: ...
	def InitDefinedLights(self) -> None: ...
	def InitDefinedViews(self) -> None: ...
	def Invalidate(self) -> None: ...
	def IsActive(self) -> bool: ...
	def IsGlobalLight(self, TheLight: V3d_Light) -> bool: ...
	def LastActiveView(self) -> bool: ...
	def MoreActiveLights(self) -> bool: ...
	def MoreActiveViews(self) -> bool: ...
	def MoreDefinedLights(self) -> bool: ...
	def MoreDefinedViews(self) -> bool: ...
	def NextActiveLights(self) -> None: ...
	def NextActiveViews(self) -> None: ...
	def NextDefinedLights(self) -> None: ...
	def NextDefinedViews(self) -> None: ...
	def PrivilegedPlane(self) -> gp_Ax3: ...
	def RectangularGridGraphicValues(self) -> Tuple[float, float, float]: ...
	def RectangularGridValues(self) -> Tuple[float, float, float, float, float]: ...
	def Redraw(self) -> None: ...
	def RedrawImmediate(self) -> None: ...
	def Remove(self) -> None: ...
	def SetCircularGridGraphicValues(self, Radius: float, OffSet: float) -> None: ...
	def SetCircularGridValues(self, XOrigin: float, YOrigin: float, RadiusStep: float, DivisionNumber: int, RotationAngle: float) -> None: ...
	def SetComputedMode(self, theMode: bool) -> None: ...
	@overload
	def SetDefaultBackgroundColor(self, theColor: Quantity_Color) -> None: ...
	@overload
	def SetDefaultBackgroundColor(self, theType: Quantity_TypeOfColor, theV1: float, theV2: float, theV3: float) -> None: ...
	def SetDefaultBgGradientColors(self, theColor1: Quantity_Color, theColor2: Quantity_Color, theFillStyle: Optional[Aspect_GradientFillMethod]) -> None: ...
	def SetDefaultComputedMode(self, theMode: bool) -> None: ...
	def SetDefaultLights(self) -> None: ...
	def SetDefaultRenderingParams(self, theParams: Graphic3d_RenderingParams) -> None: ...
	def SetDefaultShadingModel(self, theType: Graphic3d_TypeOfShadingModel) -> None: ...
	def SetDefaultTypeOfView(self, theType: V3d_TypeOfView) -> None: ...
	def SetDefaultViewProj(self, theOrientation: V3d_TypeOfOrientation) -> None: ...
	def SetDefaultViewSize(self, theSize: float) -> None: ...
	def SetDefaultVisualization(self, theType: V3d_TypeOfVisualization) -> None: ...
	@overload
	def SetGridEcho(self, showGrid: Optional[bool]) -> None: ...
	@overload
	def SetGridEcho(self, aMarker: Graphic3d_AspectMarker3d) -> None: ...
	@overload
	def SetLightOff(self, theLight: V3d_Light) -> None: ...
	@overload
	def SetLightOff(self) -> None: ...
	@overload
	def SetLightOn(self, theLight: V3d_Light) -> None: ...
	@overload
	def SetLightOn(self) -> None: ...
	def SetPrivilegedPlane(self, thePlane: gp_Ax3) -> None: ...
	def SetRectangularGridGraphicValues(self, XSize: float, YSize: float, OffSet: float) -> None: ...
	def SetRectangularGridValues(self, XOrigin: float, YOrigin: float, XStep: float, YStep: float, RotationAngle: float) -> None: ...
	@overload
	def SetViewOff(self) -> None: ...
	@overload
	def SetViewOff(self, theView: V3d_View) -> None: ...
	@overload
	def SetViewOn(self) -> None: ...
	@overload
	def SetViewOn(self, theView: V3d_View) -> None: ...
	def ShowGridEcho(self, theView: V3d_View, thePoint: Graphic3d_Vertex) -> None: ...
	def StructureManager(self) -> Graphic3d_StructureManager: ...
	def UnHighlight(self) -> None: ...
	def Update(self) -> None: ...
	def UpdateLights(self) -> None: ...

class V3d_DirectionalLight(V3d_PositionLight):
	@overload
	def __init__(self, theDirection: Optional[V3d_TypeOfOrientation], theColor: Optional[Quantity_Color], theIsHeadlight: Optional[bool]) -> None: ...
	@overload
	def __init__(self, theDirection: gp_Dir, theColor: Optional[Quantity_Color], theIsHeadlight: Optional[bool]) -> None: ...
	@overload
	def __init__(self, theViewer: V3d_Viewer, theDirection: Optional[V3d_TypeOfOrientation], theColor: Optional[Quantity_Color], theIsHeadlight: Optional[bool]) -> None: ...
	@overload
	def __init__(self, theViewer: V3d_Viewer, theXt: float, theYt: float, theZt: float, theXp: float, theYp: float, theZp: float, theColor: Optional[Quantity_Color], theIsHeadlight: Optional[bool]) -> None: ...
	def SetDirection(self, theDirection: V3d_TypeOfOrientation) -> None: ...

class V3d_PositionalLight(V3d_PositionLight):
	@overload
	def __init__(self, thePos: gp_Pnt, theColor: Optional[Quantity_Color]) -> None: ...
	@overload
	def __init__(self, theViewer: V3d_Viewer, theX: float, theY: float, theZ: float, theColor: Optional[Quantity_Color], theConstAttenuation: Optional[float], theLinearAttenuation: Optional[float]) -> None: ...

class V3d_SpotLight(V3d_PositionLight):
	@overload
	def __init__(self, thePos: gp_Pnt, theDirection: Optional[V3d_TypeOfOrientation], theColor: Optional[Quantity_Color]) -> None: ...
	@overload
	def __init__(self, thePos: gp_Pnt, theDirection: gp_Dir, theColor: Optional[Quantity_Color]) -> None: ...
	@overload
	def __init__(self, theViewer: V3d_Viewer, theX: float, theY: float, theZ: float, theDirection: Optional[V3d_TypeOfOrientation], theColor: Optional[Quantity_Color], theConstAttenuation: Optional[float], theLinearAttenuation: Optional[float], theConcentration: Optional[float], theAngle: Optional[float]) -> None: ...
	@overload
	def __init__(self, theViewer: V3d_Viewer, theXt: float, theYt: float, theZt: float, theXp: float, theYp: float, theZp: float, theColor: Optional[Quantity_Color], theConstAttenuation: Optional[float], theLinearAttenuation: Optional[float], theConcentration: Optional[float], theAngle: Optional[float]) -> None: ...
	def SetDirection(self, theOrientation: V3d_TypeOfOrientation) -> None: ...
v3d_ArrowOfRadius = v3d.ArrowOfRadius
v3d_CircleInPlane = v3d.CircleInPlane
v3d_GetProjAxis = v3d.GetProjAxis
v3d_SwitchViewsinWindow = v3d.SwitchViewsinWindow
v3d_TypeOfOrientationFromString = v3d.TypeOfOrientationFromString
v3d_TypeOfOrientationFromString = v3d.TypeOfOrientationFromString
v3d_TypeOfOrientationToString = v3d.TypeOfOrientationToString
