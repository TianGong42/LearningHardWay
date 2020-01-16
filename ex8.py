formatter = "{} {} {} {}"   # 这里定义了一个字符串

print(formatter.format(1, 2, 3, 4)) # 调用了format函数，然后将1 2 3 4 作为参数填入
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter,formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))