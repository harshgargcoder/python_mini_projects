
import random
import os
import nltk

import hangman_arts

from nltk.corpus import words


# -------------------- WORD DATABASE --------------------

# Download only if the NLTK words corpus is missing
try:
    word_list = words.words()
except LookupError:
    nltk.download("words", quiet=True)
    word_list = words.words()

word_list = list(set(
    word.lower()
    for word in word_list
    if word.isalpha() and 4 <= len(word) <= 10
))


# -------------------- GAME SETTINGS --------------------

TOTAL_LIVES = 5
lives = TOTAL_LIVES

chosen_word = random.choice(word_list)

guessed_letters = []
game_over = False
attempts = 0


# -------------------- UI FUNCTIONS --------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_header():
    print("=" * 55)
    print("              🎮 HANGMAN GAME 🎮")
    print("=" * 55)


def display_lives():
    hearts = " ".join(
        "❤️" if i < lives else "🖤"
        for i in range(TOTAL_LIVES)
    )

    print(f"\n❤️ LIVES: {hearts}")
    print(f"📊 ATTEMPTS: {attempts}")


def display_word():
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in chosen_word
    )


def display_hangman():
    print(hangman_arts.stages[TOTAL_LIVES - lives])


# -------------------- GAME START --------------------

clear_screen()
display_header()

print("\n🎯 Guess the hidden English word!")
print(f"📝 Word contains {len(chosen_word)} letters.")
print("💡 Guess one letter at a time.")

print("\n" + "-" * 55)

# Uncomment for testing
# print("DEBUG:", chosen_word)


# -------------------- MAIN GAME LOOP --------------------

while not game_over:

    display_lives()

    print("\nWORD:", display_word())

    if guessed_letters:
        print("GUESSED LETTERS:", ", ".join(sorted(guessed_letters)))

    print("\n" + "-" * 55)

    guess = input("👉 Enter your guess: ").lower().strip()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("\n❌ Please enter a single alphabet!")
        continue

    if guess in guessed_letters:
        print("\n⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)
    attempts += 1

    # Incorrect guess
    if guess not in chosen_word:
        lives -= 1
        print(f"\n❌ Wrong guess! '{guess}' is not in the word.")

    else:
        print(f"\n✅ Good guess! '{guess}' is in the word.")

    # Display updated game state
    print("\n" + "-" * 55)
    display_hangman()
    print("WORD:", display_word())

    # Check winning condition
    if all(letter in guessed_letters for letter in chosen_word):
        game_over = True
        print("\n" + "=" * 55)
        print("           🏆 CONGRATULATIONS! YOU WIN!")
        print("=" * 55)

    # Check losing condition
    elif lives == 0:
        game_over = True
        print("\n" + "=" * 55)
        print("              💀 GAME OVER!")
        print("=" * 55)
        print(f"\nThe correct word was: {chosen_word.upper()}")

# -------------------- FINAL SCORE --------------------

print(f"\n🎯 Total attempts: {attempts}")
print(f"❤️ Lives remaining: {lives}")

if lives > 0:
    print("🌟 Excellent work! Thanks for playing.")
else:
    print("Better luck next time!")

print("\n" + "=" * 55)
print("                 GAME ENDED")
print("=" * 55)

input("\nPress Enter to exit...")