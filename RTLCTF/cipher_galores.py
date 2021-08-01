a = "ikc{j1dgc3_tIpgk0_ty@113ex3_3y?}"

ALPHABET = "JKLMNOPQRSTUVWXYZABCDEFGHI"
ALPHABET = ALPHABET.lower()

ans = ''
for x in a:
    if (ord(x) > 96 and ord(x) < 123):
        x = ALPHABET[ord(x) - 97]
        ans += x
    else:
        ans += x

print(ans)