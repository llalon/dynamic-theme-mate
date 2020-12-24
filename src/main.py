import os
import numpy
import urllib.request, json
from PIL import Image
from matplotlib import colors
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk, GdkPixbuf, GLib



### Program Settings #############################################################################################
DARK_MODE = True
# The base theme
BASE_THEME = "Mint-Y"
BASE_WM_THEME = "Mint-Y"
# All the colors avaliable to the theme
BASE_THEME_COLORS = ["green", "aqua", "brown", "blue", "grey", "orange", "pink", "purple", "red", "teal"]
# Wallpaper
WALLPAPER_DIR = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_PICTURES) + "/spotlight"
WALLPAPER_COUNTRY = "CA"
WALLPAPER_URL = "https://arc.msn.com/v3/Delivery/Cache?pid=279978&fmt=json&lc=en,en-US&ctry=" + WALLPAPER_COUNTRY
##################################################################################################################


def change_theme(color, dark_mode = False, bg = WALLPAPER_DIR + "/background.jpg", theme = BASE_THEME, wm_theme = BASE_WM_THEME):
    '''Changes the desktop theme and wallpaper based on the color, mode, and theme'''

    # color must be one of the avilable colors
    if color not in BASE_THEME_COLORS:
        print("ERROR: color not avaliable\n")
        return(1)

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
            Gio.Settings(schema="org.mate.Marco.general").set_string("theme", wm_theme)
            Gio.Settings(schema="org.mate.background").set_string("picture-filename", bg)

    else:
        print("WARNING: Only MATE is supported currently")

def get_wallpaper(wallpaper_dir = WALLPAPER_DIR, country = WALLPAPER_COUNTRY):
    '''Downloads the latest spotlight wallpaper from the country to the wallpaper_dir'''
    # TODO reimpliment in python
    os.system("./spotlight.sh" + " " + wallpaper_dir)

def find_color(image = WALLPAPER_DIR + "/background.jpg"):
    '''Takes in a image, returns the most dominant color of that image'''
    img = Image.open(image)
    img.convert("RGB")
    img.resize((1, 1), resample=0)
    color = img.getpixel((0, 0))

    return(color)

def color_distance(color1, color2):
    '''Takes 2 RGB colors and returns the distance'''

    rgb1 = sRGBColor(color1[0], color1[1], color1[2])
    rgb2 = sRGBColor(color2[0], color2[1], color2[2])

    lab1 = convert_color(rgb1, LabColor)
    lab2 = convert_color(rgb2, LabColor)

    d = delta_e_cie2000(lab1, lab2)

    return(d)

def get_mode():
    '''Determines whether dark mode should be enabled or not based on the time of day and location'''
    # TODO
    return(False)

if __name__ == "__main__":
    
    get_wallpaper()

    dom_color = find_color()
    colors_rgb = [colors.to_rgb(c) for c in BASE_THEME_COLORS]
    c_dists = [color_distance(dom_color, c) for c in colors_rgb]
    est_color = BASE_THEME_COLORS[c_dists.index(min(c_dists))]

    change_theme(est_color, get_mode())