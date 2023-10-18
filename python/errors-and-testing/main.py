class NegativeNumberError(Exception):
    pass

try:
    n = int(input('Enter a numerator: '))
    d = int(input('Enter a denominator: '))

    if n < 0 or d < 0:
        raise NegativeNumberErrorr()

    q = n / d # Exception was raised when trying to divide by zero. 

    print(q)
except ZeroDivisionError:
    print('Denominator cannot be 0')
except ValueError:
    print('Inputs must be positive')
except NegativeNumberError:
    print('Inputs must be positive integers')
except Exception as e:
    print('Something went wrong')
    print(e)
    # Log the debug information (including traceback) to an error log file.