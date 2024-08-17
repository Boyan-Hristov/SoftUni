# for loop се използва когато знаем предварително броя на итерациите
# while loop – докато условието е вярно, цикълът ще се изпълнява (до безкрай) !!!
# винаги да се пише 1 ред, който да гарантира, че няма да се изпадне в безкраен while цикъл –
# както е долу number +=1 – променя условието

for number in range(1, 10):
    print(number)

number = 1
while number < 10:
    print(number)
    number +=1

line = input()
while line != "Stop":
    print("Loop")
    line = input()

# continue ни връща обратно в началото на цикъла, всичко след него в тялота на цикъла не се изпълнява
# както break, continue се използва само в цикъл