# 🎮 Python Hangman Game

A terminal-based Hangman game built using Python. Guess the hidden English word one letter at a time before running out of lives!

The game uses the NLTK English words corpus to generate a large collection of words dynamically, along with traditional ASCII Hangman drawings and a heart-based lives system.

## ✨ Features

- 🎯 **Random Word Selection:** Selects random English words using the NLTK dictionary.
- 📚 **Large Vocabulary:** Uses thousands of English words without manually maintaining a word list.
- ❤️ **Lives Counter:** Displays remaining lives using heart indicators.
- 🎨 **Traditional Hangman Artwork:** Shows the Hangman drawing as incorrect guesses increase.
- 🔤 **Dynamic Word Display:** Reveals correctly guessed letters while hiding the remaining characters.
- ⚠️ **Input Validation:** Prevents invalid inputs and repeated guesses.
- 📊 **Attempt Tracking:** Counts the total number of guesses.
- 🏆 **Win/Lose Conditions:** Displays the final result and reveals the correct word when the player loses.
- 🖥️ **Terminal Interface:** Provides a clean and interactive command-line experience.

## 🛠️ Technologies Used

- Python 3
- Random Module
- NLTK (Natural Language Toolkit)
- OS Module
- Python Lists, Loops and Functions

## 📂 Project Structure

```text
hangman_miniproject_py/
│
├── main.py
├── hangman_arts.py
├── README.md
└── __pycache__/
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/harshgargcoder/python_mini_projects/tree/main/hangman_project
```

### 2. Navigate to the Hangman project

```bash
cd Python_mini_project/hangman_miniproject_py
```

### 3. Install NLTK

```bash
pip install nltk
```

### 4. Run the game

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

**Note:** On the first run, the application downloads the NLTK English words corpus. An internet connection is required for this initial download.

## 🎮 How to Play

1. Run the Python application.
2. The game randomly selects an English word.
3. Enter one alphabet at a time to guess the hidden word.
4. Correct guesses reveal the corresponding letters.
5. Incorrect guesses reduce your remaining lives and progress the Hangman drawing.
6. Avoid losing all your lives before guessing the complete word.
7. Win by correctly identifying every letter!

## 💻 Example Gameplay

```text
=======================================================
                  🎮 HANGMAN GAME 🎮
=======================================================

🎯 Guess the hidden English word!
📝 Word contains 5 letters.

❤️ LIVES: ❤️ ❤️ ❤️ ❤️ ❤️
📊 ATTEMPTS: 0

WORD: _ _ _ _ _

👉 Enter your guess: a

✅ Good guess! 'a' is in the word.

WORD: _ a _ _ _

👉 Enter your guess: z

❌ Wrong guess! 'z' is not in the word.

❤️ LIVES: ❤️ ❤️ ❤️ ❤️ 🖤
```

*Example gameplay illustration. The actual word is randomly selected.*

## 🧠 Python Concepts Practiced

- Functions and parameters
- `while` and `for` loops
- Conditional statements (`if-else`)
- Lists and list indexing
- String manipulation
- Random word selection
- List membership (`in` operator)
- Input validation
- Exception handling
- Python modules and imports
- Working with third-party libraries

## 🚀 Future Improvements

- Add difficulty levels (Easy, Medium and Hard).
- Add a Play Again option.
- Introduce word categories such as Animals, Technology and Countries.
- Add a hint system.
- Implement a scoring and leaderboard system.
- Create a graphical interface using Tkinter.

## 👨‍💻 Author

**Harsh Garg**

Python Developer | Exploring Python, Backend Development & Problem Solving

---

⭐ If you find this project interesting, consider giving the repository a star!

