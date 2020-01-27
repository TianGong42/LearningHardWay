# 显示覆盖，当需要子类里的函数有不同的行为，需要覆盖子类中的函数
class Parent(object):
    
    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()