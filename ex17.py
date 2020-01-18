from sys import argv
from os.path import exists

script, from_file, to_file = argv

# 这一行只是一个文本，并打印输出变量
print(f"Copying from {from_file} to {to_file}")

# we could do these
# 打开需要复制的文件
in_file = open(from_file)
# 并读取为一个文件对象
indata = in_file.read()

# 打印输出这个文件对象的长度
print(f"The input fi {len(indata)} bytes long")

# 判断是to_file文件是否存在，exists方法判断文件是否存在
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

"""
echo "This is a test file." > test.txt 创建test.txt文件
cat test.txt                           查看test.txt文件的内容
"""