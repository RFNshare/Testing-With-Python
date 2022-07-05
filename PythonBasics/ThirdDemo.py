greeting = "Good Morning"

if greeting == "Morning":
    print("Condition Matches")
else:
    print("Condition Do not match")

print("If Else is completed")

obj = [2, 3, 4, 5, 6, 7, 8, 9]
for i in obj:
    print(i)
print("***************")
a = 0
for i in range(6):
    a += i
print(a)
print("***************")
for j in range(1, 10, 4):
    print(j)

print("***************")
it = 4
for k in obj:
    if k == 4:
        continue
    print(k)