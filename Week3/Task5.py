# Write a program to find the most frequent word in a text file

import string

def most_frequent_word(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    if not words:
        return None, 0
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    most_word = max(freq, key=freq.get)
    return most_word, freq[most_word]

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    word, count = most_frequent_word(filename)
    if word:
        print(f"The most frequent word is '{word}' (appeared {count} times).")
    else:
        print("No words found in the file.")