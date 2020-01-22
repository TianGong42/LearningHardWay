from sys import exit

def gold_room():
    print("这房间都是金子，你要多少钱")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = input(choice)
    else:
        dead("伙计，学着打一个数字.")
    
    if how_much < 50:
        print("很好，你不贪心，你赢了!")
        exit(0)
    else:
        dead("你这个贪婪的混蛋!")

# 进入熊房
def bear_room():
    print("这里有一头熊")   # 这是一个
    print("这头熊有一罐蜂蜜")
    print("胖熊在另一扇门前.")
    print("你打算怎么移动这只熊 ")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("熊看着你，然后扇了你一巴掌.")
        elif choice == "taunt bear" and not bear_moved:
            print("熊离开这个门.")
            print("你能穿过它")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("熊生气了，咬了你的腿.")
        elif choice == "开门" and bear_moved:
            gold_room()
        else:
            print("I got no idea what what means.")

def cthulhu_room():
    print("在这里你可以看到邪恶的克图鲁.")
    print("他，它，无论什么盯着你，你都会发疯.")
    print("你是逃命还是吃脑袋?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job! ")
    exit(0)

def start():
    print("你在一个黑暗的房间.")   # 你在一个黑暗的房间
    print("你的左边和右边都有一个门.") # 你的左边和右边都有一个门
    print("你选择哪个?")    # 你选择哪个

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("你在房间里绊了一跤，然后饿死了.")


start()