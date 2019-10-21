#!/usr/bin/env python3

ei_mag = b'\x7f\x45\x4c\x46'        # Magic bytes
ei_class = b'\x01'                  # Architecture 1=32, 2=64
ei_data = b'\x01'                   # endianess 1=LE, 2=BE
ei_version = b'\x01'                # ELF version fixed value
ei_osabi = b'\x00'                  # Target system ABI
ei_abiversion = b'\x00'             # ABI version, none defined for linux
ei_pad = b'\x00\x00\x00\x00\x00\x00\x00'# Padding

e_type = b'\x00\x02'                # Type of file 2=EXECUTABLE
e_machine = b'\x00\x5e'             # specifies ISA
e_version = b'\x00\x00\x00\x01'     # ELF Version 1=CURRENT

e_entry = b'\x40\x00\x04\x00'       # entrypoint
e_phoff = b'\x00\x00\x00\x34'       # Program Header offset
e_shoff = b'\x00\x07\x00\x74'       # Section Header offset c0074

e_flags = b'\x00\x00\x03\x00'       # Flags - depending on chip/arch
e_ehsize = b'\x00\x34'              # ELF header size, 32Bit=52 64Bit=64
e_phentsize = b'\x00\x20'           # Progam header table entry
e_phnum = b'\x00\x02'               # Num entries on Program header table
e_shentsize = b'\x00\x28'           # Size of a section header table entry
e_shnum = b'\x00\x0f'               # Num entries in Section header table
e_shstrndx = b'\x00\x00'            # Index of section header tbl entry that contains section names


elf_header = [ei_class, ei_data, ei_version, ei_osabi, ei_abiversion, ei_pad, e_type, e_machine, e_version, e_entry, e_phoff, e_shoff, e_flags, e_ehsize, e_phentsize, e_phnum, e_shentsize, e_shnum, e_shstrndx]

# 3ff90000 segment
p0_type = b'\x00\x00\x00\x01'        # Type of segment: 1=loadable, 0=unused, 2=dynamic
p0_offset = b'\x00\x00\x00\x74'      # Offset of segment in file image
p0_vaddr = b'\x3f\xf9\x00\x00'       # Virtual address
p0_paddr = b'\x3f\xf9\x00\x00'       # Physical address
p0_filesz = b'\x00\x01\x00\x00'      # Segment size, may be 0
p0_memsz = b'\x00\x01\x00\x00'       # Segment size in memory, may be 0
p0_flags = b'\x00\x00\x00\x06'       # Flags (32bit position)
p0_align = b'\x00\x00\x00\x01'       # 0/1 = no alignment, otherwhise positive power of 2 number
p0_hdr = [p0_type, p0_offset, p0_vaddr, p0_paddr, p0_filesz, p0_memsz, p0_flags, p0_align]

# 40000000 segment
p1_type = b'\x00\x00\x00\x01'
p1_offset = b'\x00\x01\x00\x74'     # old offset 10074
p1_vaddr = b'\x40\x00\x00\x00'
p1_paddr = b'\x40\x00\x00\x00'
p1_filesz = b'\x00\x06\x00\x00'
p1_memsz = b'\x00\x06\x00\x00'
p1_flags = b'\x00\x00\x00\x06'
p1_align = b'\x00\x00\x00\x01'
p1_hdr = [p1_type, p1_offset, p1_vaddr, p1_paddr, p1_filesz, p1_memsz, p1_flags, p1_align]

arraylist = [elf_header, p0_hdr, p1_hdr]

f = open('elf_hdr.bin', 'wb')

f.write(ei_mag)                     # Magic Bytes always written the same! LE/BE

for array in arraylist:
    for val in array:
        if len(val) == 1:
            f.write(val)
        elif ei_data == b'\x01':
            val = val[::-1]
            f.write(val)
        else:
            f.write(val)
