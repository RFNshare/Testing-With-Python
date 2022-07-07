path = '../resources/sample.txt'
lst = []
with open(path, 'r') as reader:
    a = reader.read().split()
    rev = reversed(a)
    with open(path, 'w') as writer:
        for i in rev:
            print(i)
            writer.write(i + " ")



