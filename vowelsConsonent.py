vowels=input("Enter a letter\n")

if ("a"==vowels or "e"==vowels or "i"==vowels or "o"==vowels or "u"==vowels):
    print(f"{vowels} is a lower case vowel")

elif("A"==vowels or "E"==vowels or "I"==vowels or "O"==vowels or "U"==vowels):
    print(f"{vowels} is an upper case vowel")

else:
    print(f"{vowels} is a consonant letter")