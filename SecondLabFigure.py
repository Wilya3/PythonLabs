from abc import abstractmethod


class Figure:
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except Exception as e:
            print("Ошибка инициализации координат")
            print(e)

    @abstractmethod
    def calcPerimeter(self):
        pass

    @abstractmethod
    def calcArea(self):
        pass

    def print(self):
        return "Я фигура"