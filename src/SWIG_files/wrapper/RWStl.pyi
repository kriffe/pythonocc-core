from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.OSD import *
from OCC.Core.Message import *
from OCC.Core.Poly import *


class RWStl:
	@staticmethod
	def ReadAscii(self, thePath: OSD_Path, theProgInd: Optional[Message_ProgressIndicator]) -> Poly_Triangulation: ...
	@staticmethod
	def ReadBinary(self, thePath: OSD_Path, theProgInd: Optional[Message_ProgressIndicator]) -> Poly_Triangulation: ...
	@overload
	@staticmethod
	def ReadFile(self, theFile: OSD_Path, aProgInd: Optional[Message_ProgressIndicator]) -> Poly_Triangulation: ...
	@overload
	@staticmethod
	def ReadFile(self, theFile: str, aProgInd: Optional[Message_ProgressIndicator]) -> Poly_Triangulation: ...
	@staticmethod
	def WriteAscii(self, theMesh: Poly_Triangulation, thePath: OSD_Path, theProgInd: Optional[Message_ProgressIndicator]) -> bool: ...
	@staticmethod
	def WriteBinary(self, theMesh: Poly_Triangulation, thePath: OSD_Path, theProgInd: Optional[Message_ProgressIndicator]) -> bool: ...

#classnotwrapped
class RWStl_Reader:
	pass
rwstl_ReadAscii = rwstl.ReadAscii
rwstl_ReadBinary = rwstl.ReadBinary
rwstl_ReadFile = rwstl.ReadFile
rwstl_ReadFile = rwstl.ReadFile
rwstl_WriteAscii = rwstl.WriteAscii
rwstl_WriteBinary = rwstl.WriteBinary
