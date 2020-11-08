#XOR cipher
import argparse

parser = argparse.ArgumentParser(description='XOR Cipher')
parser.add_argument('-t', '--text', type=str, help='Input text for the Cipher')
parser.add_argument('-k', '--key', type=str, help='Input Key')
args = parser.parse_args()

txt = args.text
user_key = args.key

ascii_txt = []
result = []
keys = []


for l in range(len(txt)):
    num = txt[l]
    key = user_key[l%len(user_key)]
    res = chr(ord(num) ^ ord(key))

    ascii_txt.append(num)
    keys.append(key)
    result.append(res)
    

print("Result:","".join(result))
#print("text   ", ascii_txt)
#print("key    ", keys)
