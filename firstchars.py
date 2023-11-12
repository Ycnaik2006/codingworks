sentence=input("Enter a sentence:")
words=sentence.split()
word=""
for w in words:
    if w:
        word+=w[0]
print("the word formed by joining the first char of each word is :",word)
