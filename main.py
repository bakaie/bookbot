def main():
    text = ""
    with open("./books/frankenstein.txt") as f:
        text = f.read()
    words = word_count(text)
    letters = letter_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")
    for letter in letters.keys():
        print(f"the '{letter}' character was found {letters[letter]} times")
    print("--- End report ---")

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letters = {}
    lowercase = text.lower()
    for letter in lowercase:
        if letter.isalpha():
            if letter in letters.keys():
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

main()