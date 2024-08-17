# for цикъл – колко пъти трябва да се изпълни определно действие \
              # работи само с цели числа

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# Трябва ми променлива, която да сменя стойността си от 1 до 10.
# За number искам диапазон от 1 до 10 включително.
# for number in range(1, 10):
#     # Трябва всеки път да я принтирам.
#     print(number)


# for number in range(1, 10, 2):
#     print(number)

# for number in range(start, final, step)
# финална стойност е exclusive и не се включва в цикъла, крайната стойност е final - 1
# стъпката определя как ще се движим през целите числа

# 3 възможности:
# for number in range(start, final, step) -> ползва се когато искаме да прескачаме
# for number in range(start, final) -> стъпката е 1 по подразбиране
                                       # ползва се когато ни интересува на коя итерация се намираме
# for number in range(final) -> началната стойност е 0 по подразбиране
                               # ползва се когато ни интересува броя на итерациите

#for number in range(1, 11) == for number in range(1, 10 + 1)

# string = "text"
# text_length = len(string)
# print(text_length)
# print(string[0])
# print(string[1])
# print(string[2])
# print(string[3])
# # индексите започват от 0 -> стойността на последния индекс е равна на дължината на текста - 1
# # ако искаме да прочетем текста наобратно -> индексите могат да са отрицателни и започват от -1
# print(string[-1])
# print(string[-2])
# print(string[-3])
# print(string[-4])

string = "text"
for index in range(0, len(string)):
    print(f"Index = {index}, symbol = {string[index]}")

# горният код е аналогичен с долния

string = "text"
for character in string:
    print(character)

string = "text"
for index, character in enumerate(string):
    print(f"Index = {index}, symbol = {character}")
