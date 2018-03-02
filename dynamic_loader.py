#!/usr/bin/python3
#encoding:utf-8
#Tutorial: http://www.knight-of-pi.org/ [ARTICLE!]
#Licence: http://creativecommons.org/licenses/by-nc-sa/3.0/
# Author: Johannes Bergs

import glob, importlib

def load_components(source='./components/'):
    """ Import a number of modules from a given source dynamically for
    all modules following the pattern source/xyz/xyz.py with a class Xyz """

    components = []
    device_directories = [device for device in glob.glob(source + u"*/")
                                         if not '__pycache__/' in device]

    for directory in device_directories:
        component = directory[len(source):].strip('/')        
        component_path = source.strip('./').strip('/') + 2 * ('.' + component)
        mod = importlib.import_module(component_path)
        components.append(getattr(mod, component.capitalize()))

    return components

if __name__ == "__main__":
    print([component.__name__ for component in load_components()])
