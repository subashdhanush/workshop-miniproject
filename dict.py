from PyDictionary import PyDictionary

dictionary=PyDictionary()

word=input("enter a word")
meaning=dictionary.meaning(word)
print(meaning)

if meaning:
    print(meaning)
else:
    print("not found")    