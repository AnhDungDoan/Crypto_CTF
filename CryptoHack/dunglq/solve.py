from Crypto.Util.number import getPrime, isPrime, bytes_to_long

e = 65537
N = 25155990855409315020613173493361950995687137094731229073857223990108072506838006937986622152133594550340943510683357680183063679219347040591757162330384922909310550938934789336407149360477567400136265610911276053212779416829656722982071942508655312824469827757692925023306642192396001459634076527587547268998000148178647028917586793777372968871991906004082708882906146785461418460898096662655973240496653971260242979389079870110213589586673305919747948799659751595022911132732468173885823719642859416307718576933907422977615927338830955629327233275049288853619750065047148332750578907113612208546625989406376337319473
c = 4401596078952223472152618234744493029672484597419290638747419288801211745130439374198676109646322636433711750231065251405004816635375427950340091841931141160846538637273177302452856395079047558938958712019156378422169429322820232439008001831648327823418884691049658084404205630052011486311848753720763436630630918749442959627537941337201358553523758183243520925969584411230358485486552370772554528559539532487447693232305910022409887480535081816598752707425501846045549348440499016841399293408704695654922075278560267202766191582296817615285193661761565093131516288534719043440579783120897629017535576665377852200509

alphabet = "0123456789abc"

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def _int_to_13(x: int):
    res = []
    while x > 0:
        res.append(alphabet[x % 13])
        x //= 13
    return ''.join(res[::-1])

def _13_to_int(s: str):
    return int(s, 13)

def genkey(bits):
    while True:
        p = getPrime(bits)
        q = _13_to_int(_int_to_13(p)[::-1])
        if isPrime(q):
            e = 65537
            while True:
                if gcd(e, (p - 1) * (q - 1)) == 1:
                    return e, p, q
                e += 1


p = 19520053
print(_int_to_13(p))
q = _int_to_13(p)[::-1]
print(q)
p = _int_to_13(p)

print(_int_to_13(_13_to_int(p) * _13_to_int(q)))