ItemsInCart = 0
# 2 Items will be added to cart

if ItemsInCart != 2:
    # raise Exception("Products Cart Count Not Matching")
    pass
# assert (ItemsInCart == 2)

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e, "File Not Found")
finally:
    print("Finally, Fail/Pass. Cleaning Up Records Anyway")
