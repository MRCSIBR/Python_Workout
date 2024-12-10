import time
import threading

# Definimos una función para ejecutar el temporizador
def run_timer():
    # Pedimos al usuario que presione Enter para comenzar el timer
    input("Presiona Enter para comenzar el timer...")
    
    # Registramos el momento en que se inicia el temporizador
    start_time = time.time()  # Obtenemos el tiempo actual en segundos
    
    # Iniciamos un hilo para mostrar el tiempo transcurrido
    def mostrar_tiempo():
        while True:
            # Registramos el momento actual
            current_time = time.time()
            
            # Calculamos el tiempo transcurrido
            elapsed_time = current_time - start_time  # Restamos el tiempo inicial del tiempo actual
            
            # Convertimos el tiempo transcurrido a formato hora, minuto y segundo
            hours = int(elapsed_time // 3600)  # Obtenemos las horas
            minutes = int((elapsed_time % 3600) // 60)  # Obtenemos los minutos
            seconds = int(elapsed_time % 60)  # Obtenemos los segundos
            
            # Imprimimos el tiempo transcurrido en formato 00:00:00
            print(f"\rTiempo transcurrido: {hours:02d}:{minutes:02d}:{seconds:02d}  Presiona Enter para detener el timer...", end="")
            
            # Esperamos un segundo antes de actualizar el tiempo
            time.sleep(1)
    
    # Iniciamos el hilo
    hilo = threading.Thread(target=mostrar_tiempo)
    hilo.daemon = True  # Configuramos el hilo como demonio para que se detenga cuando el programa principal se detenga
    hilo.start()
    
    # Esperamos a que el usuario presione Enter para detener el timer
    input()
    
    # Calculamos el tiempo total transcurrido
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Imprimimos el resultado final
    print(f"\nTiempo total transcurrido: {elapsed_time:.2f} segundos")

# Verificamos si el script se está ejecutando directamente (no como módulo importado)
if __name__ == "__main__":
    # Llamamos a la función para ejecutar el temporizador
    run_timer()
