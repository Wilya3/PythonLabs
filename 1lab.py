from datetime import date


class Product:
    def __init__(self, name="Default name", cost=100, year=date.today().year):
        self.name = name
        self.cost = cost
        self.year = year

    def __del__(self):
        print("Объект удален: " + self.name)

    def __str__(self):
        return "Название: " + self.name + ". Стоимость: " + str(self.cost) + ". Год производства: " + str(
            self.year) + "."

    def productReleaseDateYearsAgo(self):
        different = date.today().year - self.year
        return different

    def increaseCostIfTV(self):
        if self.name.rfind("TV") != -1:  # Если в названии товара не будет подстроки TV, то увеличения не произойдет
            self.cost = self.cost * 1.2


if __name__ == "__main__":
    print("Обработка стандартного объекта")
    appObject = Product()
    print("Лет прошло после создания товара: " + str(appObject.productReleaseDateYearsAgo()))
    appObject.increaseCostIfTV()
    print(appObject)

    print("//////////////////////////////////////////////////////")
    listWithInputObjects = []
    while True:
        try:
            print("Введите название товара:")
            name = input()
            print("Введите стоимость товара:")
            cost = int(input())
            print("Введите год производства товара:")
            year = int(input())
            listWithInputObjects.append(Product(name, cost, year))

            print("Повторить ввод? (y/n)")
            answer = input()
            if answer != "y" and answer != "n":
                print("Ошибка ввода. Повторный ввод отменен.")
                break
            if answer == "n":
                print("Повторный ввод отменен.")
                break
        except Exception:
            print("Неверный ввод. Повторите ввод данных сначала.")
            continue

    for i in range(len(listWithInputObjects)):
        print(listWithInputObjects[i])
        print("Лет прошло после создания товара: " + str(listWithInputObjects[i].productReleaseDateYearsAgo()))
        listWithInputObjects[i].increaseCostIfTV()
        print("Данные об объекте после обработки: " + str(listWithInputObjects[i]) + "\n")
