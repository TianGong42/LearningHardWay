class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")  # 因为覆盖了父类的.altered()方法，所以执行这行是正常的
        super(Child, self).altered()            #调用了super(Child, self).altered()，这里访问到了父类，所以这里会调用父类的方法
        print("CHILD, AFTER PARENT altered()")  # 最后执行这行

dad = Parent()
son = Child()

dad.altered()
son.altered()