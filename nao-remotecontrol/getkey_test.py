from getkey import getkey, keys
key = getkey()
if key == keys.UP:
    print('up')
elif key == keys.DOWN:
    print('down')
elif key == 'a':
    print('a')
elif key == 'Y':
    print("Handle `shift-y`")
else:
    # Handle other text characters
    buffer += key
    print(buffer)
