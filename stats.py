def word_count(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    
    return counter

def count_characters(text):
    character_occurrences = dict({})

    for character in text:
        lower_character = character.lower()
        if lower_character in  character_occurrences:
            character_occurrences[lower_character] += 1
        else:
            character_occurrences[lower_character] = 1
    
    return character_occurrences

def sort_dictionary(dictionary):
    def sort_on(items):
        return items["num"]
    
    sorted = []

    for data in dictionary:
        appearances = dictionary[data]
        sorted.append({"char": data, "num": appearances})
    
    sorted.sort(reverse = True, key = sort_on)

    return sorted