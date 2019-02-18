import Bio
from collections import Counter
from Bio import SeqIO

max_gc_id = None
max_gc = 0
for record in SeqIO.parse('gc_cont', "fasta"):
    c = Counter(record.seq)
    gc = float(c['C'] + c['G'])/float(len(record.seq))
    if gc > max_gc:
        max_gc, max_gc_id = gc, record.id

print max_gc_id
print max_gc*100