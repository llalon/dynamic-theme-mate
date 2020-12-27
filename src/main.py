#!/usr/bin/python
import sys
import os
import argparse
import funcs
import settings

def main():
    '''main'''

    parser = argparse.ArgumentParser(description='dynamic-theme-mate')
    parser.add_argument(
        '--background',
        default="",
        help='provide path to background image (default: Daily Microsoft Spotlight)'
    )
    namespace = parser.parse_args()
    print(namespace.background)

    if namespace.background == "":
        bg = funcs.get_bg()
    else:
        bg = namespace.background

    funcs.change_bg(bg)
    funcs.change_theme(bg, funcs.get_dark_mode(settings.DARK_MODE))


if __name__ == "__main__":
    main()
