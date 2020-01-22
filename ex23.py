import sys 
script, encoding, error = sys.argv

# 这个就是一个普通的main函数
def main(language_file, encoding ,errors):
    # 这句话就做了一件事，从文件对象中读取一行
    line = language_file.readline()

    if line:   # 如果line对象有值，将会执行下面的内容
        print_line(line, encoding, errors)   # 调用了print_line
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()  # 将每行结尾的\n删除掉
    raw_bytes = next_lang.encode(encoding, errors = errors) # 将文本内容中的东西解码成原始字节码
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages,encoding,error)