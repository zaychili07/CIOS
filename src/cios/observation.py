from dataclasses import dataclass


@dataclass
class CellObservation:
    dataset: str
    node_id: int
    t: int
    z: int
    y: int
    x: int
    confidence: float = 1.0