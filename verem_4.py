print('Practical task 1')
print("Calculation of employee's salary")
print('\n'
      '')
from sys import argv
path, ar1, ar2, ar3 = argv
ar1, ar2, ar3 = map(int, argv[1:])
sal = ar1 * ar2 + ar3
print('The number of working hours:', ar1)
print('Salary for 1 hour, rubles:', ar2)
print('Bonus, rubles:', ar3)
print("The employee's salary:", sal)
print('\n'
      '')

print('Practical task 2')
print("The values are larger than the previous ones")
print('\n'
      '')
old = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [old[i] for i in range(1, len(old)) if old[i] > old[i-1]]
print(old)
print(new)
print('\n'
      '')

print('Practical task 3')
print("Numbers from 20 to 240, multiples of 20 or 21")
print('\n'
      '')
li = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(li)
print('\n'
      '')

print('Practical task 4')
print("Non-duplicate list items")
print('\n'
      '')
li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('li', li)
unique_li = [i for i in li if li.count(i) == 1]
print("unique_li", unique_li)
print('\n'
      '')

print('Practical task 5')
print("Multiplication of all even list items from 100 to 1000")
print('\n'
      '')
from functools import reduce
li = [i for i in range(100, 1001) if i % 2 == 0]
print(li)
print(reduce(lambda a, b: a * b, li))
print('\n'
      '')

print('Practical task 6')
print('An iterator that generates integers starting from 3 to 10')
from itertools import count
for el in count(3):
      print(el)
      if el == 10:
            break
print('\n'
      'An interator that repeats the elements of a list')
from itertools import cycle
li = list(range(10, 30, 2))
print(li)
for i, j in enumerate(cycle(li)):
      print(j)
      if i > 16:
            break