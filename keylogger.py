import json
from pynput.keyboard import Key, Listener

keys_pressed = set()
last_key_pressed = None


def on_press(key):
    global last_key_pressed
    try:
        last_key_pressed = key.char
        print(f'key {key.char} pressed')
    except AttributeError:
        last_key_pressed = str(key)
        print(f'key {key} pressed')
    keys_pressed.add(last_key_pressed)


def write_json_file():
    global last_key_pressed
    data = {
        "Keys pressed": list(keys_pressed)  # Convert set to list
    }

    # Write data to a JSON file
    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("JSON file written with the keys pressed!")


def on_release(key):
    print(f'\n{key} released')
    keys_pressed.discard(key)

    # Check if the command key is released
    if key == Key.cmd and last_key_pressed == "s":
        write_json_file()

    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
