import os
import hashlib

# Função para calcular o hash MD5
def calcular_hash_md5(conteudo):
    hash_object = hashlib.md5(conteudo.encode())
    return hash_object.hexdigest()

# Caminho do arquivo
input_file = r'F:\EDU-PEN\Redes de Computadores\Outras disciplinas\Criptografia\20240925\dictionary.txt'
output_file = r'F:\EDU-PEN\Redes de Computadores\Outras disciplinas\Criptografia\20240925\dictionaryMD5.txt'

# Verifica se o arquivo de entrada existe
if not os.path.exists(input_file):
    print(f"Erro: O arquivo {input_file} não foi encontrado.")
else:
    # Lê o conteúdo do arquivo de entrada e calcula os hashes
    with open(input_file, 'r') as arq_input:
        with open(output_file, 'w') as arq_output:
            for linha in arq_input:
                linha = linha.strip()
                if linha:
                    hash_md5 = calcular_hash_md5(linha)
                    arq_output.write(f'{linha},{hash_md5}\n')

    print("Hashes MD5 armazenados em dictionaryMD5.txt com sucesso!")