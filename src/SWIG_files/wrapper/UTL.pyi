from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Storage import *
from OCC.Core.TCollection import *
from OCC.Core.OSD import *
from OCC.Core.Resource import *


class UTL:
	@staticmethod
	def AddToUserInfo(self, aData: Storage_Data, anInfo: TCollection_ExtendedString) -> None: ...
	@staticmethod
	def CString(self, anExtendedString: TCollection_ExtendedString) -> str: ...
	@staticmethod
	def Disk(self, aPath: OSD_Path) -> TCollection_ExtendedString: ...
	@staticmethod
	def ExtendedString(self, anAsciiString: TCollection_AsciiString) -> TCollection_ExtendedString: ...
	@overload
	@staticmethod
	def Extension(self, aPath: OSD_Path) -> TCollection_ExtendedString: ...
	@overload
	@staticmethod
	def Extension(self, aFileName: TCollection_ExtendedString) -> TCollection_ExtendedString: ...
	@staticmethod
	def FileIterator(self, aPath: OSD_Path, aMask: TCollection_ExtendedString) -> OSD_FileIterator: ...
	@staticmethod
	def Find(self, aResourceManager: Resource_Manager, aResourceName: TCollection_ExtendedString) -> bool: ...
	@staticmethod
	def GUID(self, anXString: TCollection_ExtendedString) -> Standard_GUID: ...
	@staticmethod
	def IntegerValue(self, anExtendedString: TCollection_ExtendedString) -> int: ...
	@staticmethod
	def IsReadOnly(self, aFileName: TCollection_ExtendedString) -> bool: ...
	@staticmethod
	def LocalHost(self) -> TCollection_ExtendedString: ...
	@staticmethod
	def Name(self, aPath: OSD_Path) -> TCollection_ExtendedString: ...
	@staticmethod
	def OpenFile(self, aFile: Storage_BaseDriver, aName: TCollection_ExtendedString, aMode: Storage_OpenMode) -> Storage_Error: ...
	@staticmethod
	def Path(self, aFileName: TCollection_ExtendedString) -> OSD_Path: ...
	@staticmethod
	def Trek(self, aPath: OSD_Path) -> TCollection_ExtendedString: ...
	@staticmethod
	def Value(self, aResourceManager: Resource_Manager, aResourceName: TCollection_ExtendedString) -> TCollection_ExtendedString: ...
	@staticmethod
	def xgetenv(self, aCString: str) -> TCollection_ExtendedString: ...

# harray1 classes
# harray2 classes
# harray2 classes

utl_AddToUserInfo = utl.AddToUserInfo
utl_CString = utl.CString
utl_Disk = utl.Disk
utl_ExtendedString = utl.ExtendedString
utl_Extension = utl.Extension
utl_Extension = utl.Extension
utl_FileIterator = utl.FileIterator
utl_Find = utl.Find
utl_GUID = utl.GUID
utl_IntegerValue = utl.IntegerValue
utl_IsReadOnly = utl.IsReadOnly
utl_LocalHost = utl.LocalHost
utl_Name = utl.Name
utl_OpenFile = utl.OpenFile
utl_Path = utl.Path
utl_Trek = utl.Trek
utl_Value = utl.Value
utl_xgetenv = utl.xgetenv
