from typing import Tuple


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self._x = x
        self._y = y

    def set_x(self, x: int) -> None:
        self._x = x

    def set_y(self, y: int) -> None:
        self._y = y

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get(self) -> Tuple[int, int]:
        return (self._x, self._y)

    def move(self, dx: int, dy: int) -> None:
        self._x += dx
        self._y += dy

    def __str__(self) -> str:
        return f"({self._x}, {self._y})" 


if __name__ == "__main__":
    point_a = Point()
    point_b = Point(2, 5)

    print(point_a)
    print(point_b)

