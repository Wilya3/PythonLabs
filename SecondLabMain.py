from SecondLabEllipse import Ellipse
from SecondLabRhombus import Rhombus
from SecondLabParallelepiped import Parallelepiped

if __name__ == "__main__":
    print("Введите число, соответствующее фигуре")
    print("1 - Ромб")
    print("2 - Параллелепипед")
    print("3 - Эллипс")
    #try:
    flag = int(input())
    if flag == 1:
        rhombus = Rhombus(0, 0, 5, 60)
        print("Площадь ромба: " + str(rhombus.calcArea()))
        print("Периметр ромба: " + str(rhombus.calcPerimeter()))
    elif flag == 2:
        parall = Parallelepiped(0, 0, 3, 5, 5)
        print("Площадь параллелепипеда: " + str(parall.calcArea()))
        print("Периметр параллелепипеда: " + str(parall.calcPerimeter()))
    elif flag == 3:
        ellipse = Ellipse(0, 0, 3, 5)
        print("Площадь эллипса: " + str(ellipse.calcArea()))
        print("Периметр эллипса: " + str(ellipse.calcPerimeter()))
    else:
        raise Exception
    #except Exception:
        #print("Ошибка ввода")