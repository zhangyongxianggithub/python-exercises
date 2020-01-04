l = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        l.append(str(num))
print(','.join(l))

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=',')

while True:
    reply = input('type some world:')
    if reply == 'stop':
        break
    try:
        int(reply)
    except:
        print('Bad input！'*8)
    else:
        print(int(reply)**2)
print('Bye!!!!')
