# Ejercicio Pag. 19

def pig_latin(palabra):
    vocales = "aeiou"

    if palabra[0].lower() in vocales:
        # Si la palabra comienza con una vocal, simplemente agrega "way" al final
        palabra_pig_latin = palabra + "way"
    else:
        # Si la palabra comienza con una consonante, mueve la primera consonante o grupo de consonantes
        # al final y agrega "ay"
        indice_primera_vocal = next((i for i, caracter in enumerate(palabra) if caracter.lower() in vocales), None)
        if indice_primera_vocal is not None:
            palabra_pig_latin = palabra[indice_primera_vocal:] + palabra[:indice_primera_vocal] + "ay"
        else:
            # Si no hay vocales, trátalo como una palabra sin vocales y simplemente agrega "ay"
            palabra_pig_latin = palabra + "ay"

    return palabra_pig_latin

if __name__ == "__main__":
    # Obtén la entrada del usuario
    entrada_usuario = input("Ingresa una palabra para convertirla a Pig Latin: ")

    # Convierte la entrada a Pig Latin
    resultado_pig_latin = pig_latin(entrada_usuario)

    # Muestra el resultado
    print(f"Representación de Pig Latin: {resultado_pig_latin}")
