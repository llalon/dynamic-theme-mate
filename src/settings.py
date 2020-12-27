import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib


DARK_MODE = "dynamic"
BASE_THEME = "Mint-Y"
BASE_WM_THEME = "Mint-Y"
BASE_THEME_COLORS = ["green", "aqua", "brown", "blue", "grey", "orange", "pink", "purple", "red", "teal"]
BG_DIR = GLib.get_user_special_dir(GLib.UserDirectory.DIRECTORY_PICTURES) + "/spotlight"
BG_COUNTRY = "CA"
BG_URL = "https://arc.msn.com/v3/Delivery/Cache?pid=279978&fmt=json&lc=en,en-US&ctry=" + BG_COUNTRY
