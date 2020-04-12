from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.TColgp import *
from OCC.Core.Quantity import *
from OCC.Core.gp import *
from OCC.Core.TCollection import *


class Vrml_VertexOrdering(IntEnum):
	Vrml_UNKNOWN_ORDERING: int = ...
	Vrml_CLOCKWISE: int = ...
	Vrml_COUNTERCLOCKWISE: int = ...
Vrml_UNKNOWN_ORDERING = Vrml_VertexOrdering.Vrml_UNKNOWN_ORDERING
Vrml_CLOCKWISE = Vrml_VertexOrdering.Vrml_CLOCKWISE
Vrml_COUNTERCLOCKWISE = Vrml_VertexOrdering.Vrml_COUNTERCLOCKWISE

class Vrml_FontStyleFamily(IntEnum):
	Vrml_SERIF: int = ...
	Vrml_SANS: int = ...
	Vrml_TYPEWRITER: int = ...
Vrml_SERIF = Vrml_FontStyleFamily.Vrml_SERIF
Vrml_SANS = Vrml_FontStyleFamily.Vrml_SANS
Vrml_TYPEWRITER = Vrml_FontStyleFamily.Vrml_TYPEWRITER

class Vrml_SeparatorRenderCulling(IntEnum):
	Vrml_OFF: int = ...
	Vrml_ON: int = ...
	Vrml_AUTO: int = ...
Vrml_OFF = Vrml_SeparatorRenderCulling.Vrml_OFF
Vrml_ON = Vrml_SeparatorRenderCulling.Vrml_ON
Vrml_AUTO = Vrml_SeparatorRenderCulling.Vrml_AUTO

class Vrml_Texture2Wrap(IntEnum):
	Vrml_REPEAT: int = ...
	Vrml_CLAMP: int = ...
Vrml_REPEAT = Vrml_Texture2Wrap.Vrml_REPEAT
Vrml_CLAMP = Vrml_Texture2Wrap.Vrml_CLAMP

class Vrml_FaceType(IntEnum):
	Vrml_UNKNOWN_FACE_TYPE: int = ...
	Vrml_CONVEX: int = ...
Vrml_UNKNOWN_FACE_TYPE = Vrml_FaceType.Vrml_UNKNOWN_FACE_TYPE
Vrml_CONVEX = Vrml_FaceType.Vrml_CONVEX

class Vrml_AsciiTextJustification(IntEnum):
	Vrml_LEFT: int = ...
	Vrml_CENTER: int = ...
	Vrml_RIGHT: int = ...
Vrml_LEFT = Vrml_AsciiTextJustification.Vrml_LEFT
Vrml_CENTER = Vrml_AsciiTextJustification.Vrml_CENTER
Vrml_RIGHT = Vrml_AsciiTextJustification.Vrml_RIGHT

class Vrml_ConeParts(IntEnum):
	Vrml_ConeSIDES: int = ...
	Vrml_ConeBOTTOM: int = ...
	Vrml_ConeALL: int = ...
Vrml_ConeSIDES = Vrml_ConeParts.Vrml_ConeSIDES
Vrml_ConeBOTTOM = Vrml_ConeParts.Vrml_ConeBOTTOM
Vrml_ConeALL = Vrml_ConeParts.Vrml_ConeALL

class Vrml_SFImageNumber(IntEnum):
	Vrml_NULL: int = ...
	Vrml_ONE: int = ...
	Vrml_TWO: int = ...
	Vrml_THREE: int = ...
	Vrml_FOUR: int = ...
Vrml_NULL = Vrml_SFImageNumber.Vrml_NULL
Vrml_ONE = Vrml_SFImageNumber.Vrml_ONE
Vrml_TWO = Vrml_SFImageNumber.Vrml_TWO
Vrml_THREE = Vrml_SFImageNumber.Vrml_THREE
Vrml_FOUR = Vrml_SFImageNumber.Vrml_FOUR

class Vrml_MaterialBindingAndNormalBinding(IntEnum):
	Vrml_DEFAULT: int = ...
	Vrml_OVERALL: int = ...
	Vrml_PER_PART: int = ...
	Vrml_PER_PART_INDEXED: int = ...
	Vrml_PER_FACE: int = ...
	Vrml_PER_FACE_INDEXED: int = ...
	Vrml_PER_VERTEX: int = ...
	Vrml_PER_VERTEX_INDEXED: int = ...
Vrml_DEFAULT = Vrml_MaterialBindingAndNormalBinding.Vrml_DEFAULT
Vrml_OVERALL = Vrml_MaterialBindingAndNormalBinding.Vrml_OVERALL
Vrml_PER_PART = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_PART
Vrml_PER_PART_INDEXED = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_PART_INDEXED
Vrml_PER_FACE = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_FACE
Vrml_PER_FACE_INDEXED = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_FACE_INDEXED
Vrml_PER_VERTEX = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_VERTEX
Vrml_PER_VERTEX_INDEXED = Vrml_MaterialBindingAndNormalBinding.Vrml_PER_VERTEX_INDEXED

class Vrml_ShapeType(IntEnum):
	Vrml_UNKNOWN_SHAPE_TYPE: int = ...
	Vrml_SOLID: int = ...
Vrml_UNKNOWN_SHAPE_TYPE = Vrml_ShapeType.Vrml_UNKNOWN_SHAPE_TYPE
Vrml_SOLID = Vrml_ShapeType.Vrml_SOLID

class Vrml_WWWAnchorMap(IntEnum):
	Vrml_MAP_NONE: int = ...
	Vrml_POINT: int = ...
Vrml_MAP_NONE = Vrml_WWWAnchorMap.Vrml_MAP_NONE
Vrml_POINT = Vrml_WWWAnchorMap.Vrml_POINT

class Vrml_CylinderParts(IntEnum):
	Vrml_CylinderSIDES: int = ...
	Vrml_CylinderTOP: int = ...
	Vrml_CylinderBOTTOM: int = ...
	Vrml_CylinderALL: int = ...
Vrml_CylinderSIDES = Vrml_CylinderParts.Vrml_CylinderSIDES
Vrml_CylinderTOP = Vrml_CylinderParts.Vrml_CylinderTOP
Vrml_CylinderBOTTOM = Vrml_CylinderParts.Vrml_CylinderBOTTOM
Vrml_CylinderALL = Vrml_CylinderParts.Vrml_CylinderALL

class Vrml_FontStyleStyle(IntEnum):
	Vrml_NONE: int = ...
	Vrml_BOLD: int = ...
	Vrml_ITALIC: int = ...
Vrml_NONE = Vrml_FontStyleStyle.Vrml_NONE
Vrml_BOLD = Vrml_FontStyleStyle.Vrml_BOLD
Vrml_ITALIC = Vrml_FontStyleStyle.Vrml_ITALIC

class Vrml:
	pass

class Vrml_AsciiText(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aString: TColStd_HArray1OfAsciiString, aSpacing: float, aJustification: Vrml_AsciiTextJustification, aWidth: float) -> None: ...
	def Justification(self) -> Vrml_AsciiTextJustification: ...
	def SetJustification(self, aJustification: Vrml_AsciiTextJustification) -> None: ...
	def SetSpacing(self, aSpacing: float) -> None: ...
	def SetString(self, aString: TColStd_HArray1OfAsciiString) -> None: ...
	def SetWidth(self, aWidth: float) -> None: ...
	def Spacing(self) -> float: ...
	def String(self) -> TColStd_HArray1OfAsciiString: ...
	def Width(self) -> float: ...

class Vrml_Cone:
	def __init__(self, aParts: Optional[Vrml_ConeParts], aBottomRadius: Optional[float], aHeight: Optional[float]) -> None: ...
	def BottomRadius(self) -> float: ...
	def Height(self) -> float: ...
	def Parts(self) -> Vrml_ConeParts: ...
	def SetBottomRadius(self, aBottomRadius: float) -> None: ...
	def SetHeight(self, aHeight: float) -> None: ...
	def SetParts(self, aParts: Vrml_ConeParts) -> None: ...

class Vrml_Coordinate3(Standard_Transient):
	@overload
	def __init__(self, aPoint: TColgp_HArray1OfVec) -> None: ...
	@overload
	def __init__(self) -> None: ...
	def Point(self) -> TColgp_HArray1OfVec: ...
	def SetPoint(self, aPoint: TColgp_HArray1OfVec) -> None: ...

class Vrml_Cube:
	def __init__(self, aWidth: Optional[float], aHeight: Optional[float], aDepth: Optional[float]) -> None: ...
	def Depth(self) -> float: ...
	def Height(self) -> float: ...
	def SetDepth(self, aDepth: float) -> None: ...
	def SetHeight(self, aHeight: float) -> None: ...
	def SetWidth(self, aWidth: float) -> None: ...
	def Width(self) -> float: ...

class Vrml_Cylinder:
	def __init__(self, aParts: Optional[Vrml_CylinderParts], aRadius: Optional[float], aHeight: Optional[float]) -> None: ...
	def Height(self) -> float: ...
	def Parts(self) -> Vrml_CylinderParts: ...
	def Radius(self) -> float: ...
	def SetHeight(self, aHeight: float) -> None: ...
	def SetParts(self, aParts: Vrml_CylinderParts) -> None: ...
	def SetRadius(self, aRadius: float) -> None: ...

class Vrml_DirectionalLight:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aOnOff: bool, aIntensity: float, aColor: Quantity_Color, aDirection: gp_Vec) -> None: ...
	def Color(self) -> Quantity_Color: ...
	def Direction(self) -> gp_Vec: ...
	def Intensity(self) -> float: ...
	def OnOff(self) -> bool: ...
	def SetColor(self, aColor: Quantity_Color) -> None: ...
	def SetDirection(self, aDirection: gp_Vec) -> None: ...
	def SetIntensity(self, aIntensity: float) -> None: ...
	def SetOnOff(self, aOnOff: bool) -> None: ...

class Vrml_FontStyle:
	def __init__(self, aSize: Optional[float], aFamily: Optional[Vrml_FontStyleFamily], aStyle: Optional[Vrml_FontStyleStyle]) -> None: ...
	def Family(self) -> Vrml_FontStyleFamily: ...
	def SetFamily(self, aFamily: Vrml_FontStyleFamily) -> None: ...
	def SetSize(self, aSize: float) -> None: ...
	def SetStyle(self, aStyle: Vrml_FontStyleStyle) -> None: ...
	def Size(self) -> float: ...
	def Style(self) -> Vrml_FontStyleStyle: ...

class Vrml_Group:
	def __init__(self) -> None: ...

class Vrml_IndexedFaceSet(Standard_Transient):
	@overload
	def __init__(self, aCoordIndex: TColStd_HArray1OfInteger, aMaterialIndex: TColStd_HArray1OfInteger, aNormalIndex: TColStd_HArray1OfInteger, aTextureCoordIndex: TColStd_HArray1OfInteger) -> None: ...
	@overload
	def __init__(self) -> None: ...
	def CoordIndex(self) -> TColStd_HArray1OfInteger: ...
	def MaterialIndex(self) -> TColStd_HArray1OfInteger: ...
	def NormalIndex(self) -> TColStd_HArray1OfInteger: ...
	def SetCoordIndex(self, aCoordIndex: TColStd_HArray1OfInteger) -> None: ...
	def SetMaterialIndex(self, aMaterialIndex: TColStd_HArray1OfInteger) -> None: ...
	def SetNormalIndex(self, aNormalIndex: TColStd_HArray1OfInteger) -> None: ...
	def SetTextureCoordIndex(self, aTextureCoordIndex: TColStd_HArray1OfInteger) -> None: ...
	def TextureCoordIndex(self) -> TColStd_HArray1OfInteger: ...

class Vrml_IndexedLineSet(Standard_Transient):
	@overload
	def __init__(self, aCoordIndex: TColStd_HArray1OfInteger, aMaterialIndex: TColStd_HArray1OfInteger, aNormalIndex: TColStd_HArray1OfInteger, aTextureCoordIndex: TColStd_HArray1OfInteger) -> None: ...
	@overload
	def __init__(self) -> None: ...
	def CoordIndex(self) -> TColStd_HArray1OfInteger: ...
	def MaterialIndex(self) -> TColStd_HArray1OfInteger: ...
	def NormalIndex(self) -> TColStd_HArray1OfInteger: ...
	def SetCoordIndex(self, aCoordIndex: TColStd_HArray1OfInteger) -> None: ...
	def SetMaterialIndex(self, aMaterialIndex: TColStd_HArray1OfInteger) -> None: ...
	def SetNormalIndex(self, aNormalIndex: TColStd_HArray1OfInteger) -> None: ...
	def SetTextureCoordIndex(self, aTextureCoordIndex: TColStd_HArray1OfInteger) -> None: ...
	def TextureCoordIndex(self) -> TColStd_HArray1OfInteger: ...

class Vrml_Info:
	def __init__(self, aString: Optional[TCollection_AsciiString]) -> None: ...
	def SetString(self, aString: TCollection_AsciiString) -> None: ...
	def String(self) -> TCollection_AsciiString: ...

class Vrml_Instancing:
	def __init__(self, aString: TCollection_AsciiString) -> None: ...

class Vrml_LOD(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aRange: TColStd_HArray1OfReal, aCenter: gp_Vec) -> None: ...
	def Center(self) -> gp_Vec: ...
	def Range(self) -> TColStd_HArray1OfReal: ...
	def SetCenter(self, aCenter: gp_Vec) -> None: ...
	def SetRange(self, aRange: TColStd_HArray1OfReal) -> None: ...

class Vrml_Material(Standard_Transient):
	@overload
	def __init__(self, aAmbientColor: Quantity_HArray1OfColor, aDiffuseColor: Quantity_HArray1OfColor, aSpecularColor: Quantity_HArray1OfColor, aEmissiveColor: Quantity_HArray1OfColor, aShininess: TColStd_HArray1OfReal, aTransparency: TColStd_HArray1OfReal) -> None: ...
	@overload
	def __init__(self) -> None: ...
	def AmbientColor(self) -> Quantity_HArray1OfColor: ...
	def DiffuseColor(self) -> Quantity_HArray1OfColor: ...
	def EmissiveColor(self) -> Quantity_HArray1OfColor: ...
	def SetAmbientColor(self, aAmbientColor: Quantity_HArray1OfColor) -> None: ...
	def SetDiffuseColor(self, aDiffuseColor: Quantity_HArray1OfColor) -> None: ...
	def SetEmissiveColor(self, aEmissiveColor: Quantity_HArray1OfColor) -> None: ...
	def SetShininess(self, aShininess: TColStd_HArray1OfReal) -> None: ...
	def SetSpecularColor(self, aSpecularColor: Quantity_HArray1OfColor) -> None: ...
	def SetTransparency(self, aTransparency: TColStd_HArray1OfReal) -> None: ...
	def Shininess(self) -> TColStd_HArray1OfReal: ...
	def SpecularColor(self) -> Quantity_HArray1OfColor: ...
	def Transparency(self) -> TColStd_HArray1OfReal: ...

class Vrml_MaterialBinding:
	@overload
	def __init__(self, aValue: Vrml_MaterialBindingAndNormalBinding) -> None: ...
	@overload
	def __init__(self) -> None: ...
	def SetValue(self, aValue: Vrml_MaterialBindingAndNormalBinding) -> None: ...
	def Value(self) -> Vrml_MaterialBindingAndNormalBinding: ...

class Vrml_MatrixTransform:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aMatrix: gp_Trsf) -> None: ...
	def Matrix(self) -> gp_Trsf: ...
	def SetMatrix(self, aMatrix: gp_Trsf) -> None: ...

class Vrml_Normal(Standard_Transient):
	@overload
	def __init__(self, aVector: TColgp_HArray1OfVec) -> None: ...
	@overload
	def __init__(self) -> None: ...
	def SetVector(self, aVector: TColgp_HArray1OfVec) -> None: ...
	def Vector(self) -> TColgp_HArray1OfVec: ...

class Vrml_NormalBinding:
	@overload
	def __init__(self, aValue: Vrml_MaterialBindingAndNormalBinding) -> None: ...
	@overload
	def __init__(self) -> None: ...
	def SetValue(self, aValue: Vrml_MaterialBindingAndNormalBinding) -> None: ...
	def Value(self) -> Vrml_MaterialBindingAndNormalBinding: ...

class Vrml_OrthographicCamera:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aPosition: gp_Vec, aOrientation: Vrml_SFRotation, aFocalDistance: float, aHeight: float) -> None: ...
	def FocalDistance(self) -> float: ...
	def Height(self) -> float: ...
	def Orientation(self) -> Vrml_SFRotation: ...
	def Position(self) -> gp_Vec: ...
	def SetFocalDistance(self, aFocalDistance: float) -> None: ...
	def SetHeight(self, aHeight: float) -> None: ...
	def SetOrientation(self, aOrientation: Vrml_SFRotation) -> None: ...
	def SetPosition(self, aPosition: gp_Vec) -> None: ...

class Vrml_PerspectiveCamera:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aPosition: gp_Vec, aOrientation: Vrml_SFRotation, aFocalDistance: float, aHeightAngle: float) -> None: ...
	def Angle(self) -> float: ...
	def FocalDistance(self) -> float: ...
	def Orientation(self) -> Vrml_SFRotation: ...
	def Position(self) -> gp_Vec: ...
	def SetAngle(self, aHeightAngle: float) -> None: ...
	def SetFocalDistance(self, aFocalDistance: float) -> None: ...
	def SetOrientation(self, aOrientation: Vrml_SFRotation) -> None: ...
	def SetPosition(self, aPosition: gp_Vec) -> None: ...

class Vrml_PointLight:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aOnOff: bool, aIntensity: float, aColor: Quantity_Color, aLocation: gp_Vec) -> None: ...
	def Color(self) -> Quantity_Color: ...
	def Intensity(self) -> float: ...
	def Location(self) -> gp_Vec: ...
	def OnOff(self) -> bool: ...
	def SetColor(self, aColor: Quantity_Color) -> None: ...
	def SetIntensity(self, aIntensity: float) -> None: ...
	def SetLocation(self, aLocation: gp_Vec) -> None: ...
	def SetOnOff(self, aOnOff: bool) -> None: ...

class Vrml_PointSet:
	def __init__(self, aStartIndex: Optional[int], aNumPoints: Optional[int]) -> None: ...
	def NumPoints(self) -> int: ...
	def SetNumPoints(self, aNumPoints: int) -> None: ...
	def SetStartIndex(self, aStartIndex: int) -> None: ...
	def StartIndex(self) -> int: ...

class Vrml_Rotation:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aRotation: Vrml_SFRotation) -> None: ...
	def Rotation(self) -> Vrml_SFRotation: ...
	def SetRotation(self, aRotation: Vrml_SFRotation) -> None: ...

class Vrml_SFImage(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aWidth: int, aHeight: int, aNumber: Vrml_SFImageNumber, anArray: TColStd_HArray1OfInteger) -> None: ...
	def Array(self) -> TColStd_HArray1OfInteger: ...
	def ArrayFlag(self) -> bool: ...
	def Height(self) -> int: ...
	def Number(self) -> Vrml_SFImageNumber: ...
	def SetArray(self, anArray: TColStd_HArray1OfInteger) -> None: ...
	def SetHeight(self, aHeight: int) -> None: ...
	def SetNumber(self, aNumber: Vrml_SFImageNumber) -> None: ...
	def SetWidth(self, aWidth: int) -> None: ...
	def Width(self) -> int: ...

class Vrml_SFRotation:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aRotationX: float, aRotationY: float, aRotationZ: float, anAngle: float) -> None: ...
	def Angle(self) -> float: ...
	def RotationX(self) -> float: ...
	def RotationY(self) -> float: ...
	def RotationZ(self) -> float: ...
	def SetAngle(self, anAngle: float) -> None: ...
	def SetRotationX(self, aRotationX: float) -> None: ...
	def SetRotationY(self, aRotationY: float) -> None: ...
	def SetRotationZ(self, aRotationZ: float) -> None: ...

class Vrml_Scale:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aScaleFactor: gp_Vec) -> None: ...
	def ScaleFactor(self) -> gp_Vec: ...
	def SetScaleFactor(self, aScaleFactor: gp_Vec) -> None: ...

class Vrml_Separator:
	@overload
	def __init__(self, aRenderCulling: Vrml_SeparatorRenderCulling) -> None: ...
	@overload
	def __init__(self) -> None: ...
	def RenderCulling(self) -> Vrml_SeparatorRenderCulling: ...
	def SetRenderCulling(self, aRenderCulling: Vrml_SeparatorRenderCulling) -> None: ...

class Vrml_ShapeHints:
	def __init__(self, aVertexOrdering: Optional[Vrml_VertexOrdering], aShapeType: Optional[Vrml_ShapeType], aFaceType: Optional[Vrml_FaceType], aAngle: Optional[float]) -> None: ...
	def Angle(self) -> float: ...
	def FaceType(self) -> Vrml_FaceType: ...
	def SetAngle(self, aAngle: float) -> None: ...
	def SetFaceType(self, aFaceType: Vrml_FaceType) -> None: ...
	def SetShapeType(self, aShapeType: Vrml_ShapeType) -> None: ...
	def SetVertexOrdering(self, aVertexOrdering: Vrml_VertexOrdering) -> None: ...
	def ShapeType(self) -> Vrml_ShapeType: ...
	def VertexOrdering(self) -> Vrml_VertexOrdering: ...

class Vrml_Sphere:
	def __init__(self, aRadius: Optional[float]) -> None: ...
	def Radius(self) -> float: ...
	def SetRadius(self, aRadius: float) -> None: ...

class Vrml_SpotLight:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aOnOff: bool, aIntensity: float, aColor: Quantity_Color, aLocation: gp_Vec, aDirection: gp_Vec, aDropOffRate: float, aCutOffAngle: float) -> None: ...
	def Color(self) -> Quantity_Color: ...
	def CutOffAngle(self) -> float: ...
	def Direction(self) -> gp_Vec: ...
	def DropOffRate(self) -> float: ...
	def Intensity(self) -> float: ...
	def Location(self) -> gp_Vec: ...
	def OnOff(self) -> bool: ...
	def SetColor(self, aColor: Quantity_Color) -> None: ...
	def SetCutOffAngle(self, aCutOffAngle: float) -> None: ...
	def SetDirection(self, aDirection: gp_Vec) -> None: ...
	def SetDropOffRate(self, aDropOffRate: float) -> None: ...
	def SetIntensity(self, aIntensity: float) -> None: ...
	def SetLocation(self, aLocation: gp_Vec) -> None: ...
	def SetOnOff(self, anOnOff: bool) -> None: ...

class Vrml_Switch:
	def __init__(self, aWhichChild: Optional[int]) -> None: ...
	def SetWhichChild(self, aWhichChild: int) -> None: ...
	def WhichChild(self) -> int: ...

class Vrml_Texture2:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aFilename: TCollection_AsciiString, aImage: Vrml_SFImage, aWrapS: Vrml_Texture2Wrap, aWrapT: Vrml_Texture2Wrap) -> None: ...
	def Filename(self) -> TCollection_AsciiString: ...
	def Image(self) -> Vrml_SFImage: ...
	def SetFilename(self, aFilename: TCollection_AsciiString) -> None: ...
	def SetImage(self, aImage: Vrml_SFImage) -> None: ...
	def SetWrapS(self, aWrapS: Vrml_Texture2Wrap) -> None: ...
	def SetWrapT(self, aWrapT: Vrml_Texture2Wrap) -> None: ...
	def WrapS(self) -> Vrml_Texture2Wrap: ...
	def WrapT(self) -> Vrml_Texture2Wrap: ...

class Vrml_Texture2Transform:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aTranslation: gp_Vec2d, aRotation: float, aScaleFactor: gp_Vec2d, aCenter: gp_Vec2d) -> None: ...
	def Center(self) -> gp_Vec2d: ...
	def Rotation(self) -> float: ...
	def ScaleFactor(self) -> gp_Vec2d: ...
	def SetCenter(self, aCenter: gp_Vec2d) -> None: ...
	def SetRotation(self, aRotation: float) -> None: ...
	def SetScaleFactor(self, aScaleFactor: gp_Vec2d) -> None: ...
	def SetTranslation(self, aTranslation: gp_Vec2d) -> None: ...
	def Translation(self) -> gp_Vec2d: ...

class Vrml_TextureCoordinate2(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aPoint: TColgp_HArray1OfVec2d) -> None: ...
	def Point(self) -> TColgp_HArray1OfVec2d: ...
	def SetPoint(self, aPoint: TColgp_HArray1OfVec2d) -> None: ...

class Vrml_Transform:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aTranslation: gp_Vec, aRotation: Vrml_SFRotation, aScaleFactor: gp_Vec, aScaleOrientation: Vrml_SFRotation, aCenter: gp_Vec) -> None: ...
	def Center(self) -> gp_Vec: ...
	def Rotation(self) -> Vrml_SFRotation: ...
	def ScaleFactor(self) -> gp_Vec: ...
	def ScaleOrientation(self) -> Vrml_SFRotation: ...
	def SetCenter(self, aCenter: gp_Vec) -> None: ...
	def SetRotation(self, aRotation: Vrml_SFRotation) -> None: ...
	def SetScaleFactor(self, aScaleFactor: gp_Vec) -> None: ...
	def SetScaleOrientation(self, aScaleOrientation: Vrml_SFRotation) -> None: ...
	def SetTranslation(self, aTranslation: gp_Vec) -> None: ...
	def Translation(self) -> gp_Vec: ...

class Vrml_TransformSeparator:
	def __init__(self) -> None: ...

class Vrml_Translation:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aTranslation: gp_Vec) -> None: ...
	def SetTranslation(self, aTranslation: gp_Vec) -> None: ...
	def Translation(self) -> gp_Vec: ...

class Vrml_WWWAnchor:
	def __init__(self, aName: Optional[TCollection_AsciiString], aDescription: Optional[TCollection_AsciiString], aMap: Optional[Vrml_WWWAnchorMap]) -> None: ...
	def Description(self) -> TCollection_AsciiString: ...
	def Map(self) -> Vrml_WWWAnchorMap: ...
	def Name(self) -> TCollection_AsciiString: ...
	def SetDescription(self, aDescription: TCollection_AsciiString) -> None: ...
	def SetMap(self, aMap: Vrml_WWWAnchorMap) -> None: ...
	def SetName(self, aName: TCollection_AsciiString) -> None: ...

class Vrml_WWWInline:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aName: TCollection_AsciiString, aBboxSize: gp_Vec, aBboxCenter: gp_Vec) -> None: ...
	def BboxCenter(self) -> gp_Vec: ...
	def BboxSize(self) -> gp_Vec: ...
	def Name(self) -> TCollection_AsciiString: ...
	def SetBboxCenter(self, aBboxCenter: gp_Vec) -> None: ...
	def SetBboxSize(self, aBboxSize: gp_Vec) -> None: ...
	def SetName(self, aName: TCollection_AsciiString) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

vrml_CommentWriter = vrml.CommentWriter
