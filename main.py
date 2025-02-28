from stats import word_count, char_count, sort_dict
import sys

def get_book_text(filename):
    with open(filename) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    if (len(sys.argv) < 2):
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    dictio = char_count(text)
    print_list = sort_dict(dictio)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path)
    print("----------- Word Count ----------")
    print("Found " + str(word_count(text)) + " total words")
    print("--------- Character Count -------")

    for item in range (0, len(print_list)):
        for key, value in print_list[item].items():
            if key.isalpha():
                print(f"{key}: {value}")

    print("============= END ===============")
        


    
    
    

    

main()