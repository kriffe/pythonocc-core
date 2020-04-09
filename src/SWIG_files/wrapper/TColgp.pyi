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

# harray1 classes
class TColgp_HArray1OfVec(TColgp_Array1OfVec, Standard_Transient): ...

class TColgp_HArray1OfXY(TColgp_Array1OfXY, Standard_Transient): ...

class TColgp_HArray1OfCirc2d(TColgp_Array1OfCirc2d, Standard_Transient): ...

class TColgp_HArray1OfPnt2d(TColgp_Array1OfPnt2d, Standard_Transient): ...

class TColgp_HArray1OfDir(TColgp_Array1OfDir, Standard_Transient): ...

class TColgp_HArray1OfLin2d(TColgp_Array1OfLin2d, Standard_Transient): ...

class TColgp_HArray1OfPnt(TColgp_Array1OfPnt, Standard_Transient): ...

class TColgp_HArray1OfXYZ(TColgp_Array1OfXYZ, Standard_Transient): ...

class TColgp_HArray1OfVec2d(TColgp_Array1OfVec2d, Standard_Transient): ...

class TColgp_HArray1OfDir2d(TColgp_Array1OfDir2d, Standard_Transient): ...

# harray2 classes

class TColgp_HArray2OfLin2d(TColgp_Array2OfLin2d, Standard_Transient): ...


class TColgp_HArray2OfVec(TColgp_Array2OfVec, Standard_Transient): ...


class TColgp_HArray2OfCirc2d(TColgp_Array2OfCirc2d, Standard_Transient): ...


class TColgp_HArray2OfPnt2d(TColgp_Array2OfPnt2d, Standard_Transient): ...


class TColgp_HArray2OfDir2d(TColgp_Array2OfDir2d, Standard_Transient): ...


class TColgp_HArray2OfDir(TColgp_Array2OfDir, Standard_Transient): ...


class TColgp_HArray2OfPnt(TColgp_Array2OfPnt, Standard_Transient): ...


class TColgp_HArray2OfVec2d(TColgp_Array2OfVec2d, Standard_Transient): ...


class TColgp_HArray2OfXYZ(TColgp_Array2OfXYZ, Standard_Transient): ...


class TColgp_HArray2OfXY(TColgp_Array2OfXY, Standard_Transient): ...

# harray2 classes

class TColgp_HSequenceOfXY(TColgp_SequenceOfXY, Standard_Transient): ...


class TColgp_HSequenceOfPnt2d(TColgp_SequenceOfPnt2d, Standard_Transient): ...


class TColgp_HSequenceOfPnt(TColgp_SequenceOfPnt, Standard_Transient): ...


class TColgp_HSequenceOfXYZ(TColgp_SequenceOfXYZ, Standard_Transient): ...


class TColgp_HSequenceOfVec2d(TColgp_SequenceOfVec2d, Standard_Transient): ...


class TColgp_HSequenceOfDir2d(TColgp_SequenceOfDir2d, Standard_Transient): ...


class TColgp_HSequenceOfVec(TColgp_SequenceOfVec, Standard_Transient): ...


class TColgp_HSequenceOfDir(TColgp_SequenceOfDir, Standard_Transient): ...


