def triangular(n):
    total = 0
    if n < 0:
        return "berikan bilangan bulat positif"
    if n == 1:
        return 1
    while n > 0:
        total += n 
        n-= 1
    return total
print(triangular(5))