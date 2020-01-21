from sys import argv

# 解析从命令行中拿到的参数
script,input_file = argv

# 打印函数，打印出文件对象的所有内容
def print_all(f):
    print(f.read())

# 重置
def rewind(f):
    f.seek(0)

# 打印输出函数，打印行数，和读取对应的一行
def print_a_line(line_count, f):
    print(line_count, f.readline())

# 获取文件对象
current_file = open(input_file)

# 打印整个文件
print("First let's print the whole file:\n")

print_all(current_file)
# 重置
print("Now let's rewind, kind of like a tape.")
# 光标重新移动到第一行开始
rewind(current_file)
# 让我们打印三行
print("Let's print three lines:")
# 打印第一行
current_line = 1
print_a_line(current_line,current_file)
# 打印第二行
current_line = current_line + 1
print_a_line(current_line, current_file)
# 打印第三行
current_line = current_line + 1
print_a_line(current_line, current_file)