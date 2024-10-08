#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: [seneca_id]

def operate(number1, number2, operator):
    if operator == 'add':
        return number1 + number2
    if operator == 'subtract':
        return number1 - number2
    if operator == 'multiply':
        return number1 * number2
    return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))        # 15
    print(operate(10, 5, 'subtract'))   # 5
    print(operate(10, 5, 'multiply'))   # 50
    print(operate(10, 5, 'divide'))     # Error: function operator can be "add", "subtract", or "multiply"
