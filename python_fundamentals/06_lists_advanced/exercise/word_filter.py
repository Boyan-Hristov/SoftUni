words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
# print("\n".join(filtered_words))
for element in filtered_words:
    print(element)
