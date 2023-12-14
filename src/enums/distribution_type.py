from enum import Enum


class DistributionType(Enum):
    GENERAL_MODEL = "GENERAL_MODEL"
    TRANSFER_IN_HOUSE = "TRANSFER_IN_HOUSE"
    B2B = "B2B"
    PRECEDING_SOFTWARE = "PRECEDING_SOFTWARE"

    @property
    def api_value(self) -> str:
        return {
            self.GENERAL_MODEL: "10",
            self.TRANSFER_IN_HOUSE: "30",
            self.B2B: "40",
            self.PRECEDING_SOFTWARE: "50",
        }[self]

    @classmethod
    def choices(cls):
        return [x.value for x in cls]
