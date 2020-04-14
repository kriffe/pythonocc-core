from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.TColStd import *

#the following typedef cannot be wrapped as is
Units_QtsSequence = NewType('Units_QtsSequence', Any)
#the following typedef cannot be wrapped as is
Units_TksSequence = NewType('Units_TksSequence', Any)
#the following typedef cannot be wrapped as is
Units_UtsSequence = NewType('Units_UtsSequence', Any)

class units:
	@staticmethod
	def Convert(avalue: float, afirstunit: str, asecondunit: str) -> float: ...
	@staticmethod
	def DictionaryOfUnits(amode: Optional[bool] = False) -> Units_UnitsDictionary: ...
	@staticmethod
	def Dimensions(aType: str) -> Units_Dimensions: ...
	@staticmethod
	def FirstQuantity(aunit: str) -> str: ...
	@overload
	@staticmethod
	def FromSI(aData: float, aUnit: str) -> float: ...
	@overload
	@staticmethod
	def FromSI(aData: float, aUnit: str, aDim: Units_Dimensions) -> float: ...
	@staticmethod
	def LexiconFile(afile: str) -> None: ...
	@staticmethod
	def LexiconFormula() -> Units_Lexicon: ...
	@staticmethod
	def LexiconUnits(amode: Optional[bool] = True) -> Units_Lexicon: ...
	@staticmethod
	def NullDimensions() -> Units_Dimensions: ...
	@staticmethod
	def Quantity(aquantity: str) -> Units_Quantity: ...
	@overload
	@staticmethod
	def ToSI(aData: float, aUnit: str) -> float: ...
	@overload
	@staticmethod
	def ToSI(aData: float, aUnit: str, aDim: Units_Dimensions) -> float: ...
	@staticmethod
	def UnitsFile(afile: str) -> None: ...

class Units_Explorer:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aunitssystem: Units_UnitsSystem) -> None: ...
	@overload
	def __init__(self, aunitsdictionary: Units_UnitsDictionary) -> None: ...
	@overload
	def __init__(self, aunitssystem: Units_UnitsSystem, aquantity: str) -> None: ...
	@overload
	def __init__(self, aunitsdictionary: Units_UnitsDictionary, aquantity: str) -> None: ...
	@overload
	def Init(self, aunitssystem: Units_UnitsSystem) -> None: ...
	@overload
	def Init(self, aunitsdictionary: Units_UnitsDictionary) -> None: ...
	@overload
	def Init(self, aunitssystem: Units_UnitsSystem, aquantity: str) -> None: ...
	@overload
	def Init(self, aunitsdictionary: Units_UnitsDictionary, aquantity: str) -> None: ...
	def IsActive(self) -> bool: ...
	def MoreQuantity(self) -> bool: ...
	def MoreUnit(self) -> bool: ...
	def NextQuantity(self) -> None: ...
	def NextUnit(self) -> None: ...
	def Quantity(self) -> TCollection_AsciiString: ...
	def Unit(self) -> TCollection_AsciiString: ...

class Units_Lexicon(Standard_Transient):
	def __init__(self) -> None: ...
	def AddToken(self, aword: str, amean: str, avalue: float) -> None: ...
	def Creates(self) -> None: ...
	def Dump(self) -> None: ...
	def Sequence(self) -> Units_TokensSequence: ...

class Units_Measurement:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, avalue: float, atoken: Units_Token) -> None: ...
	@overload
	def __init__(self, avalue: float, aunit: str) -> None: ...
	def Add(self, ameasurement: Units_Measurement) -> Units_Measurement: ...
	def Convert(self, aunit: str) -> None: ...
	@overload
	def Divide(self, ameasurement: Units_Measurement) -> Units_Measurement: ...
	@overload
	def Divide(self, avalue: float) -> Units_Measurement: ...
	def Dump(self) -> None: ...
	def Fractional(self) -> Units_Measurement: ...
	def HasToken(self) -> bool: ...
	def Integer(self) -> Units_Measurement: ...
	def Measurement(self) -> float: ...
	@overload
	def Multiply(self, ameasurement: Units_Measurement) -> Units_Measurement: ...
	@overload
	def Multiply(self, avalue: float) -> Units_Measurement: ...
	def Power(self, anexponent: float) -> Units_Measurement: ...
	def Subtract(self, ameasurement: Units_Measurement) -> Units_Measurement: ...
	def Token(self) -> Units_Token: ...

class Units_Sentence:
	def __init__(self, alexicon: Units_Lexicon, astring: str) -> None: ...
	def Dump(self) -> None: ...
	def Evaluate(self) -> Units_Token: ...
	def IsDone(self) -> bool: ...
	@overload
	def Sequence(self) -> Units_TokensSequence: ...
	@overload
	def Sequence(self, asequenceoftokens: Units_TokensSequence) -> None: ...
	def SetConstants(self) -> None: ...

class Units_Token(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aword: str) -> None: ...
	@overload
	def __init__(self, atoken: Units_Token) -> None: ...
	@overload
	def __init__(self, aword: str, amean: str) -> None: ...
	@overload
	def __init__(self, aword: str, amean: str, avalue: float) -> None: ...
	@overload
	def __init__(self, aword: str, amean: str, avalue: float, adimension: Units_Dimensions) -> None: ...
	@overload
	def Add(self, aninteger: int) -> Units_Token: ...
	@overload
	def Add(self, atoken: Units_Token) -> Units_Token: ...
	def Creates(self) -> Units_Token: ...
	@overload
	def Dimensions(self) -> Units_Dimensions: ...
	@overload
	def Dimensions(self, adimensions: Units_Dimensions) -> None: ...
	def Divide(self, atoken: Units_Token) -> Units_Token: ...
	def Divided(self, avalue: float) -> float: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	@overload
	def IsEqual(self, astring: str) -> bool: ...
	@overload
	def IsEqual(self, atoken: Units_Token) -> bool: ...
	@overload
	def IsGreater(self, astring: str) -> bool: ...
	@overload
	def IsGreater(self, atoken: Units_Token) -> bool: ...
	def IsGreaterOrEqual(self, atoken: Units_Token) -> bool: ...
	def IsLessOrEqual(self, astring: str) -> bool: ...
	@overload
	def IsNotEqual(self, astring: str) -> bool: ...
	@overload
	def IsNotEqual(self, atoken: Units_Token) -> bool: ...
	def Length(self) -> int: ...
	@overload
	def Mean(self) -> TCollection_AsciiString: ...
	@overload
	def Mean(self, amean: str) -> None: ...
	def Multiplied(self, avalue: float) -> float: ...
	def Multiply(self, atoken: Units_Token) -> Units_Token: ...
	@overload
	def Power(self, atoken: Units_Token) -> Units_Token: ...
	@overload
	def Power(self, anexponent: float) -> Units_Token: ...
	def Subtract(self, atoken: Units_Token) -> Units_Token: ...
	def Update(self, amean: str) -> None: ...
	@overload
	def Value(self) -> float: ...
	@overload
	def Value(self, avalue: float) -> None: ...
	@overload
	def Word(self) -> TCollection_AsciiString: ...
	@overload
	def Word(self, aword: str) -> None: ...

class Units_Unit(Standard_Transient):
	@overload
	def __init__(self, aname: str, asymbol: str, avalue: float, aquantity: Units_Quantity) -> None: ...
	@overload
	def __init__(self, aname: str, asymbol: str) -> None: ...
	@overload
	def __init__(self, aname: str) -> None: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	def IsEqual(self, astring: str) -> bool: ...
	def Name(self) -> TCollection_AsciiString: ...
	@overload
	def Quantity(self) -> Units_Quantity: ...
	@overload
	def Quantity(self, aquantity: Units_Quantity) -> None: ...
	def Symbol(self, asymbol: str) -> None: ...
	def SymbolsSequence(self) -> TColStd_HSequenceOfHAsciiString: ...
	def Token(self) -> Units_Token: ...
	@overload
	def Value(self) -> float: ...
	@overload
	def Value(self, avalue: float) -> None: ...

class Units_UnitsDictionary(Standard_Transient):
	def __init__(self) -> None: ...
	def ActiveUnit(self, aquantity: str) -> TCollection_AsciiString: ...
	def Creates(self) -> None: ...
	@overload
	def Dump(self, alevel: int) -> None: ...
	@overload
	def Dump(self, adimensions: Units_Dimensions) -> None: ...
	def Sequence(self) -> Units_QuantitiesSequence: ...

class Units_UnitsSystem(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aName: str, Verbose: Optional[bool] = False) -> None: ...
	def Activate(self, aquantity: str, aunit: str) -> None: ...
	def Activates(self) -> None: ...
	def ActiveUnit(self, aquantity: str) -> TCollection_AsciiString: ...
	def ActiveUnitsSequence(self) -> TColStd_HSequenceOfInteger: ...
	def ConvertSIValueToUserSystem(self, aquantity: str, avalue: float) -> float: ...
	def ConvertUserSystemValueToSI(self, aquantity: str, avalue: float) -> float: ...
	def ConvertValueToUserSystem(self, aquantity: str, avalue: float, aunit: str) -> float: ...
	def Dump(self) -> None: ...
	def IsEmpty(self) -> bool: ...
	def QuantitiesSequence(self) -> Units_QuantitiesSequence: ...
	def Remove(self, aquantity: str, aunit: str) -> None: ...
	def Specify(self, aquantity: str, aunit: str) -> None: ...

class Units_MathSentence(Units_Sentence):
	def __init__(self, astring: str) -> None: ...

class Units_ShiftedToken(Units_Token):
	def __init__(self, aword: str, amean: str, avalue: float, amove: float, adimensions: Units_Dimensions) -> None: ...
	def Creates(self) -> Units_Token: ...
	def Divided(self, avalue: float) -> float: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	def Move(self) -> float: ...
	def Multiplied(self, avalue: float) -> float: ...

class Units_ShiftedUnit(Units_Unit):
	@overload
	def __init__(self, aname: str, asymbol: str, avalue: float, amove: float, aquantity: Units_Quantity) -> None: ...
	@overload
	def __init__(self, aname: str, asymbol: str) -> None: ...
	@overload
	def __init__(self, aname: str) -> None: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	@overload
	def Move(self, amove: float) -> None: ...
	@overload
	def Move(self) -> float: ...
	def Token(self) -> Units_Token: ...

class Units_UnitSentence(Units_Sentence):
	@overload
	def __init__(self, astring: str) -> None: ...
	@overload
	def __init__(self, astring: str, aquantitiessequence: Units_QuantitiesSequence) -> None: ...
	def Analyse(self) -> None: ...
	def SetUnits(self, aquantitiessequence: Units_QuantitiesSequence) -> None: ...

class Units_UnitsLexicon(Units_Lexicon):
	def __init__(self) -> None: ...
	def Creates(self, amode: Optional[bool] = True) -> None: ...
	def Dump(self) -> None: ...

#classnotwrapped
class Units_Quantity: ...

#classnotwrapped
class Units_Dimensions: ...

# harray1 classes
# harray2 classes
# hsequence classes

class Units_TokensSequence(Units_TksSequence, Standard_Transient):
    def __init__(self) -> None: ...
    def __init__(self, other: Units_TksSequence) -> None: ...
    def Sequence(self) -> Units_TksSequence: ...
    def Append(self, theSequence: Units_TksSequence) -> None: ...


class Units_QuantitiesSequence(Units_QtsSequence, Standard_Transient):
    def __init__(self) -> None: ...
    def __init__(self, other: Units_QtsSequence) -> None: ...
    def Sequence(self) -> Units_QtsSequence: ...
    def Append(self, theSequence: Units_QtsSequence) -> None: ...


class Units_UnitsSequence(Units_UtsSequence, Standard_Transient):
    def __init__(self) -> None: ...
    def __init__(self, other: Units_UtsSequence) -> None: ...
    def Sequence(self) -> Units_UtsSequence: ...
    def Append(self, theSequence: Units_UtsSequence) -> None: ...


units_Convert = units.Convert
units_DictionaryOfUnits = units.DictionaryOfUnits
units_Dimensions = units.Dimensions
units_FirstQuantity = units.FirstQuantity
units_FromSI = units.FromSI
units_FromSI = units.FromSI
units_LexiconFile = units.LexiconFile
units_LexiconFormula = units.LexiconFormula
units_LexiconUnits = units.LexiconUnits
units_NullDimensions = units.NullDimensions
units_Quantity = units.Quantity
units_ToSI = units.ToSI
units_ToSI = units.ToSI
units_UnitsFile = units.UnitsFile
