product = input()

product_type = "unknown"
if product == "banana" \
    or product == "apple" \
    or product == "kiwi" \
    or product == "cherry" \
    or product == "lemon" \
    or product == "grapes":
    product_type = "fruit"
elif product == "tomato" \
    or product == "cucumber" \
    or product == "pepper" \
    or product == "carrot" :
    product_type = "vegetable"

print(product_type)
