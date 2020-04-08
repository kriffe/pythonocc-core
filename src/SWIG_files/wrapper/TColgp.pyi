from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *

#the following typedef cannot be wrapped as is
TColgp_Array1OfCirc2d = NewType('TColgp_Array1OfCirc2d', Any)
#the following typedef cannot be wrapped as is
TColgp_Array1OfDir = NewType('TColgp_Array1OfDir', Any)
#the following typedef cannot be wrapped as is
TColgp_Array1OfDir2d = NewType('TColgp_Array1OfDir2d', Any)
#the following typedef cannot be wrapped as is
TColgp_Array1OfLin2d = NewType('TColgp_Array1OfLin2d', Any)
#the following typedef cannot be wrapped as is
TColgp_Array1OfPnt = NewType('TColgp_Array1OfPnt', Any)
#the following typedef cannot be wrapped as is
TColgp_Array1OfPnt2d = NewType('TColgp_Array1OfPnt2d', Any)
#the following typedef cannot be wrapped as is
TColgp_Array1OfVec = NewType('TColgp_Array1OfVec', Any)
#the following typedef cannot be wrapped as is
TColgp_Array1OfVec2d = NewType('TColgp_Array1OfVec2d', Any)
#the following typedef cannot be wrapped as is
TColgp_Array1OfXY = NewType('TColgp_Array1OfXY', Any)
#the following typedef cannot be wrapped as is
TColgp_Array1OfXYZ = NewType('TColgp_Array1OfXYZ', Any)
#the following typedef cannot be wrapped as is
TColgp_Array2OfCirc2d = NewType('TColgp_Array2OfCirc2d', Any)
#the following typedef cannot be wrapped as is
TColgp_Array2OfDir = NewType('TColgp_Array2OfDir', Any)
#the following typedef cannot be wrapped as is
TColgp_Array2OfDir2d = NewType('TColgp_Array2OfDir2d', Any)
#the following typedef cannot be wrapped as is
TColgp_Array2OfLin2d = NewType('TColgp_Array2OfLin2d', Any)
#the following typedef cannot be wrapped as is
TColgp_Array2OfPnt = NewType('TColgp_Array2OfPnt', Any)
#the following typedef cannot be wrapped as is
TColgp_Array2OfPnt2d = NewType('TColgp_Array2OfPnt2d', Any)
#the following typedef cannot be wrapped as is
TColgp_Array2OfVec = NewType('TColgp_Array2OfVec', Any)
#the following typedef cannot be wrapped as is
TColgp_Array2OfVec2d = NewType('TColgp_Array2OfVec2d', Any)
#the following typedef cannot be wrapped as is
TColgp_Array2OfXY = NewType('TColgp_Array2OfXY', Any)
#the following typedef cannot be wrapped as is
TColgp_Array2OfXYZ = NewType('TColgp_Array2OfXYZ', Any)
#the following typedef cannot be wrapped as is
TColgp_SequenceOfArray1OfPnt2d = NewType('TColgp_SequenceOfArray1OfPnt2d', Any)
#the following typedef cannot be wrapped as is
TColgp_SequenceOfAx1 = NewType('TColgp_SequenceOfAx1', Any)
#the following typedef cannot be wrapped as is
TColgp_SequenceOfDir = NewType('TColgp_SequenceOfDir', Any)
#the following typedef cannot be wrapped as is
TColgp_SequenceOfDir2d = NewType('TColgp_SequenceOfDir2d', Any)
#the following typedef cannot be wrapped as is
TColgp_SequenceOfPnt = NewType('TColgp_SequenceOfPnt', Any)
#the following typedef cannot be wrapped as is
TColgp_SequenceOfPnt2d = NewType('TColgp_SequenceOfPnt2d', Any)
#the following typedef cannot be wrapped as is
TColgp_SequenceOfVec = NewType('TColgp_SequenceOfVec', Any)
#the following typedef cannot be wrapped as is
TColgp_SequenceOfVec2d = NewType('TColgp_SequenceOfVec2d', Any)
#the following typedef cannot be wrapped as is
TColgp_SequenceOfXY = NewType('TColgp_SequenceOfXY', Any)
#the following typedef cannot be wrapped as is
TColgp_SequenceOfXYZ = NewType('TColgp_SequenceOfXYZ', Any)
