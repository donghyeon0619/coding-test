def test(x, y=[]):
    y.append(x)
    return y

print(test(1))
print(test(2))