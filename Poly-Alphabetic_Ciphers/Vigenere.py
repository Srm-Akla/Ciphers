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
            print("Enter -t 'text'")

    def encrypt(self):
        for i in range(len(self.args.encrypt)):
            #if self.args.encrypt[i].isspace():
            #    self.encrypt_txt.append(" ")
            #elif self.args.encrypt[i].isupper():
            upper = ((ord(self.args.encrypt[i])+ord(self.key[i%len(self.key)]))%26)+65
            self.encrypt_txt.append(chr(upper))
            #elif self.args.encrypt[i].islower():
            #    lower = ((ord(self.args.encrypt[i])+ord(self.key[i%len(self.key)]))%26)+97
            #    self.encrypt_txt.append(chr(lower))
        return "".join(self.encrypt_txt) 

if __name__ == '__main__':
    vigenere()
