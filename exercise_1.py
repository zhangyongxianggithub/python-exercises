l = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        l.append(str(num))
print(','.join(l))

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=',')
