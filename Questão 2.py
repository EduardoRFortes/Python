print("Informe valores para uma lista: ")
list = []
valor = 0
while(valor != 999):
    valor = int(input())
    list.append(int(valor))
list.sort()
print(list)