def factorial_without_multiplication(n):
    sum =1
    for i in range(1,n):
        K = sum
        while i >0:
            sum+=K
            i-=1
    return sum

print(factorial_without_multiplication(9))