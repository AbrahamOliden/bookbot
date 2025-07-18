import sys
from stats import word_count
from stats import count_characters
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        counted_words = word_count(text)
        counted_characters = count_characters(text)
        sorted_characters = sort_dictionary(counted_characters)

        stringified_count = ""

        for character in sorted_characters:
            if character["char"].isalpha():
                stringified_count = stringified_count + f"{character["char"]}: {character["num"]}" + "\n"

        report_string = (
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {filepath}...\n"
        "----------- Word Count ----------\n"
        f"Found {counted_words} total words\n"
        "--------- Character Count -------\n"
        f"{stringified_count}\n"
        "============= END ==============="
        )

        return report_string


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    print(get_book_text(f"{path_to_book}"))

main()