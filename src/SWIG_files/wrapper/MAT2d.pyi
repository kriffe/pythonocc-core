from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *
from OCC.Core.MAT import *
from OCC.Core.Bisector import *


class MAT2d_BiInt:
	def __init__(self, I1: int, I2: int) -> None: ...
	@overload
	def FirstIndex(self) -> int: ...
	@overload
	def FirstIndex(self, I1: int) -> None: ...
	def IsEqual(self, B: MAT2d_BiInt) -> bool: ...
	@overload
	def SecondIndex(self) -> int: ...
	@overload
	def SecondIndex(self, I2: int) -> None: ...

class MAT2d_Circuit(Standard_Transient):
	def __init__(self, aJoinType: Optional[GeomAbs_JoinType], IsOpenResult: Optional[bool]) -> None: ...
	def Connexion(self, Index: int) -> MAT2d_Connexion: ...
	def ConnexionOn(self, Index: int) -> bool: ...
	def LineLength(self, IndexLine: int) -> int: ...
	def NumberOfItems(self) -> int: ...
	def Perform(self, aFigure: MAT2d_SequenceOfSequenceOfGeometry, IsClosed: TColStd_SequenceOfBoolean, IndRefLine: int, Trigo: bool) -> None: ...
	def RefToEqui(self, IndLine: int, IndCurve: int) -> TColStd_SequenceOfInteger: ...
	def Value(self, Index: int) -> Geom2d_Geometry: ...

class MAT2d_Connexion(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, LineA: int, LineB: int, ItemA: int, ItemB: int, Distance: float, ParameterOnA: float, ParameterOnB: float, PointA: gp_Pnt2d, PointB: gp_Pnt2d) -> None: ...
	@overload
	def Distance(self) -> float: ...
	@overload
	def Distance(self, aDistance: float) -> None: ...
	def Dump(self, Deep: Optional[int], Offset: Optional[int]) -> None: ...
	@overload
	def IndexFirstLine(self) -> int: ...
	@overload
	def IndexFirstLine(self, anIndex: int) -> None: ...
	@overload
	def IndexItemOnFirst(self) -> int: ...
	@overload
	def IndexItemOnFirst(self, anIndex: int) -> None: ...
	@overload
	def IndexItemOnSecond(self) -> int: ...
	@overload
	def IndexItemOnSecond(self, anIndex: int) -> None: ...
	@overload
	def IndexSecondLine(self) -> int: ...
	@overload
	def IndexSecondLine(self, anIndex: int) -> None: ...
	def IsAfter(self, aConnexion: MAT2d_Connexion, aSense: float) -> bool: ...
	@overload
	def ParameterOnFirst(self) -> float: ...
	@overload
	def ParameterOnFirst(self, aParameter: float) -> None: ...
	@overload
	def ParameterOnSecond(self) -> float: ...
	@overload
	def ParameterOnSecond(self, aParameter: float) -> None: ...
	@overload
	def PointOnFirst(self) -> gp_Pnt2d: ...
	@overload
	def PointOnFirst(self, aPoint: gp_Pnt2d) -> None: ...
	@overload
	def PointOnSecond(self) -> gp_Pnt2d: ...
	@overload
	def PointOnSecond(self, aPoint: gp_Pnt2d) -> None: ...
	def Reverse(self) -> MAT2d_Connexion: ...

class MAT2d_MapBiIntHasher:
	@staticmethod
	def HashCode(self, theKey: MAT2d_BiInt, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(self, Key1: MAT2d_BiInt, Key2: MAT2d_BiInt) -> bool: ...

class MAT2d_Mat2d:
	def __init__(self, IsOpenResult: Optional[bool]) -> None: ...
	def Bisector(self) -> MAT_Bisector: ...
	def CreateMat(self, aTool: MAT2d_Tool2d) -> None: ...
	def CreateMatOpen(self, aTool: MAT2d_Tool2d) -> None: ...
	def Init(self) -> None: ...
	def IsDone(self) -> bool: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def NumberOfBisectors(self) -> int: ...
	def SemiInfinite(self) -> bool: ...

class MAT2d_MiniPath:
	def __init__(self) -> None: ...
	def ConnexionsFrom(self, Index: int) -> MAT2d_SequenceOfConnexion: ...
	def Father(self, Index: int) -> MAT2d_Connexion: ...
	def IsConnexionsFrom(self, Index: int) -> bool: ...
	def IsRoot(self, Index: int) -> bool: ...
	def Path(self) -> MAT2d_SequenceOfConnexion: ...
	def Perform(self, Figure: MAT2d_SequenceOfSequenceOfGeometry, IndStart: int, Sense: bool) -> None: ...
	def RunOnConnexions(self) -> None: ...

class MAT2d_Tool2d:
	def __init__(self) -> None: ...
	def BisecFusion(self, Index1: int, Index2: int) -> None: ...
	def ChangeGeomBis(self, Index: int) -> Bisector_Bisec: ...
	def Circuit(self) -> MAT2d_Circuit: ...
	def CreateBisector(self, abisector: MAT_Bisector) -> None: ...
	def Distance(self, abisector: MAT_Bisector, param1: float, param2: float) -> float: ...
	def Dump(self, bisector: int, erease: int) -> None: ...
	def FirstPoint(self, anitem: int) -> Tuple[int, float]: ...
	def GeomBis(self, Index: int) -> Bisector_Bisec: ...
	def GeomElt(self, Index: int) -> Geom2d_Geometry: ...
	def GeomPnt(self, Index: int) -> gp_Pnt2d: ...
	def GeomVec(self, Index: int) -> gp_Vec2d: ...
	def InitItems(self, aCircuit: MAT2d_Circuit) -> None: ...
	def IntersectBisector(self, bisectorone: MAT_Bisector, bisectortwo: MAT_Bisector) -> Tuple[float, int]: ...
	def NumberOfItems(self) -> int: ...
	def Sense(self, aside: MAT_Side) -> None: ...
	def SetJoinType(self, aJoinType: GeomAbs_JoinType) -> None: ...
	def Tangent(self, bisector: int) -> int: ...
	def TangentAfter(self, anitem: int, IsOpenResult: bool) -> int: ...
	def TangentBefore(self, anitem: int, IsOpenResult: bool) -> int: ...
	def ToleranceOfConfusion(self) -> float: ...
	@overload
	def TrimBisector(self, abisector: MAT_Bisector) -> bool: ...
	@overload
	def TrimBisector(self, abisector: MAT_Bisector, apoint: int) -> bool: ...

#classnotwrapped
class MAT2d_SketchExplorer:
	pass

#classnotwrapped
class MAT2d_CutCurve:
	pass
MAT2d_MapBiIntHasher_HashCode = MAT2d_MapBiIntHasher.HashCode
MAT2d_MapBiIntHasher_IsEqual = MAT2d_MapBiIntHasher.IsEqual
