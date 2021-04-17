def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if(num % i == 0):
            divisors.append(i)
    
    print(divisors)

def input_number():
    num = input("Enter number you want to find divisors of: ")
    find_divisors(num)

input_number()