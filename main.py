import random
import hangman_art
import hangman_words

lives = 6
print(hangman_art.logo)

# choose a word randomly from word_list
chosen_word = random.choice(hangman_words.word_list)

# Create a display list with underscores representing each letter in the chosen word
display=[]
for _ in range(len(chosen_word)):
    display+='_'
print(display)

game_over = False
guessed_letters = []

while not game_over:
    guess_letter = input("\nGuess a letter: ").lower()

    # check if letter was already guessed
    if guess_letter in guessed_letters:
        print(f"You've already guessed '{guess_letter}'. Try a different letter.")
        continue

    guessed_letters.append(guess_letter)

    # check if  guessed letter is in the chosen word
    if guess_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess_letter:
                display[position] = guess_letter
    else:
        lives -= 1
        print(f"'{guess_letter}' is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print('You lose')
            print(f"The word was: {chosen_word}")

    print(display)

    if '_' not in display:
        game_over = True
        print('You win')

    print(hangman_art.stages[lives])
