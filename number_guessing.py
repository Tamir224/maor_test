import random
def number_guessing():
    correct_answer = random.randint(1,100)

    while True:
        user_choice = input('Please enter a number between 1 to 100: ')

        if user_choice.isdigit():  # Check if input is a digit
            user_choice = int(user_choice)

            if 1 <= user_choice <= 100:
                if user_choice > correct_answer:
                    user_choice = input('Your guess is too high')
                elif user_choice < correct_answer:
                    user_choice = input('Your guess is too low')
                else:
                    return 'Your guess is correct'
            else:
                print('Please enter a number between 1 to 100')
        else:
            print('Please enter a valid number')

print(number_guessing())