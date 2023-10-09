import random


def guess_number(n):
    random_number = random.randint(1, n)
    my_guess = 0
    while my_guess != random_number:
        my_guess = int(input('enter your guessing number: '))
        if my_guess > random_number:
            print("Sorry, Your guess is too high!! Try again.")
        elif my_guess < random_number:
            print("Sorry, Your guess is too low!! Try again.")
    print("Yayy!! your guess is correct!!!!!")


guess_number(10)
