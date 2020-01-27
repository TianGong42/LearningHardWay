# 隐式继承，当父类定义了一个函数，但没有在子类中定义会发生隐式行为
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()