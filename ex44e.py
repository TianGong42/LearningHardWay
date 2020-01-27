class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()  # 组合，暂时我觉得很奇怪的技术。直接使用别的类和模块

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AGTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()