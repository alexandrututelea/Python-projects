import random
def choose_word():
    word_list = ["coffee", "table", "paper", "individual"]
    return random.choice(word_list)
def display(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord to guess: " + display(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter")
            continue

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
        else:
            guessed_letters.append(guess)

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You`ve guessed the word: {word}")
            break
    if attempts == 0:
        print(f"You`ve run out of attempts! The word was: {word}")
hangman()
