
def while_list(k,a):
    i = 0 
    numbers = []
    while i < k:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + a
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")
        print("The numbers: ")



while_list(7,2)
