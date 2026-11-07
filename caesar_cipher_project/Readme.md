# 🔐 Caesar Cipher – Secret Code Machine

A Python-based interactive Caesar Cipher application that allows users to encrypt and decrypt secret messages using a letter-shifting algorithm.

Built as a Python learning project, this application features an interactive terminal interface, colored output, random shift generation, and a reusable encryption/decryption function.

## ✨ Features

- 🔒 **Message Encryption:** Convert normal messages into secret codes.
- 🔓 **Message Decryption:** Decode previously encrypted messages.
- 🎲 **Random Shift:** Generate a random shift value between 1 and 25.
- 🎨 **Colored Terminal UI:** Hacker-style interface with ANSI colors.
- ⏳ **Loading Animation:** Simulated processing animation.
- 🔄 **Interactive Menu:** Perform multiple encryption and decryption operations.
- 🛡️ **Input Validation:** Handle invalid shift values.
- 🔁 **Alphabet Wrapping:** Uses modulo arithmetic to handle shifts beyond the alphabet boundaries.
- 📝 **Preserves Spaces and Special Characters:** Non-alphabetic characters remain unchanged.

## 🛠️ Technologies Used

- Python 3
- `string` – Alphabet generation.
- `random` – Random shift generation.
- `os` – Terminal screen clearing.
- `time` – Loading animation.

All modules used are part of Python's standard library. No external packages are required.

## 📂 Project Structure

```text
Caesar-Cipher/
│
├── main.py
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/harshgargcoder/python_mini_projects/tree/main/caesar_cipher_project
```

### 2. Navigate to the project directory

```bash
cd Caesar-Cipher
```

### 3. Run the application

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

## 🚀 How to Use

1. Run the Python application.
2. Select an operation from the menu:
   - `1` – Encrypt a message.
   - `2` – Decrypt a message.
   - `3` – Randomly select encryption or decryption mode.
   - `4` – Exit the application.
3. Enter your message.
4. Provide a shift number or enter `random`.
5. View your encrypted or decrypted result.
6. Choose whether to perform another operation.

## 💻 Example

### Encryption

**Input:**

```text
Mode: ENCODE
Message: hello world
Shift: 3
```

**Output:**

```text
khoor zruog
```

### Decryption

**Input:**

```text
Mode: DECODE
Message: khoor zruog
Shift: 3
```

**Output:**

```text
hello world
```

## 🧠 How Caesar Cipher Works

Caesar Cipher is a substitution encryption technique in which each letter is shifted by a fixed number of positions in the alphabet.

For example, with a shift of 3:

```text
Original:  a b c d e f g h i j
Encrypted: d e f g h i j k l m
```

The modulo operator (`%`) ensures that the alphabet wraps around when the shift exceeds the last letter.

## 📚 Python Concepts Practiced

- Functions and parameters
- `for` and `while` loops
- Conditional statements (`if-else`)
- String manipulation
- Lists and string indexing
- Modulo arithmetic
- Exception handling (`try-except`)
- Python standard libraries
- ANSI terminal colors
- Return statements and function reusability

## ⚠️ Disclaimer

This project is intended for educational purposes only. Caesar Cipher is a basic encryption technique and is not suitable for protecting sensitive information.

## 👨‍💻 Author

**Harsh Garg**

Python Developer | Exploring Python, Backend Development & Problem Solving

---

⭐ If you find this project interesting, consider giving the repository a star!
