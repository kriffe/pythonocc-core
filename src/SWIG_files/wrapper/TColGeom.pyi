from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *

#the following typedef cannot be wrapped as is
TColGeom_Array1OfBSplineCurve = NewType('TColGeom_Array1OfBSplineCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom_Array1OfBezierCurve = NewType('TColGeom_Array1OfBezierCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom_Array1OfCurve = NewType('TColGeom_Array1OfCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom_Array1OfSurface = NewType('TColGeom_Array1OfSurface', Any)
#the following typedef cannot be wrapped as is
TColGeom_Array2OfBezierSurface = NewType('TColGeom_Array2OfBezierSurface', Any)
#the following typedef cannot be wrapped as is
TColGeom_Array2OfSurface = NewType('TColGeom_Array2OfSurface', Any)
#the following typedef cannot be wrapped as is
TColGeom_SequenceOfBoundedCurve = NewType('TColGeom_SequenceOfBoundedCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom_SequenceOfCurve = NewType('TColGeom_SequenceOfCurve', Any)
#the following typedef cannot be wrapped as is
TColGeom_SequenceOfSurface = NewType('TColGeom_SequenceOfSurface', Any)
