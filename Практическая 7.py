# #Вариант 2
# #№1
# def s(a, h):
#     s = 3*a*h
#     return(s)
# a = float(input('Введите длину сторону треугольника '))
# h = float(input('Введите длину высоты к стороне '))
# print('Площадь правильного шестиугольника равна: ', s(a,h))

#№2
# import math
# def s(a1, a2, a3, a4, a5, a6):
#     s1 = (a1 * a2) 
#     s2 = (a3 * a4)
#     s3 = (a5 * a6) 
#     return(s1, s2, s3)
# a1 = float(input())
# a2 = float(input())
# a3 = float(input())
# a4 = float(input())
# a5 = float(input())
# a6 = float(input())
# print(s(a1, a2, a3, a4, a5, a6))

# #Вариант 3
# #№1
# import math
# def g(a1, b1, a2, b2):
#     g1 = math.sqrt(a1**2 + b1**2)
#     g2 = math.sqrt(a2 ** 2 + b2 ** 2)
#     if g1 > g2:
#         return('g1 > g2')
#     if g1 < g2:
#         return('g2 > g1')
#     else:
#         return('g1 = g2')
# a1 = float(input())
# b1 = float(input())
# a2 = float(input())
# b2 = float(input())
# print(g(a1, b1, a2, b2))

# #№2
# def sort(s):
#     return(sorted(s))
# s = str(input('Введите произвольную строку '))
# print(s)
# print(sort(s))



