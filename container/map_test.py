map = {}

x = map.setdefault('a', [])
x.extend([1, 2, 3])
print(map)
x = map.get('a')

print(x)
