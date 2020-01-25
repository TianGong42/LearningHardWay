## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## is-a 是什么关系,狗是动物
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## is-a 是什么关系，猫是动物
class Cat(Animal):

    def __init__(self, name):
        ## has-a 猫有名字
        self.name = name

## is-a 人是对象
class Person(object):
    def __init__(self, name):
        ## has-a 人有名字
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## is-a 攻城狮是人
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## has-a 攻城狮有薪水
        self.salary = salary

## is-a 鱼是对象
class Fish(object):
    pass

## is-a 三文鱼是鱼
class Salmon(Fish):
    pass

## is-a 比目鱼是鱼
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## is-a 撒旦是猫
satan = Cat("Satan")

## is-a mary是猫
mary = Person("Marry")

## is-a mary的猫是撒旦
mary.pet = satan

## is-a frank是一个攻城狮
frank = Employee("Frank", 120000)

## is-a frank的宠物是rover
frank.pet = rover

## is-a 海豹是鱼
flipper = Fish()

## is-a crouse是三文鱼
crouse = Salmon()

## is-a harry是比目鱼
harry = Halibut()

