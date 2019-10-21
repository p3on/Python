# ELF

Snippets that I used for debugging / loading the esp32 memory dump into IDA (using xtensilica addon for IDA).

As the addon only handled .elf files very well, the idea was to wrap an ELF-Header/Trailer around the dump and load it into IDA. Worked so far as IDA loaded the self generated ELF file but the segments seemed off and the functions very not recognized.

### Procedure

- Dump the memory ares you wish to analyze (0x3ff9_0000 to 0x3ff9_ffff and 0x4000_0000 to 0x4005_ffff or more)
- adjust the makeELFheader.py, this generates the ELF header containing the program header table (I used it to map the two areas into the virtual address space)
- Run makeELFtrailer.py, this uses the dumped information from the esp32_rom.elf reference file and copies the section table into your new ELF-trailer

Final Step: after running all the scripts there should be three or more files (ELFhdr, memdump 1 to n, ELFtrailer) concatenate and check if it is valid with:

```bash
file esp32_rom.elf
esp32_rom.elf: ELF 32-bit LSB executable, Tensilica Xtensa, version 1 (SYSV), statically linked, not stripped
```

After that IDA should accept the file, you can force analysis but this results in partially bad analyzed code - what causes this problem may be the different address alignments in the segments (at least it looks like that in the dumpelf output from the reference file).
