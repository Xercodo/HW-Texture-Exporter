#!/usr/bin/env python

from gimpfu import *
from os.path import join

def export_HW_Layers(image, __unused_drawable, directory, name_pattern):
    for layer in image.layers:
        filename = directory + "\\" + name_pattern + "_" + layer.name + ".tga" #join(directory, name_pattern % layer.name)
        raw_filename = name_pattern + "_" + layer.name + ".tga"
        rle = 0
        origin = 0
        pdb.file_tga_save(image, layer, filename, raw_filename, rle, origin)

register(
    "python_fu_export_HW_Layers",
    "Save all layers into separate files",
    "Save all layers into separate files",
    "Xercodo",
    "Xercodo",
    "2015",
    "<Image>/File/Export HW Maps...",
    "*",
    [
        (PF_DIRNAME, "directory", "Directory to put the images in", "/"),
        (PF_STRING, "name_pattern", "Base file name. Output will be name__layer.tga", ""),
    ],
    [],
    export_HW_Layers
)

main()