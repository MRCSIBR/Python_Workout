import time

def run_timer():
    input("Press Enter to start the timer...")
    start_time = time.time()
    input("Press Enter to stop the timer...")
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"\nElapsed time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    run_timer()
