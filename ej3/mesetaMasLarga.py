from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
  if len(l) == 0:
    return 0
  
  max = 0
  count = 0
  current_val = l[0]

  for i in range(len(l)):
    if l[i] == current_val:
      count += 1
    else:
      current_val = l[i]
      count = 1
    if count > max:
      max = count

  return max

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))