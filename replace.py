def replace_characters(sentence):
    vowels_translation = str.maketrans("aeiou", "#" * 5)
    consonants_translation = str.maketrans("bcdfghjklmnpqrstvwxyz", "$" * 21)
    
    # Apply both translation tables sequentially
    modified_sentence = sentence.translate(vowels_translation).translate(consonants_translation)
    
    return modified_sentence

# Input sentence
user_input = input("Enter a sentence: ")

# Replace vowels with "#" and consonants with "$"
modified_sentence = replace_characters(user_input)
 
# Output the modified sentence
print("Modified Sentence:", modified_sentence)
