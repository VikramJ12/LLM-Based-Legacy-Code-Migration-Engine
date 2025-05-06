Here is the converted Python code:

```
from dataclasses import dataclass
from typing import Tuple

@dataclass
class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def translate(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def print_point(self) -> None:
        print(f"Point at ({self.x}, {self.y})")

def main() -> int:
    p = Point(1.0, 2.0)
    init_point(p)
    print_point(p)
    translate(p, 3.0, 4.0)
    print_point(p)
    return 0

def init_point(point: Point) -> None:
    point.x = 1.0
    point.y = 2.0

def print_point(point: Point) -> None:
    print(f"Point at ({point.x}, {point.y})")

def translate(point: Point, dx: float, dy: float) -> None:
    point.translate(dx, dy)

if __name__ == "__main__":
    result = main()
```