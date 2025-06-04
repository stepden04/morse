from morse import *

def decrypt(morse: str) -> str:
    message = ""
    letters = []
    chunks = morse.split(" ")
    for t in chunks:
        translated = MORSE_LETTERS[t]
        message += translated
        letters.append(translated)
    return " ".join(letters)

def main():
    print("Hello world!")
    print(decrypt(".... . .-.. .-.. --- .-- --- .-. .-.. -.."))

if __name__ == "__main__":
    main()
