from datetime import datetime
from suntime import Sun, SunTimeException
import gi
gi.require_version('Geoclue', '2.0')
from gi.repository import Geoclue

def get_dark_mode(mode):
    '''Takes the mode (dynamic, dark, light) and returns a bool based on whether dark mode is enabled or not'''
    
    dark_mode = False

    if mode == "dynamic":
        clue = Geoclue.Simple.new_sync('something',Geoclue.AccuracyLevel.NEIGHBORHOOD,None)
        coords = clue.get_location()
        lat = coords.get_property('latitude')
        lon = coords.get_property('longitude')

        sun = Sun(lat, lon)

        sr = sun.get_sunrise_time()
        ss = sun.get_sunset_time()
        print('Today the sun raised at {} and get down at {} UTC' .format(sr.strftime('%H:%M'), ss.strftime('%H:%M')))

        time = datetime.utcnow()

        print(ss.time())
        print(sr.time())
        print(time.time())

        print(ss.time() - sr.time())


    elif mode == "dark":
        dark_mode = True

    return(dark_mode)


if __name__ == "__main__":
    get_dark_mode("dynamic")