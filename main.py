from morse import *
from sound import signal

def decrypt(morse: str) -> str:
    message = ""
    letters = []
    chunks = [x for x in morse.split(" ") if x]

    for t in chunks:
        translated = MORSE_LETTERS.get(t, "?")
        message += translated
        letters.append(translated)
    print(letters)
    return "".join(letters)

def encrypt(text: str) -> str:
    text = text.upper()
    morse_code = []
    for char in text:
        if char == " ":
            morse_code.append("@")
        elif char in LETTERS_MORSE:
            morse_code.append(LETTERS_MORSE[char])
        elif char == "":
            pass
        else:
            morse_code.append("?")
    print(morse_code)
    return " ".join(morse_code)
    
def main():
    print("(1) Morse to text")
    print("(2) Text to morse")
    choice = input("")
    if choice == "1":
        morse = input("Please insert your morse code here: ")
        decoded_morse = decrypt(morse)
        print(decoded_morse)

    elif choice == "2":
        text = input("Please insert your text here: ")
        morse = encrypt(text)
        print(morse)
        option = input("Would you like sound [Y/n] ")
        if option == "n":
            pass
        else:
            signal(morse)

        signal(morse) 
    
    else:
        print("Error please put in a valid choice.")
    # [Y/n]
if __name__ == "__main__":
    main()
