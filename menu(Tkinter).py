from tkinter import *
import math

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
    n = int(n)
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
       d += 2
    return d * d > n

def Factor(n): #складывание простых множителей в массив
   n = int(n)
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

#---------------------------------------------------------------------------------------------------------------------

def baby_giant():


    def alg(a, b, p):

        a = int(a)
        b = int(b)
        p = int(p)

        H = int(p ** (1 / 2)) + 1

        # print('H = ', H)

        c = (a ** H) % p
        # print('c = ', c)
        u = {}
        v = {}
        u[0] = 0

        for i in range(1, H + 1):
            u[i] = ((c ** i) % p)
        u = list(u.items())
        u.sort(key=lambda item: item[1])  # магия для сортировок значений по возрастанию с сохранением их ключа
        u = dict(u)

        for k in range(H + 1):  # магия для сортировок значений по возрастанию с сохранением их ключа
            v[k] = ((b * (a ** k)) % p)
        v = list(v.items())
        v.sort(key=lambda item: item[1])
        v = dict(v)

        # print(u)
        # print(v)

        # x = []
        x = 0

        # нужно хранить индексы для совпадающих элементов(u и v)
        # хотя по сути достаточно найти первые совпадающие элементы и по одному u, v
        # x = H*u - v (mod p-1)

        for key in u:
            for keys in v:
                if v[keys] == u[key]:
                    # x.append((H*key - keys) % (p-1))
                    x = (H * key - keys) % (p - 1)
                    break  # чтобы не перебирать словари до упора, выход из цикла при первом найденном x




        text = str(a)+"^"+str(x)+" = "+str(b)+" mod("+str(p)+")"  #вставить текст
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = int(a.get())
            b_val = int(b.get())
            p_val = int(p.get())

            if(b_val>p_val):
                inserter("Введите b<p")

            else:

                if(isSimple(p_val)!=True):
                    inserter("Введите простое p")
                else:
                    inserter(alg(a_val, b_val,p_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Алгоритм согласования")
    frame = Frame(win)
    frame.grid()
    win.resizable(width=False, height=False)

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите a").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3)
    b_lab = Label(frame, text="Введите b").grid(row=1, column=4)

    p = Entry(frame, width = 16)
    p.grid(row=1, column = 5)
    p_lab = Label(frame, text = "Введите p").grid(row=1,column = 6)

    but = Button(frame, text="Рассчитать", width=11, command=handler).grid(row=1, column=7, padx=(9, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="darkred", font="Arial 12", width=65, height=20)

    output.grid(row=2, columnspan=8)

#--------------------------------------------------------------------------------------------------------------------------

def pohlig_hell():


    def alg(a, b, p):

        a = int(a)
        b = int(b)
        p = int(p)

        thisone = set(Factor(p - 1))  # множество элементов из factor, чтобы выделить q(без повторов)

        # теперь нужно как-то посчитать a[i] для q[i] (степень)
        # для этого напишем словарь, в который поместим элементы множества ключами, а в значении будем держать степень
        qi = dict()

        # пока что заполим значения нулями
        for keys in thisone:
            qi[keys] = 0

        for k in Factor(p - 1):
            if k in qi:
                qi[k] += 1  # будем накручивать счётчик, когда ключ встречается в thisone
        # теперь имеется словарь, который учитывает степень простых множителей

        b0 = b

        r = dict()  # создаем словарь для ri, там будет хитрость
        tup = []  # создаем список, который потом будет переделан под кортеж и передан в значение словаря

        for key in qi:
            for j in range(key):
                tup.append(int((a ** (j * (p - 1) / key)) % p))  # складываем в словарь значения для a в разных степенях
            r[key] = tuple(tup)
            tup.clear()

        # теперь r - таблица значений для поиска a
        # состав r: ключ - qi, значение - кортеж ai в степени, j - индекс элемента в кортеже

        x = []  # на сумму xi

        chineese_theorem = dict()  # словарик для финального хранения qi - ключ, N = x (mod qi)

        # x0 находим вне цикла каким-то образом


        # теперь одна из самых громоздких функций в коде

        for q in r:
            b_i = int((b ** ((p - 1) / q)) % p)  # нашли первую b_i для x0
            for k in range(q):
                if r[q][k] == int(b_i):
                    x.append(k)  # нахождение x0
            degree = 0  # нахождение массива x1...xi
            for j in range(q - 1):
                degree -= x[j] * (q ** j)
                b_i = ((b * a ** degree) ** ((p - 1) / (q ** (j + 2)))) % p
                for k in range(q):
                    if r[q][k] == int(b_i):
                        x.append(k)  # нахождение x[j+1]

            xx = 0
            for i in range(len(x)):
                xx += x[i] * (q ** i)

            # не так всё просто, в модуле нужно учитывать степень, поэтому
            deg = qi[q]
            chineese_theorem[q ** deg] = xx

            x.clear()  # очищаем массив

        # и, наконец, реализация китайской теоремы об остатках через алгоритм Гаусса
        M = 1
        x = 0
        for q in chineese_theorem:
            M *= q

        for mi in chineese_theorem:
            b = M / mi
            c = chineese_theorem[mi]
            xi = Evk(b, mi)
            x += xi * c * b

        x = int(x % M)


        text = str(a)+"^"+str(x)+" = "+str(int(b0))+" mod("+str(p)+")"  #вставить текст
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    def handler():
        try:
            # make sure that we entered correct values
            a_val = int(a.get())
            b_val = int(b.get())
            p_val = int(p.get())

            if(b_val>p_val):
                inserter("Введите b<p")

            else:

                if(isSimple(p_val)!=True):
                    inserter("Введите простое p")
                else:
                    inserter(alg(a_val, b_val,p_val))
        except ValueError:
            inserter("Убедитесь, что вы ввели оба числа")

    win = Toplevel(root)
    win.title("Алгоритм Полига-Хеллмана")
    frame = Frame(win)
    frame.grid()
    win.resizable(width=False, height=False)

    a = Entry(frame, width=16)
    a.grid(row=1, column=1, padx=(4, 0))
    a_lab = Label(frame, text="Введите a").grid(row=1, column=2)

    b = Entry(frame, width=16)
    b.grid(row=1, column=3)
    b_lab = Label(frame, text="Введите b").grid(row=1, column=4)

    p = Entry(frame, width = 16)
    p.grid(row=1, column = 5)
    p_lab = Label(frame, text = "Введите p").grid(row=1,column = 6)

    but = Button(frame, text="Рассчитать", width=11, command=handler).grid(row=1, column=7, padx=(9, 0))

    # место для вывода решения уравнения
    output = Text(frame, bg="darkred", font="Arial 12", width=65, height=20)

    output.grid(row=2, columnspan=8)


#------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title("Коллоквиум по дискретной математике")
root.minsize(500,300)
root.resizable(width=False, height=False)  # выключаем возможность изменять окно


fra1 = Frame(root)
fra1.grid()

lab = Label(root, text="Алгоритмы дискретного логарифмирования \n Поиск решения уравнения a^x = b (mod p)", font="Arial 12", width=60, height=15)
lab.grid()
m = Menu(root)
root.config(menu=m)

fm = Menu(m,tearoff=0) #меню для натуральных чисел
m.add_command(label="Алгоритм Солгасования",command = baby_giant)

hm = Menu(m,tearoff=0) #меню для натуральных чисел
m.add_command(label="Алгоритм Полига-Хеллмана",command = pohlig_hell) #добавить команду


def exit_(event):
    root.destroy()


root.bind('<Escape>', exit_)
root.mainloop()
