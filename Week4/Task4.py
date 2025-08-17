#  Implement a program that uses a dictionary to count the frequency of each character in a string.
def char_frequency(s):
    """
    Counts the frequency of each character in the string s.
    Returns a dictionary with characters as keys and frequencies as values.
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example usage:
if __name__ == "__main__":
    input_str = "cosmic code"
    frequencies = char_frequency(input_str)
    print("Character frequencies:")
    for char, count in frequencies.items():
        print(f"'{char}': {count}")