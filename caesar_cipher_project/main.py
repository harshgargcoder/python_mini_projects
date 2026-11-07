
import string
import random
import os
import time

alphabet = string.ascii_lowercase

# -------------------- COLORS --------------------

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
PURPLE = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"


# -------------------- UI FUNCTIONS --------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def loading(message):
    print(f"\n{YELLOW}{message}", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print(RESET)


def display_header():
    print(CYAN + BOLD)
    print("=" * 55)
    print(r"""
     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗
    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
    ██║     ██║██████╔╝███████║█████╗  ██████╔╝
    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    """)
    print("              SECRET CODE MACHINE")
    print("=" * 55)
    print(RESET)


def display_menu():
    print(f"""
{PURPLE}╔═══════════════════════════════════════════════╗
║                 SELECT MODE                    ║
╠═══════════════════════════════════════════════╣
║   [1]  🔒  ENCRYPT MESSAGE                     ║
║   [2]  🔓  DECRYPT MESSAGE                     ║
║   [3]  🎲  RANDOM SHIFT NUMBER                 ║
║   [4]  ❌  EXIT                                ║
╚═══════════════════════════════════════════════╝{RESET}
""")


# -------------------- CIPHER FUNCTION --------------------

def caeser(original_text, shift_amount, encode_or_decode):

    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter in alphabet:

            shifted_position = alphabet.index(letter) + shift_amount

            shifted_position %= len(alphabet)

            output_text += alphabet[shifted_position]

        else:
            output_text += letter

    return output_text


# -------------------- MAIN PROGRAM --------------------

should_continue = True

while should_continue:

    clear_screen()
    display_header()
    display_menu()

    choice = input(f"{CYAN}Select an option (1-4): {RESET}")

    if choice == "1":
        direction = "encode"

    elif choice == "2":
        direction = "decode"

    elif choice == "3":
        direction = random.choice(["encode", "decode"])
        print(f"\n{YELLOW}Random mode selected: {direction.upper()}{RESET}")

    elif choice == "4":
        print(f"\n{GREEN}🔐 Thank you for using Cipher Machine!{RESET}")
        print("Your secrets are safe. Goodbye!")
        break

    else:
        print(f"\n{RED}Invalid option! Please select 1-4.{RESET}")
        time.sleep(1.5)
        continue

    text = input("\n📝 Enter your secret message: ").lower()

    shift = input("🔢 Enter shift number (or type 'random'): ").lower()

    if shift == "random":
        shift = random.randint(1, 25)
        print(f"{YELLOW}Random shift generated: {shift}{RESET}")

    else:
        try:
            shift = int(shift)
        except ValueError:
            print(f"{RED}Invalid shift number!{RESET}")
            time.sleep(1.5)
            continue

    # Normalize large shift values
    shift %= 26

    loading("Processing your secret message")

    result = caeser(
        original_text=text,
        shift_amount=shift,
        encode_or_decode=direction
    )

    print(f"\n{GREEN}{BOLD}╔══════════════════════════════════════════╗")
    print("║             OPERATION COMPLETE          ║")
    print("╚══════════════════════════════════════════╝")

    print(f"\n🔑 MODE       : {direction.upper()}")
    print(f"🔢 SHIFT      : {shift}")
    print(f"📩 ORIGINAL   : {text}")
    print(f"🔐 RESULT     : {result}{RESET}")

    print("\n" + "-" * 50)

    again = input(
        f"{CYAN}Would you like to perform another operation? (yes/no): {RESET}"
    ).lower()

    if again != "yes":
        should_continue = False

print(f"\n{PURPLE}Session terminated. Stay mysterious! 🕵️{RESET}")
