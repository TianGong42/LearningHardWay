# 通过argv获取文件名
from sys import argv

script, filename = argv

# open方法，接受一个参数。获取一个文件对象
txt = open(filename)

print(f"Here's your file {filename}:")

# 调用read()方法打印文本对象的内容
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())