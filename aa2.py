import periodictable

def calcular_peso_elemento(elemento):
    try:
        masa_atomica = periodictable.elements.symbol(elemento).mass
        return masa_atomica
    except periodictable.core.periodictable.InvalidElementError:
        return None

elemento = input("Ingresa el símbolo del elemento: ")
peso = calcular_peso_elemento(elemento)

if peso is not None:
    print("El peso del elemento {} es: {:.4f} g/mol".format(elemento, peso))
else:
    print("Elemento no encontrado en la tabla periódica.")
