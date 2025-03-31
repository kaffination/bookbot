def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char not in characters:
            characters[char] = 0
        characters[char] += 1
    return characters

def sort_dict(char_dict):
    return dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
