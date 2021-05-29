import random

from params import p
from params import g

def keygen():
    ''' Generate a random integer a in the range 1,…,q , where q is the order of g.
    In our case, q=(p−1)/2 , but if q is unknown, it suffices to generate a uniformly 
    in the range 1,…,p , because if a is generated uniformly at random from the range   
    1,…,p, then amodq will be almost uniformly distributed in the range 0,…,q−1 .
    Once a has been generated:
    The secret key is a .
    The public key is h=g^a modp .
    The order of an element g, mod p, is the smallest positive integer q such that g^q = 1 mod p'''

    a = random.randint(1,p)
    sk = a
    pk = pow(g,a,p)
    return pk,sk

def encrypt(pk,m):
    # To encrypt m ,generate a random r in the range 1≤r≤q, and set (c1,c2)=(g^r modp,h^r m modp)
    r = random.randint(1,p)
    c1 = pow(g,r,p)
    c2 = (pow(pk,r,p)*(m%p)) % p
    return [c1,c2]

def decrypt(sk,c):
    (c1,c2) = c
    m = ((c2 % p) * pow(c1,-sk,p)) % p
    return m


