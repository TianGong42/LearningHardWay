print("Let's practice everything.")  # 让我们来实践一些东西
print('You \'d need to know \'bout escapes with \\ that do:')
print('\n newline and \t tabs.')

poem = """
\tThe lovely world                可爱的世界
with logic so firmaly planted     逻辑如此坚定
cannot discern \n the needs of love  无法辨别爱的需要
nor comprehend passion from intuition  也不能凭借直觉理解激情
and requires an explanation            这里需要一个解释
\n\t\twhere there is none.
"""

print("--------------------")
print(poem)
print("--------------------")

five = 10 - 2 + 3 - 6
print(f"The should be five:{five}")

def secret_formula(started):    # 秘方
    jelly_beans = started * 500 # 果冻豆
    jars = jelly_beans / 1000   # 罐
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string,格式化输出
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))