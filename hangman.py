import random
from hangman_wordlist import word_list
from hangman_arts import stages

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|w
                    __/ |                      
                   |___/    '''

print(logo)
lives = 6

choosen_word =random.choice(word_list)
print(choosen_word)


placeholder = ""
word_length = len(choosen_word)
for position in range (word_length):
     placeholder += "_"
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
        
    print(guess)

    display = ""

    for letter in choosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

    print(display)

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[lives])