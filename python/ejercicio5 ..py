import random

# Palabras para el juego
palabras = ["perro", "gato", "elefante", "rinoceronte", "jirafa"]

# Función para elegir una palabra al azar
def elegir_palabra(lista_palabras):
    palabra = random.choice(lista_palabras)
    return palabra.upper()

# Función para jugar
def jugar(palabra):
    # Configuración del juego
    letras_adivinadas = []
    vidas = 6
    adivinado = False

    # Dibujar la estructura del ahorcado
    print(" _ _ _ _ _ ")
    print("|         |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")

    # Bucle principal del juego
    while not adivinado and vidas > 0:
        # Mostrar el estado actual del juego
        print("\nTienes", vidas, "vidas")
        letra_usuario = input("Ingresa una letra: ").upper()

        # Si la letra ya ha sido adivinada
        if letra_usuario in letras_adivinadas:
            print("Ya adivinaste esa letra, intenta otra vez.")
        # Si la letra no está en la palabra
        elif letra_usuario not in palabra:
            print(letra_usuario, "no está en la palabra.")
            vidas -= 1
        # Si la letra está en la palabra
        else:
            print("¡Excelente! La letra", letra_usuario, "está en la palabra.")
            letras_adivinadas.append(letra_usuario)

        # Mostrar la palabra con las letras adivinadas
        letras_lista = [letra if letra in letras_adivinadas else "_" for letra in palabra]
        print(" ".join(letras_lista))

        # Si se ha adivinado la palabra completa
        if "_" not in letras_lista:
            adivinado = True

    # Mensaje de resultado final
    if adivinado:
        print("\n¡Felicidades! Has adivinado la palabra.")
    else:
        print("\nLo siento, has perdido. La palabra era", palabra)

# Función principal
def main():
    palabra = elegir_palabra(palabras)
    jugar(palabra)
    while input("¿Quieres jugar otra vez? (S/N) ").upper() == "S":
        palabra = elegir_palabra(palabras)
        jugar(palabra)

if __name__ == "__main__":
    main()

