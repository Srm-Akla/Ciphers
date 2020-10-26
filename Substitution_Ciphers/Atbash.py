#Atbash Cipher

class Atbash:
    def __init__(self):
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--text', type=str, required=False)
        self.args = parser.parse_args()

        self.cipher_txt = []

        if self.args.text:
            print("Plain Text:",self.args.text)
            print("Cipher Text:",self.cipher())
        else:
            print("Choose -e for encrypt or -d for decrypt")

    def cipher(self):
        for letter in self.args.text:
            if letter == chr(32):
                self.cipher_txt.append(" ")
            elif letter >= chr(65) and letter <= chr(90):
                upper = (25-(ord(letter)-65))+65
                self.cipher_txt.append(chr(upper))
            elif letter >= chr(97) and letter <= chr(122):
                lower = (25-(ord(letter)-97))+97
                self.cipher_txt.append(chr(lower))
        return "".join(self.cipher_txt)

if __name__ == "__main__":
    Atbash()

