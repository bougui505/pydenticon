#!/usr/bin/env python3
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-09-24 21:35:10 (UTC+0200)

import pydenticon
import argparse

parser = argparse.ArgumentParser(description='Generate an identicon')
parser.add_argument('-s', '--size', type=int, nargs='+', default=[10, 10],
		    help='Size of the identicon. Default 10 10')
parser.add_argument('-i', '--inp', type=str, required=True,
		    help='Input string to hash')
parser.add_argument('-o', '--out', type=str, default='identicon.png',
		    help='Input string to hash. Default: identicon.png')
args = parser.parse_args() 

# Set-up a list of foreground colours (taken from Sigil).
foreground = [ "rgb(45,79,255)",
"rgb(254,180,44)",
"rgb(226,121,234)",
"rgb(30,179,253)",
"rgb(232,77,65)",
"rgb(49,203,115)",
"rgb(141,69,170)" ]

# Set-up a background colour (taken from Sigil).
background = "rgb(224,224,224)"

generator = pydenticon.Generator(args.size[0], args.size[1],
				 foreground=foreground,
                                 background=background)
identicon_png = generator.generate(args.inp, 200, 200,
                                   output_format="png")
with open(args.out, 'wb') as outf:
    outf.write(identicon_png)
