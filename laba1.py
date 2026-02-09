x = 10
y = 5
z = 0
#z = x - y тоесть x = z + y 10 = z + 5
#Простой вариант
while z + 5 != 10:
  z += 1
print(z)

#Через Бинарный способ
def binary_code(x, y):
    if y == 0:
        return x
#0 <=z <=x
    low, high = 0, x
  #Наши границы от 0 до 10

    while low <= high:
        z = (low + high)//2
        if y + z == x:
            return z
        elif y + z < x:
            ow = z + 1
        else:
            high = z - 1
    return low

print({binary_code(10,5)})
