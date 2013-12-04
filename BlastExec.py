
import sys
import os
import Config
global threads

def usage():
    print """
    BlastExec.py query_file.fasta db_file output.xml
    """
    exit()

def sendblast(query_file, db_file, threads, prefix):
    command="blastx -query %s -outfmt 5 -db %s -evalue 1e-3 -num_threads %s -out %s" % (query_file, db_file, threads, prefix)
    print "Excuting alignments with blast"
    os.system(command)

def main():
    if len(sys.argv)!=4:
        usage()
    query_file=sys.argv[1]
    db_file=sys.argv[2]
    prefix=sys.argv[3]
    threads=Config.max_threads
    sendblast(query_file, db_file, threads, prefix)
    
main()