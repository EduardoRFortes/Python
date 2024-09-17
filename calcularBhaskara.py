import math
print("Calcule Bhaskara")
print("informe A")
A = float(input())
print("informe B")
B = float(input())
print("informe C")
C = float(input())
print("\n A:", A, "\n B:", B, "\n C:", C)
Del = (math.pow(B,2)-(4*A*C))
if(Del > 0):
  res1 = -B - (math.sqrt(Del))
  res2 = (res1)/(2*A)
  res3 = -B + (math.sqrt(Del))
  res4 = (res3)/(2*A)
  print("\n Logo, seu resultado é:", "-\n X':", res2, "\n X'':", res4)
elif(Del < 0):
  print("\n Não há raiz real para esse resultado")
else:
  res1 = -B - (math.sqrt(Del))
  res2 = (res1)/(2*A)
  print("\n Logo, seu resultado é:", res2)