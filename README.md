# dynamic-theme-mate

A utility to automatically change the wallpaper and color theme for Mate.

Downloads the daily windows spotlight wallpaper and adjusts the system color theme to match.

Dynamic switching of dark and light mode based on sunrise and set timing.

Tested and designed for Linux Mint Mate 20.1 however it should work on any distro.

## Dependencies

This is based on the default Linux Mint theme Mint-Y

```bash
sudo apt install mint-themes mint-y-icons python3-colormath python3-matplotlib python3-gi jg wget gir1.2-geoclue-2.0
pip3 install suntime
```

## Usage

If no background argument is given the daily windows spotlight image will be used.

```bash
python3 main.py [-h] [--background BACKGROUND]
```
## Project status

Coming soon:
* GUI
* Support for other desktops


## Contributing

Pull requests are welcome.

