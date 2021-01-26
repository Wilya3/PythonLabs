from SecondLabFigure import Figure
import math


class Rhombus(Figure):
    def __init__(self, x, y, side, angle):
        super(Rhombus, self).__init__(x, y)
        try:
            self.side = float(side)
            self.angle = float(angle)
        except Exception:
            print("Ошибка инициализации стороны и угла ромба")

    def calcArea(self):
        return self.side * self.side * math.sin(self.angle * math.pi / 180)

    def calcPerimeter(self):
        return self.side * 4
