def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)

        print(f"Begin report of {path} ")
        print(f"{word_count} words found in the document")
        for character, count in character_count.items():
            if character.isalpha():
                print(f"The '{character}' character was found {count} times")

    
def count_words(text):
    words = text.split()

    return len(words)


def count_characters(text):
    lowercased_text = text.lower()
    unique_characrers = list(set(lowercased_text))
    character_dictionary = {}

    for character in unique_characrers:
        character_dictionary[character] = lowercased_text.count(character)

    return character_dictionary


main()
