n = int(input())
b = 0
c = 2
lista = []
while b < n:
    d = 0
    for i in range(2,c + 1):
        if c % i == 0:
            d += 1
    if d == 1:
            lista.append(c)
            b += 1
    c += 1
r = 0
while r < n:
    print(lista[r])
    r+=1
