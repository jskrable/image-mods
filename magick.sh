#!/usr/bin/env bash
# coding: utf-8
"""
magick.sh
01-15-2021
jack skrable
"""

composite Downloads/triple-word-score.jpg -gravity center -compose Multiply Downloads/strategize.jpg Downloads/output.jpg
composite Downloads/triple-word-score.jpg -gravity center -compose Multiply Downloads/strategize.jpg Downloads/multiply.jpg
composite Downloads/triple-word-score.jpg -gravity center -compose Divide Downloads/strategize.jpg Downloads/divide.jpg
composite Downloads/triple-word-score.jpg -gravity center -compose Lighten Downloads/strategize.jpg Downloads/lighten.jpg
composite triple-word-score.jpg -gravity center -compose Screen strategize.jpg screen.jpg
composite triple-word-score.jpg -gravity center -compose bumpmap strategize.jpg bumpmap.jpg
