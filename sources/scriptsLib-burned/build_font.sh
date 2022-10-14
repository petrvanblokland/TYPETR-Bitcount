#!/bin/sh

set -e  # make sure to abort on error
set -x  # echo commands


fontmake -m Source/PixelColorDemo.designspace -o variable --output-dir build

python add_colrv1.py build/PixelColorDemo-VF.ttf
