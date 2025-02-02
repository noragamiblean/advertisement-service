from dataclasses import dataclass

@dataclass(frozen=True)
class Location:
    x: int
    y: int