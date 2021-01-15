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

options=(Divide_Dst Divide_Src Plus Minus Minus_Dst Minus_Src Bumpmap Divide Lighten Multiply Screen)
read -p "Enter image 1: " image1
read -p "Enter image 2: " image2
read -p "Enter output directory: " outdir
mkdir $outdir
# image1=
# image2=
# outdir=
for i in "${options[@]}"; 
    do composite $image1 -gravity center -compose $i $image2 "$outdir/$i.jpg";
done;