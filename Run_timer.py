import time

def run_timer():
    input("Presiona Enter para comenzar el timer...")
    start_time = time.time()
    input("Presiona Enter para detener el timer...")
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"\nTiempo transcurrido: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    run_timer()
