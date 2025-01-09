import time
import os
import platform

def beep():
    """Play a beep sound."""
    system_platform = platform.system()

    if system_platform == "Windows":
        # Use winsound for Windows
        import winsound
        frequency = 440  # Hz
        duration = 1000  # milliseconds
        winsound.Beep(frequency, duration)
    else:
        # Use system beep for macOS and Linux
        print("\a")  # ASCII bell character
        time.sleep(0.5)  # Add a small delay to ensure the beep is heard

def main():
    """Beep every 5 seconds."""
    try:
        print("Beeping every 5 seconds. Press Ctrl+C to stop.")
        while True:
            beep()  # Play the beep sound
            time.sleep(5)  # Wait for 5 seconds
    except KeyboardInterrupt:
        print("\nProgram stopped.")

if __name__ == "__main__":
    main()
