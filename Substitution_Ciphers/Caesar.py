#!/bin/python3

import argparse

class Caeser:
    def __init__(self):

        parser = argparse.ArgumentParser()
        parser.add_argument("-e", "--encrypt", help="Enter text for encryption:", type=str, required=False)
        parser.add_argument("-d", "--decrypt", help="Enter text for decryption:", type=str, required=False)
        parser.add_argument("-k", "--key", type=int, help="Enter text for decryption:", required=True)
        self.txt = parser.parse_args()

        self.result= []
        self.key = self.txt.key

        if self.txt.encrypt:
            print(self.encrypt())
        elif self.txt.decrypt:
            print(self.decrypt())
        else:
            print(self.key)

    def encrypt(self):
        for letter in self.txt.encrypt:
            if letter == chr(32):
                self.result.append(" ")
            elif letter > chr(65) and letter < chr(90):
                self.result.append(chr((ord(letter)+self.key-65)%26 + 65))
            elif letter > chr(97) and letter < chr(122):
                self.result.append(chr((ord(letter)+self.key-97)%26 + 97))
        return "".join(self.result)

    def decrypt(self):
        for letter in self.txt.decrypt:
            if letter == chr(32):
                self.result.append(" ")
            elif letter > chr(65) and letter < chr(90):
                self.result.append(chr((ord(letter)+(26-self.key)-65)%26 + 65))
            elif letter > chr(97) and letter < chr(122):
                self.result.append(chr((ord(letter)+(26-self.key)-97)%26 + 97))
        return "".join(self.result)

if __name__ == "__main__":
    Caeser() 
