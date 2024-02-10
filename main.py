# class Grandparents:
#     height = 170
#     satiety = 100
#     age = 60
#
#
# class Parents(Grandparents):
#     age = 40
#
#
# class Children(Parents):
#     height = 50
#
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
#
#
# ch = Children()

class Hello_world:
    hello = "hello"
    _hello = "_hello"
    __hello = "__hello"

    def __init__(self):
        self.world = "world"
        self._world = "_world"
        self.__world = "__world"

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)


class Hi(Hello_world):
    def hi_printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)


h = Hello_world()
h.printer()
hi = Hi()
hi.hi_printer()
