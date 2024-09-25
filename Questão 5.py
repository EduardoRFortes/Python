import hashlib

def calcular_hash(senha):
    hash_object = hashlib.sha512(senha.encode())  
    return hash_object.hexdigest()  

print("Informe um usuário e uma senha: ")
nome = input("nome: ")
senha = input("senha: ")
arqNome = 'usuarios.txt'

with open(arqNome, 'w') as arq:
    senha_hash = calcular_hash(senha)
    arq.write(f'{nome},{senha_hash}\n')

print("Usuário e senha armazenados com sucesso!")