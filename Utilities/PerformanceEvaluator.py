import os
import sys
import random
from Bio import SeqIO
def genDataset(filename, number_seqs, outfile):
    print "Getting %s random sequences from %s" % (number_seqs, filename)
    secuencias=SeqIO.parse(open(filename, "r"), "fasta")
    secuencias=list(secuencias)
    random.shuffle(secuencias)
    aleatorias=[]
    for i in range(0, number_seqs):
        aleatorias.append(secuencias[i])
    escritras=SeqIO.write(aleatorias, outfile, "fasta")
    return outfile
    
def usage():
    exit()
    
def main():
    if len(sys.argv)!=6:
        usage()
    in_file=sys.argv[1]
    out_dir=sys.argv[3]
    wanted_gos=sys.argv[2]
    db_blasts=sys.argv[4].split(",")
    n_seqs=sys.argv[5].split(",")
    for n_seq in n_seqs:
        for db_blast in db_blasts:
            print "Working with %s and %s database" % (n_seq, db_blast)
            out_dir=sys.argv[3]
            out_dir=out_dir+"_"+n_seq+"_"+db_blast 
            selectedSeq=in_file+n_seq
            selectedSeq=genDataset(in_file, int(n_seq), selectedSeq)
            hit2terms_file="%s/hits2terms.csv" % out_dir
            counted_GOs="%s/Counted_GOs.tab" % out_dir
            go2contigs_file="%s/go2contigs.csv" % out_dir
            out_img="%s/output.png" % out_dir
            out_pdf="%s/Report.pdf" % out_dir
            salida_csv='%s/query2hits.csv' % out_dir
            salida_xml='%s/query2hits.xml' % out_dir
            analisiscommand="python2 goFullAnalisis.py %s %s %s %s > %s.log " % (selectedSeq, wanted_gos, out_dir, db_blast, out_dir)
            os.system(analisiscommand)
            print "Executing %s " % analisiscommand
    
main()
    