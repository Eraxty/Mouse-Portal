import subprocess

def get_mouse_position():
    result = subprocess.check_output(
        ["hyprctl", "cursorpos"],
        text=True
    )
    x, y = result.strip().split(",")
    return int(x), int(y)