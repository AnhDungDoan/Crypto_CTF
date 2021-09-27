from string import ascii_lowercase, digits
CHARSET = "DUCTF{}_!?'" + ascii_lowercase + digits
n = len(CHARSET)

FLAG = "CTF{"
enc = "yw5d"

# for x in enc:
#     print(CHARSET.index(x), end = ' ')


# for a in range(39,47):
#     for b in range(0,47):
#         for c in range(0,47):
#             for d in range(0,47):
#                 for e in range(0,47):
#                     temp = (a+b+c+d+e+1) %47
#                     if (temp < 20):
#                         f = 20 - temp
#                     elif (temp > 20):
#                         f = 67 - temp
#                     else:
#                         f = 67 - temp
#                     ans = ""
#                     for ch in FLAG:
#                         x = CHARSET.index(ch)
#                         fract = (a*pow(x,6) + b*pow(x,5) + c*pow(x,4) + d*pow(x,3) + e*pow(x,2) + f*x + 1) %47
#                         ans = ans + CHARSET[fract]
#                     if (ans == enc):
#                         print(a,", ",b,", ",c,", ",d,", ",e,", ",f)
                        #quit()
#                     #print(ans)
g = 1
a,b,c,d,e,f = 41 ,  15 ,  40 ,  9 ,  28 ,  27
enc = "Ujyw5dnFofaou0au3nx3Cn84"
flag = ""
def cal_frac(x):
    fract = (a*pow(x,6) + b*pow(x,5) + c*pow(x,4) + d*pow(x,3) + e*pow(x,2) + f*x + 1) %47
    return fract

for i in range(len(enc)):
    for x in CHARSET:
        if (CHARSET[cal_frac(CHARSET.index(x))] == enc[i]):
            flag += x
            break

print(len(enc))
print(len(flag))
print(flag)
