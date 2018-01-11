import random


money = 15
max_money = 15
rolls = 0

while money > 0:
    dice = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    dice_total = dice + dice_two
    if dice_total == 7:
        money += 4
        rolls += 1
        max_money += 4
        print("You won this round.")
        print("Dollars left %s" % money)
    elif dice_total != 7:
        money -= 1
        rolls += 1
        max_money -= 1
        print("Sorry.")
        print("Dollars left %s" % money)


if money == 0:
    print("You're out of here!")
    print(rolls)

# max(max_money, money)
# print(max(max_money, money))
# filter(max(max_money, money))
# print(filter(max(max_money, money)))
