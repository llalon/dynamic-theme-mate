#!/usr/bin/python
import settings
import os
from datetime import datetime, timezone
from suntime import Sun, SunTimeException
from PIL import Image
from matplotlib import colors
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Geoclue', '2.0')
from gi.repository import Gtk, Gio, Gdk, GdkPixbuf, GLib, Geoclue


def change_bg(bg=settings.BG_DIR + "/background.jpg"):
    '''Changes the desktop background to bg'''

    # Apply the theme. TODO: Support for other desktops
    if os.getenv("XDG_CURRENT_DESKTOP") == "MATE":
        Gio.Settings(schema="org.mate.background").set_string(
            "picture-filename", str(bg))
    else:
        print("WARNING: Only MATE is supported currently")


def change_theme(bg=settings.BG_DIR + "/background.jpg", dark_mode=False, theme=settings.BASE_THEME, wm_theme=settings.BASE_WM_THEME, theme_colors=settings.BASE_THEME_COLORS):
    '''Changes the desktop gtk and icon theme color to match the background bg'''

    # Find the best color match based on the background
    dom_color = find_color(bg)
    colors_rgb = [colors.to_rgb(c) for c in theme_colors]
    c_dists = [color_distance(dom_color, c) for c in colors_rgb]
    color = theme_colors[c_dists.index(min(c_dists))]

    if dark_mode:
        theme = "%s-Dark" % theme
        wm_theme = "%s-Dark" % wm_theme

    # The base theme for Mint-Y is green
    if color != "green" and theme == "Mint-Y":
        theme = "%s-%s" % (theme, color.title())

    # Apply the theme. TODO Support for other desktops
    if os.getenv("XDG_CURRENT_DESKTOP") == "MATE":
        settings = Gio.Settings(schema="org.mate.interface")
        settings.set_string("gtk-theme", theme)
        settings.set_string("icon-theme", theme)
        Gio.Settings(schema="org.mate.Marco.general").set_string(
            "theme", wm_theme)
    else:
        print("WARNING: Only MATE is supported currently")


def get_dark_mode(mode=settings.DARK_MODE):
    '''Takes the mode (dynamic, dark, light) and returns a bool based on whether dark mode is enabled or not'''

    dark_mode = False

    if mode == "dynamic":
        clue = Geoclue.Simple.new_sync(
            'something', Geoclue.AccuracyLevel.NEIGHBORHOOD, None)
        coords = clue.get_location()
        lat = coords.get_property('latitude')
        lon = coords.get_property('longitude')

        sun = Sun(lat, lon)

        sr = sun.get_sunrise_time()
        ss = sun.get_sunset_time()
        ct = datetime.now(timezone.utc)

        if ct < sr and ct > ss:
            dark_mode = True

    elif mode == "dark":
        dark_mode = True

    return(dark_mode)


def find_color(image=settings.BG_DIR + "/background.jpg"):
    '''Takes in a image, returns the most dominant color of that image'''
    img = Image.open(image)
    img.convert("RGB")
    img.resize((1, 1), resample=0)
    color = img.getpixel((0, 0))

    return(color)


def color_distance(color1, color2):
    '''Takes 2 RGB colors and returns the distance d'''

    rgb1 = sRGBColor(color1[0], color1[1], color1[2])
    rgb2 = sRGBColor(color2[0], color2[1], color2[2])

    lab1 = convert_color(rgb1, LabColor)
    lab2 = convert_color(rgb2, LabColor)

    d = delta_e_cie2000(lab1, lab2)

    return(d)


def get_bg(bg_dir=settings.BG_DIR, country=settings.BG_COUNTRY):
    '''Downloads the latest spotlight bg from the country to the bg_dir'''
    # TODO reimpliment in python
    os.system("./spotlight.sh" + " " + bg_dir)

    # Return the file path to that background
    return(bg_dir + "/background.jpg")


if __name__ == "__main__":
    pass
