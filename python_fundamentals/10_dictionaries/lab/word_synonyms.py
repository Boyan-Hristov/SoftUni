words_count = int(input())
synonyms = {}
for word in range(words_count):
    current_word = input()
    synonym = input()
    if current_word not in synonyms:
        synonyms[current_word] = []
    synonyms[current_word].append(synonym)
for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")
