import os
import numpy
import urllib.request, json
from PIL import Image
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk, GdkPixbuf, GLib



### Settings
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


# This function changes the desktop color theme to match the wallpaper. 
def change_color(color):

    theme = BASE_THEME
    wm_theme = BASE_WM_THEME
    dark_mode = DARK_MODE

    # color must be one of the avilable colors
    if color not in BASE_THEME_COLORS:
        print("ERROR: color not avaliable\n")
        return(1)

    if dark_mode:
        theme = "%s-Dark" % theme
        wm_theme = "%s-Dark" % wm_theme

    # The base theme is already green no need to specify this
    if color != "green":
        theme = "%s-%s" % (theme, color.title())

    # Apply the theme
    if os.getenv("XDG_CURRENT_DESKTOP") == "MATE":
            #settings = Gio.Settings(schema="org.mate.interface")
            #settings.set_string("gtk-theme", theme)
            #settings.set_string("icon-theme", theme)
            #Gio.Settings(schema="org.mate.Marco.general").set_string("theme", wm_theme)
            pass


# This function downloads the daily wallpaper
def get_wallpaper():
    # TODO reimpliment in python
    os.system("./spotlight.sh" + " " + WALLPAPER_DIR)

# This function determines the most dominant color of the background using PILLOW
def find_color():
    img = Image.open(WALLPAPER_DIR + "/background.jpg")
    img.convert("RGB")
    img.resize((1, 1), resample=0)

    dom_color = img.getpixel((0, 0))

# This function determines the distance between 2 RGB colors
def ColorDistance(rgb1,rgb2):
    '''d = {} distance between two colors(3)'''
    rm = 0.5*(rgb1[0]+rgb2[0])
    d = sum((2+rm,4,3-rm)*(rgb1-rgb2)**2)**0.5
    return d

if __name__ == "__main__":
    #change_color("red")
    #get_wallpaper()
    find_color()