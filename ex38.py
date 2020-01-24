ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that")

stuff = ten_things.split(' ')   # 将一个字符串拆成一个list
print(stuff)
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

"""
整个while循环，判断stuff list是不是小于10，
小于10整个循环将继续执行
执行内容：从more_stuff列表使用pop()方法取出内容，然后将取出的内容加入到
stuff列表中
"""
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things wiht stuff.")

# 打印stuff列表里的数据，第一个位置的元素
print(stuff[1])
# 打印stuff列表里的数据，最后一个位置的元素
print(stuff[-1])
print(stuff.pop())
# join方法，将整个sutff列表使用空格链接
print(' '.join(stuff))

print('#'.join(stuff[3:5]))