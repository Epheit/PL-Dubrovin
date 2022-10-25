#Вариант 1
#№1
# n = int(input())
# a = []
# f = 0
# q = 0
# for i in range(n):
#     c = input().split()
#     for i in range(len(c)):
#         c[i] = int(c[i])
#     a.append(c)
# print(a)
# for p in range(len(a)):
#     for k in range(len(a[p])):
#         if k > p:
#             if a[p][k] >=0:
#                 print(a[p][k])
#                 f += 1
#                 q += (a[p][k])
# print(f, q)

#№2
# n = int(input())
# b = []
# m = 0
# p = 0
# for i in range(n):
#     c = input().split()
#     for i in range(len(c)):
#         c[i] = int(c[i])
#     b.append(c)
# print(b)
# for k in range(len(b)):
#     m = b[k].index(min(b[k]))
#     b[k][m], b[k][0]= b[k][0], b[k][m]
#     p = b[k].index(max(b[k]))
#     b[k][p], b[k][-1] = b[k][-1], b[k][p]
# print(b)

# Вариант 5
#№1
# n = int(input())
# a = []
# for i in range(n):
#     c = input().split()
#     for i in range(len(c)):
#         c[i] = int(c[i])
#     a.append(c)
# print(a)
# for i in range(len(a)):
#     a[i].sort()
# print(a)

#№2
# n = int(input())
# a = []
# f = 0
# for i in range(n):
#     c = input().split()
#     for i in range(len(c)):
#         c[i] = int(c[i])
#     a.append(c)
# print(a)
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j] %2 ==0: a[i][j] =0
#         else: a[i][j] = 1
# print(a)