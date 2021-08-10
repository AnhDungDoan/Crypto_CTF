# def f(x):
#     yield((x:=-~x)*x+-~-x)%727

# #exec('def f(x):'+'yield((x:=-~x)*x+-~-x)%727;'*100)
# g = 281
# for _ in range(100):
#     #print(g, end = ' ')
#     g=f(g)

# m = list(map(lambda c:ord(c)^next(g),list(open('f').read())))
# print(m)


exec('def f(x):'+'yield ((x:=x+1)*x-x+1) %727;'*100)
g = f(470)
print(*map(lambda c:chr(int(c)^next(g)),list(open('output.txt').read().split())), end = '')

# for i in range(257,10000):
#     if ((i*i + i + 1) % 727 == 363):
#         print(i)
#         break