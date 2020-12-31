#Vigenere Cipher

import argparse

class vigenere:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-e', '--encrypt', help="Enter Encryption Text", type=str, required=False)
        parser.add_argument('-d', '--decrypt', help="Enter Decryption Text", type=str, required=False)
        parser.add_argument('-k', '--key', help="Enter KEY", type=str, required=False)
        self.args = parser.parse_args()

        self.encrypt_txt = []
        self.decrypt_txt = []
        self.key = "KEY"

        if self.args.encrypt:
            #print("Plain Text:",self.args.encrypt)
            print("Cipher Text:",self.encrypt())
        else:
            print("Plain Text:",self.decrypt())

    def encrypt(self):
        for i in range(len(self.args.encrypt)):
            upper = ((ord(self.args.encrypt[i])+ord(self.key[i%len(self.key)]))%26)+65
            self.encrypt_txt.append(chr(upper))
        return "".join(self.encrypt_txt) 
    def decrypt(self):
        for i in range(len(self.args.decrypt)):
            upper = ((ord(self.args.decrypt[i])-ord(self.key[i%len(self.key)])+26)%26)+65
            self.decrypt_txt.append(chr(upper))
        return "".join(self.decrypt_txt) 

if __name__ == '__main__':
    vigenere()
