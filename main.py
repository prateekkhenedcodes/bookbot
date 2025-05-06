from stats import get_num_words, get_num_characters, sort_num_char
from sys import argv

def main():
    book_path = ""

    if len(argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        book_path = argv[1]
        
    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {book_path}...")

    book_content = get_book_text(book_path)

    print("----------- Word Count ----------")

    num_words = get_num_words(book_content)
    print(f"Found {num_words} total words")


    num_char = get_num_characters(book_content)

    sorted_dict = sort_num_char(num_char)

    print("--------- Character Count -------")

    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"'{key}: {value}'")
        else:
            continue

def get_book_text(book_path):
    with open(book_path) as f: 
        return f.read()
    

main()
