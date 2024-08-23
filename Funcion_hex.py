def to_hex(datos_entrada: str) -> str:
    """
    Convierte una cadena de caracteres a hexadecimal.
    """
    if not isinstance(datos_entrada, str):
        raise TypeError("La entrada debe ser una cadena de caracteres")

    try:
        # Convierte los datos de entrada a hexadecimal
        hex_chars = [f"{ord(caracter):02x}" for caracter in datos_entrada]
        salida_hexadecimal = "".join(hex_chars)
        return salida_hexadecimal
    except Exception as e:
        raise ValueError(f"Error al convertir a hexadecimal: {e}")

if __name__ == "__main__":
    # Obtén la entrada del usuario
    entrada_usuario = input("Ingresa los datos a convertir a hexadecimal: ")

    # Convierte la entrada a hexadecimal
    try:
        resultado_hexadecimal = to_hex(entrada_usuario)
        print(f"Representación hexadecimal: {resultado_hexadecimal}")
    except Exception as e:
        print(f"Error: {e}")
