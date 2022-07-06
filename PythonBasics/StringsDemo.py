str = "https://rfnshare.github.io/"
str1 = "Abdullah"
str2 = "Abdullah Al Faroque"
# Substring check
print(str1 in str2)
# Print String index
print(str[1])
# Print SubString
print(str[8:16])
# concatenation
print("{} {}".format(str, str1))
print(str1 + str)

# String Split
var = str2.split(" ")
print(var)

# Full Strip, Left Strip, Right Strip
str4 = " great "
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())
