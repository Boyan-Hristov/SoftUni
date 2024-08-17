import re

barcodes_count = int(input())
for text in range(barcodes_count):
    string = input()
    valid_barcode_pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"
    product_group_pattern = r"\d"
    match = re.search(valid_barcode_pattern, string)
    if match:
        # barcode_list = list(match.group())
        product_group = re.findall(product_group_pattern, string)
        # product_group = [digit for digit in barcode_list if digit.isdigit()]
        if product_group:
            print(f"Product group: {''.join(product_group)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")


