from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.Bnd import *
from OCC.Core.IntTools import *
from OCC.Core.TopoDS import *
from OCC.Core.TopTools import *
from OCC.Core.TopAbs import *
from OCC.Core.gp import *

#the following typedef cannot be wrapped as is
BOPDS_DataMapIteratorOfDataMapOfPaveBlockCommonBlock = NewType('BOPDS_DataMapIteratorOfDataMapOfPaveBlockCommonBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_DataMapIteratorOfDataMapOfPaveBlockListOfInteger = NewType('BOPDS_DataMapIteratorOfDataMapOfPaveBlockListOfInteger', Any)
#the following typedef cannot be wrapped as is
BOPDS_DataMapIteratorOfDataMapOfPaveBlockListOfPaveBlock = NewType('BOPDS_DataMapIteratorOfDataMapOfPaveBlockListOfPaveBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_DataMapIteratorOfDataMapOfShapeCoupleOfPaveBlocks = NewType('BOPDS_DataMapIteratorOfDataMapOfShapeCoupleOfPaveBlocks', Any)
#the following typedef cannot be wrapped as is
BOPDS_DataMapOfIntegerListOfPaveBlock = NewType('BOPDS_DataMapOfIntegerListOfPaveBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_DataMapOfPaveBlockListOfInteger = NewType('BOPDS_DataMapOfPaveBlockListOfInteger', Any)
#the following typedef cannot be wrapped as is
BOPDS_DataMapOfPaveBlockListOfPaveBlock = NewType('BOPDS_DataMapOfPaveBlockListOfPaveBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_DataMapOfShapeCoupleOfPaveBlocks = NewType('BOPDS_DataMapOfShapeCoupleOfPaveBlocks', Any)
#the following typedef cannot be wrapped as is
BOPDS_IndexedDataMapOfPaveBlockListOfInteger = NewType('BOPDS_IndexedDataMapOfPaveBlockListOfInteger', Any)
#the following typedef cannot be wrapped as is
BOPDS_IndexedDataMapOfPaveBlockListOfPaveBlock = NewType('BOPDS_IndexedDataMapOfPaveBlockListOfPaveBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_IndexedDataMapOfShapeCoupleOfPaveBlocks = NewType('BOPDS_IndexedDataMapOfShapeCoupleOfPaveBlocks', Any)
#the following typedef cannot be wrapped as is
BOPDS_IndexedMapOfPaveBlock = NewType('BOPDS_IndexedMapOfPaveBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_ListIteratorOfListOfPave = NewType('BOPDS_ListIteratorOfListOfPave', Any)
#the following typedef cannot be wrapped as is
BOPDS_ListIteratorOfListOfPaveBlock = NewType('BOPDS_ListIteratorOfListOfPaveBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_ListOfPave = NewType('BOPDS_ListOfPave', Any)
#the following typedef cannot be wrapped as is
BOPDS_ListOfPaveBlock = NewType('BOPDS_ListOfPaveBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_MapIteratorOfMapOfCommonBlock = NewType('BOPDS_MapIteratorOfMapOfCommonBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_MapIteratorOfMapOfPair = NewType('BOPDS_MapIteratorOfMapOfPair', Any)
#the following typedef cannot be wrapped as is
BOPDS_MapIteratorOfMapOfPave = NewType('BOPDS_MapIteratorOfMapOfPave', Any)
#the following typedef cannot be wrapped as is
BOPDS_MapIteratorOfMapOfPaveBlock = NewType('BOPDS_MapIteratorOfMapOfPaveBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_MapOfCommonBlock = NewType('BOPDS_MapOfCommonBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_MapOfPair = NewType('BOPDS_MapOfPair', Any)
#the following typedef cannot be wrapped as is
BOPDS_MapOfPave = NewType('BOPDS_MapOfPave', Any)
#the following typedef cannot be wrapped as is
BOPDS_MapOfPaveBlock = NewType('BOPDS_MapOfPaveBlock', Any)
BOPDS_PDS = NewType('BOPDS_PDS', BOPDS_DS)
BOPDS_PIterator = NewType('BOPDS_PIterator', BOPDS_Iterator)
BOPDS_PIteratorSI = NewType('BOPDS_PIteratorSI', BOPDS_IteratorSI)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfCurve = NewType('BOPDS_VectorOfCurve', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfFaceInfo = NewType('BOPDS_VectorOfFaceInfo', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfIndexRange = NewType('BOPDS_VectorOfIndexRange', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfInterfEE = NewType('BOPDS_VectorOfInterfEE', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfInterfEF = NewType('BOPDS_VectorOfInterfEF', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfInterfEZ = NewType('BOPDS_VectorOfInterfEZ', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfInterfFF = NewType('BOPDS_VectorOfInterfFF', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfInterfFZ = NewType('BOPDS_VectorOfInterfFZ', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfInterfVE = NewType('BOPDS_VectorOfInterfVE', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfInterfVF = NewType('BOPDS_VectorOfInterfVF', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfInterfVV = NewType('BOPDS_VectorOfInterfVV', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfInterfVZ = NewType('BOPDS_VectorOfInterfVZ', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfInterfZZ = NewType('BOPDS_VectorOfInterfZZ', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfListOfPaveBlock = NewType('BOPDS_VectorOfListOfPaveBlock', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfPair = NewType('BOPDS_VectorOfPair', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfPoint = NewType('BOPDS_VectorOfPoint', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfShapeInfo = NewType('BOPDS_VectorOfShapeInfo', Any)
#the following typedef cannot be wrapped as is
BOPDS_VectorOfVectorOfPair = NewType('BOPDS_VectorOfVectorOfPair', Any)

class BOPDS_VectorOfPave:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, theLower: int, theUpper: int): ...
    def __getitem__(self, index: int) -> BOPDS_Pave: ...
    def __setitem__(self, index: int, value: BOPDS_Pave) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[BOPDS_Pave]:
    def next(self) -> BOPDS_Pave: ...
    __next__ = next

class BOPDS_CommonBlock(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def AddFace(self, aF: int) -> None: ...
	def AddPaveBlock(self, aPB: BOPDS_PaveBlock) -> None: ...
	def AppendFaces(self, aLF: TColStd_ListOfInteger) -> None: ...
	@overload
	def Contains(self, thePB: BOPDS_PaveBlock) -> bool: ...
	@overload
	def Contains(self, theF: int) -> bool: ...
	def Dump(self) -> None: ...
	def Edge(self) -> int: ...
	def Faces(self) -> TColStd_ListOfInteger: ...
	def IsPaveBlockOnEdge(self, theIndex: int) -> bool: ...
	def IsPaveBlockOnFace(self, theIndex: int) -> bool: ...
	def PaveBlock1(self) -> BOPDS_PaveBlock: ...
	def PaveBlockOnEdge(self, theIndex: int) -> BOPDS_PaveBlock: ...
	def PaveBlocks(self) -> BOPDS_ListOfPaveBlock: ...
	def SetEdge(self, theEdge: int) -> None: ...
	def SetFaces(self, aLF: TColStd_ListOfInteger) -> None: ...
	def SetPaveBlocks(self, aLPB: BOPDS_ListOfPaveBlock) -> None: ...
	def SetRealPaveBlock(self, thePB: BOPDS_PaveBlock) -> None: ...
	def SetTolerance(self, theTol: float) -> None: ...
	def Tolerance(self) -> float: ...

class BOPDS_CoupleOfPaveBlocks:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, thePB1: BOPDS_PaveBlock, thePB2: BOPDS_PaveBlock) -> None: ...
	def Index(self) -> int: ...
	def IndexInterf(self) -> int: ...
	def PaveBlock1(self) -> BOPDS_PaveBlock: ...
	def PaveBlock2(self) -> BOPDS_PaveBlock: ...
	def PaveBlocks(self, thePB1: BOPDS_PaveBlock, thePB2: BOPDS_PaveBlock) -> None: ...
	def SetIndex(self, theIndex: int) -> None: ...
	def SetIndexInterf(self, theIndex: int) -> None: ...
	def SetPaveBlock1(self, thePB: BOPDS_PaveBlock) -> None: ...
	def SetPaveBlock2(self, thePB: BOPDS_PaveBlock) -> None: ...
	def SetPaveBlocks(self, thePB1: BOPDS_PaveBlock, thePB2: BOPDS_PaveBlock) -> None: ...
	def SetTolerance(self, theTol: float) -> None: ...
	def Tolerance(self) -> float: ...

class BOPDS_Curve:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def Box(self) -> Bnd_Box: ...
	def ChangeBox(self) -> Bnd_Box: ...
	def ChangePaveBlock1(self) -> BOPDS_PaveBlock: ...
	def ChangePaveBlocks(self) -> BOPDS_ListOfPaveBlock: ...
	def ChangeTechnoVertices(self) -> TColStd_ListOfInteger: ...
	def Curve(self) -> IntTools_Curve: ...
	def HasEdge(self) -> bool: ...
	def InitPaveBlock1(self) -> None: ...
	def PaveBlocks(self) -> BOPDS_ListOfPaveBlock: ...
	def SetBox(self, theBox: Bnd_Box) -> None: ...
	def SetCurve(self, theC: IntTools_Curve) -> None: ...
	def SetPaveBlocks(self, theLPB: BOPDS_ListOfPaveBlock) -> None: ...
	def SetTolerance(self, theTol: float) -> None: ...
	def TangentialTolerance(self) -> float: ...
	def TechnoVertices(self) -> TColStd_ListOfInteger: ...
	def Tolerance(self) -> float: ...

class BOPDS_DS:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def AddInterf(self, theI1: int, theI2: int) -> bool: ...
	def AddShapeSD(self, theIndex: int, theIndexSD: int) -> None: ...
	def Allocator(self) -> NCollection_BaseAllocator: ...
	def AloneVertices(self, theF: int, theLI: TColStd_ListOfInteger) -> None: ...
	@overload
	def Append(self, theSI: BOPDS_ShapeInfo) -> int: ...
	@overload
	def Append(self, theS: TopoDS_Shape) -> int: ...
	def Arguments(self) -> TopTools_ListOfShape: ...
	def BuildBndBoxSolid(self, theIndex: int, theBox: Bnd_Box, theCheckInverted: Optional[bool]) -> None: ...
	def ChangeFaceInfo(self, theIndex: int) -> BOPDS_FaceInfo: ...
	def ChangePaveBlocks(self, theIndex: int) -> BOPDS_ListOfPaveBlock: ...
	def ChangePaveBlocksPool(self) -> BOPDS_VectorOfListOfPaveBlock: ...
	def ChangeShapeInfo(self, theIndex: int) -> BOPDS_ShapeInfo: ...
	def Clear(self) -> None: ...
	def CommonBlock(self, thePB: BOPDS_PaveBlock) -> BOPDS_CommonBlock: ...
	def Dump(self) -> None: ...
	def FaceInfo(self, theIndex: int) -> BOPDS_FaceInfo: ...
	def FaceInfoIn(self, theIndex: int, theMPB: BOPDS_IndexedMapOfPaveBlock, theMVP: TColStd_MapOfInteger) -> None: ...
	def FaceInfoOn(self, theIndex: int, theMPB: BOPDS_IndexedMapOfPaveBlock, theMVP: TColStd_MapOfInteger) -> None: ...
	def FaceInfoPool(self) -> BOPDS_VectorOfFaceInfo: ...
	def HasFaceInfo(self, theIndex: int) -> bool: ...
	@overload
	def HasInterf(self, theI: int) -> bool: ...
	@overload
	def HasInterf(self, theI1: int, theI2: int) -> bool: ...
	def HasInterfShapeSubShapes(self, theI1: int, theI2: int, theFlag: Optional[bool]) -> bool: ...
	def HasInterfSubShapes(self, theI1: int, theI2: int) -> bool: ...
	def HasPaveBlocks(self, theIndex: int) -> bool: ...
	def HasShapeSD(self, theIndex: int) -> Tuple[bool, int]: ...
	def Index(self, theS: TopoDS_Shape) -> int: ...
	def Init(self, theFuzz: Optional[float]) -> None: ...
	def InitPaveBlocksForVertex(self, theNV: int) -> None: ...
	def InterfEE(self) -> BOPDS_VectorOfInterfEE: ...
	def InterfEF(self) -> BOPDS_VectorOfInterfEF: ...
	def InterfEZ(self) -> BOPDS_VectorOfInterfEZ: ...
	def InterfFF(self) -> BOPDS_VectorOfInterfFF: ...
	def InterfFZ(self) -> BOPDS_VectorOfInterfFZ: ...
	def InterfVE(self) -> BOPDS_VectorOfInterfVE: ...
	def InterfVF(self) -> BOPDS_VectorOfInterfVF: ...
	def InterfVV(self) -> BOPDS_VectorOfInterfVV: ...
	def InterfVZ(self) -> BOPDS_VectorOfInterfVZ: ...
	def InterfZZ(self) -> BOPDS_VectorOfInterfZZ: ...
	def Interferences(self) -> BOPDS_MapOfPair: ...
	def IsCommonBlock(self, thePB: BOPDS_PaveBlock) -> bool: ...
	def IsCommonBlockOnEdge(self, thePB: BOPDS_PaveBlock) -> bool: ...
	def IsNewShape(self, theIndex: int) -> bool: ...
	def IsSubShape(self, theI1: int, theI2: int) -> bool: ...
	def IsValidShrunkData(self, thePB: BOPDS_PaveBlock) -> bool: ...
	@staticmethod
	def NbInterfTypes(self) -> int: ...
	def NbRanges(self) -> int: ...
	def NbShapes(self) -> int: ...
	def NbSourceShapes(self) -> int: ...
	def PaveBlocks(self, theIndex: int) -> BOPDS_ListOfPaveBlock: ...
	def PaveBlocksPool(self) -> BOPDS_VectorOfListOfPaveBlock: ...
	def Paves(self, theIndex: int, theLP: BOPDS_ListOfPave) -> None: ...
	def Range(self, theIndex: int) -> BOPDS_IndexRange: ...
	def Rank(self, theIndex: int) -> int: ...
	def RealPaveBlock(self, thePB: BOPDS_PaveBlock) -> BOPDS_PaveBlock: ...
	def RefineFaceInfoIn(self) -> None: ...
	def RefineFaceInfoOn(self) -> None: ...
	def ReleasePaveBlocks(self) -> None: ...
	def SetArguments(self, theLS: TopTools_ListOfShape) -> None: ...
	def SetCommonBlock(self, thePB: BOPDS_PaveBlock, theCB: BOPDS_CommonBlock) -> None: ...
	def Shape(self, theIndex: int) -> TopoDS_Shape: ...
	def ShapeInfo(self, theIndex: int) -> BOPDS_ShapeInfo: ...
	def ShapesSD(self) -> TColStd_DataMapOfIntegerInteger: ...
	def SharedEdges(self, theF1: int, theF2: int, theLI: TColStd_ListOfInteger, theAllocator: NCollection_BaseAllocator) -> None: ...
	def SubShapesOnIn(self, theNF1: int, theNF2: int, theMVOnIn: TColStd_MapOfInteger, theMVCommon: TColStd_MapOfInteger, thePBOnIn: BOPDS_IndexedMapOfPaveBlock, theCommonPB: BOPDS_MapOfPaveBlock) -> None: ...
	def UpdateCommonBlock(self, theCB: BOPDS_CommonBlock, theFuzz: float) -> None: ...
	def UpdateCommonBlockWithSDVertices(self, theCB: BOPDS_CommonBlock) -> None: ...
	@overload
	def UpdateFaceInfoIn(self, theIndex: int) -> None: ...
	@overload
	def UpdateFaceInfoIn(self, theFaces: TColStd_MapOfInteger) -> None: ...
	@overload
	def UpdateFaceInfoOn(self, theIndex: int) -> None: ...
	@overload
	def UpdateFaceInfoOn(self, theFaces: TColStd_MapOfInteger) -> None: ...
	def UpdatePaveBlock(self, thePB: BOPDS_PaveBlock) -> None: ...
	def UpdatePaveBlockWithSDVertices(self, thePB: BOPDS_PaveBlock) -> None: ...
	def UpdatePaveBlocks(self) -> None: ...
	def UpdatePaveBlocksWithSDVertices(self) -> None: ...

class BOPDS_FaceInfo:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def ChangePaveBlocksIn(self) -> BOPDS_IndexedMapOfPaveBlock: ...
	def ChangePaveBlocksOn(self) -> BOPDS_IndexedMapOfPaveBlock: ...
	def ChangePaveBlocksSc(self) -> BOPDS_IndexedMapOfPaveBlock: ...
	def ChangeVerticesIn(self) -> TColStd_MapOfInteger: ...
	def ChangeVerticesOn(self) -> TColStd_MapOfInteger: ...
	def ChangeVerticesSc(self) -> TColStd_MapOfInteger: ...
	def Clear(self) -> None: ...
	def Index(self) -> int: ...
	def PaveBlocksIn(self) -> BOPDS_IndexedMapOfPaveBlock: ...
	def PaveBlocksOn(self) -> BOPDS_IndexedMapOfPaveBlock: ...
	def PaveBlocksSc(self) -> BOPDS_IndexedMapOfPaveBlock: ...
	def SetIndex(self, theI: int) -> None: ...
	def VerticesIn(self) -> TColStd_MapOfInteger: ...
	def VerticesOn(self) -> TColStd_MapOfInteger: ...
	def VerticesSc(self) -> TColStd_MapOfInteger: ...

class BOPDS_IndexRange:
	def __init__(self) -> None: ...
	def Contains(self, theIndex: int) -> bool: ...
	def Dump(self) -> None: ...
	def First(self) -> int: ...
	def Indices(self) -> Tuple[int, int]: ...
	def Last(self) -> int: ...
	def SetFirst(self, theI1: int) -> None: ...
	def SetIndices(self, theI1: int, theI2: int) -> None: ...
	def SetLast(self, theI2: int) -> None: ...

class BOPDS_Iterator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def BlockLength(self) -> int: ...
	def DS(self) -> BOPDS_DS: ...
	def ExpectedLength(self) -> int: ...
	def Initialize(self, theType1: TopAbs_ShapeEnum, theType2: TopAbs_ShapeEnum) -> None: ...
	def IntersectExt(self, theIndicies: TColStd_MapOfInteger) -> None: ...
	def More(self) -> bool: ...
	@staticmethod
	def NbExtInterfs(self) -> int: ...
	def Next(self) -> None: ...
	def Prepare(self, theCtx: Optional[IntTools_Context], theCheckOBB: Optional[bool], theFuzzyValue: Optional[float]) -> None: ...
	def RunParallel(self) -> bool: ...
	def SetDS(self, pDS: BOPDS_PDS) -> None: ...
	def SetRunParallel(self, theFlag: bool) -> None: ...
	def Value(self) -> Tuple[int, int]: ...

class BOPDS_Pair:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theIndex1: int, theIndex2: int) -> None: ...
	def HashCode(self, theUpperBound: int) -> int: ...
	def Indices(self) -> Tuple[int, int]: ...
	def IsEqual(self, theOther: BOPDS_Pair) -> bool: ...
	def SetIndices(self, theIndex1: int, theIndex2: int) -> None: ...

class BOPDS_PairMapHasher:
	@staticmethod
	def HashCode(self, thePair: BOPDS_Pair, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(self, thePair1: BOPDS_Pair, thePair2: BOPDS_Pair) -> bool: ...

class BOPDS_Pave:
	def __init__(self) -> None: ...
	def Contents(self) -> Tuple[int, float]: ...
	def Dump(self) -> None: ...
	def Index(self) -> int: ...
	def IsEqual(self, theOther: BOPDS_Pave) -> bool: ...
	def IsLess(self, theOther: BOPDS_Pave) -> bool: ...
	def Parameter(self) -> float: ...
	def SetIndex(self, theIndex: int) -> None: ...
	def SetParameter(self, theParameter: float) -> None: ...

class BOPDS_PaveBlock(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def AppendExtPave(self, thePave: BOPDS_Pave) -> None: ...
	def AppendExtPave1(self, thePave: BOPDS_Pave) -> None: ...
	def ChangeExtPaves(self) -> BOPDS_ListOfPave: ...
	def ContainsParameter(self, thePrm: float, theTol: float) -> Tuple[bool, int]: ...
	def Dump(self) -> None: ...
	def Edge(self) -> int: ...
	def ExtPaves(self) -> BOPDS_ListOfPave: ...
	@overload
	def HasEdge(self) -> bool: ...
	@overload
	def HasEdge(self) -> Tuple[bool, int]: ...
	def HasSameBounds(self, theOther: BOPDS_PaveBlock) -> bool: ...
	def HasShrunkData(self) -> bool: ...
	def Indices(self) -> Tuple[int, int]: ...
	def IsSplitEdge(self) -> bool: ...
	def IsSplittable(self) -> bool: ...
	def IsToUpdate(self) -> bool: ...
	def OriginalEdge(self) -> int: ...
	def Pave1(self) -> BOPDS_Pave: ...
	def Pave2(self) -> BOPDS_Pave: ...
	def Range(self) -> Tuple[float, float]: ...
	def RemoveExtPave(self, theVertNum: int) -> None: ...
	def SetEdge(self, theEdge: int) -> None: ...
	def SetOriginalEdge(self, theEdge: int) -> None: ...
	def SetPave1(self, thePave: BOPDS_Pave) -> None: ...
	def SetPave2(self, thePave: BOPDS_Pave) -> None: ...
	def SetShrunkData(self, theTS1: float, theTS2: float, theBox: Bnd_Box, theIsSplittable: bool) -> None: ...
	def ShrunkData(self, theBox: Bnd_Box) -> Tuple[float, float, bool]: ...
	def Update(self, theLPB: BOPDS_ListOfPaveBlock, theFlag: Optional[bool]) -> None: ...

class BOPDS_PaveMapHasher:
	@staticmethod
	def HashCode(self, thePave: BOPDS_Pave, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(self, aPave1: BOPDS_Pave, aPave2: BOPDS_Pave) -> bool: ...

class BOPDS_Point:
	def __init__(self) -> None: ...
	def Index(self) -> int: ...
	def Pnt(self) -> gp_Pnt: ...
	def Pnt2D1(self) -> gp_Pnt2d: ...
	def Pnt2D2(self) -> gp_Pnt2d: ...
	def SetIndex(self, theIndex: int) -> None: ...
	def SetPnt(self, thePnt: gp_Pnt) -> None: ...
	def SetPnt2D1(self, thePnt: gp_Pnt2d) -> None: ...
	def SetPnt2D2(self, thePnt: gp_Pnt2d) -> None: ...

class BOPDS_ShapeInfo:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def Box(self) -> Bnd_Box: ...
	def ChangeBox(self) -> Bnd_Box: ...
	def ChangeSubShapes(self) -> TColStd_ListOfInteger: ...
	def Dump(self) -> None: ...
	def Flag(self) -> int: ...
	def HasBRep(self) -> bool: ...
	@overload
	def HasFlag(self) -> bool: ...
	@overload
	def HasFlag(self) -> Tuple[bool, int]: ...
	def HasReference(self) -> bool: ...
	def HasSubShape(self, theI: int) -> bool: ...
	def IsInterfering(self) -> bool: ...
	def Reference(self) -> int: ...
	def SetBox(self, theBox: Bnd_Box) -> None: ...
	def SetFlag(self, theI: int) -> None: ...
	def SetReference(self, theI: int) -> None: ...
	def SetShape(self, theS: TopoDS_Shape) -> None: ...
	def SetShapeType(self, theType: TopAbs_ShapeEnum) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def ShapeType(self) -> TopAbs_ShapeEnum: ...
	def SubShapes(self) -> TColStd_ListOfInteger: ...

class BOPDS_SubIterator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def DS(self) -> BOPDS_DS: ...
	def ExpectedLength(self) -> int: ...
	def Initialize(self) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Prepare(self) -> None: ...
	def SetDS(self, pDS: BOPDS_PDS) -> None: ...
	def SetSubSet1(self, theLI: TColStd_ListOfInteger) -> None: ...
	def SetSubSet2(self, theLI: TColStd_ListOfInteger) -> None: ...
	def SubSet1(self) -> TColStd_ListOfInteger: ...
	def SubSet2(self) -> TColStd_ListOfInteger: ...
	def Value(self) -> Tuple[int, int]: ...

class BOPDS_Tools:
	@staticmethod
	def HasBRep(self, theT: TopAbs_ShapeEnum) -> bool: ...
	@staticmethod
	def IsInterfering(self, theT: TopAbs_ShapeEnum) -> bool: ...
	@overload
	@staticmethod
	def TypeToInteger(self, theT1: TopAbs_ShapeEnum, theT2: TopAbs_ShapeEnum) -> int: ...
	@overload
	@staticmethod
	def TypeToInteger(self, theT: TopAbs_ShapeEnum) -> int: ...

class BOPDS_InterfEE(BOPDS_Interf):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def CommonPart(self) -> IntTools_CommonPrt: ...
	def SetCommonPart(self, theCP: IntTools_CommonPrt) -> None: ...

class BOPDS_InterfEF(BOPDS_Interf):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def CommonPart(self) -> IntTools_CommonPrt: ...
	def SetCommonPart(self, theCP: IntTools_CommonPrt) -> None: ...

class BOPDS_InterfEZ(BOPDS_Interf):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...

class BOPDS_InterfFF(BOPDS_Interf):
	def __init__(self) -> None: ...
	def ChangeCurves(self) -> BOPDS_VectorOfCurve: ...
	def ChangePoints(self) -> BOPDS_VectorOfPoint: ...
	def Curves(self) -> BOPDS_VectorOfCurve: ...
	def Init(self, theNbCurves: int, theNbPoints: int) -> None: ...
	def Points(self) -> BOPDS_VectorOfPoint: ...
	def SetTangentFaces(self, theFlag: bool) -> None: ...
	def TangentFaces(self) -> bool: ...

class BOPDS_InterfFZ(BOPDS_Interf):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...

class BOPDS_InterfVE(BOPDS_Interf):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def Parameter(self) -> float: ...
	def SetParameter(self, theT: float) -> None: ...

class BOPDS_InterfVF(BOPDS_Interf):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def SetUV(self, theU: float, theV: float) -> None: ...
	def UV(self) -> Tuple[float, float]: ...

class BOPDS_InterfVV(BOPDS_Interf):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...

class BOPDS_InterfVZ(BOPDS_Interf):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...

class BOPDS_InterfZZ(BOPDS_Interf):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...

class BOPDS_IteratorSI(BOPDS_Iterator):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAllocator: NCollection_BaseAllocator) -> None: ...
	def UpdateByLevelOfCheck(self, theLevel: int) -> None: ...

#classnotwrapped
class BOPDS_Interf: ...

# harray1 classes
# harray2 classes
# hsequence classes

BOPDS_DS_NbInterfTypes = BOPDS_DS.NbInterfTypes
BOPDS_Iterator_NbExtInterfs = BOPDS_Iterator.NbExtInterfs
BOPDS_PairMapHasher_HashCode = BOPDS_PairMapHasher.HashCode
BOPDS_PairMapHasher_IsEqual = BOPDS_PairMapHasher.IsEqual
BOPDS_PaveMapHasher_HashCode = BOPDS_PaveMapHasher.HashCode
BOPDS_PaveMapHasher_IsEqual = BOPDS_PaveMapHasher.IsEqual
BOPDS_Tools_HasBRep = BOPDS_Tools.HasBRep
BOPDS_Tools_IsInterfering = BOPDS_Tools.IsInterfering
BOPDS_Tools_TypeToInteger = BOPDS_Tools.TypeToInteger
BOPDS_Tools_TypeToInteger = BOPDS_Tools.TypeToInteger
