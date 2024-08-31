from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()


def on_press(key):
    try:
        print('key {0} pressed'.format(key.char))
    except AttributeError:
        print('key {0} pressed'.format(key))


def on_release(key):
    print('\n{0} released'.format(key))
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
