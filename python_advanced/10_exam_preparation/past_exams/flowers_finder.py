from collections import deque

words = {
    "rose": list("rose"),
    "tulip": list("tulip"),
    "lotus": list("lotus"),
    "daffodil": list("daffodil")
}

vowels = deque(input().split())
consonants = input().split()
is_found = False

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in words.keys():
        for letter in (vowel, consonant):
            if letter in words[word]:
                occurrences = word.count(letter)
                for i in range(occurrences):
                    words[word].remove(letter)
                    if not words[word]:
                        print(f"Word found: {word}")
                        is_found = True
                        break
            if is_found:
                break
        if is_found:
            break
    if is_found:
        break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
