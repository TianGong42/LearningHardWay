# this one is like your scripts with argv
# 这个函数和之前通过命令行来执行python脚本方式很像，就是解包的方式
# 本质上来讲，就是将函数的所有参数接受进来，然后放到叫args的列表里
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
# 这种方式比较直观，两个入参就好了
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()