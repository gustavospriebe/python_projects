lista = []

# This program receive user inputs and transform them into a phrase. Int isn't accepted.

def phrase(x): # Capitalizes the first letter of the sentence.
    capitalize = str(x).capitalize()
    if x.startswith(('how', 'what', 'why', 'who')):
        return f'{capitalize}?'
    else:
        return f'{capitalize}.'


def loop(): # Loop through the user inputs and put . If the \end is inserted, then break the program and return the result.
    while True:
        user_input = input('Say something: ')
        try:
            user_input = int(user_input)
            continue
        except ValueError:
            if user_input == '\end':
                final = lambda x: print(' '.join(x)) # Join the phrases into a sentence.
                final(lista)
                break
            lista.append(phrase(user_input))

loop() # Inicialize the program.