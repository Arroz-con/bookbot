import sys
from stats import get_number_of_words, get_number_of_characters, get_sorted_characters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def print_final_result(words_count, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for index in sorted_dict:
        if index["char"].isalpha():
            print(f"{index["char"]}: {index["num"]}")
    print("============= END ===============")

def main():
    book_text = get_book_text(book_path)
    words_num = get_number_of_words(book_text)
    character_numbers = get_number_of_characters(book_text)
    characters_sorted = get_sorted_characters(character_numbers)
    print_final_result(words_num, characters_sorted)


main()
