#!/usr/bin/python3

import re
from Crypto.Util.number import long_to_bytes
from Crypto.Random import random
# from secret import REAL_COORDS, FLAG_MSG
FLAG_MSG = 'ok'
REAL_COORDS = 5756627544102572649201219381096443309301530404084814366157678459246004007288774904822314549
FAKE_COORDS = 5754622710042474278449745314387128858128432138153608237186776198754180710586599008803960884

sub = 2004834060098370751474066709314451173098265931206128970902260491823296702175896018353665
              
p = 13318541149847924181059947781626944578116183244453569385428199356433634355570023190293317369383937332224209312035684840187128538690152423242800697049469987

def create_shares(secret):
    r1 = 11079272668242383312266966133619520877880133526995366478847034875667436601844511972949488586180142963943851736558226981319885086146972756033966657408933756
    r2 = 10073879051456915684656951822132190997361502575820386640867739152116985996286495415561137156221962439297483886246389438573062840619319585981062400310966967
    s1 = r1*r2*secret % p
    s2 = r1*r1*r2*secret % p
    s3 = r1*r2*r2*secret % p
    return [s1, s2, s3]

def reveal_secret(shares):
    s1, s2, s3 = shares
    secret = pow(s1, 3, p) * pow(s2*s3, -1, p) % p
    return secret

def run_combiner(shares):
    try:
        your_share = int(input('Enter your share: '))
        return reveal_secret([your_share, shares[1], shares[2]])
    except:
        print('Invalid share')
        exit()

def is_coords(s):
    try:
        return re.match(r'-?\d+\.\d+?, -?\d+\.\d+', long_to_bytes(s).decode())
    except:
        return False

def main():
    shares = create_shares(REAL_COORDS)
    print(f'Your share is: {shares[0]}')
    print(f'Your two friends input their shares into the combiner and excitedly wait for you to do the same...')

    secret_coords = run_combiner(shares)
    print(f'The secret is revealed: {secret_coords}')
    if not is_coords(secret_coords):
        print('"Hey those don\'t look like coordinates!"')
        print('Your friends grow a bit suspicious, but you manage to convince them that you just entered a digit wrong. You decide to try again...')
    else:
        print('"Let\'s go get the treasure!!"')
        print('Your friends run off to the revealed location to look for the treasure...')
        exit()

    secret_coords = run_combiner(shares)
    if not is_coords(secret_coords):
        print('"This is way too sus!!"')
        exit()

    if secret_coords == FAKE_COORDS:
        print('You\'ve successfully deceived your friends!')

        try:
            real_coords = int(input('Now enter the real coords: '))
            if real_coords == REAL_COORDS:
                print(FLAG_MSG)
            else:
                print('Incorrect!')
        except:
            print('Incorrect!')
    else:
        print('You are a terrible trickster!')

if __name__ == '__main__':
    main()
