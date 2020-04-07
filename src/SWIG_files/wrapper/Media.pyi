from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.Image import *
from OCC.Core.Graphic3d import *


class Media_BufferPool(Standard_Transient):
	def __init__(self) -> None: ...
	def BufferSize(self) -> False: ...
	def GetBuffer(self) -> False: ...
	def Release(self) -> None: ...

class Media_CodecContext(Standard_Transient):
	def __init__(self) -> None: ...
	def CanProcessPacket(self, thePacket: Media_Packet) -> False: ...
	def Close(self) -> None: ...
	def Context(self) -> False: ...
	def Flush(self) -> None: ...
	def ReceiveFrame(self, theFrame: Media_Frame) -> False: ...
	def SendPacket(self, thePacket: Media_Packet) -> False: ...
	def SizeX(self) -> False: ...
	def SizeY(self) -> False: ...
	def StreamIndex(self) -> False: ...

class Media_FormatContext(Standard_Transient):
	def __init__(self) -> None: ...
	def Close(self) -> None: ...
	def Context(self) -> False: ...
	def Duration(self) -> False: ...
	def NbSteams(self) -> int: ...
	def OpenInput(self, theInput: TCollection_AsciiString) -> False: ...
	def PtsStartBase(self) -> False: ...
	def ReadPacket(self, thePacket: Media_Packet) -> False: ...
	def Stream(self, theIndex: int) -> False: ...

class Media_Frame(Standard_Transient):
	def __init__(self) -> None: ...
	def BestEffortTimestamp(self) -> False: ...
	def ChangeFrame(self) -> False: ...
	def Format(self) -> False: ...
	@staticmethod
	def FormatOcct2FFmpeg(self, theFormat: Image_Format) -> int: ...
	def Frame(self) -> False: ...
	def InitWrapper(self, thePixMap: Image_PixMap) -> False: ...
	def IsEmpty(self) -> False: ...
	def IsFullRangeYUV(self) -> False: ...
	def IsLocked(self) -> False: ...
	def PixelAspectRatio(self) -> False: ...
	def Pts(self) -> False: ...
	def Size(self) -> Graphic3d_Vec2i: ...
	def SizeX(self) -> False: ...
	def SizeY(self) -> False: ...
	@staticmethod
	def Swap(self, theFrame1: Media_Frame, theFrame2: Media_Frame) -> None: ...
	def Unref(self) -> None: ...

class Media_IFrameQueue:
	def LockFrame(self) -> Media_Frame: ...
	def ReleaseFrame(self, theFrame: Media_Frame) -> None: ...

class Media_Packet(Standard_Transient):
	def __init__(self) -> None: ...
	def ChangeData(self) -> False: ...
	def ChangePacket(self) -> False: ...
	def Data(self) -> False: ...
	def Dts(self) -> False: ...
	def Duration(self) -> False: ...
	def DurationSeconds(self) -> False: ...
	def IsKeyFrame(self) -> False: ...
	def Packet(self) -> False: ...
	def Pts(self) -> False: ...
	def SetKeyFrame(self) -> None: ...
	def Size(self) -> False: ...
	def StreamIndex(self) -> False: ...
	def Unref(self) -> None: ...

class Media_PlayerContext(Standard_Transient):
	def __init__(self, theFrameQueue: Media_IFrameQueue) -> None: ...
	@staticmethod
	def DumpFirstFrame(self, theSrcVideo: TCollection_AsciiString, theMediaInfo: TCollection_AsciiString) -> Media_Frame: ...
	def Pause(self) -> None: ...
	def PlayPause(self) -> Tuple[bool, float, float]: ...
	def PlaybackState(self) -> Tuple[bool, float, float]: ...
	def Resume(self) -> None: ...
	def Seek(self, thePosSec: float) -> None: ...
	def SetInput(self, theInputPath: TCollection_AsciiString, theToWait: bool) -> None: ...
	def ToForceRgb(self) -> False: ...

class Media_Scaler(Standard_Transient):
	def __init__(self) -> None: ...
	def Convert(self, theSrc: Media_Frame, theRes: Media_Frame) -> False: ...
	def IsValid(self) -> False: ...
	def Release(self) -> None: ...

class Media_Timer(Standard_Transient):
	def __init__(self) -> None: ...
	def ElapsedTime(self) -> float: ...
	def IsStarted(self) -> bool: ...
	def Pause(self) -> None: ...
	def PlaybackSpeed(self) -> float: ...
	def Seek(self, theTime: float) -> None: ...
	def SetPlaybackSpeed(self, theSpeed: float) -> None: ...
	def Start(self) -> None: ...
	def Stop(self) -> None: ...
