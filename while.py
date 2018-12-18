number = 22
running = True
while running:
    guess = int(input("enter an interger:"))

    if guess == number:
        print ("bingo")
        running = False
    elif guess > number:
        print ("big")
    elif guess < number:
        print ("small")
else:
    print ("loop over")
print ("finish")