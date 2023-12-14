import os
os.system('cls')
# Palabra a adivinar
palabra = "python"
# Estado actual de la palabra a mostrar al jugador
result = "_" * len(palabra)
# Número de intentos restantes
intentos_restantes = 3
print ("Bienvenido al juego del Ahorcado")
# Bucle principal del juego
while intentos_restantes > 0 and result != palabra:
  print("Palabra:", result)
  print("Intentos restantes:", intentos_restantes)
  # Solicitar al jugador ingresar una letra o la palabra completa
  print ("Ingresa una letra o la palabra completa: ")
  entrada = input().lower()
  if len(entrada) == 1:
    # El jugador ingresó una letra
    if entrada in palabra:
      # La letra ingresada está en la palabra
      for i in range(len(palabra)):
        if palabra[i] == entrada:
          result = result[:i] + entrada + result[i + 1:]
          #result = result.replace(result, entrada+(" _ "*(len(palabra))))
    else:
      # La letra ingresada no está en la palabra
      intentos_restantes -= 1
  else:
    # El jugador ingresó la palabra completa
    if entrada == palabra:
      result = palabra
    else:
      intentos_restantes -= 1
# Mostrar resultado del juego
if result == palabra:
  print("¡Felicidades! Has adivinado la palabra:", palabra)
else:
  print("Has perdido. La palabra era:", palabra)