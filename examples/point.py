```python
class Point:
    """
    Represents a point in 2D space.
    """

    def __init__(self, x: float, y: float):
        """
        Initializes a Point object.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self.x: float = x
        self.y: float = y

    def translate(self, dx: float, dy: float) -> None:
        """
        Translates the point by the given amounts.

        Args:
            dx (float): The amount to translate in the x direction.
            dy (float): The amount to translate in the y direction.
        """
        self.x += dx
        self.y += dy

    def print_point(self) -> None:
        """
        Prints the coordinates of the point.
        """
        print(f"Point at ({self.x}, {self.y})")


def main() -> None:
    """
    Main function to demonstrate the Point class.
    """
    p: Point = Point(1.0, 2.0)
    p.print_point()
    p.translate(3.0, 4.0)
    p.print_point()


if __name__ == "__main__":
    main()
```