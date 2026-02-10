def vowel_or_consonant(ch):
    char =ch.lower()
    vowel="aeiou"
    if char in vowel:
        print("It is a vowel")
    else:
        print("It is a consonant")
ch=input()
vowel_or_consonant(ch)