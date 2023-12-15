import os
os.system('cls')
palabra = "ahorcado"
result = "_" * len(palabra)
intentos_restantes = 3
print ("Bienvenido al juego del Ahorcado")
while intentos_restantes > 0 and result != palabra:
  print(f"Palabra: {result}")
  print(f"Intentos restantes: {intentos_restantes}")
  entrada = input("Ingresa una letra o la palabra completa: ").lower()
  if len(entrada) == 1:
    if entrada in palabra:
      for i in range(len(palabra)):
        if palabra[i] == entrada:
          result = result[:i] + entrada + result[i + 1:]
    else:
      intentos_restantes -= 1
  else:
    if entrada == palabra:
      result = palabra
    else:
      intentos_restantes -= 1
if result == palabra:
  print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
else:
  print(f"Has perdido. La palabra era: {palabra}")