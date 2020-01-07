def fac(f):
    if f == 0 or f == 1:
        return 1
    return f * fac(f - 1)


in_number = input('input the number:')
print(fac(int(in_number)))

# use while loop
n = int(input('input a number: '))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)
#use for loop
n = int(input('input a number: '))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)
#use lambda
n = int(input('input a number: '))
fact = 1
def short_fact(x):return 1 if x<=1 else x*short_fact(x-1)
print(short_fact(n))

