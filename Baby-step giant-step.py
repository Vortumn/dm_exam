import math
from primal import isPrime

print("Поиск решения уравнения a^x = b (mod p)")


while True:
    print('Введите простое число p')
    p = int(input())
    if isPrime(p):
        break

print('Введите a')
a = int(input())
b = p + 1

while (b>p):
    print('Введите b < p')
    b = int(input())


H = int(math.sqrt(p)) + 1

#print('H = ', H)

c = (a ** H) % p
# kinda magic
u = sorted([(i, (c ** i) % p) for i in range(1, H + 1)], key = lambda item: item[1])
v = sorted([(i, (b * a ** i) % p) for i in range(H + 1)], key = lambda item: item[1])

for i in u:
    for j in v:
        if i[1] == j[1]:
            x = (i[0] * H - j[0]) % (p - 1)
            break
try:
    print("{}^{} = {} (mod  {})".format(a, x, b, p))
except:
    print("Нет решения")