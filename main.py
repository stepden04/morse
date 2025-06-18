from morse import *

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
    msg = "Hello World"
    morse_code = encrypt(msg)
    text = decrypt(morse_code)
    print(f"{msg} -> {morse_code}")
    print(f"{morse_code} -> {text}")
    
if __name__ == "__main__":
    main()
