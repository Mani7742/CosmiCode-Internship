# Write a program to find the longest word in a sentence
#  provided by the user, ignoring punctuation.

import string

def find_longest_word(sentence):
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.translate(translator)
    words = cleaned_sentence.split()
    if not words:
        return ""
    longest_word = max(words, key=len)
    return longest_word

if __name__ == "__main__":
    user_sentence = input("Enter a sentence: ")
    longest = find_longest_word(user_sentence)
    print("Longest word:", longest)