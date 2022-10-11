# #Вариант 1
# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
# print(max(a))
# a.reverse()
# print(a)

# n = int(input())
# a = []
# p = 0
# c = 0
# for i in range(n):
#     a.append(int(input()))
# print(a)
# print(a[0])
# for j in range(len(a)):
#     s = a[j]
#     p += s
# print(p)
# c = p/n
# a[0] = c
# print(a)

# #Вариант 2
# n = int(input())
# a = []
# p = 0
# c = 0
# for i in range(n):
#     a.append(int(input()))
# print(a)
# print((min(a)), a.index(min(a)))

# a = []
# b = []
# c = []
# n = int(input())
# for i in range(n):
#     a.append(int(input()))
# print(a)
# for p in a:
#     if p >= 0:
#         b.append(p)
#     else:
#         c.append(p)
# print(a, b, c)

# #Вариант 8
# a = []
# k = 0
# c = 1
# n = int(input())
# for i in range(n):
#     a.append(int(input()))
# print(a)
# for p in a:
#     k += p
#     c *= p
# print(c, k)

# a = []
# c = 0
# n = int(input())
# for i in range(n):
#     a.append(int(input()))
# print(a)
# for p in a:
#     c += p/n
# for g in range(len(a)):
#     if a[g] == 0:
#         a[g] = c
# print(c)
# print(a)