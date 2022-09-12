print('HomeWork4')
import random
n=int(input('Введите кол-во детей в классе: '))
for i in range(n):
    r=random.randint(150,200)
    print(r, end=' ')
# Так и не понял как можно рассортировать рандомные числа , и выполнить условия

pety=int(input())

j=1
for i in r:
    if pety <=i:
        j+= 1
print(j)
