m = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

vershina = 9
vis = [vershina]
us = [vershina]
t1 = {}
t = 1

while us:
    nl = []
    for n in us:
        for i, znachenie in enumerate(m[n - 1]):
            if znachenie == 1 and (i + 1) not in vis:
                vis.append(i + 1)
                t1[i + 1] = t + 1
                nl.append(i + 1)
    us = nl
    t += 1

t1[vershina] = 1

print("Вершина: Уровень")
for v1 in sorted(t1):
    print(v1, ":", t1[v1])
