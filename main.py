from stats import get_num_words, get_book_text, get_num_characters

def main():
    book_path = "books/frankenstein.txt"

    book_content = get_book_text(book_path)


    num_words = get_num_words(book_content)
    print(f"{num_words} words found in the document")


    num_char = get_num_characters(book_content)
    print(num_char)
    # for key, value in num_char:




main()
