import random 
import hangman_art
import hangman_words
# if you call the module by from .... import aaa then you can write aaa only to call it.


lives = 6
#choose a random word
chosen_word = random.choice(hangman_words.word_list)

# create a placeholder with the same number
placeholder = ""
for position in range(0,len(chosen_word)):
    placeholder += "_"


# display the right letter in the place



game_over = False
correct_letters = []

# get the letter guess from the user
while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter 
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, thaht's not in the word. You lost a life")
        if lives == 0:
            game_over = True
            print("You lose.")


    if "_" not in display:
        game_over = True
        print("You win.")
    
    print(hangman_art.stages[lives])
    
     
    
