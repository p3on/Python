#!/usr/bin/env python3

from PIL import Image
import argparse, math, sys

pars = argparse.ArgumentParser()
pars.add_argument("-f", "--file", help="File to load numbers from", required=True)
pars.add_argument("-s", "--save", help="file to save image to")
pars.add_argument("-b", "--binary", help="enable binary Mode for binary files", default=False)

args = pars.parse_args()

fn = "rnd_numbers.jpg"

if not(args.file):
    print("file parameter has to be served")
    pars.print_help()
    sys.exit(2)

if args.save:
    fn = args.save + '.jpg'

doc = args.file

num = []

print('[ i ] - Step 1/3: Reading file contents...')

if not (args.binary):
    with open(doc) as f:    
        for l in f:
            try:
                tmp = (l.rstrip())
                tmp = (tmp.split(';')[1]) # change like needed
                if len(tmp) < 8:
                    fill = 8 - len(tmp)
                    dum = '0'*fill
                    tmp = dum + '' + tmp
                for t in tmp:
                    if t == 0:
                        num.append(0)
                        num.append(0)
                        num.append(0)
                        num.append(0)
                    else:
                        hex = "{0:04b}".format(int(t,16))
                        for h in hex:
                            num.append(h)
            except Exception as e:
                pass
                # print('Value: {} | Error: {}'.format(l, e))
else:
    with open(doc, 'rb') as f:
        byte = True
        while byte:
            byte = f.read(1)
            i = int.from_bytes(byte, byteorder='big')
            bits = '{0:08b}'.format(i)
            for b in bits:
                if b == '0':
                    num.append(0)
                else:
                    num.append(1)

size = math.floor(math.sqrt(len(num)))
# print(size)
# print(num[111])

image = Image.new("1", (size,size))
i = 0

print('[ i ] - Step 2/3: Positioning pixels...')

for x_axis in range(size):
    for y_axis in range(size):
        color = (num[i])
        image.putpixel((x_axis, y_axis), int(color))
        i += 1

print('[ i ] - Step 3/3: Creating image...')

image.save(fn)
