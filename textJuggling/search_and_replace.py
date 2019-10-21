def readSentences(openedFile):
    """Function to read sentences from the different files, read sentences identified by an '&' instead of a '#'
    Args:
        openedFile: FileHandler to the file being read
    Returns:
        sentences: Array of sentences read from file
    """
    read = 0
    sentences = []
    currentLine = 0
    jmp1 = 0
    jmp2 = 0

    for line in openedFile:
        currentLine += 1
        if (read == 0) and (re.match(r'&[0-9]{1,3}', line.decode('utf-8'))): # check if sentence 2 read
            jmp1 = len(line)
            read = 1
        elif (read == 1):
            sentences.append(line.strip(b'\n')) # save sentence
            jmp2 = len(line)
            openedFile.seek(-(jmp1+jmp2), 1) # jmp back to line identifier from cur pos (1)
            openedFile.write(('#' + str(math.ceil(currentLine/2)) + '\n').encode()) # change line identifier to sentence saved
            openedFile.seek(jmp2, 1) # go back to where we left reading
            read = 0 # reset status
    
    return sentences
