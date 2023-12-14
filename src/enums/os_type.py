from enum import Enum


class OsType(Enum):
    LINUX = "LINUX"
    WINDOWS = "WINDOWS"
    MAC = "MAC"
    ETC = "ETC"

    @property
    def api_value(self) -> str:
        return {
            self.LINUX: "100",
            self.WINDOWS: "200",
            self.MAC: "300",
            self.ETC: "999",
        }[self]

    @classmethod
    def choices(cls):
        return [x.value for x in cls]
