def fibonacci(max_num):
    num_1 = 0
    num_2 = 1
    for i in range(max_num):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2
 
for num in fibonacci(6):
    print(num)
