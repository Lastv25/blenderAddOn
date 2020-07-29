'''
author: Monjoux Hugo
date:
'''


bl_info = {
    "name":        "My First Add On",
    "description": "addOn to experiment the add On development",
    "author":      "Hugo Monjoux",
    "version":     (0, 0, 1),
    "blender":     (2, 80, 0),
    "warning":     "This version is still in development."
}



# Test Environment
##################################

import os
import sys
import traceback
from os.path import dirname, join, abspath, basename
currentDirectory = dirname(abspath(__file__))
addonsDirectory = dirname(currentDirectory)
compilationInfoPath = join(currentDirectory, "compilation_info.json")
addonName = basename(currentDirectory)


if addonName != "MyFirstAddOn":
    message = ("\n\n"
        "The name of the folder containing this addon has to be 'MyFirstAddOn'.\n"
        "Please rename it.")
    raise Exception(message)


try: from . import auto_load
except: pass

if "auto_load" not in globals():
    message = ("\n\n"
        "The Animation Nodes addon cannot be registered correctly.\n"
        "Please try to remove and install it again.\n"
        "If it still does not work, report it.\n")
    raise Exception(message)

# register
##################################

from . import auto_load
auto_load.init()

def register():
    auto_load.register()
    print("Registered My First Add On")

def unregister():
    auto_load.unregister()
    print("Unregistered My First Add On")

