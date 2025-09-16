import sys

for text in sys.stdin:
    words = text.split()
    sentence = []
    vowels = "aeiouy"

    for i in range(len(words)):
        firstWord = words[i]
        firstLetter = firstWord[:1]
        if firstLetter in vowels: 
            vowel = words[i] + "yay"
            sentence.append(vowel)
        # consonant

        else:
            for j, k in enumerate(words[i]): 
                index = -1
                if k in vowels:
                    index = j
                    consonant = words[i]
                    consonant1 = consonant[:index]
                    consonant2 = consonant[index:]
                    consonant = consonant2 + consonant1 + "ay"
                    break
            sentence.append(consonant)

    for b in range(len(sentence)):
        if b == len(sentence)-1:
            print(sentence[b])
        else:
            print(sentence[b], end=" ")