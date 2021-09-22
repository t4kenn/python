import math

class Circle:
    PI = 3.1415

    def calc_circunference(self, radius):
        res = 2 * Circle.PI * radius
        return math.floor(res * 10 ** 3) / (10 ** 3)

    def calc_area(self, radius):
        res = Circle.PI * radius ** 2
        return math.floor(res * 10 ** 3) / (10 ** 3)

class Main:

    def execute(self):
        circle = Circle()

        radius = int(input("半径を整数値で入力:"))

        circunference = circle.calc_circunference(radius)

        area = circle.calc_area(radius)

        print("円周の長さは{}です。".format(circunference))
        print("円の面積は{}です。".format(area))

main = Main()
main.execute()