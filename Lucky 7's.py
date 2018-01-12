import random


money = 15
max_money = 15
rolls = 0

while money > 0:
    dice = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    dice_total = dice + dice_two
    if dice_total == 7:
        print("You won this round.")
        print("Dollars left %s" % money)
        rolls += 1
        money += 4
        if money > max_money:



    elif dice_total != 7:
        money -= 1
        rolls += 1
        print("Sorry.")
        print("Dollars left %s" % money)

# while max_money >= 15:
#     if max_money >= 15:




if money == 0:
    print("You're out of here!")
    print(rolls)


# max(max_money, money)
# print(max(max_money, money))
# filter(max(max_money, money))
# print(filter(max(max_money, money)))
