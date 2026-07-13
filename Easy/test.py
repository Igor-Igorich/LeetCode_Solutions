#это тестовый файл созданный с планшета


# Task 1.1

# version 1
'''
flag = 1
while flag != 0:
    try:
        num = int(input('Введите число:'))
    except ValueError:
        print('Ошибка: введите корректное число.')
    else:
        flag = 0

print(f'{num} * 10 = {num * 10}')

'''
# version 2
'''
while True:
    try:
        user_input = input('Введите число: ')
        num = float(user_input)
    except ValueError:
        print('Ошибка: введите корректное число.')
    else:
        break

print(f'{num} * 10 = {num * 10}')

'''

# Task 1.2

def divide_numbers(a: int | float, b: int | float) -> int | float:
    result = 0
    
    try:
        result = a / b
    except ZeroDivisionError as z:
        print(f'{z}: На ноль делить нельзя!')
    except TypeError as t:
        print(f'{t}: Ошибка типов данных!')

    return result
'''
print(divide_numbers(1, 'a'))
'''


# Task 1.3

def new_divide_numbers(a, b):

    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as z:
        print(f'{z}')
    except Exception as t:
        print(f'{t}')
    else:
        return result
'''
print(new_divide_numbers(1, 12312))
'''


# Task 2.1

def read_file_content(filename):
    try:
        file = open(filename, encoding='utf-8')
    except FileNotFoundError:
        print('Файл не найден.')
    else:
        print(file.read())
    finally:
        try:
            file.close()
            print('Файл закрыт')
        except NameError:
            print('Файл не был открыт, закрывать нечего.')

def read_file_content_good(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            print(file.read())
        print('Файл закрыт.')
    except FileNotFoundError:
        print('Файл не найден.')

'''
def main():
    filename = input('Введите название файла: ')
    read_file_content_good(filename)

if __name__ == '__main__':
    main()
'''


# Task 2.2

class MyOperationError(Exception):
    '''Была введена некорректная операция.
    Допускаются только + - * /
    '''
    
    def __str__(self):
        return f'Допускаются только операции: + - * /'

def simple_calculator():
    
    while True:
        op_1 = input('Введите 1-ый операнд: ')
        op_2 = input('Введите 2-ой операнд: ')
        oprt = input('Введите операцию (+, -, *, /): ')
        res = 0
    
        try:
            op_1 = float(op_1)
            op_2 = float(op_2)
            
            match oprt:
                case '*':
                    res = op_1 * op_2
                case '+':
                    res = op_1 + op_2
                case '-':
                    res = op_1 - op_2
                case '/':
                    res = op_1 / op_2
                case _:
                    raise MyOperationError
        
        except ValueError:
            print('Операнды должны быть числами!')
        except ZeroDivisionError:
            print('Делить на ноль нельзя!')
        except MyOperationError as my_error:
            print(my_error)
        else:
            print(f'Результат = {res}')
        finally:
            answer = input('Хотите выполнить еще одну операцию? (yes/no) ').lower().strip()
            if answer in ('нет', 'н', 'no', 'n'):
                break
            elif answer in ('да', 'д', 'yes', 'y'):
                continue
            else:
                print('Пожалуйста, введите "да" или "нет"')

'''
if __name__ == '__main__':
    simple_calculator()
'''


# Task 3.3 

# Трансформация исключения (цепочка исключений) с сохранением причины для отладки
def process_data(data):
    try:
        num = int(data)
        return num
    except ValueError as original_error:
        raise TypeError('Ошибка обработки данных') from original_error
'''
if __name__ == '__main__':
    data = input('Input data: ')
    process_data(data)
'''




####################### Модуль warnings (Предупреждения) #######################

# РАЗОБРАТЬ !!!

import warnings
import functools

def deprecated(message="Эта функция устарела и будет удалена в будущих версиях."):
    """Декоратор для пометки функций как устаревших."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                message,
                DeprecationWarning,
                stacklevel=2
            )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@deprecated()
def old_function():
    """Старая функция, которую нужно заменить."""
    print("Я всё ещё работаю!")