import math

def isSimple(n): #проверка на простоту числа
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
       d += 2
    return d * d > n

print("Поиск решения уравнения a^x = b (mod p)")


while True:
    print('Введите простое число p')
    p = int(input())
    if isSimple(p):
        break

print('Введите a')
a = int(input())
b = 9999**99

while (b>p):
    print('Введите b < p')
    b = int(input())


H = int(p ** (1 / 2)) + 1

#print('H = ', H)

c = (a ** H) % p
#print('c = ', c)
u = {}
v = {}
u[0] = 0

for i in range(1, H + 1):
    u[i] = ((c ** i) % p)
u = list(u.items())
u.sort(key=lambda item: item[1]) #магия для сортировок значений по возрастанию с сохранением их ключа
u = dict(u)


for k in range(H + 1):          #магия для сортировок значений по возрастанию с сохранением их ключа
    v[k]=((b * (a ** k)) % p)
v = list(v.items())
v.sort(key=lambda item: item[1])
v = dict(v)

#print(u)
#print(v)

#x = []
x = 0

# нужно хранить индексы для совпадающих элементов(u и v)
# хотя по сути достаточно найти первые совпадающие элементы и по одному u, v
# x = H*u - v (mod p-1)

for key in u:
    for keys in  v:
        if v[keys] == u[key]:
            #x.append((H*key - keys) % (p-1))
            x = (H*key - keys) % (p-1)
            break #чтобы не перебирать словари до упора, выход из цикла при первом найденном x

print()

print(a, "^", x, " = ", b, "mod(",p, ")")

