from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

#the following typedef cannot be wrapped as is
BVH_Array2d = NewType('BVH_Array2d', Any)
#the following typedef cannot be wrapped as is
BVH_Array2f = NewType('BVH_Array2f', Any)
#the following typedef cannot be wrapped as is
BVH_Array2i = NewType('BVH_Array2i', Any)
#the following typedef cannot be wrapped as is
BVH_Array3d = NewType('BVH_Array3d', Any)
#the following typedef cannot be wrapped as is
BVH_Array3f = NewType('BVH_Array3f', Any)
#the following typedef cannot be wrapped as is
BVH_Array3i = NewType('BVH_Array3i', Any)
#the following typedef cannot be wrapped as is
BVH_Array4d = NewType('BVH_Array4d', Any)
#the following typedef cannot be wrapped as is
BVH_Array4f = NewType('BVH_Array4f', Any)
#the following typedef cannot be wrapped as is
BVH_Array4i = NewType('BVH_Array4i', Any)
#the following typedef cannot be wrapped as is
BVH_EncodedLink = NewType('BVH_EncodedLink', Any)
#the following typedef cannot be wrapped as is
BVH_Mat4d = NewType('BVH_Mat4d', Any)
#the following typedef cannot be wrapped as is
BVH_Mat4f = NewType('BVH_Mat4f', Any)
#the following typedef cannot be wrapped as is
BVH_PrimitiveSet3d = NewType('BVH_PrimitiveSet3d', Any)
#the following typedef cannot be wrapped as is
BVH_Vec2d = NewType('BVH_Vec2d', Any)
#the following typedef cannot be wrapped as is
BVH_Vec2f = NewType('BVH_Vec2f', Any)
#the following typedef cannot be wrapped as is
BVH_Vec2i = NewType('BVH_Vec2i', Any)
#the following typedef cannot be wrapped as is
BVH_Vec3d = NewType('BVH_Vec3d', Any)
#the following typedef cannot be wrapped as is
BVH_Vec3f = NewType('BVH_Vec3f', Any)
#the following typedef cannot be wrapped as is
BVH_Vec3i = NewType('BVH_Vec3i', Any)
#the following typedef cannot be wrapped as is
BVH_Vec4d = NewType('BVH_Vec4d', Any)
#the following typedef cannot be wrapped as is
BVH_Vec4f = NewType('BVH_Vec4f', Any)
#the following typedef cannot be wrapped as is
BVH_Vec4i = NewType('BVH_Vec4i', Any)

class BVH_AxisSelector:
	@staticmethod
	def MainAxis(self, theSize: BVH_VecNt) -> int: ...

class BVH_Tree():
	def __init__(self) -> None: ...
	@overload
	def AddInnerNode(self, theMinPoint: BVH_VecNt, theMaxPoint: BVH_VecNt, theLftChild: int, theRghChild: int) -> False: ...
	@overload
	def AddInnerNode(self, theLftChild: int, theRghChild: int) -> False: ...
	@overload
	def AddLeafNode(self, theMinPoint: BVH_VecNt, theMaxPoint: BVH_VecNt, theBegElem: int, theEndElem: int) -> False: ...
	@overload
	def AddLeafNode(self, theBegElem: int, theEndElem: int) -> False: ...
	def Clear(self) -> None: ...
	def CollapseToQuadTree(self) -> False: ...
	def EstimateSAH(self) -> False: ...
	def Reserve(self, theNbNodes: int) -> None: ...
	def SetInner(self, theNodeIndex: int) -> None: ...
	def SetOuter(self, theNodeIndex: int) -> None: ...

class BVH_Tree():
	def __init__(self) -> None: ...

#classnotwrapped
class BVH_Tools:
	pass

#classnotwrapped
class BVH_BuildTool:
	pass

#classnotwrapped
class BVH_BuildThread:
	pass

#classnotwrapped
class BVH_Sorter:
	pass

#classnotwrapped
class BVH_ObjectSet:
	pass

#classnotwrapped
class BVH_Box:
	pass

#classnotwrapped
class CenterAxis:
	pass

#classnotwrapped
class SurfaceCalculator:
	pass

#classnotwrapped
class BoxMinMax:
	pass

#classnotwrapped
class BVH_Distance:
	pass

#classnotwrapped
class BVH_ObjectTransient:
	pass

#classnotwrapped
class BVH_Object:
	pass

#classnotwrapped
class BVH_QuickSorter:
	pass

#classnotwrapped
class BVH_Set:
	pass

#classnotwrapped
class BVH_SpatialMedianBuilder:
	pass

#classnotwrapped
class BVH_Tree:
	pass

#classnotwrapped
class BVH_PrimitiveSet:
	pass

#classnotwrapped
class BVH_BuildQueue:
	pass

#classnotwrapped
class BVH_BuilderTransient:
	pass

#classnotwrapped
class BVH_Builder:
	pass

#classnotwrapped
class BVH_Properties:
	pass

#classnotwrapped
class BVH_Transform:
	pass

#classnotwrapped
class MatrixOp:
	pass

#classnotwrapped
class UnitVector:
	pass

#classnotwrapped
class BVH_RadixSorter:
	pass

#classnotwrapped
class BitPredicate:
	pass

#classnotwrapped
class BitComparator:
	pass

#classnotwrapped
class RadixSorter:
	pass

#classnotwrapped
class VectorType:
	pass

#classnotwrapped
class MatrixType:
	pass

#classnotwrapped
class ArrayType:
	pass

#classnotwrapped
class VecComp:
	pass

#classnotwrapped
class Array:
	pass

#classnotwrapped
class BVH_Triangulation:
	pass

#classnotwrapped
class BVH_PairDistance:
	pass

#classnotwrapped
class BVH_TreeBaseTransient:
	pass

#classnotwrapped
class BVH_TreeBase:
	pass

#classnotwrapped
class BVH_QuadTree:
	pass

#classnotwrapped
class BVH_BinaryTree:
	pass

#classnotwrapped
class BVH_SweepPlaneBuilder:
	pass

#classnotwrapped
class BVH_BaseTraverse:
	pass

#classnotwrapped
class BVH_Traverse:
	pass

#classnotwrapped
class BVH_PairTraverse:
	pass

#classnotwrapped
class BVH_BoxSet:
	pass

#classnotwrapped
class BVH_Geometry:
	pass

#classnotwrapped
class BVH_QueueBuilder:
	pass

#classnotwrapped
class BVH_DistanceField:
	pass

#classnotwrapped
class BVH_LinearBuilder:
	pass

#classnotwrapped
class BoundData:
	pass

#classnotwrapped
class UpdateBoundTask:
	pass

#classnotwrapped
class BVH_Bin:
	pass

#classnotwrapped
class BVH_BinnedBuilder:
	pass

#classnotwrapped
class BVH_AxisSelector:
	pass

# harray1 classes
# harray2 classes
# harray2 classes

