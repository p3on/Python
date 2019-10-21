#!/usr/bin/env python3

# reference dict, all values 4 byte
sec_hdr = {
    '.sh_name' : 0,         # b'\x00\x00\x00\x00',
    '.sh_type' : 0,         # b'\x00\x00\x00\x00',
    '.sh_flags' : 0,        # b'\x00\x00\x00\x00',
    '.sh_addr' : 0,         # b'\x00\x00\x00\x00',
    '.sh_offset' : 0,       # b'\x00\x00\x00\x00',
    '.sh_size' : 0,         # b'\x00\x00\x00\x00',
    '.sh_link' : 0,         # b'\x00\x00\x00\x00',
    '.sh_info' : 0,         # b'\x00\x00\x00\x00',
    '.sh_addralign' : 0,    # b'\x00\x00\x00\x00',
    '.sh_entsize' : 0       # b'\x00\x00\x00\x00'
}

order = ('.sh_name', '.sh_type', '.sh_flags', '.sh_addr', '.sh_offset', '.sh_size', '.sh_link', '.sh_info', '.sh_addralign', '.sh_entsize')

base3 = int('0x3FF90000', 16)
base4 = int('0x40000000', 16)

offset3 = int('0x74', 16)   # offset durch elf header und program header table
offset4 = offset3 + 65536  # 65536 old offset 393216

outfile = open('sec_hdr_trailer.bin', 'wb')

i = 1       # Starting with SHT_NULL section counted

def write():
    global sec_hdr

    # keep rest and write binary data bulkaction
    for o in order:
        s = sec_hdr[o]
        # print(int(s).to_bytes(4, byteorder='little'))
        outfile.write(int(s).to_bytes(4, byteorder='little'))

def writeData():
    global sec_hdr
    global i
    if sec_hdr['.sh_addr'] == '0x0':
        return
    # calculate difference from base and link to own file offset
    #print(i)
    #print(sec_hdr['.sh_addr'])
    base = base3 if sec_hdr['.sh_addr'].startswith('0x3') else base4
    dif = int(sec_hdr['.sh_addr'], 16) - base
    sec_hdr['.sh_addr'] = int(sec_hdr['.sh_addr'], 16) # conver to int so bulkaction is easier
    offset = offset3 if (base==base3) else offset4
    # change offset
    sec_hdr['.sh_offset'] = dif + offset

    write()
    
    i += 1

write()     # write SHT_NULL type section header

with open('esp32_rom.dumpelf', 'r') as fp:
    line = True
    check = 0
    while line:
        line = fp.readline()
        if not (('.sh_' in line) or ('.p_' in line)):
            check = 0
            continue
        line = line.split(',')[0]
        l1, l2 = line.split('=')
        l2 = l2.strip()
        l1 = l1.strip()
        if (l1 == '.sh_addr') and (('0x3FFA' in l2) or ('0x3FFB' in l2) or ('0x3FFE' in l2)):
            print(l2)
            check = 0
            continue
        sec_hdr[l1] = l2

        if l1 == '.sh_name':
            check = 1

        if l1 == '.sh_entsize' and check == 1:
            writeData()

outfile.close()

print("Number of entries in Section header table: {}".format(i))
