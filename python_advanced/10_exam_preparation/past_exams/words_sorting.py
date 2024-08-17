def words_sorting(*args):
    result = ""
    words = {}
    for word in args:
        words[word] = sum([ord(x) for x in word])

    if sum({value for value in words.values()}) % 2 != 0:
        sorted_words = sorted(words.items(), key=lambda x: -x[1])
    else:
        sorted_words = sorted(words.items())

    for data in sorted_words:
        result += f"{data[0]} - {data[1]}\n"

    return result


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
