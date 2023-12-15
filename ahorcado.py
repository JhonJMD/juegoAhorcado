import os
os.system('cls')
palabra = "ahorcado"
result = "_" * len(palabra)
intentosRestantes = 3
print ("Bienvenido al juego del Ahorcado")
while intentosRestantes > 0 and result != palabra:
  print(f"Palabra: {result}")
  print(f"Intentos restantes: {intentosRestantes}")
  entrada = input("Ingresa una letra o la palabra completa: ").lower()
  if len(entrada) == 1:
    if entrada in palabra:
      for i in range(len(palabra)):
        if palabra[i] == entrada:
          result = result[:i] + entrada + result[i + 1:]
    else:
      intentosRestantes -= 1
  else:
    if entrada == palabra:
      result = palabra
    else:
      intentosRestantes -= 1
if result == palabra:
  print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
else:
  print(f"Has perdido. La palabra era: {palabra}")