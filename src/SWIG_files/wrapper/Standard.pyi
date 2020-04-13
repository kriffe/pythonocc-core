from enum import IntEnum
from typing import overload, NewType, Optional, Tuple


Standard_Address = NewType('Standard_Address', None)
Standard_Boolean = NewType('Standard_Boolean', bool)
Standard_Byte = NewType('Standard_Byte', str)
Standard_CString = NewType('Standard_CString', str)
Standard_Character = NewType('Standard_Character', str)
#the following typedef cannot be wrapped as is
Standard_ErrorHandlerCallback = NewType('Standard_ErrorHandlerCallback', Any)
Standard_ExtCharacter = NewType('Standard_ExtCharacter', str)
Standard_ExtString = NewType('Standard_ExtString', str)
#the following typedef cannot be wrapped as is
Standard_IStream = NewType('Standard_IStream', Any)
Standard_Integer = NewType('Standard_Integer', int)
#the following typedef cannot be wrapped as is
Standard_OStream = NewType('Standard_OStream', Any)
Standard_PByte = NewType('Standard_PByte', Standard_Byte)
Standard_PCharacter = NewType('Standard_PCharacter', str)
Standard_PErrorHandler = NewType('Standard_PErrorHandler', Standard_ErrorHandler)
Standard_PExtCharacter = NewType('Standard_PExtCharacter', str)
Standard_Real = NewType('Standard_Real', float)
#the following typedef cannot be wrapped as is
Standard_SStream = NewType('Standard_SStream', Any)
Standard_ShortReal = NewType('Standard_ShortReal', float)
Standard_Size = NewType('Standard_Size', int)
Standard_ThreadId = NewType('Standard_ThreadId', Standard_Size)
#the following typedef cannot be wrapped as is
Standard_Time = NewType('Standard_Time', Any)
Standard_UUID = NewType('Standard_UUID', str)
Standard_Utf16Char = NewType('Standard_Utf16Char', str)
Standard_Utf32Char = NewType('Standard_Utf32Char', str)
Standard_Utf8Char = NewType('Standard_Utf8Char', str)
Standard_Utf8UChar = NewType('Standard_Utf8UChar', str)
Standard_WideChar = NewType('Standard_WideChar', str)
int16_t = NewType('int16_t', int)
int32_t = NewType('int32_t', int)
int64_t = NewType('int64_t', int)
int8_t = NewType('int8_t', int)
uint16_t = NewType('uint16_t', int)
uint32_t = NewType('uint32_t', int)
uint64_t = NewType('uint64_t', int)
uint8_t = NewType('uint8_t', int)

class Standard_HandlerStatus(IntEnum):
	Standard_HandlerVoid: int = ...
	Standard_HandlerJumped: int = ...
	Standard_HandlerProcessed: int = ...
Standard_HandlerVoid = Standard_HandlerStatus.Standard_HandlerVoid
Standard_HandlerJumped = Standard_HandlerStatus.Standard_HandlerJumped
Standard_HandlerProcessed = Standard_HandlerStatus.Standard_HandlerProcessed

class standard:
	@staticmethod
	def Allocate(aSize: int) -> None: ...
	@staticmethod
	def AllocateAligned(theSize: int, theAlign: int) -> None: ...
	@staticmethod
	def Purge() -> int: ...
	@staticmethod
	def Reallocate(aStorage: None, aNewSize: int) -> None: ...

class Standard_ArrayStreamBuffer():
	pass

class Standard_Condition:
	def Check(self) -> False: ...
	def CheckReset(self) -> False: ...
	def Reset(self) -> None: ...
	def Set(self) -> None: ...
	@overload
	def Wait(self) -> None: ...

class Standard_ErrorHandler:
	def __init__(self) -> None: ...
	def Catches(self, aType: Standard_Type) -> bool: ...
	def Destroy(self) -> None: ...
	def Error(self) -> Standard_Failure: ...
	@staticmethod
	def IsInTryBlock() -> bool: ...
	@staticmethod
	def LastCaughtError() -> Standard_Failure: ...
	def Unlink(self) -> None: ...

class Standard_GUID:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aGuid: str) -> None: ...
	@overload
	def __init__(self, aGuid: Standard_ExtString) -> None: ...
	@overload
	def __init__(self, a32b: int, a16b1: Standard_ExtCharacter, a16b2: Standard_ExtCharacter, a16b3: Standard_ExtCharacter, a8b1: str, a8b2: str, a8b3: str, a8b4: str, a8b5: str, a8b6: str) -> None: ...
	@overload
	def __init__(self, aGuid: Standard_UUID) -> None: ...
	@overload
	def __init__(self, aGuid: Standard_GUID) -> None: ...
	@overload
	def Assign(self, uid: Standard_GUID) -> None: ...
	@overload
	def Assign(self, uid: Standard_UUID) -> None: ...
	@staticmethod
	def CheckGUIDFormat(aGuid: str) -> bool: ...
	def Hash(self, Upper: int) -> int: ...
	@staticmethod
	def HashCode(theGUID: Standard_GUID, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(string1: Standard_GUID, string2: Standard_GUID) -> bool: ...
	def IsNotSame(self, uid: Standard_GUID) -> bool: ...
	def IsSame(self, uid: Standard_GUID) -> bool: ...
	def ToCString(self, aStrGuid: Standard_PCharacter) -> None: ...
	def ToExtString(self, aStrGuid: Standard_PExtCharacter) -> None: ...
	def ToUUID(self) -> Standard_UUID: ...

class Standard_MMgrRoot:
	def Allocate(self, theSize: int) -> None: ...
	def Free(self, thePtr: None) -> None: ...
	def Purge(self, isDestroyed: Optional[bool]) -> int: ...
	def Reallocate(self, thePtr: None, theSize: int) -> None: ...

class Standard_Static_Assert:
	@staticmethod
	def assert_ok() -> None: ...

class Standard_Transient:
	@overload
	def __init__(self) -> None: ...
	def DecrementRefCounter(self) -> int: ...
	def Delete(self) -> None: ...
	def DynamicType(self) -> Standard_Type: ...
	def GetRefCount(self) -> int: ...
	def IncrementRefCounter(self) -> None: ...
	@overload
	def IsInstance(self, theType: Standard_Type) -> bool: ...
	@overload
	def IsInstance(self, theTypeName: str) -> bool: ...
	@overload
	def IsKind(self, theType: Standard_Type) -> bool: ...
	@overload
	def IsKind(self, theTypeName: str) -> bool: ...
	def This(self) -> Standard_Transient: ...
	@staticmethod
	def get_type_descriptor() -> Standard_Type: ...
	@staticmethod
	def get_type_name() -> str: ...

class Standard_MMgrOpt(Standard_MMgrRoot):
	def __init__(self, aClear: Optional[bool], aMMap: Optional[bool], aCellSize: Optional[int], aNbPages: Optional[int], aThreshold: Optional[int]) -> None: ...
	def Allocate(self, aSize: int) -> None: ...
	def Free(self, thePtr: None) -> None: ...
	def Purge(self, isDestroyed: bool) -> int: ...
	def Reallocate(self, thePtr: None, theSize: int) -> None: ...

class Standard_MMgrRaw(Standard_MMgrRoot):
	def __init__(self, aClear: Optional[bool]) -> None: ...
	def Allocate(self, aSize: int) -> None: ...
	def Free(self, thePtr: None) -> None: ...
	def Reallocate(self, thePtr: None, theSize: int) -> None: ...

class Standard_MMgrTBBalloc(Standard_MMgrRoot):
	def __init__(self, aClear: Optional[bool]) -> None: ...
	def Allocate(self, aSize: int) -> None: ...
	def Free(self, thePtr: None) -> None: ...
	def Reallocate(self, thePtr: None, theSize: int) -> None: ...

class Standard_OutOfMemory(Standard_ProgramError):
	def __init__(self, theMessage: Optional[str]) -> None: ...
	def GetMessageString(self) -> str: ...
	@staticmethod
	def NewInstance(theMessage: Optional[str]) -> Standard_OutOfMemory: ...
	@overload
	@staticmethod
	def Raise(theMessage: Optional[str]) -> None: ...
	@overload
	@staticmethod
	def Raise(theMessage: Standard_SStream) -> None: ...
	def SetMessageString(self, aMessage: str) -> None: ...

class Standard_Persistent(Standard_Transient):
	def __init__(self) -> None: ...
	def GetTypeNum(self) -> int: ...
	def SetTypeNum(self, value: int) -> None: ...

#classnotwrapped
class Standard_AncestorIterator: ...

#classnotwrapped
class Standard_Static_Assert: ...

#classnotwrapped
class Standard_CLocaleSentry: ...

#classnotwrapped
class Standard_Type: ...

#classnotwrapped
class Standard_Failure: ...

#classnotwrapped
class Standard_Mutex: ...

#classnotwrapped
class Standard_ReadLineBuffer: ...

#classnotwrapped
class Standard_ProgramError: ...

#classnotwrapped
class Standard_ReadBuffer: ...

# harray1 classes
# harray2 classes
# hsequence classes

standard_Allocate = standard.Allocate
standard_AllocateAligned = standard.AllocateAligned
standard_Purge = standard.Purge
standard_Reallocate = standard.Reallocate
Standard_ErrorHandler_IsInTryBlock = Standard_ErrorHandler.IsInTryBlock
Standard_ErrorHandler_LastCaughtError = Standard_ErrorHandler.LastCaughtError
Standard_GUID_CheckGUIDFormat = Standard_GUID.CheckGUIDFormat
Standard_GUID_HashCode = Standard_GUID.HashCode
Standard_GUID_IsEqual = Standard_GUID.IsEqual
Standard_Transient_get_type_descriptor = Standard_Transient.get_type_descriptor
Standard_Transient_get_type_name = Standard_Transient.get_type_name
Standard_OutOfMemory_NewInstance = Standard_OutOfMemory.NewInstance
Standard_OutOfMemory_Raise = Standard_OutOfMemory.Raise
Standard_OutOfMemory_Raise = Standard_OutOfMemory.Raise
