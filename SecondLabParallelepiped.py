from SecondLabFigure import Figure


class Parallelepiped(Figure):
    def __init__(self, x, y, weight, height, length):
        super(Parallelepiped, self).__init__(x, y)
        try:
            self.weight = float(weight)
            self.height = float(height)
            self.length = float(length)
        except Exception:
            print("Ошибка инициализации длин параллелепипеда")

    def calcArea(self):
        return 2 * (self.weight * self.height + self.weight * self.length + self.height * self.length)

    def calcPerimeter(self):
        return 4 * self.weight + 4 * self.length + 4 * self.height