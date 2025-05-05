def get_book_text(book_path):
    with open(book_path) as f: 
        return f.read()
    

def get_num_words(book_content):
    return len(book_content.split())


def get_num_characters(book_content):
    my_dict = {}
    for char in book_content:
        char = char.lower()
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict
            
