#!/usr/bin/env python
from PIL import Image
import sys
import math

def makePng(input):
#	binary = open(input,'r').read()
	f = open(input,'r')
	binary = f.read()
	f.close()
	
	size = int(math.sqrt(len(binary)))
	print('file len:%d\nPNG size:%d * %d' % (len(binary), size, size))
	#new black image
	image = Image.new("RGB", (size, size), "black")
	
	for i in range(0, size):
		for j in range(0, size):
				if binary[i*size+j] == '1':
						#if binary has value 1 at that point in the 2D array, 
						#set pixel to white
						image.putpixel((i, j), (255, 255, 255))
	image.save("output.png")

makePng(sys.argv[1])
