def numbers_sum(*args):
    result = ""
    positives = [x for x in args if x > 0]
    negatives = [y for y in args if y < 0]

    result += f"{sum(negatives)}\n{sum(positives)}\n"
    if abs(sum(negatives)) > sum(positives):
        result += "The negatives are stronger than the positives"
    else:
        result += "The positives are stronger than the negatives"

    return result


numbers = [int(x) for x in input().split()]

print(numbers_sum(*numbers))
