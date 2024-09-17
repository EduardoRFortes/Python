import math
print("Cálculo do IMC")
print("informe o seu peso:")
Peso = float(input())
print("informe a sua altura:")
Altura = float(input())
print("\n O seu peso é:", Peso, "\n A sua altura é:", Altura)
print("\n Logo, o seu IMC é:", Peso/(math.pow(Altura,2)))