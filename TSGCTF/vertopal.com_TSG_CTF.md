---
jupyter:
  colab:
    name: TSG CTF.ipynb
    toc_visible: true
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .markdown id="D5V6NeHkQjhs"}
# **TSG CTF**
:::

::: {.cell .markdown id="_crUG92MRMgB"}
# **Beginner\'s Crypto**
:::

::: {.cell .markdown id="vHGsnfwTRUUn"}
**Problem:**

*beginners_crypto_2021.py*

    from secret import e
    from Crypto.Util.number import getStrongPrime, isPrime
     
    p = getStrongPrime(1024)
    q = getStrongPrime(1024)
    N = p * q
    phi = (p - 1) * (q - 1)
     
    with open('flag.txt', 'rb') as f:
        flag = int.from_bytes(f.read(), 'big')
     
    assert(isPrime(e))
    assert(isPrime(e + 2))
    assert(isPrime(e + 4))
     
    e1 = pow(e, 0x10001, phi)
    e2 = pow(e + 2, 0x10001, phi)
    e3 = pow(e + 4, 0x10001, phi)
     
    c1 = pow(flag, e1, N)
    c2 = pow(flag, e2, N)
    c3 = pow(flag, e3, N)
     
    print(f'p = {p}')
    print(f'q = {q}')
    print(f'c1 = {c1}')
    print(f'c2 = {c2}')
    print(f'c3 = {c3}')

*output.txt*

    p = 167710954518007348037383082265231465648795974011761905177264545864288011527333715495850532989338171489309608848431113452814709692343039027970312735521415071265608660628968391884287240987858607818275329135585153511665148279408708087727501421558738163577629329044315775019460018956186674179846621352371150072281
    q = 130354329753344570838569091064852072757046774566775609047544069941246798511317343102715733555464772099991834579660053860799207243561908291522943696711982657846373844514551117658179060004064010647453939332217996817580433587341521331941287365948919907797478197717562721233289937471168288241937022054501586986443
    c1 = 2560344169447809042170685026483682125499025654554670516499742981486615082413150123244985585751880264831112089324011804397189638172356179296987581738515619297036118472798499254785110885662931526277474101787493114656242031264678448394380651657330967744585361662315313462698221954777506355498445242300193032704972074020068699180111637362566860530694807230108024167631423062629721393506643291591971626450262144814424411172618188943774725105690851574922374544865628890948773274109561622040022136970632948166009941425683576381155722191980954262373394704682297682490061906408535261437100820855976015526295573831744458528440
    c2 = 9041231631916227099296501948589424780380702196870972231114747229225732542137483840187783630590878594711315671224997985975031038623195921968945234067183003568830416719957054703139219879265482072634572699299971785171441858501409377942183918216246312330291820452436486171483461790388518159980027140392750222843449604265528929311978655519463562520038992870162220913137870017065557254099767583925177889051326144499369420594398043223307161794788085369471538477803421726790780799629276012701406231535048423554314287152404245482928538931953627397633165453319078105028671410039195670727134471011040601278722143504641171853743
    c3 = 3193069356811106774640161554961405075257002069448498144279061282023129342916422283816661697787316681475161942522570615456264481238277711114193792510286127129056376618422336477707825009085263623755329815306483253646072909132096678270667136193038337386976289222105363398033633185639402128949635525665502328717781718263894690234837016959581149138917064108193064639981137359869717065147934752707676203651598070046066514316196771853484143158367616177332902152347890310640338106015356361617700741042461419248117687350565094928451141103632305400493998164788411031832078388030194992306440474662871408938796429927990102583837
:::

::: {.cell .markdown id="Sphl-vPDSTKw"}
**Solve**

Nhận xét:

-   Do e, e+2 và e+4 đều là số nguyên tố, ta nghĩ ngay đến e = 3 [đây là
    chỗ chứng
    minh](https://math.stackexchange.com/questions/1653536/show-that-we-cannot-have-a-prime-triplet-of-the-form-p-p-2-p-4-for)
-   Do e và e +2 là 2 số nguyên tố cùng nhau -\> e\^65537 và
    (e+2)\^65537 đều là 2 số nguyên tố cùng nhau =\> GCD = 1. Từ đây ta
    dùng thuật giải Euclid mở rộng và dễ dàng tìm flag

***solve.py***

    from Crypto.Util.number import *
    import math
    import gmpy2

    p = 167710954518007348037383082265231465648795974011761905177264545864288011527333715495850532989338171489309608848431113452814709692343039027970312735521415071265608660628968391884287240987858607818275329135585153511665148279408708087727501421558738163577629329044315775019460018956186674179846621352371150072281
    q = 130354329753344570838569091064852072757046774566775609047544069941246798511317343102715733555464772099991834579660053860799207243561908291522943696711982657846373844514551117658179060004064010647453939332217996817580433587341521331941287365948919907797478197717562721233289937471168288241937022054501586986443
    c1 = 2560344169447809042170685026483682125499025654554670516499742981486615082413150123244985585751880264831112089324011804397189638172356179296987581738515619297036118472798499254785110885662931526277474101787493114656242031264678448394380651657330967744585361662315313462698221954777506355498445242300193032704972074020068699180111637362566860530694807230108024167631423062629721393506643291591971626450262144814424411172618188943774725105690851574922374544865628890948773274109561622040022136970632948166009941425683576381155722191980954262373394704682297682490061906408535261437100820855976015526295573831744458528440
    c2 = 9041231631916227099296501948589424780380702196870972231114747229225732542137483840187783630590878594711315671224997985975031038623195921968945234067183003568830416719957054703139219879265482072634572699299971785171441858501409377942183918216246312330291820452436486171483461790388518159980027140392750222843449604265528929311978655519463562520038992870162220913137870017065557254099767583925177889051326144499369420594398043223307161794788085369471538477803421726790780799629276012701406231535048423554314287152404245482928538931953627397633165453319078105028671410039195670727134471011040601278722143504641171853743
    c3 = 3193069356811106774640161554961405075257002069448498144279061282023129342916422283816661697787316681475161942522570615456264481238277711114193792510286127129056376618422336477707825009085263623755329815306483253646072909132096678270667136193038337386976289222105363398033633185639402128949635525665502328717781718263894690234837016959581149138917064108193064639981137359869717065147934752707676203651598070046066514316196771853484143158367616177332902152347890310640338106015356361617700741042461419248117687350565094928451141103632305400493998164788411031832078388030194992306440474662871408938796429927990102583837
    e = 3

    n = p*q
    phi = (q-1) * (p-1)
    e1 = pow(e, 0x10001, phi)
    e2 = pow(e + 2, 0x10001, phi)
    e3 = pow(e + 4, 0x10001, phi)

    g1 = inverse(e1, e2)
    g2 = ((e1 * g1 - 1) // e2)
     
    flag = (pow(c1, g1, n) * inverse((pow(c2, g2, n)), n)) % n 
     
    print(long_to_bytes(int(flag)))

> FLAG: TSGCTF{You are intuitively understanding the distribution of
> prime numbers! Bonus: You can solve this challenge w/ N instead of p
> and q!}
:::

::: {.cell .markdown id="_qd9KKBwajqj"}
# **Minimalist\'s Private**
:::

::: {.cell .markdown id="EywqPhcxaqw2"}
**Problem**

> The smaller is the better. I have removed all the unnecessary things
> in my private.

*encrypt.py*

    from Crypto.Util.number import getStrongPrime, isPrime
    from random import randrange
    #from secret import p, q, L, e, d

    p = getStrongPrime(2048)
    q = getStrongPrime(2048)
    L = 3
    e = 3
    d = 3

    class RSA:
        def __init__(self, p, q, L, e, d):
            assert(isPrime(p) and isPrime(q))
            self.N = p * q
            self.L = L
            self.e = e
            self.d = d

            # these are the normal RSA conditions
            for _ in range(100):
                assert(pow(randrange(1, self.N), self.L, self.N) == 1)
            assert(self.e * self.d % self.L == 1)

            # minimal is the best
            assert(self.L * self.L <= 10000 * self.N)

        def gen_private_key(self):
            return (self.N, self.d)

        def gen_public_key(self):
            return (self.N, self.e)

        def encrypt(self, msg):
            return pow(msg, self.e, self.N)

        def decrypt(self, c):
            return pow(c, self.d, self.N)

    flag = open('flag.txt', 'rb').read()
    msg = int.from_bytes(flag, byteorder='big')
    assert(msg < p * q)

    rsa = RSA(p, q, L, e, d)
    encrypted = rsa.encrypt(msg)
    assert(rsa.decrypt(encrypted) == msg)

    print(f'N, e = {rsa.gen_public_key()}')
    print(f'c = {encrypted}')
:::

::: {.cell .markdown id="GjBt1rM5oMSu"}
**Solve**

Lại nhận xét:

-   Do n là tích 2 số nguyên tố 2048 bit, nên khi random trong (1, N)
    100 lần thì xác suất để ra 1 trong 2 số nguyên tố trên là rất thấp
    -\> số random sẽ là nguyên tố cùng nhau với N
-   Theo [phi hàm
    Carmichael](https://en.wikipedia.org/wiki/Carmichael_function). Ta
    dễ dàng biết được L = LCM(p-1, q-1) (với p, q là 2 số nguyên tố mà
    tích của chúng là N)
-   Có: LCM(p-1, q-1) = ((p-1) \* (q-1)) / GCD(p-1, q-1). Mà L*L \<=
    10000*N =\> len(L) \<= 510 bits. Ta lại có (p-1) \* (q-1) sẽ \<=
    1007 bits =\> GCD(p-1, q-1) sẽ khoảng 500bits.
-   Gọi s*a = p-1, s*b = q - 1 =\> N = p*q = (sa + 1)*(sb + 1) =
    a*b*s\^2 + a*b*s + 1
-   Bruteforce a, b =\> p, q =\> phi =\> flag

solve.py

    import gmpy2
    from Crypto.Util.number import *

    N = 1108103848370322618250236235096737547381026108763302516499816051432801216813681568375319595638932562835292256776016949573972732881586209527824393027428125964599378845347154409633878436868422905300799413838645686430352484534761305185938956589612889463246508935994301443576781452904666072122465831585156151
    e = 65537
    c = 254705401581808316199469430068831357413481187288921393400711004895837418302514065107811330660948313420965140464021505716810909691650540609799307500282957438243553742714371028405100267860418626513481187170770328765524251710154676478766892336610743824131087888798846367363259860051983889314134196889300426

    def quadratic_solve(a,b,c):
        return (-b + gmpy2.iroot(b*b - 4*a*c, 2)[0])//(2*a)

    for a in range(1, 2**15):
        for b in range(1, 2**15):
            s = quadratic_solve(a*b, a+b, 1 - N)
            p = s*a + 1
            q = s*b + 1
            if p*q == N and isPrime(p) and isPrime(q):
                phi = (p-1)*(q-1)
                d = pow(e, -1, phi)
                m = pow(c, d, N)
                print(long_to_bytes(m).decode())
                exit()

> FLAG:
> TSGCTF{Roll_Safe:\_You_c4n\'t_be_exploited_1f_you_are_a\_minimali5t_enough_and_y0u_don\'t_have_any_s3crets_in_your_mind}
:::