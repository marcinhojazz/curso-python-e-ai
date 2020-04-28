# x = 2 in (1, 2, 3, 4, 5)
# x = 2 in (2, 4, 6, 8, 10)

# y = 2 in range(1, 6)
# y = 2 in range(2, 11, 2)

# x= (2 or 10) in (1, 2, 3, 4, 5)
# x= (2 and 10) in (1, 2, 3, 4, 5)
x = (2 or 10) and (3 or 11) in (1, 2, 3, 4, 5)

print(x)

