import random
import timeit
timeit.timeit(stmt='pass', setup='pass', number=1000000, globals=None)

#min
l1 = [random.randint(0, 100) for _ in range(10 + 1)]
l1 = sorted(l1)
def minlist(l1):
    return l1[0]

#max
l2 = [random.randint(0, 100) for _ in range(10 + 1)]
l2 = sorted(l2)
def maxlist(l2):
    return l2[-1]
# print(minlist(l1), maxlist(l1))

#sum
l3 = [random.randint(0,100) for _ in range(10+1)]
l3 = sorted(l3)
# print(l3)

def sumlist(l3):
    s = 0
    for x in l3:
        if  x != 0:
            s = s + x
    return s

# print(sumlist(l3))

#prod
l4 = [random.randint(0,100) for _ in range(10+1)]
l4 = sorted(l4)
# print(l4)
def prodlist(l4):
    m = l4[0]
    for i in l4:
        if i == 0:
            print('0')
            break
        else:
            m = m * i
        if i == 1:
            m = m * 1
    return m

# print(prodlist(l4))

#filter
l5 = [random.randint(0,100) for _ in range(10+1)]
l5 = sorted(l5)
print(l5)
x = 25
result_g = []
result_l = []
def filterlist(l5):
    print('max = ', maxlist(l5))
    print('min = ', minlist(l5))
    for n in range(len(l5)):
        if maxlist(l5) - x > minlist(l5) + x:
            n_val = l5[-(n+1)]
            print('back = ', n_val)
        else:
            n_val = l5[(n+1)]
            print('run = ', n_val)

        if n_val > x:
            result_g.append(n_val)
        if n_val < x:
            result_l.append(n_val)
    print(f'Больше {x}: {result_g}, Меньше {x} {result_l}')
    return result_g, result_l

print(filterlist(l5))
print("\n" + "-"*30)
print("Замер с помощью default_timer:")
start = timeit.default_timer()
filterlist(l5)  # Один запуск функции
end = timeit.default_timer()
print(f"Время выполнения одного запуска: {end - start:.8f} секунд")
