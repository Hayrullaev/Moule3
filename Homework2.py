def print_params(a=1, b='Строка', c=True):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')


'''вызов функции без аргумента'''
print_params()
# # чтобы был отсутп при выводе ответа
print()

'''вызов с одним аргументов'''
print_params(b=25)
print()

'''вызов с двумя аргументами'''
print_params(5, c=[1, 2, 3])
print()

# '''вызов с терьемя аргументами'''
print_params(10, 'HI', 15 >= 15)
print()
# Расспаковка параметров

valus_list = [4, 'Life', False]
valus_dict = {'a':16, 'b': 'World', 'c': True}

def print_params(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, '=', value)

print_params(*valus_list, **valus_dict)

print()
#  распаковка + отдельные параметры
valus_list_2 = [56, 'Love']
print_params(*valus_list_2, 42)