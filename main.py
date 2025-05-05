from stats import get_num_words, get_book_text

def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    num_words = get_num_words(book_content)
    print(f"{num_words} words found in the document")



main()
