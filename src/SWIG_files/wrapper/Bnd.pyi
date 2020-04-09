from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TColStd import *
from OCC.Core.TColgp import *
from OCC.Core.BVH import *

#the following typedef cannot be wrapped as is
Bnd_Array1OfBox = NewType('Bnd_Array1OfBox', Any)
#the following typedef cannot be wrapped as is
Bnd_Array1OfBox2d = NewType('Bnd_Array1OfBox2d', Any)
#the following typedef cannot be wrapped as is
Bnd_Array1OfSphere = NewType('Bnd_Array1OfSphere', Any)
#the following typedef cannot be wrapped as is
Bnd_SeqOfBox = NewType('Bnd_SeqOfBox', Any)

class Bnd_B2d:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theCenter: gp_XY, theHSize: gp_XY) -> None: ...
	@overload
	def Add(self, thePnt: gp_XY) -> None: ...
	@overload
	def Add(self, thePnt: gp_Pnt2d) -> None: ...
	@overload
	def Add(self, theBox: Bnd_B2d) -> None: ...
	def Clear(self) -> None: ...
	def CornerMax(self) -> gp_XY: ...
	def CornerMin(self) -> gp_XY: ...
	def Enlarge(self, theDiff: float) -> None: ...
	@overload
	def IsIn(self, theBox: Bnd_B2d) -> bool: ...
	@overload
	def IsIn(self, theBox: Bnd_B2d, theTrsf: gp_Trsf2d) -> bool: ...
	@overload
	def IsOut(self, thePnt: gp_XY) -> bool: ...
	@overload
	def IsOut(self, theCenter: gp_XY, theRadius: float, isCircleHollow: Optional[bool]) -> bool: ...
	@overload
	def IsOut(self, theOtherBox: Bnd_B2d) -> bool: ...
	@overload
	def IsOut(self, theOtherBox: Bnd_B2d, theTrsf: gp_Trsf2d) -> bool: ...
	@overload
	def IsOut(self, theLine: gp_Ax2d) -> bool: ...
	@overload
	def IsOut(self, theP0: gp_XY, theP1: gp_XY) -> bool: ...
	def IsVoid(self) -> bool: ...
	def Limit(self, theOtherBox: Bnd_B2d) -> bool: ...
	def SetCenter(self, theCenter: gp_XY) -> None: ...
	def SetHSize(self, theHSize: gp_XY) -> None: ...
	def SquareExtent(self) -> float: ...
	def Transformed(self, theTrsf: gp_Trsf2d) -> Bnd_B2d: ...

class Bnd_B2f:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theCenter: gp_XY, theHSize: gp_XY) -> None: ...
	@overload
	def Add(self, thePnt: gp_XY) -> None: ...
	@overload
	def Add(self, thePnt: gp_Pnt2d) -> None: ...
	@overload
	def Add(self, theBox: Bnd_B2f) -> None: ...
	def Clear(self) -> None: ...
	def CornerMax(self) -> gp_XY: ...
	def CornerMin(self) -> gp_XY: ...
	def Enlarge(self, theDiff: float) -> None: ...
	@overload
	def IsIn(self, theBox: Bnd_B2f) -> bool: ...
	@overload
	def IsIn(self, theBox: Bnd_B2f, theTrsf: gp_Trsf2d) -> bool: ...
	@overload
	def IsOut(self, thePnt: gp_XY) -> bool: ...
	@overload
	def IsOut(self, theCenter: gp_XY, theRadius: float, isCircleHollow: Optional[bool]) -> bool: ...
	@overload
	def IsOut(self, theOtherBox: Bnd_B2f) -> bool: ...
	@overload
	def IsOut(self, theOtherBox: Bnd_B2f, theTrsf: gp_Trsf2d) -> bool: ...
	@overload
	def IsOut(self, theLine: gp_Ax2d) -> bool: ...
	@overload
	def IsOut(self, theP0: gp_XY, theP1: gp_XY) -> bool: ...
	def IsVoid(self) -> bool: ...
	def Limit(self, theOtherBox: Bnd_B2f) -> bool: ...
	def SetCenter(self, theCenter: gp_XY) -> None: ...
	def SetHSize(self, theHSize: gp_XY) -> None: ...
	def SquareExtent(self) -> float: ...
	def Transformed(self, theTrsf: gp_Trsf2d) -> Bnd_B2f: ...

class Bnd_B3d:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theCenter: gp_XYZ, theHSize: gp_XYZ) -> None: ...
	@overload
	def Add(self, thePnt: gp_XYZ) -> None: ...
	@overload
	def Add(self, thePnt: gp_Pnt) -> None: ...
	@overload
	def Add(self, theBox: Bnd_B3d) -> None: ...
	def Clear(self) -> None: ...
	def CornerMax(self) -> gp_XYZ: ...
	def CornerMin(self) -> gp_XYZ: ...
	def Enlarge(self, theDiff: float) -> None: ...
	@overload
	def IsIn(self, theBox: Bnd_B3d) -> bool: ...
	@overload
	def IsIn(self, theBox: Bnd_B3d, theTrsf: gp_Trsf) -> bool: ...
	@overload
	def IsOut(self, thePnt: gp_XYZ) -> bool: ...
	@overload
	def IsOut(self, theCenter: gp_XYZ, theRadius: float, isSphereHollow: Optional[bool]) -> bool: ...
	@overload
	def IsOut(self, theOtherBox: Bnd_B3d) -> bool: ...
	@overload
	def IsOut(self, theOtherBox: Bnd_B3d, theTrsf: gp_Trsf) -> bool: ...
	@overload
	def IsOut(self, theLine: gp_Ax1, isRay: Optional[bool], theOverthickness: Optional[float]) -> bool: ...
	@overload
	def IsOut(self, thePlane: gp_Ax3) -> bool: ...
	def IsVoid(self) -> bool: ...
	def Limit(self, theOtherBox: Bnd_B3d) -> bool: ...
	def SetCenter(self, theCenter: gp_XYZ) -> None: ...
	def SetHSize(self, theHSize: gp_XYZ) -> None: ...
	def SquareExtent(self) -> float: ...
	def Transformed(self, theTrsf: gp_Trsf) -> Bnd_B3d: ...

class Bnd_B3f:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theCenter: gp_XYZ, theHSize: gp_XYZ) -> None: ...
	@overload
	def Add(self, thePnt: gp_XYZ) -> None: ...
	@overload
	def Add(self, thePnt: gp_Pnt) -> None: ...
	@overload
	def Add(self, theBox: Bnd_B3f) -> None: ...
	def Clear(self) -> None: ...
	def CornerMax(self) -> gp_XYZ: ...
	def CornerMin(self) -> gp_XYZ: ...
	def Enlarge(self, theDiff: float) -> None: ...
	@overload
	def IsIn(self, theBox: Bnd_B3f) -> bool: ...
	@overload
	def IsIn(self, theBox: Bnd_B3f, theTrsf: gp_Trsf) -> bool: ...
	@overload
	def IsOut(self, thePnt: gp_XYZ) -> bool: ...
	@overload
	def IsOut(self, theCenter: gp_XYZ, theRadius: float, isSphereHollow: Optional[bool]) -> bool: ...
	@overload
	def IsOut(self, theOtherBox: Bnd_B3f) -> bool: ...
	@overload
	def IsOut(self, theOtherBox: Bnd_B3f, theTrsf: gp_Trsf) -> bool: ...
	@overload
	def IsOut(self, theLine: gp_Ax1, isRay: Optional[bool], theOverthickness: Optional[float]) -> bool: ...
	@overload
	def IsOut(self, thePlane: gp_Ax3) -> bool: ...
	def IsVoid(self) -> bool: ...
	def Limit(self, theOtherBox: Bnd_B3f) -> bool: ...
	def SetCenter(self, theCenter: gp_XYZ) -> None: ...
	def SetHSize(self, theHSize: gp_XYZ) -> None: ...
	def SquareExtent(self) -> float: ...
	def Transformed(self, theTrsf: gp_Trsf) -> Bnd_B3f: ...

class Bnd_BoundSortBox:
	def __init__(self) -> None: ...
	def Add(self, theBox: Bnd_Box, boxIndex: int) -> None: ...
	@overload
	def Compare(self, theBox: Bnd_Box) -> TColStd_ListOfInteger: ...
	@overload
	def Compare(self, P: gp_Pln) -> TColStd_ListOfInteger: ...
	def Destroy(self) -> None: ...
	def Dump(self) -> None: ...
	@overload
	def Initialize(self, CompleteBox: Bnd_Box, SetOfBox: Bnd_HArray1OfBox) -> None: ...
	@overload
	def Initialize(self, SetOfBox: Bnd_HArray1OfBox) -> None: ...
	@overload
	def Initialize(self, CompleteBox: Bnd_Box, nbComponents: int) -> None: ...

class Bnd_BoundSortBox2d:
	def __init__(self) -> None: ...
	def Add(self, theBox: Bnd_Box2d, boxIndex: int) -> None: ...
	def Compare(self, theBox: Bnd_Box2d) -> TColStd_ListOfInteger: ...
	def Dump(self) -> None: ...
	@overload
	def Initialize(self, CompleteBox: Bnd_Box2d, SetOfBox: Bnd_HArray1OfBox2d) -> None: ...
	@overload
	def Initialize(self, SetOfBox: Bnd_HArray1OfBox2d) -> None: ...
	@overload
	def Initialize(self, CompleteBox: Bnd_Box2d, nbComponents: int) -> None: ...

class Bnd_Box:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theMin: gp_Pnt, theMax: gp_Pnt) -> None: ...
	@overload
	def Add(self, Other: Bnd_Box) -> None: ...
	@overload
	def Add(self, P: gp_Pnt) -> None: ...
	@overload
	def Add(self, P: gp_Pnt, D: gp_Dir) -> None: ...
	@overload
	def Add(self, D: gp_Dir) -> None: ...
	def CornerMax(self) -> gp_Pnt: ...
	def CornerMin(self) -> gp_Pnt: ...
	def Distance(self, Other: Bnd_Box) -> float: ...
	def Dump(self) -> None: ...
	def Enlarge(self, Tol: float) -> None: ...
	def FinitePart(self) -> Bnd_Box: ...
	def Get(self) -> Tuple[float, float, float, float, float, float]: ...
	def GetGap(self) -> float: ...
	def HasFinitePart(self) -> bool: ...
	def IsOpen(self) -> bool: ...
	def IsOpenXmax(self) -> bool: ...
	def IsOpenXmin(self) -> bool: ...
	def IsOpenYmax(self) -> bool: ...
	def IsOpenYmin(self) -> bool: ...
	def IsOpenZmax(self) -> bool: ...
	def IsOpenZmin(self) -> bool: ...
	@overload
	def IsOut(self, P: gp_Pnt) -> bool: ...
	@overload
	def IsOut(self, L: gp_Lin) -> bool: ...
	@overload
	def IsOut(self, P: gp_Pln) -> bool: ...
	@overload
	def IsOut(self, Other: Bnd_Box) -> bool: ...
	@overload
	def IsOut(self, Other: Bnd_Box, T: gp_Trsf) -> bool: ...
	@overload
	def IsOut(self, T1: gp_Trsf, Other: Bnd_Box, T2: gp_Trsf) -> bool: ...
	@overload
	def IsOut(self, P1: gp_Pnt, P2: gp_Pnt, D: gp_Dir) -> bool: ...
	def IsThin(self, tol: float) -> bool: ...
	def IsVoid(self) -> bool: ...
	def IsWhole(self) -> bool: ...
	def IsXThin(self, tol: float) -> bool: ...
	def IsYThin(self, tol: float) -> bool: ...
	def IsZThin(self, tol: float) -> bool: ...
	def OpenXmax(self) -> None: ...
	def OpenXmin(self) -> None: ...
	def OpenYmax(self) -> None: ...
	def OpenYmin(self) -> None: ...
	def OpenZmax(self) -> None: ...
	def OpenZmin(self) -> None: ...
	@overload
	def Set(self, P: gp_Pnt) -> None: ...
	@overload
	def Set(self, P: gp_Pnt, D: gp_Dir) -> None: ...
	def SetGap(self, Tol: float) -> None: ...
	def SetVoid(self) -> None: ...
	def SetWhole(self) -> None: ...
	def SquareExtent(self) -> float: ...
	def Transformed(self, T: gp_Trsf) -> Bnd_Box: ...
	@overload
	def Update(self, aXmin: float, aYmin: float, aZmin: float, aXmax: float, aYmax: float, aZmax: float) -> None: ...
	@overload
	def Update(self, X: float, Y: float, Z: float) -> None: ...

class Bnd_Box2d:
	def __init__(self) -> None: ...
	@overload
	def Add(self, Other: Bnd_Box2d) -> None: ...
	@overload
	def Add(self, thePnt: gp_Pnt2d) -> None: ...
	@overload
	def Add(self, thePnt: gp_Pnt2d, theDir: gp_Dir2d) -> None: ...
	@overload
	def Add(self, D: gp_Dir2d) -> None: ...
	def Dump(self) -> None: ...
	def Enlarge(self, theTol: float) -> None: ...
	def Get(self) -> Tuple[float, float, float, float]: ...
	def GetGap(self) -> float: ...
	def IsOpenXmax(self) -> bool: ...
	def IsOpenXmin(self) -> bool: ...
	def IsOpenYmax(self) -> bool: ...
	def IsOpenYmin(self) -> bool: ...
	@overload
	def IsOut(self, P: gp_Pnt2d) -> bool: ...
	@overload
	def IsOut(self, Other: Bnd_Box2d) -> bool: ...
	@overload
	def IsOut(self, theOther: Bnd_Box2d, theTrsf: gp_Trsf2d) -> bool: ...
	@overload
	def IsOut(self, T1: gp_Trsf2d, Other: Bnd_Box2d, T2: gp_Trsf2d) -> bool: ...
	def IsVoid(self) -> bool: ...
	def IsWhole(self) -> bool: ...
	def OpenXmax(self) -> None: ...
	def OpenXmin(self) -> None: ...
	def OpenYmax(self) -> None: ...
	def OpenYmin(self) -> None: ...
	@overload
	def Set(self, thePnt: gp_Pnt2d) -> None: ...
	@overload
	def Set(self, thePnt: gp_Pnt2d, theDir: gp_Dir2d) -> None: ...
	def SetGap(self, Tol: float) -> None: ...
	def SetVoid(self) -> None: ...
	def SetWhole(self) -> None: ...
	def SquareExtent(self) -> float: ...
	def Transformed(self, T: gp_Trsf2d) -> Bnd_Box2d: ...
	@overload
	def Update(self, aXmin: float, aYmin: float, aXmax: float, aYmax: float) -> None: ...
	@overload
	def Update(self, X: float, Y: float) -> None: ...

class Bnd_OBB:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theCenter: gp_Pnt, theXDirection: gp_Dir, theYDirection: gp_Dir, theZDirection: gp_Dir, theHXSize: float, theHYSize: float, theHZSize: float) -> None: ...
	@overload
	def __init__(self, theBox: Bnd_Box) -> None: ...
	@overload
	def Add(self, theOther: Bnd_OBB) -> None: ...
	@overload
	def Add(self, theP: gp_Pnt) -> None: ...
	def Center(self) -> gp_XYZ: ...
	def Enlarge(self, theGapAdd: float) -> None: ...
	def GetVertex(self, theP_list: List[gp_Pnt]) -> bool: ...
	def IsAABox(self) -> bool: ...
	def IsCompletelyInside(self, theOther: Bnd_OBB) -> bool: ...
	@overload
	def IsOut(self, theOther: Bnd_OBB) -> bool: ...
	@overload
	def IsOut(self, theP: gp_Pnt) -> bool: ...
	def IsVoid(self) -> bool: ...
	def Position(self) -> gp_Ax3: ...
	def ReBuild(self, theListOfPoints: TColgp_Array1OfPnt, theListOfTolerances: Optional[TColStd_Array1OfReal], theIsOptimal: Optional[bool]) -> None: ...
	def SetAABox(self, theFlag: bool) -> None: ...
	def SetCenter(self, theCenter: gp_Pnt) -> None: ...
	def SetVoid(self) -> None: ...
	def SetXComponent(self, theXDirection: gp_Dir, theHXSize: float) -> None: ...
	def SetYComponent(self, theYDirection: gp_Dir, theHYSize: float) -> None: ...
	def SetZComponent(self, theZDirection: gp_Dir, theHZSize: float) -> None: ...
	def SquareExtent(self) -> float: ...
	def XDirection(self) -> gp_XYZ: ...
	def XHSize(self) -> float: ...
	def YDirection(self) -> gp_XYZ: ...
	def YHSize(self) -> float: ...
	def ZDirection(self) -> gp_XYZ: ...
	def ZHSize(self) -> float: ...

class Bnd_Range:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theMin: float, theMax: float) -> None: ...
	@overload
	def Add(self, theParameter: float) -> None: ...
	@overload
	def Add(self, theRange: Bnd_Range) -> None: ...
	def Common(self, theOther: Bnd_Range) -> None: ...
	def Delta(self) -> float: ...
	def Enlarge(self, theDelta: float) -> None: ...
	def GetBounds(self) -> Tuple[bool, float, float]: ...
	def GetIntermediatePoint(self, theLambda: float) -> Tuple[bool, float]: ...
	def GetMax(self) -> Tuple[bool, float]: ...
	def GetMin(self) -> Tuple[bool, float]: ...
	def IsIntersected(self, theVal: float, thePeriod: Optional[float]) -> int: ...
	@overload
	def IsOut(self, theValue: float) -> bool: ...
	@overload
	def IsOut(self, theRange: Bnd_Range) -> bool: ...
	def IsVoid(self) -> bool: ...
	def SetVoid(self) -> None: ...
	def Shift(self, theVal: float) -> None: ...
	def Shifted(self, theVal: float) -> Bnd_Range: ...
	def TrimFrom(self, theValLower: float) -> None: ...
	def TrimTo(self, theValUpper: float) -> None: ...
	def Union(self, theOther: Bnd_Range) -> bool: ...

class Bnd_Sphere:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theCntr: gp_XYZ, theRad: float, theU: int, theV: int) -> None: ...
	def Add(self, theOther: Bnd_Sphere) -> None: ...
	def Center(self) -> gp_XYZ: ...
	def Distance(self, theNode: gp_XYZ) -> float: ...
	def Distances(self, theXYZ: gp_XYZ) -> Tuple[float, float]: ...
	@overload
	def IsOut(self, theOther: Bnd_Sphere) -> bool: ...
	@overload
	def IsOut(self, thePnt: gp_XYZ) -> Tuple[bool, float]: ...
	def IsValid(self) -> bool: ...
	def Project(self, theNode: gp_XYZ, theProjNode: gp_XYZ) -> Tuple[bool, float, bool]: ...
	def Radius(self) -> float: ...
	def SetValid(self, isValid: bool) -> None: ...
	def SquareDistance(self, theNode: gp_XYZ) -> float: ...
	def SquareDistances(self, theXYZ: gp_XYZ) -> Tuple[float, float]: ...
	def SquareExtent(self) -> float: ...
	def U(self) -> int: ...
	def V(self) -> int: ...

class Bnd_Tools:
	@overload
	@staticmethod
	def Bnd2BVH(self, theBox: Bnd_Box2d) -> False: ...
	@overload
	@staticmethod
	def Bnd2BVH(self, theBox: Bnd_Box) -> False: ...

# harray1 classes
class Bnd_HArray1OfBox(Bnd_Array1OfBox, Standard_Transient): ...

class Bnd_HArray1OfSphere(Bnd_Array1OfSphere, Standard_Transient): ...

class Bnd_HArray1OfBox2d(Bnd_Array1OfBox2d, Standard_Transient): ...

# harray2 classes
# harray2 classes

Bnd_Tools_Bnd2BVH = Bnd_Tools.Bnd2BVH
Bnd_Tools_Bnd2BVH = Bnd_Tools.Bnd2BVH
