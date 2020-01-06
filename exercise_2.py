def fac(f):
    if f == 0 or f == 1:
        return 1
    return f * fac(f - 1)


in_number = input('input the number:')
print(fac(int(in_number)))