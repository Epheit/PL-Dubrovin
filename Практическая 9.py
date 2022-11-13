# f1 = open('C:/Users/User/Documents/Dubrovin K/PL-Dubrovin/kPr9/vvod.txt', 'r')
# f2 = open('C:/Users/User/Documents/Dubrovin K/PL-Dubrovin/kPr9/vivod.txt', 'w')
# g = 0
# q = 0
# print(f1)
# k = [[int(n)for n in x.split()]for x in f1]
# print(k)
# for p in range(len(k)):
#     for c in range(len(k[p])):
#         if c > p:
#             if k[p][c] >=0:
#                 print(k[p][c])
#                 g  += 1
#                 q += (k[p][c])
# print(g, q)
# f2.write('Количество элементов над главной диагональю: ')
# f2.write(str(g) + '\n')
# f2.write('Сумма элементов, находящихся над главной диагональю: ')
# f2.write(str(q) + '\n')

# f1 = open('C:/Users/User/Documents/Dubrovin K/PL-Dubrovin/kPr9/vvod.txt', 'r')
# f2 = open('C:/Users/User/Documents/Dubrovin K/PL-Dubrovin/kPr9/vivod.txt', 'w')
# print(f1)
# k = [[int(n)for n in x.split()]for x in f1]
# a = []
# for h in range(len(k)):
#     m = k[h].index(min(k[h]))
#     k[h][m], k[h][0]= k[h][0], k[h][m]
#     p = k[h].index(max(k[h]))
#     k[h][p], k[h][-1] = k[h][-1], k[h][p]
# print(k)
# f2.write(''.join(str(k)))

# f1 = open('C:/Users/User/Documents/Dubrovin K/PL-Dubrovin/kPr9/vvod.txt', 'r')
# f2 = open('C:/Users/User/Documents/Dubrovin K/PL-Dubrovin/kPr9/vivod.txt', 'w')
# print(f1)
# k = [[int(n)for n in x.split()]for x in f1]
# for i in range(len(k)):
#     k[i].sort()
# print(k)
# f2.write(str(k))

# f1 = open('C:/Users/User/Documents/Dubrovin K/PL-Dubrovin/kPr9/vvod.txt', 'r')
# f2 = open('C:/Users/User/Documents/Dubrovin K/PL-Dubrovin/kPr9/vivod.txt', 'w')
# k = [[int(n)for n in x.split()]for x in f1]
# for i in range(len(k)):
#     for j in range(len(k[i])):
#         if k[i][j] %2 ==0: k[i][j] =0
#         else: k[i][j] = 1
# print(k)
# f2.write(str(k))