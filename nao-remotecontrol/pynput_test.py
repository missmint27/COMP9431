from pynput import keyboard

up = 0
left = 0
turn = 0


def on_press(key):
    global up
    global left
    global turn
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        #print('special key {0} pressed'.format(key))
        if up == 0 and key == keyboard.Key.ctrl:
            print('ctrl down')
            up = 1
        if left == 0 and key == keyboard.Key.shift:
            print('shift-l down')
            left = 1
        if turn == 0 and key == keyboard.Key.shift_r:
            print('shift_r down')
            turn = 1


def on_release(key):
    global up
    global left
    global turn
    if key == keyboard.Key.alt:
        return False
    if key == keyboard.Key.ctrl:
        print('ctrl up')
        up = 0
    if key == keyboard.Key.shift:
        print('shift_l up')
        left = 0
    if  key == keyboard.Key.shift_r:
        print('shift_r up')
        turn = 0

# Collect events until released

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



