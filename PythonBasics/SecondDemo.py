values = [1, 2, "raju", 4.5, 7]

# List is a data type that allow multiple values and can be different data types.
print(values[0])
print(values[3])

# Print last index value
print(values[-1])

# Print Partial Data from list (Extract sub index)
print(values[0:2])

# Inject in the list
values.insert(3, "Faroque")
print(values)

# Inject in the last
values.append("End")
print(values)

# Update the Value
values[2] = "Abdullah Al"
print(values)

# Delete Index
del values[-1]
print(values)
