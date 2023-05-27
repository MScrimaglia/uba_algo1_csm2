from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def filasParecidas(matriz: List[List[int]]) -> bool :
  if len(matriz) == 1:
    return True
  diferencia = diferenciaFilas(matriz[0], matriz[1])
  for i in range (1, len(matriz)):
    if not esFilaMasN(matriz[i-1], matriz[i], diferencia):
      return False
  return True

def esFilaMasN(fila1:List, fila2:List, n:int) -> bool:
  for i in range(len(fila1)):
    if fila2[i] != fila1[i] + n:
      return False
  return True

def diferenciaFilas(fila1:List, fila2:List) -> int:
  fila_mayor = None
  fila_menor = None
  positividad = None
  if fila1[0] > fila2[0]:
    fila_mayor = fila1
    fila_menor = fila2
    positividad = -1
  else:
    fila_mayor = fila2
    fila_menor = fila1
    positividad = 1
  res = positividad * (fila_mayor[0] - fila_menor[0])
  return res

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))
