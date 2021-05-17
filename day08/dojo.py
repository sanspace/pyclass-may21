squareGenerator=(x**2 for x in range(0,11))   

print(squareGenerator)

for i in squareGenerator:
    print(i, end=" ")
print()

print(sum(squareGenerator))
