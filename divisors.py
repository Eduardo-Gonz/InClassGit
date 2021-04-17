def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if(num % i == 0):
            divisors.append(i)


find_divisors(5)