import random
import time
random.seed(time.time())

def hangman():
    print("=== Welcome to Hangman Game ===\n")

    word_list = ["python", "hangman", "keyboard", "laptop", "program","java","car","bike"]
    word_to_guess = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    display_word = ["_" for _ in word_to_guess]

    while incorrect_guesses < max_incorrect and "_" in display_word:
        print("\nWord to guess: ", " ".join(display_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabetical character.")
            continue
        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("✅ Good guess!")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    display_word[i] = guess
        else:
            print("❌ Wrong guess.")
            incorrect_guesses += 1

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
    else:
        print("\n💀 Game Over! The correct word was:", word_to_guess)

if __name__ == "__main__":
    hangman()

