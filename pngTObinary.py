from PIL import Image
import sys

def makeBinary(image):
	binary = ""
	size = image.size[0]
	print('PNG size:%d * %d\nfile len:%d' % (size, size, size*size))
	for i in range(0, size):
		for j in range(0, size):
			#if the pixel is black
			if image.getpixel((i, j)) == (0, 0, 0):
				binary += "1"
			else:
				binary += "0"

	with open("output.txt", "w") as text_file:
		text_file.write(str(binary))
image = Image.open(sys.argv[1])
makeBinary(image)
