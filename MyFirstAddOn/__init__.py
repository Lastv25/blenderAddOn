
'''
Copyright (C) 2017 Jacques Lucke
mail@jlucke.com
Created by Jacques Lucke
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


bl_info = {
    "name":        "Animation Nodes",
    "description": "Node based visual scripting system designed for motion graphics in Blender.",
    "author":      "Jacques Lucke",
    "version":     (2, 1, 7),
    "blender":     (2, 80, 0),
    "location":    "Animation Nodes Editor",
    "category":    "Node",
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
from MyFirstAddOn.auto_load import *

try: pass
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
    print("Registered Animation Nodes")

def unregister():
    auto_load.unregister()
    print("Unregistered Animation Nodes")
