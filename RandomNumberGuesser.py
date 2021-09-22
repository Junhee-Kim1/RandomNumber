import random
print("number Guessing Game!")
number=random.randint(1,9)
chance=0
print("guess number")
while chance<5:
    guess=int(input("enter your guess!: "))
    if guess == number:
        print("you win!")   
        break
    elif guess<number:
        print("your number is too low")
    else:
        print("your number is too High")
    chance=chance+1
if not chance<5:
    print("you lose the number was" , number)