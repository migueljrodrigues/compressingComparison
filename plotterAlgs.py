import matplotlib
from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib.patches as mpatches

global algorithms
algorithms = ['Huffman C','Huffman D',
'Shannon-Fano C', 'Shannon-Fano D',
'ZIP C', 'ZIP D',
'LZW C','LZW D',
'Huffman+LZW C','Huffman+LZW D',
'LZW + Huffman C','LZW + Huffman D'] 
global cipherTime
cipherTime = []
global cipherSize
cipherSize = []
global decipherTime
decipherTime = []
global decipherSize
decipherSize = []


def plotDatGraph():

	style.use('ggplot')

	#tempo
	labels = []
	x = algorithms
	y = []
	internalif = 0
	internalelse = 0

	for bucket in range(0,len(algorithms)):
		try:
			if bucket % 2 == 0:
				y.append(cipherTime[internalif])
				internalif = internalif + 1
			else:
				y.append(decipherTime[internalelse])
				internalelse = internalelse + 1
		except:
			continue

	for asd in range(len(y)):
		try:
			y[asd] = y[asd].microseconds
		except:
			continue

	listofbars = plt.bar(range(len(y)), y, align='center')
	for bucket in range(0,len(algorithms)):
		try:
			if bucket % 2 != 0:
				listofbars[bucket].set_color('g')
		except:
			continue

	plt.xticks(range(len(y)), x, size='small')

	plt.title('Comparison of compression/decompression operations (Time)')
	plt.ylabel('Time (microseconds)')
	plt.xlabel('Algorithms')

	plt.show()

	#size
	labels = []
	x = algorithms
	y = []
	internalif = 0
	internalelse = 0

	for bucket in range(0,len(algorithms)):
		try:
			if bucket % 2 == 0:
				y.append(cipherSize[internalif])
				try:
					labels.append(str(100-round(float(cipherSize[internalif])/decipherSize[internalif] * 100,2)) + "%")
					internalif = internalif + 1
				except:
					labels.append("")
					internalif = internalif + 1
			else:
				y.append(decipherSize[internalelse])
				internalelse = internalelse + 1
				labels.append("")
		except:
			continue

	print y

	listofbars = plt.bar(range(len(y)), y, align='center')
	for bucket in range(0,len(algorithms)):
		try:
			if bucket % 2 != 0:
				listofbars[bucket].set_color('g')
		except:
			continue
	plt.xticks(range(len(y)), x, size='small')

	plt.title('Comparison of compression/decompression operations (Space)')
	plt.ylabel('Size (bytes)')
	plt.xlabel('Algorithms')
	rects=listofbars.patches
	for rect, label in zip(rects, labels):
		height = rect.get_height()
		plt.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')

	red_patch = mpatches.Patch(label='Compress')
	plt.legend(handles=[red_patch])
	red_patch2 = mpatches.Patch(color='g',label='Decompress')
	plt.legend(handles=[red_patch2])

	plt.show()