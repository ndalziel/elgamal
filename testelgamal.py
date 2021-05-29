import unittest
from elgamal import *

class ElGamalTest(unittest.TestCase):
        
    def testEncrypt(self):
        pk, sk = keygen()
        plain = 12345
        cipher = encrypt(pk, plain)
        decrypted = decrypt(sk,cipher) 
        self.assertEqual(plain, decrypted)

    def testEncrypt2(self):
        pk, sk = keygen()
        plain = 0
        cipher = encrypt(pk, plain)
        decrypted = decrypt(sk,cipher) 
        self.assertEqual(plain, decrypted)

if __name__ == '__main__':
    unittest.main()