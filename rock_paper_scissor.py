import random
emojis = {'r':'🪨','p':'📄','s':'✂️'} 
choices = ('r', 'p', 's')
while True:
    user_choice=input('rock, paper, or scissors? (r/p/s): ').lower()
    

    if user_choice not in choices:
        print('Invalid choice! Please choose r, p, or s.')
        continue

    computer_choice = random.choice(choices)

    print(f'You chose: {emojis[user_choice]}')
    print(f'Computer chose: {emojis[computer_choice]}')
    
    if user_choice == computer_choice:
      print('It\'s a tie!')

    elif  ((user_choice == 'r' and computer_choice == 's') or 
       (user_choice == 'p' and computer_choice == 'r') or
       (user_choice == 's' and computer_choice == 'p')):
       print('You win!')

    else:
       print('You lose!')    

    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        print('Thanks for playing!')
        break
         