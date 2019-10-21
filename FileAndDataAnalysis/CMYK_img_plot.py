#!/usr/bin/env python3

from PIL import Image
import argparse, math, sys

pars = argparse.ArgumentParser()
pars.add_argument("-f", "--file", help="File to load numbers from", required=True)
pars.add_argument("-s", "--save", help="file to save image to")
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

with open(doc) as f:
    for l in f:
        try:
            tmp = (l.rstrip())
            tmp = (tmp.split(';')[0]) # change like needed
            if len(tmp) < 8:
                fill = 8 - len(tmp)
                dum = '0'*fill
                tmp = dum + '' + tmp
            c = int(tmp[:2], 16)
            m = int(tmp[2:4], 16)
            y = int(tmp[4:6], 16)
            k = int(tmp[6:8], 16)
            num.append((c,m,y,k))
        except Exception as e:
            pass
            # print('Value: {} | Error: {}'.format(l, e))

size = math.floor(math.sqrt(len(num)))
print(size)
print(num[111])

image = Image.new("CMYK", (size,size))
i = 0

for x_axis in range(size):
    for y_axis in range(size):
        color = (num[i])
        image.putpixel((x_axis, y_axis), color)
        '''
        try:
            if len(n) < 8:
                fill = 8 - len(n)
                dum = '0'*fill
                n = dum + '' + n
            c = int(n[:2], 16)
            m = int(n[2:4], 16)
            y = int(n[4:6], 16)
            k = int(n[6:8], 16)
            #k = int(n[6:8], 16)
            color = (c, m, y, k)
            image.putpixel((x_axis,y_axis), color)
        except Exception as e:
            s = '# {} Error: {} | Value {}'.format(i, e, n)
            print(s)
        '''
        i += 1

print("creating image - please wait")

image.save(fn)
