from mouse import get_mouse_position
import time

while True:
    x, y = get_mouse_position()
    print(f"X: {x}, Y: {y}")

    time.sleep(0.05)