import owiener
from Crypto.Util.number import *
import gmpy2
import base64
morse =[84,105,65,57,73,68,69,48,77,106,77,50,78,106,77,52,77,122,99,53,78,122,107,119,78,68,81,49,77,122,65,52,78,106,65,50,77,106,81,52,77,122,69,48,79,84,69,119,77,68,107,122,78,84,69,50,78,106,89,53,77,106,73,121,77,106,107,52,79,84,65,122,77,84,85,120,77,122,107,121,78,68,103,119,77,68,65,51,79,84,85,49,78,122,89,53,79,84,103,119,77,106,77,119,78,122,85,50,77,106,81,50,78,84,81,122,78,106,107,122,78,84,81,120,78,84,85,121,78,106,81,121,77,122,69,50,77,68,107,49,78,68,85,121,79,68,73,50,78,84,73,51,79,84,81,119,79,68,85,119,77,84,107,49,77,68,77,52,77,106,77,122,77,68,103,52,78,84,73,52,79,68,77,49,78,106,99,122,78,122,81,122,79,84,81,49,78,84,99,121,78,106,69,52,77,122,65,53,79,68,69,121,77,68,89,122,78,84,65,120,78,106,107,121,77,106,85,120,79,68,89,121,78,122,85,122,77,106,77,121,78,122,69,119,77,84,89,51,79,68,99,48,77,106,89,51,77,122,107,50,79,68,99,52,78,84,69,51,78,122,103,121,77,68,77,122,79,68,81,53,78,106,89,119,77,68,69,53,78,122,77,48,77,122,103,119,79,68,77,49,79,68,103,121,77,106,69,53,77,84,107,122,78,106,85,49,78,84,103,120,78,68,99,53,79,84,103,121,79,68,107,48,77,84,73,120,78,68,85,120,78,122,85,48,77,106,81,49,77,84,107,52,78,122,99,49,77,84,89,52,79,68,69,51,77,106,73,51,78,84,107,52,77,84,85,52,78,122,65,53,79,84,107,121,79,68,81,52,77,68,107,120,78,84,77,53,78,122,103,50,77,106,103,121,79,68,85,51,78,84,99,48,78,106,103,121,77,119,112,108,73,68,48,103,77,119,112,106,73,68,48,103,77,84,85,121,77,84,89,51,78,68,73,48,77,106,99,122,79,84,99,51,78,68,77,50,78,122,65,121,79,68,107,119,77,106,99,122,77,106,99,48,78,84,65,120,78,122,77,48,77,68,69,121,78,122,89,49,79,68,103,121,78,68,103,51,77,68,65,52,77,122,77,52,79,84,99,122,77,106,77,121,78,84,65,121,77,84,99,119,77,122,85,50,77,122,99,49,77,84,81,52,79,68,69,52,78,106,65,53,78,106,73,120,79,68,89,122,79,84,99,49,77,106,85,50]

N = 84136859502569695467234125074699936259514567232762911904674991868380577043819723616944392561992394156000426265925813237357449668311429059829435172843876353576086827536591633048577570358009855597315837528016023100131680975036483780008826416135798117834942637800030085512015966116264203277679614842237339602067    
e = 3
c = 152167424273977436702890273274501734012765882487008338973232502170356375148818609621863975256

for i in range(1):
    tmp = c + i*N
    b, check = gmpy2.iroot(tmp, e)
    if (check):
        print("i =", i)
        print(long_to_bytes(b))