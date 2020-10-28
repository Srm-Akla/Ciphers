#XOR cipher

txt = "HELLO"
user_key = input("Enter Key: ")

ascii_txt = []
result = []
keys = []


for l in range(len(txt)):
    num = bin(ord(txt[l]))
    key = bin(ord(user_key[l]))
    res = bin(int(num,2) ^ int(key,2))

    ascii_txt.append(num)
    keys.append(key)
    result.append(res)
    

print("Result ", result)
print("text   ", ascii_txt)
print("key    ", keys)
