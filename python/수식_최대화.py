from itertools import permutations

def fix_order(numbers, operations, order):
    stack = []
    result = []
    
    for i in range(len(operations)):
        result.append(numbers[i])
        if not stack:
            stack.append(operations[i])
        else:
            while stack and order.index(stack[-1]) <= order.index(operations[i]):
                result.append(stack.pop())
            stack.append(operations[i])
    
    result.append(numbers[-1])
    while stack:
        result.append(stack.pop())
    
    return result
        
def calculation(expression):
    stack = []
    
    for i in expression:
        if i.isdigit():
            stack.append(i)
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(eval(str(num1) + i + str(num2)))
    return abs(stack[0])

def solution(expression):
    operations = ['+', '-', '*']
    number_list = expression
    operation_list = []
    result = []
    value = []
    operations_order = list(permutations(operations, 3))
    
    for i in operations:
        number_list = number_list.replace(i, ' ')
    number_list = number_list.split()
    
    for i in range(len(expression)):
        if expression[i] in operations:
            operation_list.append(expression[i])
    
    for order in operations_order:
        result.append(fix_order(number_list, operation_list, order))
    
    for expression in result:
        value.append(calculation(expression))
        
    return max(value)
        

print(solution("50*6-3*2"))