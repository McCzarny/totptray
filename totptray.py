#!/usr/bin/python3
"""
Tray icon tool with a TOTP implementation.
Usage:
totptray [title=key]
"""
import sys
import pyperclip
import pystray
import pyotp
from PIL import Image, ImageDraw

def create_icon():
    """
    Creates a T-shaped icon.

    :returns: A 64x64 image with "T" in a circle.
    """
    icon_size = 64
    t_width = int(0.3 * icon_size)
    t_height = int(0.4 * icon_size)
    horizontal_margin = int((icon_size - t_width) / 2)
    vertical_margin = int((icon_size - t_height) / 2)

    points = (
        (horizontal_margin, vertical_margin),
        (icon_size - horizontal_margin, vertical_margin),
        (icon_size / 2, vertical_margin),
        (icon_size / 2, icon_size - vertical_margin))

    line_size = int(0.1 * icon_size)
    image = Image.new('RGBA', (icon_size, icon_size), (0, 0, 0, 0))

    draw = ImageDraw.Draw(image)
    draw.ellipse([(0, 0), (icon_size, icon_size)], fill="white")
    draw.line(points, fill="black", width=line_size)

    return image

def copy_code(key="none"):
    """
    Copies a TOTP generated code for the given key to the clipboard.
    :param key: For for which a TOTP code should be generated.
    """
    code = pyotp.TOTP(key).now()
    print(key + ":" + code)
    pyperclip.copy(code)

def create_menu(keys):
    """
    Creates a list of menu items for each passed key.
    :param keys: A list of labeled keys in the format: "label=key".
    :returns: A list of menu items for each passed key.
    """
    return [pystray.MenuItem(x[:x.index('=')], lambda _: copy_code(x[x.index('=')+1:])) for x in keys]

def main():
    """
    Creates a tray icon with a menu that allows to copy OTP generated codes.
    """
    assert len(sys.argv) > 1
    assert all("=" in item for item in sys.argv[1:])
    icon = pystray.Icon('TOTP', icon=create_icon(), menu=create_menu(sys.argv[1:]))
    icon.run()

if __name__ == '__main__':
    main()
