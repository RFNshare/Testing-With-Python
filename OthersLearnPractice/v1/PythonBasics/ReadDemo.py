file = open("../resources/sample.txt")

# Read Number of characters by passing parameter
# print(file.read(25))
#
# # Read 1 line
print(file.readline())

# Print line by line

line = file.readline()
print("***", line)
for i in file.readline():
    print(i)
# while line != "":
#     print(line)
#     line = file.readline()
file.close()
