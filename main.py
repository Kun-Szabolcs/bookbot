from stats import get_num_words, get_char_count, sort
import sys

if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as file:
        return file.read() 

def main():
    text:str = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    chars = get_char_count(text)
    sortedChars = sort(chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sortedChars:
        if i["char"].isalpha():
            print(i["char"] + ": " + str(i["num"]))

main()