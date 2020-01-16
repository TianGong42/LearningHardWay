# 在每行print后面加了end = ' ', 告诉print不要用换行符结束这一行跑到下一行去
print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weight?", end = ' ')
weight = input()

print(f"so, you're {age} old, {height} tall and {weight} heavy.")