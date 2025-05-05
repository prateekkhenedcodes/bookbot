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


            
def sort_num_char(char_num_dict):
    sorted_list = sorted(char_num_dict.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_list)
