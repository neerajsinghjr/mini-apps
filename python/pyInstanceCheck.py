### Checking instances of integer, string, float

f_i = 100.5888

print(isinstance(5, int))
print(isinstance(5.2, float))
print(isinstance('a', str))

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

## Results
print(is_integer_num(100))
print(is_integer_num(1.23))
print(is_integer_num(100.0))
print(is_integer_num('100'))

print(f_i.is_integer())