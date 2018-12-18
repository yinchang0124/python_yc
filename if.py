number = 23
guess = int(input('enter an interger : '))

if guess == number:
    print("bingo")
elif guess < number:
    print ("little")
elif guess > number:
    print ("big")

print ("finish")