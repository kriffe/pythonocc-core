from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TopoDS import *


class XCAFNoteObjects_NoteObject(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theObj: XCAFNoteObjects_NoteObject) -> None: ...
	def GetPlane(self) -> gp_Ax2: ...
	def GetPoint(self) -> gp_Pnt: ...
	def GetPointText(self) -> gp_Pnt: ...
	def GetPresentation(self) -> TopoDS_Shape: ...
	def HasPlane(self) -> bool: ...
	def HasPoint(self) -> bool: ...
	def HasPointText(self) -> bool: ...
	def Reset(self) -> None: ...
	def SetPlane(self, thePlane: gp_Ax2) -> None: ...
	def SetPoint(self, thePnt: gp_Pnt) -> None: ...
	def SetPointText(self, thePnt: gp_Pnt) -> None: ...
	def SetPresentation(self, thePresentation: TopoDS_Shape) -> None: ...
