print('HomeWork1')
import random
n=int(input('Ведите кол-во монет: '))
k=0
for i in range(n):
    r=random.randint(0,1)
    print(r, end=' ')
    if r == 0:
        k += 1
    result = k if k<n/2 else n-k
print('')
print('минимальное кол-во монет которое нужно перевернуть:',[result])
