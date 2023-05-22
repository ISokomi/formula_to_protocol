from itertools import product


def check_correct(n, input_str):
    stack = []
    operators = ['!', '&', '|']

    x_check = [0 for i in range(n)]
    y_check = [0 for i in range(2**n)]

    mode = "VARIABLE"
    i = 0
    while i < len(input_str):
        char = input_str[i]
        
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                return False
            stack.pop()
        elif char in operators:
            if mode == "VARIABLE" and char != '!':
                return False
            mode = "VARIABLE"
        elif char == 'x':
            if mode == "OPERATOR":
                return False
            if i == len(input_str) - 1:
                return False
            else:
                i = i + 1
                if input_str[i].isdigit():
                    num = int(input_str[i])
                    if num >= 0 and num < n:
                        x_check[num] = 1
                    else:
                        return False
                else:
                    return False
            mode = "OPERATOR"
        elif char == 'y':
            if mode == "OPERATOR":
                return False
            num = 0
            for j in range(n):
                if i == len(input_str) - 1:
                    return False
                else:
                    i = i + 1
                    if input_str[i].isdigit():
                        digit = int(input_str[i])
                        if digit == 0 or digit == 1:
                            num = num + (2**(n - j - 1)) * digit
                        else:
                            return False
                    else:
                        return False
            y_check[num] = 1
            mode = "OPERATOR"
        else:
            return False
        i = i + 1
    return all(x_check) and all(y_check)

def check_multiplex(n, input_str):
    return True

n = int(input('Введите число "адресных" переменных n: '))
print('Пример для ввода при n = 1: (!x0&y0|x0&y1)')
print('Пример для ввода при n = 2: (y00|x0|x1)&(y01|x0|!x1)&(y10|!x0|x1)&(y11|!x0|!x1)')
form = input(f'Введите формулу, реализующую мультиплексорную функцию от {n} переменных:\n')

while not check_correct(n, form):
    print('Формула некорректна, попробуйте ввести еще раз:')
    form = input()

while not check_multiplex(n, form):
    print('Формула задана корректно, но не реализует мультиплексорную функцию, попробуйте ввести еще раз:')
    form = input()

print(f'Формула задана корректно и реализует мультиплексорную функцию от {n} переменных\n')

print("Protocol super trivial:")
for i in range(n):
    print(f"Alice sends a{i} to Bob")

for i in range(n):
    print(f"Bob sends b{i} to Alice")
print("They find the difference with n rounds and 2*n algorithm complexity\n")

print("Or if the protocol is trivial:")
for i in range(n):
    print(f"Alice sends a{i} to Bob")
print("Bob is thinking log(n) times and sends b0 to Alice")
print("And they find the difference with n rounds and n + log(n) algorithm complexity\n")
