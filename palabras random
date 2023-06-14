import random

def obtener_palabra_con_letra(letra):
    # Lista de palabras
    palabras = {
        "a": ["amigo", "avión", "árbol"],
        "b": ["barco", "bolsa", "bicicleta"],
        "c": ["camisa", "casa", "coche"],
        "d": ["delfín", "dado", "diente"],
        # Agrega más letras y palabras aquí
    }
    
    # Convertir la letra a minúscula
    letra = letra.lower()
    
    # Verificar si la letra ingresada está en el abecedario
    if letra not in palabras.keys():
        print("La letra ingresada no es válida.")
        return
    
    # Obtener una palabra aleatoria con la letra ingresada
    palabra = random.choice(palabras[letra])
    return palabra

# Solicitar al usuario que ingrese una letra
letra = input("Ingresa una letra: ")

# Obtener una palabra con la letra ingresada
palabra_con_letra = obtener_palabra_con_letra(letra)

# Mostrar la palabra obtenida
if palabra_con_letra:
    print("Palabra:", palabra_con_letra)
    
    #Karen_Hernandez
    #Palabras_Aleatorias
    #IEM_ESCUELA_NORMAL_PASTO
    #11-1
