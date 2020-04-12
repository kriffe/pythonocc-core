from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

#the following typedef cannot be wrapped as is
MAT_DataMapIteratorOfDataMapOfIntegerArc = NewType('MAT_DataMapIteratorOfDataMapOfIntegerArc', Any)
#the following typedef cannot be wrapped as is
MAT_DataMapIteratorOfDataMapOfIntegerBasicElt = NewType('MAT_DataMapIteratorOfDataMapOfIntegerBasicElt', Any)
#the following typedef cannot be wrapped as is
MAT_DataMapIteratorOfDataMapOfIntegerBisector = NewType('MAT_DataMapIteratorOfDataMapOfIntegerBisector', Any)
#the following typedef cannot be wrapped as is
MAT_DataMapIteratorOfDataMapOfIntegerNode = NewType('MAT_DataMapIteratorOfDataMapOfIntegerNode', Any)
#the following typedef cannot be wrapped as is
MAT_DataMapOfIntegerArc = NewType('MAT_DataMapOfIntegerArc', Any)
#the following typedef cannot be wrapped as is
MAT_DataMapOfIntegerBasicElt = NewType('MAT_DataMapOfIntegerBasicElt', Any)
#the following typedef cannot be wrapped as is
MAT_DataMapOfIntegerBisector = NewType('MAT_DataMapOfIntegerBisector', Any)
#the following typedef cannot be wrapped as is
MAT_DataMapOfIntegerNode = NewType('MAT_DataMapOfIntegerNode', Any)
#the following typedef cannot be wrapped as is
MAT_SequenceOfArc = NewType('MAT_SequenceOfArc', Any)
#the following typedef cannot be wrapped as is
MAT_SequenceOfBasicElt = NewType('MAT_SequenceOfBasicElt', Any)

class MAT_Side(IntEnum):
	MAT_Left: int = ...
	MAT_Right: int = ...
MAT_Left = MAT_Side.MAT_Left
MAT_Right = MAT_Side.MAT_Right

class MAT_Arc(Standard_Transient):
	def __init__(self, ArcIndex: int, GeomIndex: int, FirstElement: MAT_BasicElt, SecondElement: MAT_BasicElt) -> None: ...
	def FirstElement(self) -> MAT_BasicElt: ...
	def FirstNode(self) -> MAT_Node: ...
	def GeomIndex(self) -> int: ...
	def HasNeighbour(self, aNode: MAT_Node, aSide: MAT_Side) -> bool: ...
	def Index(self) -> int: ...
	def Neighbour(self, aNode: MAT_Node, aSide: MAT_Side) -> MAT_Arc: ...
	def SecondElement(self) -> MAT_BasicElt: ...
	def SecondNode(self) -> MAT_Node: ...
	def SetFirstArc(self, aSide: MAT_Side, anArc: MAT_Arc) -> None: ...
	def SetFirstElement(self, aBasicElt: MAT_BasicElt) -> None: ...
	def SetFirstNode(self, aNode: MAT_Node) -> None: ...
	def SetGeomIndex(self, anInteger: int) -> None: ...
	def SetIndex(self, anInteger: int) -> None: ...
	def SetNeighbour(self, aSide: MAT_Side, aNode: MAT_Node, anArc: MAT_Arc) -> None: ...
	def SetSecondArc(self, aSide: MAT_Side, anArc: MAT_Arc) -> None: ...
	def SetSecondElement(self, aBasicElt: MAT_BasicElt) -> None: ...
	def SetSecondNode(self, aNode: MAT_Node) -> None: ...
	def TheOtherNode(self, aNode: MAT_Node) -> MAT_Node: ...

class MAT_BasicElt(Standard_Transient):
	def __init__(self, anInteger: int) -> None: ...
	def EndArc(self) -> MAT_Arc: ...
	def GeomIndex(self) -> int: ...
	def Index(self) -> int: ...
	def SetEndArc(self, anArc: MAT_Arc) -> None: ...
	def SetGeomIndex(self, anInteger: int) -> None: ...
	def SetIndex(self, anInteger: int) -> None: ...
	def SetStartArc(self, anArc: MAT_Arc) -> None: ...
	def StartArc(self) -> MAT_Arc: ...

class MAT_Bisector(Standard_Transient):
	def __init__(self) -> None: ...
	def AddBisector(self, abisector: MAT_Bisector) -> None: ...
	@overload
	def BisectorNumber(self, anumber: int) -> None: ...
	@overload
	def BisectorNumber(self) -> int: ...
	@overload
	def DistIssuePoint(self, areal: float) -> None: ...
	@overload
	def DistIssuePoint(self) -> float: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	@overload
	def EndPoint(self, apoint: int) -> None: ...
	@overload
	def EndPoint(self) -> int: ...
	def FirstBisector(self) -> MAT_Bisector: ...
	@overload
	def FirstEdge(self, anedge: MAT_Edge) -> None: ...
	@overload
	def FirstEdge(self) -> MAT_Edge: ...
	@overload
	def FirstParameter(self, aparameter: float) -> None: ...
	@overload
	def FirstParameter(self) -> float: ...
	@overload
	def FirstVector(self, avector: int) -> None: ...
	@overload
	def FirstVector(self) -> int: ...
	@overload
	def IndexNumber(self, anumber: int) -> None: ...
	@overload
	def IndexNumber(self) -> int: ...
	@overload
	def IssuePoint(self, apoint: int) -> None: ...
	@overload
	def IssuePoint(self) -> int: ...
	def LastBisector(self) -> MAT_Bisector: ...
	def List(self) -> MAT_ListOfBisector: ...
	@overload
	def SecondEdge(self, anedge: MAT_Edge) -> None: ...
	@overload
	def SecondEdge(self) -> MAT_Edge: ...
	@overload
	def SecondParameter(self, aparameter: float) -> None: ...
	@overload
	def SecondParameter(self) -> float: ...
	@overload
	def SecondVector(self, avector: int) -> None: ...
	@overload
	def SecondVector(self) -> int: ...
	@overload
	def Sense(self, asense: float) -> None: ...
	@overload
	def Sense(self) -> float: ...

class MAT_Edge(Standard_Transient):
	def __init__(self) -> None: ...
	@overload
	def Distance(self, adistance: float) -> None: ...
	@overload
	def Distance(self) -> float: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	@overload
	def EdgeNumber(self, anumber: int) -> None: ...
	@overload
	def EdgeNumber(self) -> int: ...
	@overload
	def FirstBisector(self, abisector: MAT_Bisector) -> None: ...
	@overload
	def FirstBisector(self) -> MAT_Bisector: ...
	@overload
	def IntersectionPoint(self, apoint: int) -> None: ...
	@overload
	def IntersectionPoint(self) -> int: ...
	@overload
	def SecondBisector(self, abisector: MAT_Bisector) -> None: ...
	@overload
	def SecondBisector(self) -> MAT_Bisector: ...

class MAT_Graph(Standard_Transient):
	def __init__(self) -> None: ...
	def Arc(self, Index: int) -> MAT_Arc: ...
	def BasicElt(self, Index: int) -> MAT_BasicElt: ...
	def ChangeBasicElt(self, Index: int) -> MAT_BasicElt: ...
	def ChangeBasicElts(self, NewMap: MAT_DataMapOfIntegerBasicElt) -> None: ...
	def CompactArcs(self) -> None: ...
	def CompactNodes(self) -> None: ...
	def FusionOfBasicElts(self, IndexElt1: int, IndexElt2: int) -> Tuple[bool, int, int, bool, int, int]: ...
	def Node(self, Index: int) -> MAT_Node: ...
	def NumberOfArcs(self) -> int: ...
	def NumberOfBasicElts(self) -> int: ...
	def NumberOfInfiniteNodes(self) -> int: ...
	def NumberOfNodes(self) -> int: ...
	def Perform(self, SemiInfinite: bool, TheRoots: MAT_ListOfBisector, NbBasicElts: int, NbArcs: int) -> None: ...

class MAT_ListOfBisector(Standard_Transient):
	def __init__(self) -> None: ...
	def BackAdd(self, anitem: MAT_Bisector) -> None: ...
	def Brackets(self, anindex: int) -> MAT_Bisector: ...
	@overload
	def Current(self) -> MAT_Bisector: ...
	@overload
	def Current(self, anitem: MAT_Bisector) -> None: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	def First(self) -> None: ...
	def FirstItem(self) -> MAT_Bisector: ...
	def FrontAdd(self, anitem: MAT_Bisector) -> None: ...
	def Index(self) -> int: ...
	def Init(self, aniten: MAT_Bisector) -> None: ...
	def IsEmpty(self) -> bool: ...
	def Last(self) -> None: ...
	def LastItem(self) -> MAT_Bisector: ...
	def LinkAfter(self, anitem: MAT_Bisector) -> None: ...
	def LinkBefore(self, anitem: MAT_Bisector) -> None: ...
	def Loop(self) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def NextItem(self) -> MAT_Bisector: ...
	def Number(self) -> int: ...
	def Permute(self) -> None: ...
	def Previous(self) -> None: ...
	def PreviousItem(self) -> MAT_Bisector: ...
	def Unlink(self) -> None: ...

class MAT_ListOfEdge(Standard_Transient):
	def __init__(self) -> None: ...
	def BackAdd(self, anitem: MAT_Edge) -> None: ...
	def Brackets(self, anindex: int) -> MAT_Edge: ...
	@overload
	def Current(self) -> MAT_Edge: ...
	@overload
	def Current(self, anitem: MAT_Edge) -> None: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	def First(self) -> None: ...
	def FirstItem(self) -> MAT_Edge: ...
	def FrontAdd(self, anitem: MAT_Edge) -> None: ...
	def Index(self) -> int: ...
	def Init(self, aniten: MAT_Edge) -> None: ...
	def IsEmpty(self) -> bool: ...
	def Last(self) -> None: ...
	def LastItem(self) -> MAT_Edge: ...
	def LinkAfter(self, anitem: MAT_Edge) -> None: ...
	def LinkBefore(self, anitem: MAT_Edge) -> None: ...
	def Loop(self) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def NextItem(self) -> MAT_Edge: ...
	def Number(self) -> int: ...
	def Permute(self) -> None: ...
	def Previous(self) -> None: ...
	def PreviousItem(self) -> MAT_Edge: ...
	def Unlink(self) -> None: ...

class MAT_Node(Standard_Transient):
	def __init__(self, GeomIndex: int, LinkedArc: MAT_Arc, Distance: float) -> None: ...
	def Distance(self) -> float: ...
	def GeomIndex(self) -> int: ...
	def Index(self) -> int: ...
	def Infinite(self) -> bool: ...
	def LinkedArcs(self, S: MAT_SequenceOfArc) -> None: ...
	def NearElts(self, S: MAT_SequenceOfBasicElt) -> None: ...
	def OnBasicElt(self) -> bool: ...
	def PendingNode(self) -> bool: ...
	def SetIndex(self, anIndex: int) -> None: ...
	def SetLinkedArc(self, anArc: MAT_Arc) -> None: ...

class MAT_TListNodeOfListOfBisector(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, anitem: MAT_Bisector) -> None: ...
	def Dummy(self) -> None: ...
	def GetItem(self) -> MAT_Bisector: ...
	@overload
	def Next(self) -> MAT_TListNodeOfListOfBisector: ...
	@overload
	def Next(self, atlistnode: MAT_TListNodeOfListOfBisector) -> None: ...
	@overload
	def Previous(self) -> MAT_TListNodeOfListOfBisector: ...
	@overload
	def Previous(self, atlistnode: MAT_TListNodeOfListOfBisector) -> None: ...
	def SetItem(self, anitem: MAT_Bisector) -> None: ...

class MAT_TListNodeOfListOfEdge(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, anitem: MAT_Edge) -> None: ...
	def Dummy(self) -> None: ...
	def GetItem(self) -> MAT_Edge: ...
	@overload
	def Next(self) -> MAT_TListNodeOfListOfEdge: ...
	@overload
	def Next(self, atlistnode: MAT_TListNodeOfListOfEdge) -> None: ...
	@overload
	def Previous(self) -> MAT_TListNodeOfListOfEdge: ...
	@overload
	def Previous(self, atlistnode: MAT_TListNodeOfListOfEdge) -> None: ...
	def SetItem(self, anitem: MAT_Edge) -> None: ...

class MAT_Zone(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aBasicElt: MAT_BasicElt) -> None: ...
	def ArcOnFrontier(self, Index: int) -> MAT_Arc: ...
	def Limited(self) -> bool: ...
	def NoEmptyZone(self) -> bool: ...
	def NumberOfArcs(self) -> int: ...
	def Perform(self, aBasicElt: MAT_BasicElt) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

