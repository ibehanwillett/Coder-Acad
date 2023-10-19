def get_name():
    def inner_function():
        name = input('Enter name:')
        func(name)
    return inner_function

@get_name
def greet(name):
    print(f'Hello, {name}!')

greet(name)