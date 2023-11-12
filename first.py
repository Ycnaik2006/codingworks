# Input a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize an empty string to store the first characters
first_chars = ""

# Iterate through the words and add the first character to the result string
for word in words:
    first_chars += word[0]

# Display the result
print("Output:", first_chars)
    
