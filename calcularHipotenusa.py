import math
print("Calcule a Hipotenusa (A soma dos quadrados dos catetos)")
print("informe a medida do Cateto1")
Cat1 = float(input())
print("informe a medida do Cateto2")
Cat2 = float(input())
print("\n A medida do Cateto1 é:", Cat1, "\n A medida do Cateto2 é", Cat2)
Part1 = (math.pow(Cat1,2)+(math.pow(Cat2,2)))
print("\n Logo, a medida da Hipotenusa é:", math.sqrt(Part1))