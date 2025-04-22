import random
import HangmanArt
import HangmanWords

chosen_word = random.choice(HangmanWords.word_list)
print(chosen_word)
print(HangmanArt.logo)

placeholder = ""
for _ in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)
lives = 6
game_over = False
correct_guesses = []
wrong_guesses = []
while not game_over:
    display = ""
    guess = input("guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(guess)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_" 
    print(display)
    
    if guess not in chosen_word:
        if guess not in wrong_guesses:
            wrong_guesses.append(guess)
            lives -= 1
            print(f"wrong guess. lives remaining = {lives}")
        else:
            print(f"you already guessed {guess}, try again")
    if lives == 0:
        print("game over you lose")
        game_over = True
    if "_" not in display:
        print("You guessed it correctly. You win!")
        game_over = True
    if lives == 0:
        game_over = True
    print(HangmanArt.stages[lives])  
