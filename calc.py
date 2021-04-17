def calc(a, b):
    sum = a + b
    difference = a - b
    multiply = a * b
    division = a / b
    results = [sum, difference, multiply, division]
    sumOfResults = 0
    for x in results:
        sumOfResults += x
    
    print(sumOfResults)



calc(2,3)
