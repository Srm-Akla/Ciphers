#!/bin/python3
#ROT-5
#ROT-13
#ROT-47

import argparse

class ROT:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-rot7", help="Enter Domain:", type=str, required=False)
        parser.add_argument("-rot47", help="Enter text:", type=str, required=False)
        self.txt = parser.parse_args()

    def rot7(self):
        self.result = []
        def encrypt()
            for letter in self.txt.rot7:
                if letter == chr(32):
                    self.result.append(" ")
                elif letter > chr(65) and letter < chr(90):
                    self.result.append(chr((ord(letter)+7-65)%26 + 65))
                elif letter > chr(97) and letter < chr(122):
                    self.result.append(chr((ord(letter)+7-97)%26 + 97))
            print("".join(self.result))
        def decrypt():
            for letter in self.txt.rot7:
                if letter == chr(32):
                    self.result.append(" ")
                elif letter > chr(65) and letter < chr(90):
                    self.result.append(chr((ord(letter)+(26-7)-65)%26 + 65))
                elif letter > chr(97) and letter < chr(122):
                    self.result.append(chr((ord(letter)+(26-7)-97)%26 + 97))
            print("".join(self.result))

if __name__ == "__main__":
    rot = ROT() 
    print(rot.rot7())
