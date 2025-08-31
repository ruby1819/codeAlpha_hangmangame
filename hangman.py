import random

# List of words to choose from
word_list = ['python', 'hangman', 'programming', 'network', 'socket', 'thread', 'mutex']

# Function to save game result to a text file
def save_result_to_file(word, guessed_word, attempts_left, result):
    with open("hangman_output.txt", "a") as file:
        file.write("Word: " + word + "\n")
        file.write("Guessed: " + ''.join(guessed_word) + "\n")
        file.write("Attempts Left: " + str(attempts_left) + "\n")
        file.write("Result: " + result + "\n")
        file.write("-" * 30 + "\n")

# Main game function
def play_hangman():
    word = random.choice(word_list)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()

    print("🎮 Welcome to Hangman!")
    print("Guess the word:", ' '.join(guessed))

    while attempts > 0 and '_' in guessed:
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠ Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Current word:", ' '.join(guessed))


    if '_' not in guessed:
        print("🎉 You win! The word was:", word)
        save_result_to_file(word, guessed, attempts, "Win")
    else:
        print("💀 Game over! The word was:", word)
        save_result_to_file(word, guessed, attempts, "Loss")


if __name__ == "__main__":
    play_hangman()