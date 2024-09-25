arqNome = input("Informe um nome para o arquivo: ")
arq = open(arqNome, 'a+')
print("Informe qual operação vai utilizar: ")
print("1 - Exibir conteúdo do arquivo: ")
print("2 - Acrescentar conteúdo ao arquivo: ")
print("3 - Apagar conteúdo do arquivo: ")
print("4 - Para fechar o arquivo: ")

while True:
    opc = int(input())

    if opc == 1:
        arq.seek(0)  
        print(arq.read())  

    elif opc == 2:
        conteudo = "final\n"  
        arq.write(conteudo)  

    elif opc == 3:
        open(arqNome, 'w').close()

    elif opc == 4:
        break  

    else:
        print("Opção inválida. Tente novamente.")

arq.close()  