from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.TColStd import *

#the following typedef cannot be wrapped as is
Message_HArrayOfMsg = NewType('Message_HArrayOfMsg', Any)
#the following typedef cannot be wrapped as is
Message_ListIteratorOfListOfMsg = NewType('Message_ListIteratorOfListOfMsg', Any)
#the following typedef cannot be wrapped as is
Message_ListOfAlert = NewType('Message_ListOfAlert', Any)
#the following typedef cannot be wrapped as is
Message_ListOfMsg = NewType('Message_ListOfMsg', Any)
#the following typedef cannot be wrapped as is
Message_SequenceOfPrinters = NewType('Message_SequenceOfPrinters', Any)
#the following typedef cannot be wrapped as is
Message_SequenceOfProgressScale = NewType('Message_SequenceOfProgressScale', Any)

class Message_Status(IntEnum):
	Message_None: int = ...
	Message_Done1: int = ...
	Message_Done2: int = ...
	Message_Done3: int = ...
	Message_Done4: int = ...
	Message_Done5: int = ...
	Message_Done6: int = ...
	Message_Done7: int = ...
	Message_Done8: int = ...
	Message_Done9: int = ...
	Message_Done10: int = ...
	Message_Done11: int = ...
	Message_Done12: int = ...
	Message_Done13: int = ...
	Message_Done14: int = ...
	Message_Done15: int = ...
	Message_Done16: int = ...
	Message_Done17: int = ...
	Message_Done18: int = ...
	Message_Done19: int = ...
	Message_Done20: int = ...
	Message_Done21: int = ...
	Message_Done22: int = ...
	Message_Done23: int = ...
	Message_Done24: int = ...
	Message_Done25: int = ...
	Message_Done26: int = ...
	Message_Done27: int = ...
	Message_Done28: int = ...
	Message_Done29: int = ...
	Message_Done30: int = ...
	Message_Done31: int = ...
	Message_Done32: int = ...
	Message_Warn1: int = ...
	Message_Warn2: int = ...
	Message_Warn3: int = ...
	Message_Warn4: int = ...
	Message_Warn5: int = ...
	Message_Warn6: int = ...
	Message_Warn7: int = ...
	Message_Warn8: int = ...
	Message_Warn9: int = ...
	Message_Warn10: int = ...
	Message_Warn11: int = ...
	Message_Warn12: int = ...
	Message_Warn13: int = ...
	Message_Warn14: int = ...
	Message_Warn15: int = ...
	Message_Warn16: int = ...
	Message_Warn17: int = ...
	Message_Warn18: int = ...
	Message_Warn19: int = ...
	Message_Warn20: int = ...
	Message_Warn21: int = ...
	Message_Warn22: int = ...
	Message_Warn23: int = ...
	Message_Warn24: int = ...
	Message_Warn25: int = ...
	Message_Warn26: int = ...
	Message_Warn27: int = ...
	Message_Warn28: int = ...
	Message_Warn29: int = ...
	Message_Warn30: int = ...
	Message_Warn31: int = ...
	Message_Warn32: int = ...
	Message_Alarm1: int = ...
	Message_Alarm2: int = ...
	Message_Alarm3: int = ...
	Message_Alarm4: int = ...
	Message_Alarm5: int = ...
	Message_Alarm6: int = ...
	Message_Alarm7: int = ...
	Message_Alarm8: int = ...
	Message_Alarm9: int = ...
	Message_Alarm10: int = ...
	Message_Alarm11: int = ...
	Message_Alarm12: int = ...
	Message_Alarm13: int = ...
	Message_Alarm14: int = ...
	Message_Alarm15: int = ...
	Message_Alarm16: int = ...
	Message_Alarm17: int = ...
	Message_Alarm18: int = ...
	Message_Alarm19: int = ...
	Message_Alarm20: int = ...
	Message_Alarm21: int = ...
	Message_Alarm22: int = ...
	Message_Alarm23: int = ...
	Message_Alarm24: int = ...
	Message_Alarm25: int = ...
	Message_Alarm26: int = ...
	Message_Alarm27: int = ...
	Message_Alarm28: int = ...
	Message_Alarm29: int = ...
	Message_Alarm30: int = ...
	Message_Alarm31: int = ...
	Message_Alarm32: int = ...
	Message_Fail1: int = ...
	Message_Fail2: int = ...
	Message_Fail3: int = ...
	Message_Fail4: int = ...
	Message_Fail5: int = ...
	Message_Fail6: int = ...
	Message_Fail7: int = ...
	Message_Fail8: int = ...
	Message_Fail9: int = ...
	Message_Fail10: int = ...
	Message_Fail11: int = ...
	Message_Fail12: int = ...
	Message_Fail13: int = ...
	Message_Fail14: int = ...
	Message_Fail15: int = ...
	Message_Fail16: int = ...
	Message_Fail17: int = ...
	Message_Fail18: int = ...
	Message_Fail19: int = ...
	Message_Fail20: int = ...
	Message_Fail21: int = ...
	Message_Fail22: int = ...
	Message_Fail23: int = ...
	Message_Fail24: int = ...
	Message_Fail25: int = ...
	Message_Fail26: int = ...
	Message_Fail27: int = ...
	Message_Fail28: int = ...
	Message_Fail29: int = ...
	Message_Fail30: int = ...
	Message_Fail31: int = ...
	Message_Fail32: int = ...
Message_None = Message_Status.Message_None
Message_Done1 = Message_Status.Message_Done1
Message_Done2 = Message_Status.Message_Done2
Message_Done3 = Message_Status.Message_Done3
Message_Done4 = Message_Status.Message_Done4
Message_Done5 = Message_Status.Message_Done5
Message_Done6 = Message_Status.Message_Done6
Message_Done7 = Message_Status.Message_Done7
Message_Done8 = Message_Status.Message_Done8
Message_Done9 = Message_Status.Message_Done9
Message_Done10 = Message_Status.Message_Done10
Message_Done11 = Message_Status.Message_Done11
Message_Done12 = Message_Status.Message_Done12
Message_Done13 = Message_Status.Message_Done13
Message_Done14 = Message_Status.Message_Done14
Message_Done15 = Message_Status.Message_Done15
Message_Done16 = Message_Status.Message_Done16
Message_Done17 = Message_Status.Message_Done17
Message_Done18 = Message_Status.Message_Done18
Message_Done19 = Message_Status.Message_Done19
Message_Done20 = Message_Status.Message_Done20
Message_Done21 = Message_Status.Message_Done21
Message_Done22 = Message_Status.Message_Done22
Message_Done23 = Message_Status.Message_Done23
Message_Done24 = Message_Status.Message_Done24
Message_Done25 = Message_Status.Message_Done25
Message_Done26 = Message_Status.Message_Done26
Message_Done27 = Message_Status.Message_Done27
Message_Done28 = Message_Status.Message_Done28
Message_Done29 = Message_Status.Message_Done29
Message_Done30 = Message_Status.Message_Done30
Message_Done31 = Message_Status.Message_Done31
Message_Done32 = Message_Status.Message_Done32
Message_Warn1 = Message_Status.Message_Warn1
Message_Warn2 = Message_Status.Message_Warn2
Message_Warn3 = Message_Status.Message_Warn3
Message_Warn4 = Message_Status.Message_Warn4
Message_Warn5 = Message_Status.Message_Warn5
Message_Warn6 = Message_Status.Message_Warn6
Message_Warn7 = Message_Status.Message_Warn7
Message_Warn8 = Message_Status.Message_Warn8
Message_Warn9 = Message_Status.Message_Warn9
Message_Warn10 = Message_Status.Message_Warn10
Message_Warn11 = Message_Status.Message_Warn11
Message_Warn12 = Message_Status.Message_Warn12
Message_Warn13 = Message_Status.Message_Warn13
Message_Warn14 = Message_Status.Message_Warn14
Message_Warn15 = Message_Status.Message_Warn15
Message_Warn16 = Message_Status.Message_Warn16
Message_Warn17 = Message_Status.Message_Warn17
Message_Warn18 = Message_Status.Message_Warn18
Message_Warn19 = Message_Status.Message_Warn19
Message_Warn20 = Message_Status.Message_Warn20
Message_Warn21 = Message_Status.Message_Warn21
Message_Warn22 = Message_Status.Message_Warn22
Message_Warn23 = Message_Status.Message_Warn23
Message_Warn24 = Message_Status.Message_Warn24
Message_Warn25 = Message_Status.Message_Warn25
Message_Warn26 = Message_Status.Message_Warn26
Message_Warn27 = Message_Status.Message_Warn27
Message_Warn28 = Message_Status.Message_Warn28
Message_Warn29 = Message_Status.Message_Warn29
Message_Warn30 = Message_Status.Message_Warn30
Message_Warn31 = Message_Status.Message_Warn31
Message_Warn32 = Message_Status.Message_Warn32
Message_Alarm1 = Message_Status.Message_Alarm1
Message_Alarm2 = Message_Status.Message_Alarm2
Message_Alarm3 = Message_Status.Message_Alarm3
Message_Alarm4 = Message_Status.Message_Alarm4
Message_Alarm5 = Message_Status.Message_Alarm5
Message_Alarm6 = Message_Status.Message_Alarm6
Message_Alarm7 = Message_Status.Message_Alarm7
Message_Alarm8 = Message_Status.Message_Alarm8
Message_Alarm9 = Message_Status.Message_Alarm9
Message_Alarm10 = Message_Status.Message_Alarm10
Message_Alarm11 = Message_Status.Message_Alarm11
Message_Alarm12 = Message_Status.Message_Alarm12
Message_Alarm13 = Message_Status.Message_Alarm13
Message_Alarm14 = Message_Status.Message_Alarm14
Message_Alarm15 = Message_Status.Message_Alarm15
Message_Alarm16 = Message_Status.Message_Alarm16
Message_Alarm17 = Message_Status.Message_Alarm17
Message_Alarm18 = Message_Status.Message_Alarm18
Message_Alarm19 = Message_Status.Message_Alarm19
Message_Alarm20 = Message_Status.Message_Alarm20
Message_Alarm21 = Message_Status.Message_Alarm21
Message_Alarm22 = Message_Status.Message_Alarm22
Message_Alarm23 = Message_Status.Message_Alarm23
Message_Alarm24 = Message_Status.Message_Alarm24
Message_Alarm25 = Message_Status.Message_Alarm25
Message_Alarm26 = Message_Status.Message_Alarm26
Message_Alarm27 = Message_Status.Message_Alarm27
Message_Alarm28 = Message_Status.Message_Alarm28
Message_Alarm29 = Message_Status.Message_Alarm29
Message_Alarm30 = Message_Status.Message_Alarm30
Message_Alarm31 = Message_Status.Message_Alarm31
Message_Alarm32 = Message_Status.Message_Alarm32
Message_Fail1 = Message_Status.Message_Fail1
Message_Fail2 = Message_Status.Message_Fail2
Message_Fail3 = Message_Status.Message_Fail3
Message_Fail4 = Message_Status.Message_Fail4
Message_Fail5 = Message_Status.Message_Fail5
Message_Fail6 = Message_Status.Message_Fail6
Message_Fail7 = Message_Status.Message_Fail7
Message_Fail8 = Message_Status.Message_Fail8
Message_Fail9 = Message_Status.Message_Fail9
Message_Fail10 = Message_Status.Message_Fail10
Message_Fail11 = Message_Status.Message_Fail11
Message_Fail12 = Message_Status.Message_Fail12
Message_Fail13 = Message_Status.Message_Fail13
Message_Fail14 = Message_Status.Message_Fail14
Message_Fail15 = Message_Status.Message_Fail15
Message_Fail16 = Message_Status.Message_Fail16
Message_Fail17 = Message_Status.Message_Fail17
Message_Fail18 = Message_Status.Message_Fail18
Message_Fail19 = Message_Status.Message_Fail19
Message_Fail20 = Message_Status.Message_Fail20
Message_Fail21 = Message_Status.Message_Fail21
Message_Fail22 = Message_Status.Message_Fail22
Message_Fail23 = Message_Status.Message_Fail23
Message_Fail24 = Message_Status.Message_Fail24
Message_Fail25 = Message_Status.Message_Fail25
Message_Fail26 = Message_Status.Message_Fail26
Message_Fail27 = Message_Status.Message_Fail27
Message_Fail28 = Message_Status.Message_Fail28
Message_Fail29 = Message_Status.Message_Fail29
Message_Fail30 = Message_Status.Message_Fail30
Message_Fail31 = Message_Status.Message_Fail31
Message_Fail32 = Message_Status.Message_Fail32

class Message_Gravity(IntEnum):
	Message_Trace: int = ...
	Message_Info: int = ...
	Message_Warning: int = ...
	Message_Alarm: int = ...
	Message_Fail: int = ...
Message_Trace = Message_Gravity.Message_Trace
Message_Info = Message_Gravity.Message_Info
Message_Warning = Message_Gravity.Message_Warning
Message_Alarm = Message_Gravity.Message_Alarm
Message_Fail = Message_Gravity.Message_Fail

class Message_StatusType(IntEnum):
	Message_DONE: int = ...
	Message_WARN: int = ...
	Message_ALARM: int = ...
	Message_FAIL: int = ...
Message_DONE = Message_StatusType.Message_DONE
Message_WARN = Message_StatusType.Message_WARN
Message_ALARM = Message_StatusType.Message_ALARM
Message_FAIL = Message_StatusType.Message_FAIL

class message:
	@staticmethod
	def DefaultMessenger() -> Message_Messenger: ...
	@staticmethod
	def FillTime(Hour: int, Minute: int, Second: float) -> TCollection_AsciiString: ...

class Message_Alert(Standard_Transient):
	def GetMessageKey(self) -> str: ...
	def Merge(self, theTarget: Message_Alert) -> bool: ...
	def SupportsMerge(self) -> bool: ...

class Message_Algorithm(Standard_Transient):
	def __init__(self) -> None: ...
	@overload
	def AddStatus(self, theOther: Message_Algorithm) -> None: ...
	@overload
	def AddStatus(self, theStatus: Message_ExecStatus, theOther: Message_Algorithm) -> None: ...
	def ChangeStatus(self) -> Message_ExecStatus: ...
	def ClearStatus(self) -> None: ...
	def GetMessageNumbers(self, theStatus: Message_Status) -> TColStd_HPackedMapOfInteger: ...
	def GetMessageStrings(self, theStatus: Message_Status) -> TColStd_HSequenceOfHExtendedString: ...
	def GetMessenger(self) -> Message_Messenger: ...
	def GetStatus(self) -> Message_ExecStatus: ...
	@overload
	@staticmethod
	def PrepareReport(theError: TColStd_HPackedMapOfInteger, theMaxCount: int) -> TCollection_ExtendedString: ...
	@overload
	@staticmethod
	def PrepareReport(theReportSeq: TColStd_SequenceOfHExtendedString, theMaxCount: int) -> TCollection_ExtendedString: ...
	def SendMessages(self, theTraceLevel: Optional[Message_Gravity], theMaxCount: Optional[int]) -> None: ...
	def SendStatusMessages(self, theFilter: Message_ExecStatus, theTraceLevel: Optional[Message_Gravity], theMaxCount: Optional[int]) -> None: ...
	def SetMessenger(self, theMsgr: Message_Messenger) -> None: ...
	@overload
	def SetStatus(self, theStat: Message_Status) -> None: ...
	@overload
	def SetStatus(self, theStat: Message_Status, theInt: int) -> None: ...
	@overload
	def SetStatus(self, theStat: Message_Status, theStr: str, noRepetitions: Optional[bool]) -> None: ...
	@overload
	def SetStatus(self, theStat: Message_Status, theStr: TCollection_AsciiString, noRepetitions: Optional[bool]) -> None: ...
	@overload
	def SetStatus(self, theStat: Message_Status, theStr: TCollection_HAsciiString, noRepetitions: Optional[bool]) -> None: ...
	@overload
	def SetStatus(self, theStat: Message_Status, theStr: TCollection_ExtendedString, noRepetitions: Optional[bool]) -> None: ...
	@overload
	def SetStatus(self, theStat: Message_Status, theStr: TCollection_HExtendedString, noRepetitions: Optional[bool]) -> None: ...
	@overload
	def SetStatus(self, theStat: Message_Status, theMsg: Message_Msg) -> None: ...

class Message_ExecStatus:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, status: Message_Status) -> None: ...
	def Add(self, theOther: Message_ExecStatus) -> None: ...
	def And(self, theOther: Message_ExecStatus) -> None: ...
	@overload
	def Clear(self, status: Message_Status) -> None: ...
	@overload
	def Clear(self) -> None: ...
	def ClearAllAlarm(self) -> None: ...
	def ClearAllDone(self) -> None: ...
	def ClearAllFail(self) -> None: ...
	def ClearAllWarn(self) -> None: ...
	def IsAlarm(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def IsFail(self) -> bool: ...
	def IsSet(self, status: Message_Status) -> bool: ...
	def IsWarn(self) -> bool: ...
	@staticmethod
	def LocalStatusIndex(status: Message_Status) -> int: ...
	def Set(self, status: Message_Status) -> None: ...
	def SetAllAlarm(self) -> None: ...
	def SetAllDone(self) -> None: ...
	def SetAllFail(self) -> None: ...
	def SetAllWarn(self) -> None: ...
	@staticmethod
	def StatusByIndex(theIndex: int) -> Message_Status: ...
	@staticmethod
	def StatusIndex(status: Message_Status) -> int: ...
	@staticmethod
	def TypeOfStatus(status: Message_Status) -> Message_StatusType: ...

class Message_Messenger(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, thePrinter: Message_Printer) -> None: ...
	def AddPrinter(self, thePrinter: Message_Printer) -> bool: ...
	def ChangePrinters(self) -> Message_SequenceOfPrinters: ...
	def Printers(self) -> Message_SequenceOfPrinters: ...
	def RemovePrinter(self, thePrinter: Message_Printer) -> bool: ...
	def RemovePrinters(self, theType: Standard_Type) -> int: ...
	@overload
	def Send(self, theString: str, theGravity: Optional[Message_Gravity], putEndl: Optional[bool]) -> None: ...
	@overload
	def Send(self, theString: TCollection_AsciiString, theGravity: Optional[Message_Gravity], putEndl: Optional[bool]) -> None: ...
	@overload
	def Send(self, theString: TCollection_ExtendedString, theGravity: Optional[Message_Gravity], putEndl: Optional[bool]) -> None: ...

class Message_Msg:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theMsg: Message_Msg) -> None: ...
	@overload
	def __init__(self, theKey: str) -> None: ...
	@overload
	def __init__(self, theKey: TCollection_ExtendedString) -> None: ...
	@overload
	def Arg(self, theString: str) -> Message_Msg: ...
	@overload
	def Arg(self, theString: TCollection_AsciiString) -> Message_Msg: ...
	@overload
	def Arg(self, theString: TCollection_HAsciiString) -> Message_Msg: ...
	@overload
	def Arg(self, theString: TCollection_ExtendedString) -> Message_Msg: ...
	@overload
	def Arg(self, theString: TCollection_HExtendedString) -> Message_Msg: ...
	@overload
	def Arg(self, theInt: int) -> Message_Msg: ...
	@overload
	def Arg(self, theReal: float) -> Message_Msg: ...
	def Get(self) -> TCollection_ExtendedString: ...
	def IsEdited(self) -> bool: ...
	def Original(self) -> TCollection_ExtendedString: ...
	@overload
	def Set(self, theMsg: str) -> None: ...
	@overload
	def Set(self, theMsg: TCollection_ExtendedString) -> None: ...
	def Value(self) -> TCollection_ExtendedString: ...

class Message_MsgFile:
	@staticmethod
	def AddMsg(key: TCollection_AsciiString, text: TCollection_ExtendedString) -> bool: ...
	@staticmethod
	def HasMsg(key: TCollection_AsciiString) -> bool: ...
	@staticmethod
	def Load(theDirName: str, theFileName: str) -> bool: ...
	@staticmethod
	def LoadFile(theFName: str) -> bool: ...
	@staticmethod
	def LoadFromEnv(theEnvName: str, theFileName: str, theLangExt: Optional[str]) -> bool: ...
	@staticmethod
	def LoadFromString(theContent: str, theLength: Optional[int]) -> bool: ...
	@overload
	@staticmethod
	def Msg(key: str) -> TCollection_ExtendedString: ...
	@overload
	@staticmethod
	def Msg(key: TCollection_AsciiString) -> TCollection_ExtendedString: ...

class Message_Printer(Standard_Transient):
	def GetTraceLevel(self) -> Message_Gravity: ...
	@overload
	def Send(self, theString: TCollection_ExtendedString, theGravity: Message_Gravity, theToPutEol: bool) -> None: ...
	@overload
	def Send(self, theString: str, theGravity: Message_Gravity, theToPutEol: bool) -> None: ...
	@overload
	def Send(self, theString: TCollection_AsciiString, theGravity: Message_Gravity, theToPutEol: bool) -> None: ...
	def SetTraceLevel(self, theTraceLevel: Message_Gravity) -> None: ...

class Message_ProgressIndicator(Standard_Transient):
	def EndScope(self) -> bool: ...
	def GetNbScopes(self) -> int: ...
	def GetPosition(self) -> float: ...
	def GetScale(self) -> Tuple[float, float, float, bool]: ...
	def GetScope(self, index: int) -> Message_ProgressScale: ...
	def GetValue(self) -> float: ...
	@overload
	def Increment(self) -> None: ...
	@overload
	def Increment(self, step: float) -> None: ...
	@overload
	def NewScope(self, name: Optional[str]) -> bool: ...
	@overload
	def NewScope(self, name: TCollection_HAsciiString) -> bool: ...
	@overload
	def NewScope(self, span: float, name: Optional[str]) -> bool: ...
	@overload
	def NewScope(self, span: float, name: TCollection_HAsciiString) -> bool: ...
	@overload
	def NextScope(self, name: Optional[str]) -> bool: ...
	@overload
	def NextScope(self, span: float, name: Optional[str]) -> bool: ...
	def Reset(self) -> None: ...
	def SetInfinite(self, isInf: Optional[bool]) -> None: ...
	@overload
	def SetName(self, name: str) -> None: ...
	@overload
	def SetName(self, name: TCollection_HAsciiString) -> None: ...
	def SetRange(self, min: float, max: float) -> None: ...
	@overload
	def SetScale(self, name: str, min: float, max: float, step: float, isInf: Optional[bool]) -> None: ...
	@overload
	def SetScale(self, min: float, max: float, step: float, isInf: Optional[bool]) -> None: ...
	def SetStep(self, step: float) -> None: ...
	def SetValue(self, val: float) -> None: ...
	def Show(self, force: Optional[bool]) -> bool: ...
	def UserBreak(self) -> bool: ...

class Message_ProgressScale:
	def __init__(self) -> None: ...
	def BaseToLocal(self, val: float) -> float: ...
	def GetFirst(self) -> float: ...
	def GetInfinite(self) -> bool: ...
	def GetLast(self) -> float: ...
	def GetMax(self) -> float: ...
	def GetMin(self) -> float: ...
	def GetName(self) -> TCollection_HAsciiString: ...
	def GetStep(self) -> float: ...
	def LocalToBase(self, val: float) -> float: ...
	def SetInfinite(self, theInfinite: Optional[bool]) -> None: ...
	def SetMax(self, theMax: float) -> None: ...
	def SetMin(self, theMin: float) -> None: ...
	@overload
	def SetName(self, theName: str) -> None: ...
	@overload
	def SetName(self, theName: TCollection_HAsciiString) -> None: ...
	def SetRange(self, min: float, max: float) -> None: ...
	def SetScale(self, min: float, max: float, step: float, theInfinite: Optional[bool]) -> None: ...
	def SetSpan(self, first: float, last: float) -> None: ...
	def SetStep(self, theStep: float) -> None: ...

class Message_ProgressSentry:
	@overload
	def __init__(self, PI: Message_ProgressIndicator, name: str, min: float, max: float, step: float, isInf: Optional[bool], newScopeSpan: Optional[float]) -> None: ...
	@overload
	def __init__(self, PI: Message_ProgressIndicator, name: TCollection_HAsciiString, min: float, max: float, step: float, isInf: Optional[bool], newScopeSpan: Optional[float]) -> None: ...
	def More(self) -> bool: ...
	@overload
	def Next(self, name: Optional[str]) -> None: ...
	@overload
	def Next(self, span: float, name: Optional[str]) -> None: ...
	@overload
	def Next(self, span: float, name: TCollection_HAsciiString) -> None: ...
	def Relieve(self) -> None: ...
	def Show(self) -> None: ...

class Message_Report(Standard_Transient):
	def __init__(self) -> None: ...
	def AddAlert(self, theGravity: Message_Gravity, theAlert: Message_Alert) -> None: ...
	@overload
	def Clear(self) -> None: ...
	@overload
	def Clear(self, theGravity: Message_Gravity) -> None: ...
	@overload
	def Clear(self, theType: Standard_Type) -> None: ...
	def GetAlerts(self, theGravity: Message_Gravity) -> Message_ListOfAlert: ...
	@overload
	def HasAlert(self, theType: Standard_Type) -> bool: ...
	@overload
	def HasAlert(self, theType: Standard_Type, theGravity: Message_Gravity) -> bool: ...
	@overload
	def Merge(self, theOther: Message_Report) -> None: ...
	@overload
	def Merge(self, theOther: Message_Report, theGravity: Message_Gravity) -> None: ...
	@overload
	def SendMessages(self, theMessenger: Message_Messenger) -> None: ...
	@overload
	def SendMessages(self, theMessenger: Message_Messenger, theGravity: Message_Gravity) -> None: ...

class Message_PrinterOStream(Message_Printer):
	@overload
	def __init__(self, theTraceLevel: Optional[Message_Gravity]) -> None: ...
	@overload
	def __init__(self, theFileName: str, theDoAppend: bool, theTraceLevel: Optional[Message_Gravity]) -> None: ...
	def Close(self) -> None: ...
	def GetStream(self) -> Standard_OStream: ...
	def GetUseUtf8(self) -> bool: ...
	@overload
	def Send(self, theString: str, theGravity: Message_Gravity, putEndl: Optional[bool]) -> None: ...
	@overload
	def Send(self, theString: TCollection_AsciiString, theGravity: Message_Gravity, putEndl: Optional[bool]) -> None: ...
	@overload
	def Send(self, theString: TCollection_ExtendedString, theGravity: Message_Gravity, putEndl: Optional[bool]) -> None: ...
	def SetUseUtf8(self, useUtf8: bool) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

message_DefaultMessenger = message.DefaultMessenger
message_FillTime = message.FillTime
Message_Algorithm_PrepareReport = Message_Algorithm.PrepareReport
Message_Algorithm_PrepareReport = Message_Algorithm.PrepareReport
Message_ExecStatus_LocalStatusIndex = Message_ExecStatus.LocalStatusIndex
Message_ExecStatus_StatusByIndex = Message_ExecStatus.StatusByIndex
Message_ExecStatus_StatusIndex = Message_ExecStatus.StatusIndex
Message_ExecStatus_TypeOfStatus = Message_ExecStatus.TypeOfStatus
Message_MsgFile_AddMsg = Message_MsgFile.AddMsg
Message_MsgFile_HasMsg = Message_MsgFile.HasMsg
Message_MsgFile_Load = Message_MsgFile.Load
Message_MsgFile_LoadFile = Message_MsgFile.LoadFile
Message_MsgFile_LoadFromEnv = Message_MsgFile.LoadFromEnv
Message_MsgFile_LoadFromString = Message_MsgFile.LoadFromString
Message_MsgFile_Msg = Message_MsgFile.Msg
Message_MsgFile_Msg = Message_MsgFile.Msg
