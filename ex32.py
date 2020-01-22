the_count = [1,2,3,4,5]   # 数字列表
fruits = ['apples', 'oranges', 'pears', 'apricots'] # 字符串列表
change = [1, 'pennies', 2 , 'dimes', 3, 'quarters'] # 混合列表

# this first kind of for-loop goes through a list
# 打印数字列表
for number in the_count:
    print(f"This is count {number}")

# same as above
# 打印字符串列表
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
# 打印混合列表
for i in change:
    print(f"I got {i}")


# we can also build lists, first start with an empty one 
# 定义个空列表
elements = []

# then use the range function to do 0 to 5 counts
# range(0, 6) 就是现实0-5六个数字，并使用append方法添加数字
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# then use the range function to do 0 to 5 counts
for i in elements:
    print(f"Element was: {i}")