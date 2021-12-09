questions = ['''Which color is more beautiful?
    1. Red
    2. White
    3. Green
    4. Black
''', ''' Question 2:
    1. example1
    2. example2
    3. example3
    4. example4
''', ''' Question 3:
    1. example1
    2. example2
    3. example3
    4. example4
''', ''' Question 4:
    1. example1
    2. example2
    3. example3
    4. example4
''', ''' Question 5:
    1. example1
    2. example2
    3. example3
    4. example4
''']

answers = {questions[0]: 1, questions[1]: 2, questions[2]: 3, questions[3]: 4, questions[4]: 4}

print('Welcome to the quiz game!')

def quiz_game():
    score = 0
    for question in range(len(questions)):
        print(questions[question])
        while True:
            options = [1, 2, 3, 4]
            try:
                user_response = int(input('Digit the number of the right answer: '))
                if user_response not in options: # Validate if the answer is beetween 1 and 4
                    print('Digit a number beetween 1 and 4 according to the answer.')
                    continue
                if user_response == answers[questions[question]]:
                    score += 1
                break
            except ValueError: # If the user insert a str then the loop will restart.
                print('Digit a number not a letter.')
                continue
    print(f'You got {score} questions right!')


quiz_game()
