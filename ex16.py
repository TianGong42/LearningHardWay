from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")   # 我们要抹去
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')  # w是入写模式，但是如果写入文件不存在，就会创建一个这样的文件

print("Truncating the file. Goodbye!")
target.truncate()   #清空文件

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
# 上面三行获取三行文本

# 下面将三行文本写入
target.write(line1+ "\n" + line2 + "\n" + line3 + "\n")


print("And finally, we close it.")
target.close()