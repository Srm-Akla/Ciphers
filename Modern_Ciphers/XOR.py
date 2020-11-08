#XOR cipher

txt = ")6(*("
user_key = "asdfg" 

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
    

print("Result: ", "".join(result))
#print("text   ", ascii_txt)
#print("key    ", keys)
