def word_count(book_text):

    words = book_text.split()
    return len(words)

def char_count(input_string):
    char_dict = {}

    for char in input_string:

        char = char.lower()
        
        if not char in char_dict:
            char_dict[char] =  1
        else: 
            char_dict[char]  += 1

    return char_dict

def sort_key(dict):
    number = list(dict.keys())[0]
    return dict[number]
        
def sort_dict(input_dict):

    dict_list = []
    
    for key, value in input_dict.items():
        temp_dict = {}
        
        temp_dict[key] = value
        dict_list.append(temp_dict) 
    
    dict_list.sort(reverse=True, key=sort_key)
    return dict_list
    
        

    
    

    

        
