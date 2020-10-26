# Cryptograpy
Folder contains some Ciphers, scripts that are related to Cryptography

# Tables of Contents
- [Substitution](https://github.com/Srm-Akla/Cryptography/tree/main/Substitution_Ciphers)
- [Transposition](https://github.com/Srm-Akla/Cryptography/tree/main/Transposition_Ciphers)
- [Poly-Alphabetic]()

# Installation
Enter this command in your terminal:

    Git clone https://github.com/Srm-Akla/Cryptography/

## Substitution Ciphers

### Caesar Cipher:
Simplest and popular cipher. Each letter of text is shifted X no of positions. Learn about [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

Python: 

    python3 Caeser.py -e/-d "SOME TEXT" -k 13

Powershell: 

    pwsh Caeser.ps1 -encrypt/-decrypt -text "SOME TEXT" -key 13

### Atbash Cipher
Originally used to encrypt Hebrew. First and Last letter, Second and second to last letter and etc. are swapped. Learn more [Atbash](https://en.wikipedia.org/wiki/Atbash)

Python: 
    
    python3 Atbash.py -e/-d "SOME TEXT" -k 13

## Transposition Ciphers

### Scytale Cipher
A scytale is a tool to perform cipher. Spartans said to have used this cipher to communicate. Learn about [Scytale Cipher](https://en.wikipedia.org/wiki/Scytale)

Powershell: 
    
    pwsh Scytale.ps1 -encrypt/-decrypt -text "SOME TEXT" -key 13

## Poly-Alphabetic Ciphers

#### Vigenere Cipher
**Can only Encrypt UpperCase Letter**, trying to implement lowercase. Vigenere is method of encrypting alphabetic text by using a series of interwoven Caesar ciphers. Learn about [Vigenere](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

Python: 
    
    python3 Vigenere.py -e "SOME TEXT" -k "SOME KEY"
