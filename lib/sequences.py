#!/usr/bin/env python3

def print_fibonacci(length):

    if length <= 0:
        print('[]')
        return
    
    fibonacci_sum = 0
    fibonacci_list = []
    
    for index in range(length):

        if index <= 1:
            fibonacci_list.append(fibonacci_sum)
            fibonacci_sum += 1
        else:
            next_fibonacci_value = fibonacci_list[index - 2] + fibonacci_list[index - 1]
            fibonacci_list.append(next_fibonacci_value)
        
    print(fibonacci_list)
