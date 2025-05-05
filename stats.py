def get_book_text(book_path):
    with open(book_path) as f: 
        return f.read()
    

def get_num_words(book_content):
    return len(book_content.split())
