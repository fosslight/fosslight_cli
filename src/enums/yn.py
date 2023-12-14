from enum import Enum


class YnType(Enum):
    Y = "Y"
    N = "N"

    @property
    def api_value(self):
        return {
            self.Y: "Y",
            self.N: "N",
        }[self]

    @classmethod
    def choices(cls):
        return [x.value for x in cls]
