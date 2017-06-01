def Evk(a,b):               #расширенный алгоритм Евклида
    (xa,ya) = (1,0)
    (xb,yb) = (0,1)
    while b != 0:
        t = a
        T = (xa,ya)
        a = b
        (xa,ya) = (xb,yb)
        q = t//b
        b = t - q*b
        xb = T[0] - q*xb
        yb = T[1] - q*yb
    return xa


def isSimple(n): #проверка на простоту числа
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
       d += 2
    return d * d > n

def Factor(n): #складывание простых множителей в массив
   Ans = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           Ans.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       Ans.append(n)
   return Ans

print("Поиск решения уравнения a^x = b (mod p)")

while True:
    print('Введите простое число p')
    p = int(input())
    if isSimple(p):
        break

thisone = set(Factor(p-1)) #множество элементов из factor, чтобы выделить q(без повторов)

#теперь нужно как-то посчитать a[i] для q[i] (степень)
#для этого напишем словарь, в который поместим элементы множества ключами, а в значении будем держать степень
qi = dict()

#пока что заполим значения нулями
for keys in thisone:
    qi[keys] = 0

for k in Factor(p-1):
     if k in qi:
        qi[k] +=1 #будем накручивать счётчик, когда ключ встречается в thisone
#теперь имеется словарь, который учитывает степень простых множителей

print('Введите a')
a = int(input())
print('Введите b')
b = int(input())

b0 = b

r = dict() #создаем словарь для ri, там будет хитрость
tup = [] #создаем список, который потом будет переделан под кортеж и передан в значение словаря


for key in qi:
    for j in range(key):
        tup.append(int((a**(j*(p-1)/key))%p))  #складываем в словарь значения для a в разных степенях
    r[key] = tuple(tup)
    tup.clear()

#теперь r - таблица значений для поиска a
#состав r: ключ - qi, значение - кортеж ai в степени, j - индекс элемента в кортеже

x = [] #на сумму xi

chineese_theorem = dict() #словарик для финального хранения qi - ключ, N = x (mod qi)

#x0 находим вне цикла каким-то образом


#теперь одна из самых громоздких функций в коде

for q in r:
    b_i = int((b**((p-1)/q))%p) #нашли первую b_i для x0
    for k in range(q):
        if r[q][k] == int(b_i):
            x.append(k) #нахождение x0
    degree = 0                            #нахождение массива x1...xi
    for j in range(q-1):
        degree -= x[j]*(q**j)
        b_i = ((b*a**degree)**((p-1)/(q**(j+2))))%p
        for k in range(q):
            if r[q][k] == int(b_i):
                x.append(k)  # нахождение x[j+1]

    xx = 0
    for i in range(len(x)):
        xx += x[i]*(q**i)

    #не так всё просто, в модуле нужно учитывать степень, поэтому
    deg = qi[q]
    chineese_theorem[q**deg] = xx

    x.clear() #очищаем массив


#и, наконец, реализация китайской теоремы об остатках через алгоритм Гаусса
M = 1
x = 0
for q in chineese_theorem:
    M*=q

for mi in chineese_theorem:
    b = M/mi
    c = chineese_theorem[mi]
    xi = Evk(b,mi)
    x += xi*c*b

x = int(x % M)

print(a, "^", x, " = ", b0 , "mod(", p, ")")