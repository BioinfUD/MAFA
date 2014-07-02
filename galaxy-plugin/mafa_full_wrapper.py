import sys
import os
from random import randint


def usage():
    print """This is a wraper for the full workflow of MAFA adapted to galaxy
    python2 mafa_full_wraper.py $in_fasta $wanted_gos $database $output_pdf
    """
    exit()


def main():
    if len(sys.argv) != 6:
        usage()
    in_file = sys.argv[1]
    wg = sys.argv[2]
    out_dir = "/tmp/%s" % str(randint(1, 10000))
    db = sys.argv[3]
    output_pdf = sys.argv[4]
    try:
        os.chdir(os.environ['MAFA_BASE_DIR'])
    except:
        print "Check that $MAFA_BASE_DIR exists"
    try:
        os.system("mkdir %s" % out_dir)
    except:
        print "Can't create %s , please check your permissions over /tmp" % out_dir
    os.system("python2 GoFullAnalysis.py %s %s %s %s" % (in_file, wg, out_dir, db))
    os.system("mv %s/*pdf %s" % (out_dir, output_pdf))
    os.system("rm -rf %s" % out_dir)


main()
