def pangkat(a, b):
    if a < 0 or b < 0:
        return "hanya untuk bilangan bulat positif"
    if b > 1:
        return a*pangkat(a, b-1)
    return a
print(pangkat(3,2))