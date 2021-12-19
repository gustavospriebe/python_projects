import random

num_chances = 1
random_number = random.randint(0, 10)


def number_guesser(num_chances):
    user_input = int(input("Guess the number beetween 0 and 10: "))
    if user_input > random_number:
        print('Wrong. Try a smaller number.')
        recall_guesser(num_chances)
    if user_input < random_number:
        print('Wrong. Try a larger number.')
        recall_guesser(num_chances)
    if user_input == random_number:
        print(f'Congrats, you got it in {num_chances} guesses.')


def recall_guesser(num_chances):
    num_chances += 1
    number_guesser(num_chances)


number_guesser(num_chances)
