def fastaread(filehandle):

    # Initialize some arrays to return first
    fastaid = []
    seqarray = []

    # Open file
    f = openandread(handle)

    # First while True:/Break idiom to pass any and all blank spaces
    while True:
        line = f.readline
        if line is empty:
            return
        if line[0] is '>':           # If we find a fasta id however, then we break
            break

    # Now we'll start our other while True:/Break idiom
    # This one will find the fasta record, put that record in an array.
    # Then until the next record or end of file is encountered, it will
    # read in all the lines and return that sequence

    while True:
        if not line.startswith('>'):
            raise Error(
                    "Records in FASTA files should start with '>' character")

        title = line[1:end].rstrip()
        fastaid.append(title)

        # Initialize our seqdata variable. This one will store one single sequence
        seqdata = []

        line = f.readline()

        # This second while True:/Break idiom extract the sequence data
        while True:
            if not line:
                break
            if line [0] == '>':       # Check to see if we're onto the next record
                break
            seqdata.append(line.rstrip())
            line = f.readline()

        # Take the data in seqdata and join it together and add to the seqarray
        nts = ''.join(seqdata).replace(" ", "").replace("\r", "")
        seqarray.append(nts)

        # If we're at the end of the document we'll go ahead and return our array
        # of ids and sequences
        if not line:
            return fastaid, seqarray

def percentgc(fastaids, seqarray):

    # Finds the gc content of sequences in FASTA files

    # Initialize our seqgc variable
    # This stores all the %gc vals for seq
    seqgc = [];

    # First we need to check if the two arrays are of
    # the same length, i.e., have the same number of
    # elements in them

    if len(fastaids) != len(seqarray):
        return ValueError(
            "The number of records and sequences is not the same. Try again.")

    for seq in seqarray:
        gccount = seq.count('G') + seq.count('C')
        totcount = len(seq)
        seqgc.append(100*gccount/totcount)

    # Find the max value and index and return the fasta id and %gc
    max_gc = max(seqgc)
    max_index = seqgc.index(max_gc)

    print fastaids[max_index]
    print max_gc
