arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arr)
print(str(arr).replace(","," ")[1:-1])

print(" ".join(map(str, arr)))
print(map(str, arr))