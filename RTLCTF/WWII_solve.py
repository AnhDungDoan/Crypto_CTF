
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
stri = "ebchafgdijkpmnoz" 

ALPHABET = ALPHABET.lower()

for x in ALPHABET:
    flag = False
    for y in stri:
        if (x==y):
            flag = True
    if flag == False:
        print(x, end = '')

miss = "ol su vx wy qt"