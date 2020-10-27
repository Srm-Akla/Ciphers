#XOR cipher

txt = "HELLO"
ascii_txt = []
result = []

for l in txt:
    num = bin(ord(l))
    res = bin(int(num,2) ^ int("0110110",2))
    result.append(chr(int(res,2)))
    

print("0110110")
print("text", ascii_txt)
print("Result", result)
