def is_palindrome(word):
    # Convert the word to lowercase for case-insensitive comparison
    word = word.lower()

    # Check if the word is equal to its reverse
    return word == word[::-1]

# Example usage:
input_word = "Padma"
if is_palindrome(input_word):
    print(f"{input_word} is a palindrome!")
else:
    print(f"{input_word} is not a palindrome.")
