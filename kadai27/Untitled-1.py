def divide(func):
    def _func(a):
        return func(a)//3
    return _func

def multiply(func):
    def _func(a):
        @divide
        def _calculate(a):
            return a*10
        return _calculate(func(a))
    return _func
@divide
@multiply
def square(a):
    return a**2
print(square(9))