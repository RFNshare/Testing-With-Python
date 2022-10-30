ItemsInCart = 0
# 2 Product item will be added to cart

# assert ItemsInCart == 2
# if ItemsInCart != 2:
#     raise Exception("Products Cart Count Not Matching")

# try, except
path = '../resources/sample.txt'
try:
    with open(path, 'r') as reader:
        reader.read()
except Exception as e:
    print(e, "File name is wrong")

finally:
    print('Try Catch Complete, Cleaning Record....')
