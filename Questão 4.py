import hashlib

def calcularHash(nome):
    hashObject = hashlib.sha256(nome.encode())
    return hashObject.hexdigest()

nomes = []

while True:
    nome = input("Informe o nome do usuário (ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    nomes.append(nome)

for nome in nomes:
    hashNome = calcularHash(nome)
    print(f'Nome: {nome}, Hash SHA256: {hashNome}')
