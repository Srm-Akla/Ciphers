#Atbash Cipher

class Atbash:
    def __init__(self):
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('-e', '--encrypt', type=str, required=False)
        parser.add_argument('-d', '--decrypt', type=str, required=False)
        self.args = parser.parse_args()

        self.cipher_txt = []

        if self.args.encrypt:
            print(self.encrypt())
        elif self.args.decrypt:
            print(self.decrypt())
        else:
            print("Choose -e for encrypt or -d for decrypt")

    def encrypt(self):
        for letter in self.args.encrypt:
            self.cipher_txt.append(-(ord(letter)+1)%26)
        return self.cipher_txt

    def decrypt(self):
        for letter in self.args.decrypt:
            self.cipher_txt.append(-(ord(letter)+1)%26)
        return self.cipher_txt

if __name__ == "__main__":
    Atbash()

