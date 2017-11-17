import huffman,lzw, os, lz78
from datetime import datetime
from bitarray import bitarray
from guppy import hpy
import numpy as np
import plotterAlgs
import zipUnzip

def hufflzwRun(txt):

	a = datetime.now()
	phase_1_txt = lzw.lzwCode(txt)

	codebook = huffman.makeFrequencies(phase_1_txt)
	cipher = ''.join(codebook[c] for c in phase_1_txt)
	b = datetime.now()

	plotterAlgs.cipherTime.append((b-a))
	print "cipherTime: " + str((b-a).microseconds)

	f = open('cipheredText', 'wb')
	a = bitarray(cipher)
	f.write(a)
	f.close()

	print 'Ciphered size = ' + str(os.path.getsize('cipheredText'))
	plotterAlgs.cipherSize.append(os.path.getsize('cipheredText'))

	a = datetime.now()
	decipher = huffman.decode(cipher, codebook)
	decipher = lzw.lzwDecode(decipher)
	b = datetime.now()

	plotterAlgs.decipherTime.append(b-a)
	print "decipherTime: " + str((b-a).microseconds)

	f2 = open('decipheredText', 'w')
	f2.write(str(decipher))
	f2.close()

	printar = open('decipheredText','r')
	print printar.read()[:40]
	printar.close()

	print 'Back to original = ' + str(os.path.getsize('decipheredText'))
	plotterAlgs.decipherSize.append(os.path.getsize('decipheredText'))

def lzwhuffRun(txt):

	a = datetime.now()
	codebook = huffman.makeFrequencies(txt)
	cipher = ''.join(codebook[c] for c in txt)
	cipher = lzw.lzwCode(cipher)
	b = datetime.now()

	plotterAlgs.cipherTime.append((b-a))
	print "cipherTime: " + str((b-a).microseconds)

	f = open('cipheredText', 'wb')
	a = bitarray(cipher)
	f.write(a)
	f.close()

	print 'Ciphered size = ' + str(os.path.getsize('cipheredText'))
	plotterAlgs.cipherSize.append(os.path.getsize('cipheredText'))

	a = datetime.now()
	decipher = lzw.lzwDecode(cipher)
	decipher = huffman.decode(decipher, codebook)
	b = datetime.now()

	plotterAlgs.decipherTime.append(b-a)
	print "decipherTime: " + str((b-a).microseconds)

	f2 = open('decipheredText', 'w')
	f2.write(str(decipher))
	f2.close()

	printar = open('decipheredText','r')
	print printar.read()[:40]
	printar.close()

	print 'Back to original = ' + str(os.path.getsize('decipheredText'))
	plotterAlgs.decipherSize.append(os.path.getsize('decipheredText'))

def lzwRun(txt):

	a = datetime.now()
	cipher = lzw.lzwCode(txt)
	b = datetime.now()

	plotterAlgs.cipherTime.append(b-a)
	print "cipherTime: " + str((b-a).microseconds)

	f = open('cipheredText', 'wb')
	a = bitarray(cipher)
	f.write(a)
	f.close()

	print 'Ciphered size = ' + str(os.path.getsize('cipheredText'))
	plotterAlgs.cipherSize.append(os.path.getsize('cipheredText'))

	a = datetime.now()
	decipher = lzw.lzwDecode(cipher)
	b = datetime.now()

	plotterAlgs.decipherTime.append(b-a)
	print "decipherTime: " + str((b-a).microseconds)

	f2 = open('decipheredText', 'w')
	f2.write(str(decipher))
	f2.close()

	printar = open('decipheredText','r')
	print printar.read()[:40]
	printar.close()

	print 'Back to original = ' + str(os.path.getsize('decipheredText'))
	plotterAlgs.decipherSize.append(os.path.getsize('decipheredText'))

def huffRun(txt):

	phase_1_txt = txt

	a = datetime.now()
	codebook = huffman.makeFrequencies(phase_1_txt)
	cipher = ''.join(codebook[c] for c in phase_1_txt)
	b = datetime.now()

	plotterAlgs.cipherTime.append(b-a)
	print "cipherTime: " + str((b-a).microseconds)

	f = open('cipheredText', 'wb')
	a = bitarray(cipher)
	f.write(a)
	f.close()

	print 'Ciphered size = ' + str(os.path.getsize('cipheredText'))
	plotterAlgs.cipherSize.append(os.path.getsize('cipheredText'))

	a = datetime.now()
	decipher = huffman.decode(cipher, codebook)
	b = datetime.now()

	plotterAlgs.decipherTime.append(b-a)
	print "decipherTime: " + str((b-a).microseconds)

	f2 = open('decipheredText', 'w')
	f2.write(str(decipher))
	f2.close()

	printar = open('decipheredText','r')
	print printar.read()[:40]
	printar.close()

	print 'Back to original = ' + str(os.path.getsize('decipheredText'))
	plotterAlgs.decipherSize.append(os.path.getsize('decipheredText'))

def shannonrun(txt):

	a = datetime.now()
	os.system('python shannon-fano.py e toRead.txt cipheredText')
	b = datetime.now()
	plotterAlgs.cipherTime.append(b-a)

	a = datetime.now()
	os.system('python shannon-fano.py d cipheredText decipheredText')
	b = datetime.now()
	plotterAlgs.decipherTime.append(b-a)

	plotterAlgs.cipherSize.append(os.path.getsize('cipheredText'))

	printar = open('decipheredText','r')
	print printar.read()[:40]
	printar.close()

	plotterAlgs.decipherSize.append(os.path.getsize('decipheredText'))

def lz78Run(txt):
	a = datetime.now()
	size = lz78.encode(txt)
	b = datetime.now()
	f = open('cipheredText', 'wb')
	f.write(bitarray(size))
	f.close()

	plotterAlgs.cipherSize.append(os.path.getsize('cipheredText'))
	print "cipherSize: " + str(os.path.getsize('cipheredText'))
	plotterAlgs.cipherTime.append(b-a)
	print "cipherTime: " + str((b-a).microseconds)
	plotterAlgs.decipherTime.append(0)
	print "decipherTime: " + str(0)
	plotterAlgs.decipherSize.append(0)
	print "decipherSize: " + str(0)

	printar = open('decipheredText','r').read()[:40]
	print printar

def zipRun(txt):

	a = datetime.now()
	zipUnzip.zippit(txt)
	b = datetime.now()

	plotterAlgs.cipherTime.append(b-a)
	plotterAlgs.cipherSize.append(os.path.getsize('cipheredText'))

	print 'Cipher size: ' + str(os.path.getsize('cipheredText'))
	print 'Cipher time: ' + str(b-a)

	a = datetime.now()
	zipUnzip.unzippit()
	b = datetime.now()

	plotterAlgs.decipherTime.append(b-a)
	plotterAlgs.decipherSize.append(os.path.getsize('decipheredText'))

	print 'Cipher size: ' + str(os.path.getsize('decipheredText'))
	print 'Cipher time: ' + str(b-a)


txt = open('bible-kjv.txt','r').read()
#txt = open('toRead.txt','r').read()
#txt = open('smallToRead.txt','r').read()
#txt = 'thisisthe'
print 'Original size = ' + str(len(txt))#str(os.path.getsize('bible-kjv.txt'))
print 

print 'Huffman'
a = datetime.now()
huffRun(txt)
b = datetime.now()
print str(b-a)
print

print 'Shannon-Fano'
a = datetime.now()
shannonrun(txt)
b = datetime.now()
print str(b-a)
print 

# print 'LZ78'
# a = datetime.now()
# lz78Run(txt)
# b = datetime.now()
# print str(b-a)
# print

print 'ZIP'
a = datetime.now()
zipRun(txt)
b = datetime.now()
print str(b-a)
print

print 'LZW'
a = datetime.now()
lzwRun(txt)
b = datetime.now()
print str(b-a)
print 

print 'Huffman + LZW'
a = datetime.now()
hufflzwRun(txt)
b = datetime.now()
print str(b-a)
print

print 'LZW + Huffman'
a = datetime.now()
lzwhuffRun(txt)
b= datetime.now()
print str(b-a)
print


#plot graphs
plotterAlgs.plotDatGraph()