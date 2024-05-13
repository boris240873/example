
def find_monetka(x, y, r):
   if (x ** 2 + y ** 2) ** 0.5 <= r:

        print('Монетки в области нет')
   else:
       print('Монетка где-то рядом')


x = float(input('Введите координаты монетки X: '))

y = float(input('Введите координаты монетки Y: '))

r = int(input('Введите радиус: '))
find_monetka(x,y,r)
