from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  cantidad_vuelos = 0
  origen_actual = origen
  while hayVueloDesdeOrigen(origen_actual, vuelos):
    cantidad_vuelos += 1
    if destinoDesdeOrigen(origen_actual, vuelos) == destino:
      return cantidad_vuelos
    else:
      origen_actual = destinoDesdeOrigen(origen_actual, vuelos)
  return -1

    
def hayVueloDesdeOrigen(origen: str, vuelos: List[Tuple[str, str]]) -> bool:
  for vuelo in vuelos:
    if vuelo[0] == origen:
      return True
  return False

def destinoDesdeOrigen(origen: str, vuelos: List[Tuple[str, str]]) -> Tuple:
  for vuelo in vuelos:
    if vuelo[0] == origen:
      return vuelo[1]

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))

