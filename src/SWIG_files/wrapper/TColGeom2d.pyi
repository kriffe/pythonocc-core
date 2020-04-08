from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom2d import *

#the following typedef cannot be wrapped as is
TColGeom2d_Array1OfBSplineCurve = NewType('TColGeom2d_Array1OfBSplineCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom2d_Array1OfBezierCurve = NewType('TColGeom2d_Array1OfBezierCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom2d_Array1OfCurve = NewType('TColGeom2d_Array1OfCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom2d_SequenceOfBoundedCurve = NewType('TColGeom2d_SequenceOfBoundedCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom2d_SequenceOfCurve = NewType('TColGeom2d_SequenceOfCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom2d_SequenceOfGeometry = NewType('TColGeom2d_SequenceOfGeometry', Any)
