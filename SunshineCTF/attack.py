#!/usr/bin/python3.4
# Written by Anirudh Anand (lucif3r) : email - anirudh@anirudhanand.com   
# This program will help to decrypt cipher text to plain text if you have
# more than 1 cipher text encrypted with same Modulus (N) but different
# exponents. We use extended Euclideangm Algorithm to achieve this.

__author__ = 'lucif3r'
   
import gmpy2
from Crypto.Util.number import *


class RSAModuli:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.m = 0
        self.i = 0
    def gcd(self, num1, num2):
        """
        This function os used to find the GCD of 2 numbers.
        :param num1:
        :param num2:
        :return:
        """
        if num1 < num2:
            num1, num2 = num2, num1
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1
    def extended_euclidean(self, e1, e2):
        """
        The value a is the modular multiplicative inverse of e1 and e2.
        b is calculated from the eqn: (e1*a) + (e2*b) = gcd(e1, e2)
        :param e1: exponent 1
        :param e2: exponent 2
        """
        self.a = gmpy2.invert(e1, e2)
        self.b = (float(self.gcd(e1, e2)-(self.a*e1)))/float(e2)
    def modular_inverse(self, c1, c2, N):
        """
        i is the modular multiplicative inverse of c2 and N.
        i^-b is equal to c2^b. So if the value of b is -ve, we
        have to find out i and then do i^-b.
        Final plain text is given by m = (c1^a) * (i^-b) %N
        :param c1: cipher text 1
        :param c2: cipher text 2
        :param N: Modulus
        """
        i = gmpy2.invert(c2, N)
        mx = pow(c1, self.a, N)
        my = pow(i, int(-self.b), N)
        self.m= mx * my % N
    def print_value(self):
        print("Plain Text: ", long_to_bytes(self.m))


def main():
    c = RSAModuli()
    N  = 86683300105327745365439507825347702001838360528840593828044782382505346188827666308497121206572195142485091411381691608302239467720308057846966586611038898446400292056901615985225826651071775239736355509302701234225559345175968513640372874437860580877571155199027883755959442408968543666251138423852242301639
    c1 = 84855521319828020020448068809384113135703375013574055636013459151984904926013060168559438932572351720988574536405041219757650609586761217385808427001020204262032305874206933548737826840501447182203920238204769775531537454607204301478815830436609423437869412027820433923450056939361510843151320837485348066171
    c2 = 54197787252581595971205193568331257218605603041941882795362450109513512664722304194032130716452909927265994263753090021761991044436678485565631063700887091405932490789561882081600940995910094939803525325448032287989826156888870845730794445212288211194966299181587885508098448750830074946100105532032186340554
    e1 = 11048796690938982746152432997911442334648615616780223415034610235310401058533076125720945559697433984697892923155680783661955179131565701195219010273246901
    e2 = 9324711814017970310132549903114153787960184299541815910528651555672096706340659762220635996774790303001176856753572297256560097670723015243180488972016453
    c.extended_euclidean(e1, e2)
    c.modular_inverse(c1, c2, N)
    c.print_value()

if __name__ == '__main__':
    main()