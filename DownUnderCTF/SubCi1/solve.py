import math

flag = '𖿫𖝓玲𰆽𪃵𢙿疗𫢋𥆛🴃䶹𬑽蒵𜭱𫢋𪃵蒵🴃𜭱𩕑疗𪲳𜭱窇蒵𱫳'

ans = [60323, 55323, 57323, 58565, 55321, 57171, 63917, 55424, 56765, 55400, 56565, 55369, 56959, 30103, 55406, 56459, 55380, 56731, 55359, 56579, 19897, 55409, 56445, 33973, 55346, 57201, 55406, 56459, 55400, 56565, 33973, 55359, 56579, 55346, 57201, 55397, 56657, 30103, 55403, 56499, 55346, 57201, 31367, 33973, 55430, 57075]
def get(x):
    return (-3+int(math.sqrt(9-4*13*(7-x))))//26

for x in flag:
    print(chr(get(ord(x))), end = '')
    