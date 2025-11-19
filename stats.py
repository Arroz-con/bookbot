def get_number_of_words(text):
    words = text.split()
    return len(words)


def get_number_of_characters(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    return chars


def sort_on(items):
    return items["num"]


def get_sorted_characters(char_dict):
    new_chars_dict = []
    for k, v in char_dict.items():
        new_chars_dict.append({"char": k, "num": v})
    
    new_chars_dict.sort(reverse=True, key=sort_on)
    return new_chars_dict
