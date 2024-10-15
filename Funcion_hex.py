def convertir_entero_a_hexadecimal(entero: int) -> str:
    """
    Convierte un número entero a hexadecimal.

    Args:
        entero (int): El número entero a convertir.

    Returns:
        str: La representación hexadecimal del número entero.
    """
    return hex(entero)[2:]

if __name__ == "__main__":
    # Obtén la entrada del usuario
    entrada_usuario = int(input("Ingresa el número entero a convertir a hexadecimal: "))

    # Convierte la entrada a hexadecimal
    try:
        resultado_hexadecimal = convertir_entero_a_hexadecimal(entrada_usuario)
        print(f"Representación hexadecimal: {resultado_hexadecimal}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
