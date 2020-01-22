# 加法函数，返回加法数值
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVDING {a} / {b}")
    return a / b
# 让我们来使用这些函数
print("Let's do some math with just function:")

age = add(30, 5)

height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2 )

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ:{iq}")

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")
"""
1、先执行了除法
2、然后是乘法
3、然后是减法
"""
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what , "Can you do it by hand?")
