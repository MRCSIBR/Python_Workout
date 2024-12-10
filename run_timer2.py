# Importamos el módulo time para trabajar con fechas y horas
import time

# Definimos una función para ejecutar el temporizador
def run_timer():
    # Pedimos al usuario que presione Enter para comenzar el temporizador
    input("Presiona Enter para comenzar el timer...")
    
    # Registramos el momento en que se inicia el temporizador
    start_time = time.time()  # Obtenemos el tiempo actual en segundos
    
    # Pedimos al usuario que presione Enter para detener el temporizador
    input("Presiona Enter para detener el timer...")
    
    # Registramos el momento en que se detiene el temporizador
    end_time = time.time()  # Obtenemos el tiempo actual en segundos
    
    # Calculamos el tiempo transcurrido
    elapsed_time = end_time - start_time  # Restamos el tiempo inicial del tiempo final
    
    # Imprimimos el resultado con dos decimales
    print(f"\nTiempo transcurrido: {elapsed_time:.2f} segundos")

# Verificamos si el script se está ejecutando directamente (no como módulo importado)
if __name__ == "__main__":
    # Llamamos a la función para ejecutar el temporizador
    run_timer()
