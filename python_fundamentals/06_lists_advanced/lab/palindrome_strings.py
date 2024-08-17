words = input().split()
magic_word = input()

palindromes = [word for word in words if word == word[::-1]]
magic_word_count = palindromes.count(magic_word)
print(palindromes)
print(f"Found palindrome {magic_word_count} times")
