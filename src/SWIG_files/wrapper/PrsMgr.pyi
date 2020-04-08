from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Prs3d import *
from OCC.Core.Graphic3d import *
from OCC.Core.Bnd import *
from OCC.Core.Quantity import *
from OCC.Core.Geom import *
from OCC.Core.Aspect import *
from OCC.Core.gp import *
from OCC.Core.TColStd import *
from OCC.Core.V3d import *

Handle_PrsMgr_Presentation3d = NewType('Handle_PrsMgr_Presentation3d', Handle_PrsMgr_Presentation)
Handle_PrsMgr_PresentationManager3d = NewType('Handle_PrsMgr_PresentationManager3d', Handle_PrsMgr_PresentationManager)
Prs3d_Presentation = NewType('Prs3d_Presentation', Graphic3d_Structure)
#the following typedef cannot be wrapped as is
PrsMgr_ListOfPresentableObjects = NewType('PrsMgr_ListOfPresentableObjects', Any)
#the following typedef cannot be wrapped as is
PrsMgr_ListOfPresentableObjectsIter = NewType('PrsMgr_ListOfPresentableObjectsIter', Any)
#the following typedef cannot be wrapped as is
PrsMgr_ListOfPresentations = NewType('PrsMgr_ListOfPresentations', Any)
PrsMgr_Presentation3d = NewType('PrsMgr_Presentation3d', PrsMgr_Presentation)
PrsMgr_PresentationManager3d = NewType('PrsMgr_PresentationManager3d', PrsMgr_PresentationManager)
#the following typedef cannot be wrapped as is
PrsMgr_Presentations = NewType('PrsMgr_Presentations', Any)

class PrsMgr_TypeOfPresentation3d(IntEnum):
	PrsMgr_TOP_AllView: int = ...
	PrsMgr_TOP_ProjectorDependant: int = ...
PrsMgr_TOP_AllView = PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_AllView
PrsMgr_TOP_ProjectorDependant = PrsMgr_TypeOfPresentation3d.PrsMgr_TOP_ProjectorDependant

class PrsMgr_PresentableObject(Standard_Transient):
	def AcceptDisplayMode(self, theMode: int) -> bool: ...
	def AddChild(self, theObject: PrsMgr_PresentableObject) -> None: ...
	def AddChildWithCurrentTransformation(self, theObject: PrsMgr_PresentableObject) -> None: ...
	def AddClipPlane(self, thePlane: Graphic3d_ClipPlane) -> None: ...
	def Attributes(self) -> Prs3d_Drawer: ...
	def BoundingBox(self, theBndBox: Bnd_Box) -> None: ...
	def Children(self) -> PrsMgr_ListOfPresentableObjects: ...
	def ClipPlanes(self) -> Graphic3d_SequenceOfHClipPlane: ...
	def Color(self, theColor: Quantity_Color) -> None: ...
	def CombinedParentTransformation(self) -> Geom_Transformation: ...
	def CurrentFacingModel(self) -> Aspect_TypeOfFacingModel: ...
	def DefaultDisplayMode(self) -> int: ...
	def DisplayMode(self) -> int: ...
	def DynamicHilightAttributes(self) -> Prs3d_Drawer: ...
	def GetTransformPersistenceMode(self) -> Graphic3d_TransModeFlags: ...
	def GetTransformPersistencePoint(self) -> gp_Pnt: ...
	def HasColor(self) -> bool: ...
	def HasDisplayMode(self) -> bool: ...
	def HasHilightMode(self) -> bool: ...
	def HasMaterial(self) -> bool: ...
	def HasOwnPresentations(self) -> bool: ...
	def HasPolygonOffsets(self) -> bool: ...
	def HasTransformation(self) -> bool: ...
	def HasWidth(self) -> bool: ...
	def HilightAttributes(self) -> Prs3d_Drawer: ...
	def HilightMode(self) -> int: ...
	def InversedTransformation(self) -> gp_GTrsf: ...
	def IsInfinite(self) -> bool: ...
	def IsMutable(self) -> bool: ...
	def IsTransparent(self) -> bool: ...
	def LocalTransformation(self) -> gp_Trsf: ...
	def LocalTransformationGeom(self) -> Geom_Transformation: ...
	def Material(self) -> Graphic3d_NameOfMaterial: ...
	def Parent(self) -> PrsMgr_PresentableObject: ...
	def PolygonOffsets(self, aFactor: Standard_ShortReal, aUnits: Standard_ShortReal) -> int: ...
	def Presentations(self) -> PrsMgr_Presentations: ...
	def RemoveChild(self, theObject: PrsMgr_PresentableObject) -> None: ...
	def RemoveChildWithRestoreTransformation(self, theObject: PrsMgr_PresentableObject) -> None: ...
	def RemoveClipPlane(self, thePlane: Graphic3d_ClipPlane) -> None: ...
	def ResetTransformation(self) -> None: ...
	def SetAttributes(self, theDrawer: Prs3d_Drawer) -> None: ...
	@overload
	def SetClipPlanes(self, thePlanes: Graphic3d_SequenceOfHClipPlane) -> None: ...
	@overload
	def SetClipPlanes(self, thePlanes: Graphic3d_SequenceOfHClipPlane) -> None: ...
	def SetColor(self, theColor: Quantity_Color) -> None: ...
	def SetCurrentFacingModel(self, theModel: Optional[Aspect_TypeOfFacingModel]) -> None: ...
	def SetDisplayMode(self, theMode: int) -> None: ...
	def SetDynamicHilightAttributes(self, theDrawer: Prs3d_Drawer) -> None: ...
	def SetHilightAttributes(self, theDrawer: Prs3d_Drawer) -> None: ...
	def SetHilightMode(self, theMode: int) -> None: ...
	def SetInfiniteState(self, theFlag: Optional[bool]) -> None: ...
	def SetIsoOnTriangulation(self, theIsEnabled: bool) -> None: ...
	@overload
	def SetLocalTransformation(self, theTrsf: gp_Trsf) -> None: ...
	@overload
	def SetLocalTransformation(self, theTrsf: Geom_Transformation) -> None: ...
	def SetMaterial(self, aName: Graphic3d_MaterialAspect) -> None: ...
	def SetMutable(self, theIsMutable: bool) -> None: ...
	def SetPolygonOffsets(self, aMode: int, aFactor: Optional[Standard_ShortReal], aUnits: Optional[Standard_ShortReal]) -> None: ...
	def SetPropagateVisualState(self, theFlag: bool) -> None: ...
	@overload
	def SetToUpdate(self, theMode: int) -> None: ...
	@overload
	def SetToUpdate(self) -> None: ...
	@overload
	def SetTransformPersistence(self, theTrsfPers: Graphic3d_TransformPers) -> None: ...
	@overload
	def SetTransformPersistence(self, theMode: Graphic3d_TransModeFlags, thePoint: Optional[gp_Pnt]) -> None: ...
	def SetTransparency(self, aValue: Optional[float]) -> None: ...
	def SetTypeOfPresentation(self, theType: PrsMgr_TypeOfPresentation3d) -> None: ...
	def SetWidth(self, theWidth: float) -> None: ...
	def SynchronizeAspects(self) -> None: ...
	@overload
	def ToBeUpdated(self, theToIncludeHidden: Optional[bool]) -> bool: ...
	@overload
	def ToBeUpdated(self, ListOfMode: TColStd_ListOfInteger) -> None: ...
	def ToPropagateVisualState(self) -> bool: ...
	def TransformPersistence(self) -> Graphic3d_TransformPers: ...
	def Transformation(self) -> gp_Trsf: ...
	def TransformationGeom(self) -> Geom_Transformation: ...
	def Transparency(self) -> float: ...
	def TypeOfPresentation3d(self) -> PrsMgr_TypeOfPresentation3d: ...
	def UnsetAttributes(self) -> None: ...
	def UnsetColor(self) -> None: ...
	def UnsetDisplayMode(self) -> None: ...
	def UnsetHilightAttributes(self) -> None: ...
	def UnsetHilightMode(self) -> None: ...
	def UnsetMaterial(self) -> None: ...
	def UnsetTransparency(self) -> None: ...
	def UnsetWidth(self) -> None: ...
	def UpdateTransformation(self) -> None: ...
	def Width(self) -> float: ...
	def ZLayer(self) -> Graphic3d_ZLayerId: ...

class PrsMgr_Presentation(Graphic3d_Structure):
	def Clear(self, theWithDestruction: Optional[bool]) -> None: ...
	def Compute(self) -> None: ...
	def Display(self) -> None: ...
	def Erase(self) -> None: ...
	def Highlight(self, theStyle: Prs3d_Drawer) -> None: ...
	def IsDisplayed(self) -> bool: ...
	def Mode(self) -> int: ...
	def MustBeUpdated(self) -> bool: ...
	def Presentation(self) -> Prs3d_Presentation: ...
	def PresentationManager(self) -> PrsMgr_PresentationManager: ...
	def SetUpdateStatus(self, theUpdateStatus: bool) -> None: ...
	def Unhighlight(self) -> None: ...

class PrsMgr_PresentationManager(Standard_Transient):
	def __init__(self, theStructureManager: Graphic3d_StructureManager) -> None: ...
	def AddToImmediateList(self, thePrs: Prs3d_Presentation) -> None: ...
	def BeginImmediateDraw(self) -> None: ...
	def Clear(self, thePrsObject: PrsMgr_PresentableObject, theMode: Optional[int]) -> None: ...
	def ClearImmediateDraw(self) -> None: ...
	def Connect(self, thePrsObject: PrsMgr_PresentableObject, theOtherObject: PrsMgr_PresentableObject, theMode: Optional[int], theOtherMode: Optional[int]) -> None: ...
	def Display(self, thePrsObject: PrsMgr_PresentableObject, theMode: Optional[int]) -> None: ...
	def DisplayPriority(self, thePrsObject: PrsMgr_PresentableObject, theMode: int) -> int: ...
	def EndImmediateDraw(self, theViewer: V3d_Viewer) -> None: ...
	def Erase(self, thePrsObject: PrsMgr_PresentableObject, theMode: Optional[int]) -> None: ...
	def GetZLayer(self, thePrsObject: PrsMgr_PresentableObject) -> Graphic3d_ZLayerId: ...
	def HasPresentation(self, thePrsObject: PrsMgr_PresentableObject, theMode: Optional[int]) -> bool: ...
	def IsDisplayed(self, thePrsObject: PrsMgr_PresentableObject, theMode: Optional[int]) -> bool: ...
	def IsHighlighted(self, thePrsObject: PrsMgr_PresentableObject, theMode: Optional[int]) -> bool: ...
	def IsImmediateModeOn(self) -> bool: ...
	def Presentation(self, thePrsObject: PrsMgr_PresentableObject, theMode: Optional[int], theToCreate: Optional[bool], theSelObj: Optional[PrsMgr_PresentableObject]) -> PrsMgr_Presentation: ...
	def RedrawImmediate(self, theViewer: V3d_Viewer) -> None: ...
	def SetDisplayPriority(self, thePrsObject: PrsMgr_PresentableObject, theMode: int, theNewPrior: int) -> None: ...
	def SetVisibility(self, thePrsObject: PrsMgr_PresentableObject, theMode: int, theValue: bool) -> None: ...
	def StructureManager(self) -> Graphic3d_StructureManager: ...
	def Transform(self, thePrsObject: PrsMgr_PresentableObject, theTransformation: Geom_Transformation, theMode: Optional[int]) -> None: ...
	@overload
	def Unhighlight(self, thePrsObject: PrsMgr_PresentableObject) -> None: ...
	@overload
	def Unhighlight(self, thePrsObject: PrsMgr_PresentableObject, theMode: int) -> None: ...
	def Update(self, thePrsObject: PrsMgr_PresentableObject, theMode: Optional[int]) -> None: ...
	def UpdateHighlightTrsf(self, theViewer: V3d_Viewer, theObj: PrsMgr_PresentableObject, theMode: Optional[int], theSelObj: Optional[PrsMgr_PresentableObject]) -> None: ...
