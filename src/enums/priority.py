from enum import Enum


class Priority(Enum):
    P0 = "P0"
    P1 = "P1"
    P2 = "P2"

    @property
    def api_value(self):
        return {
            self.P0: "10",
            self.P1: "20",
            self.P2: "30",
        }[self]

    @classmethod
    def choices(cls):
        return [x.value for x in cls]
