from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Units import *


class UnitsAPI_SystemUnits(IntEnum):
	UnitsAPI_DEFAULT: int = ...
	UnitsAPI_SI: int = ...
	UnitsAPI_MDTV: int = ...
UnitsAPI_DEFAULT = UnitsAPI_SystemUnits.UnitsAPI_DEFAULT
UnitsAPI_SI = UnitsAPI_SystemUnits.UnitsAPI_SI
UnitsAPI_MDTV = UnitsAPI_SystemUnits.UnitsAPI_MDTV

class UnitsAPI:
	@staticmethod
	def AnyFromLS(self, aData: float, aUnit: str) -> float: ...
	@staticmethod
	def AnyFromSI(self, aData: float, aUnit: str) -> float: ...
	@staticmethod
	def AnyToAny(self, aData: float, aUnit1: str, aUnit2: str) -> float: ...
	@overload
	@staticmethod
	def AnyToLS(self, aData: float, aUnit: str) -> float: ...
	@overload
	@staticmethod
	def AnyToLS(self, aData: float, aUnit: str, aDim: Units_Dimensions) -> float: ...
	@overload
	@staticmethod
	def AnyToSI(self, aData: float, aUnit: str) -> float: ...
	@overload
	@staticmethod
	def AnyToSI(self, aData: float, aUnit: str, aDim: Units_Dimensions) -> float: ...
	@staticmethod
	def Check(self, aQuantity: str, aUnit: str) -> bool: ...
	@staticmethod
	def CurrentFromAny(self, aData: float, aQuantity: str, aUnit: str) -> float: ...
	@staticmethod
	def CurrentFromLS(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def CurrentFromSI(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def CurrentToAny(self, aData: float, aQuantity: str, aUnit: str) -> float: ...
	@staticmethod
	def CurrentToLS(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def CurrentToSI(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def CurrentUnit(self, aQuantity: str) -> str: ...
	@staticmethod
	def DimensionAmountOfSubstance(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionElectricCurrent(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionLength(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionLess(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionLuminousIntensity(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionMass(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionPlaneAngle(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionSolidAngle(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionThermodynamicTemperature(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionTime(self) -> Units_Dimensions: ...
	@staticmethod
	def Dimensions(self, aQuantity: str) -> Units_Dimensions: ...
	@staticmethod
	def LSToSI(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def LocalSystem(self) -> UnitsAPI_SystemUnits: ...
	@staticmethod
	def Reload(self) -> None: ...
	@staticmethod
	def SIToLS(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def Save(self) -> None: ...
	@staticmethod
	def SetCurrentUnit(self, aQuantity: str, aUnit: str) -> None: ...
	@staticmethod
	def SetLocalSystem(self, aSystemUnit: Optional[UnitsAPI_SystemUnits]) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

unitsapi_AnyFromLS = unitsapi.AnyFromLS
unitsapi_AnyFromSI = unitsapi.AnyFromSI
unitsapi_AnyToAny = unitsapi.AnyToAny
unitsapi_AnyToLS = unitsapi.AnyToLS
unitsapi_AnyToLS = unitsapi.AnyToLS
unitsapi_AnyToSI = unitsapi.AnyToSI
unitsapi_AnyToSI = unitsapi.AnyToSI
unitsapi_Check = unitsapi.Check
unitsapi_CurrentFromAny = unitsapi.CurrentFromAny
unitsapi_CurrentFromLS = unitsapi.CurrentFromLS
unitsapi_CurrentFromSI = unitsapi.CurrentFromSI
unitsapi_CurrentToAny = unitsapi.CurrentToAny
unitsapi_CurrentToLS = unitsapi.CurrentToLS
unitsapi_CurrentToSI = unitsapi.CurrentToSI
unitsapi_CurrentUnit = unitsapi.CurrentUnit
unitsapi_DimensionAmountOfSubstance = unitsapi.DimensionAmountOfSubstance
unitsapi_DimensionElectricCurrent = unitsapi.DimensionElectricCurrent
unitsapi_DimensionLength = unitsapi.DimensionLength
unitsapi_DimensionLess = unitsapi.DimensionLess
unitsapi_DimensionLuminousIntensity = unitsapi.DimensionLuminousIntensity
unitsapi_DimensionMass = unitsapi.DimensionMass
unitsapi_DimensionPlaneAngle = unitsapi.DimensionPlaneAngle
unitsapi_DimensionSolidAngle = unitsapi.DimensionSolidAngle
unitsapi_DimensionThermodynamicTemperature = unitsapi.DimensionThermodynamicTemperature
unitsapi_DimensionTime = unitsapi.DimensionTime
unitsapi_Dimensions = unitsapi.Dimensions
unitsapi_LSToSI = unitsapi.LSToSI
unitsapi_LocalSystem = unitsapi.LocalSystem
unitsapi_Reload = unitsapi.Reload
unitsapi_SIToLS = unitsapi.SIToLS
unitsapi_Save = unitsapi.Save
unitsapi_SetCurrentUnit = unitsapi.SetCurrentUnit
unitsapi_SetLocalSystem = unitsapi.SetLocalSystem
