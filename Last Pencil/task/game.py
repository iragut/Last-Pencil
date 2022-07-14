import random

n = input("How many pencils would you like to use:\n")  # number input
while True:
    if not n.isdigit():
        n = input("The number of pencils should be numeric\n")
    elif int(n) <= 0:
        n = input("The number of pencils should be positive\n")
    else:
        break
m = str(input("Who will be the first (John, Jack):\n"))  # name input
while True:
    if m == "Jack" or m == "John":
        break
    else:
        m = str(input("Choose between 'John' and 'Jack'\n"))
pen = int(n)
print("|" * pen)
while pen > 0:    # The games
    if m == "Jack":  # Bot Jack
        print(m, "'s turn")
        num = 0
        num = pen - num
        if pen == 1:
            num = 1
            print(num)
            m = "Jack"
            print("John won")
            break
        if pen % 4 == 0:
            num = 3
        elif pen % 4 == 3:
            num = 2
        elif pen % 4 == 2:
            num = 1
        else:
            num = random.randint(1, 3)
        print(num)
        print('|' * (pen - num))
        m = "John"
        pen -= num
        if pen <= 0:
            break
    if m == "John":  # Player
        print(m, "'s turn")
        num = input()
        while True:
            if not num.isdigit():
                num = input("Possible values: '1', '2' or '3'\n")
            elif int(num) > 3 or int(num) < 1:
                num = input("Possible values: '1', '2' or '3'\n")
            else:
                if int(num) >= pen:
                    if pen - int(num) == 0:
                        print("Jack won")
                        break
                    num = input("Too many pencils were taken\n")
                else:
                    break
        print('|' * (pen - int(num)))
        m = "Jack"
        pen -= int(num)
if m != "Jack":
    print("John won")
