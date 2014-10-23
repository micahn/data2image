import Image
import sys
import math


def intToBytes(n):
    bytestring = ''
    bytestring = bytestring + (chr(n/(256*256*256)))
    n = n % (256*256*256)
    bytestring = bytestring + (chr(n/(256*256)))
    n = n % (256*256)
    bytestring = bytestring + (chr(n/(256)))
    n = n % 256
    bytestring = bytestring + chr(n)
    return bytestring


def dataToImage(data):
    data = intToBytes(len(data)) + data
    size = len(data)/3
    width = int(math.floor(math.sqrt(size)))
    height = size / (width * 1.0)
    if int(height) == height:
        height = int(height)
    else:
        height = int(height + 1)
    print len(data)
    print width*height
    im = Image.new("RGB", (width, height))
    im.fromstring(data + '\x00'*(1 + (width*height)*3 - len(data)))
    return im


filename = sys.argv[1]
file = open(filename, 'rb')
im = dataToImage(file.read())
im.show()
