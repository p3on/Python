#!/usr/bin/env python3

import sys

if not(sys.argv[1]):
    exit

file = sys.argv[1]
one = 0
zero = 0

with open(file, 'rb') as f:
    byte = True
    while byte:
        byte = f.read(1)
        i = int.from_bytes(byte, byteorder='big')
        bits = '{0:08b}'.format(i)
        for b in bits:
            if b == '0':
                zero += 1
            else:
                one += 1

f.close()

print("Result:\nZeros: {}\nOnes:  {}".format(zero, one))
