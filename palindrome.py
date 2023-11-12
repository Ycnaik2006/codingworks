def is_palindrome(word):
    # Function to check if a word is a palindrome
    return word == word[::-1]

def find_palindromic_words(sentence):
    words = sentence.split()
    palindrome_words = [word for word in words if is_palindrome(word)]

    return palindrome_words

if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    palindrome_words = find_palindromic_words(input_sentence)

    if palindrome_words:
        print("Palindrome words in the sentence:")
        for word in palindrome_words:
            print(word)
    else:
        print("No palindrome words found in the sentence.")
