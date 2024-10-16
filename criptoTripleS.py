## CEASAR

key = 'abcdefghijklmnopqrstuvwxyz'

def enc_ceasar(n, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

def dec_ceasar(n, ciphertext):
    result = ''
    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result


## ROT13

key = 'abcdefghijklmnopqrstuvwxyz'
def enc_substituition(n, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

def dec_substituition(n, ciphertext):
    result = ''
    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result

## ATBLASH

def toAtBash(text):
    characters = list(text.upper())
    result = ""
    for character in characters:
        if character in code_dictionaryatblash:
            result += code_dictionaryatblash.get(character)
        else:
            result += character # preserve non-alpha chars found
    return result

alphabetatblash = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
reverse_alphabetatblash = list(reversed(alphabetatblash))
code_dictionaryatblash = dict(zip(alphabetatblash, reverse_alphabetatblash))

## ENCRIPTAR

## ceasar
origtextceasar = input("Informe o texto a ser cifrado:")
key1ceasar = input("Informe o tamanho da chave: ")
ciphertextceasar = enc_ceasar(int(key1ceasar), origtextceasar)
print("Mensagem criptografada em CEASAR:\n")
print(ciphertextceasar)

#ROT13
origtext = ciphertextceasar
ciphertext = enc_substituition(13, origtext)
print("Mensagem criptografada em ROT13:\n")
print(ciphertext)

#atblash

plainTextatblash = ciphertext
cipherTextatblash = toAtBash(plainTextatblash)
print("Mensagem criptogradada em Atblash:\n")
print(cipherTextatblash)


#DESCRIPTOGRAFAR
print("Para descriptografar a mensagem, digite: BOLA\n")
while True:
    condicao = "BOLA"
    chave = input()
    if(chave == condicao):
        cipherTextatblash = toAtBash(cipherTextatblash)
        cifrado = cipherTextatblash.lower()
        plaintext = dec_substituition(13, cifrado)
        plaintextceasar = dec_ceasar(int(key1ceasar), plaintext)
        print("A mensagem descriptografada será: ", plaintextceasar)
        break
    else:
        print("Senha incorreta;")