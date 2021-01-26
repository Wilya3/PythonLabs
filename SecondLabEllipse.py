from SecondLabFigure import Figure
import math


class Ellipse(Figure):
    def __init__(self, x, y, bigAxis, smallAxis):
        super(Ellipse, self).__init__(x, y)
        try:
            self.bigAxisHalf = float(bigAxis)
            self.smallAxisHalf = float(smallAxis)
        except Exception:
            print("Ошибка инициализации полуосей")

    def calcArea(self):
        return math.pi * self.bigAxisHalf * self.smallAxisHalf

    def calcPerimeter(self):
        return 2 * math.pi * (((self.bigAxisHalf ** 2 + self.smallAxisHalf ** 2) / 2) ** 0.5)
