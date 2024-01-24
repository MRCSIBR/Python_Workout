# Ejercicio del libro Python Workout

def convertir_a_hexadecimal(datos_entrada):
    try:
        # Convierte los datos de entrada a hexadecimal
        salida_hexadecimal = ''.join(format(ord(caracter), '02x') for caracter in datos_entrada)
        return salida_hexadecimal
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Obtén la entrada del usuario
    entrada_usuario = input("Ingresa los datos a convertir a hexadecimal: ")

    # Convierte la entrada a hexadecimal
    resultado_hexadecimal = convertir_a_hexadecimal(entrada_usuario)

    # Muestra el resultado
    print(f"Representación hexadecimal: {resultado_hexadecimal}")
