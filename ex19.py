def cheese_and_crackers(cheese_count, boxes_of_crackers):   # 奶酪和饼干
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just five the function numbers directly:")
# 调用奶酪和饼干的函数，入参为20和30
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")  # 或者我们可以使用脚本中的变量
amount_of_cheese = 10 
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)   # 函数的入参为两个变量

print("We can even do math inside too:")    # 我们可以在里面做数学公式
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the tow, variables and math:")   # 同样的，我们可以把数学公式和变量结合起来
cheese_and_crackers(amount_of_cheese + 100 , amount_of_crackers + 1000)