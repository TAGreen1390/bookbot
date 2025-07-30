def word_count(book_text):
    words = book_text.split()
    return len(words)

def character_count(book_text):
    characters = {}
    lower_case = book_text.lower()
    for char in lower_case:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] +=1
    return characters

def character_sort(characters):
    def sort_on(items):
        return items["num"]
    
    character_list = []
    for char in characters:
        num = characters[char]
        character_list.append({"char":char, "num":num})
    character_list.sort(reverse=True, key=sort_on)
    return character_list