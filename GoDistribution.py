#This script makes the distribution of GO terms anotated using second level Terms
global Dict2
global obos
import sys
import os
sys.path.append(os.path.split(sys.argv[0])[0])
sys.path.append(os.path.split(sys.argv[0])[0] + "/Utilities")
sys.path.append("Utilities")
import GoRelationalFunctions
import StringIO
import OboParser
#Function that gives GOID information (OBO imported from DB)
OBOs = OboParser.parseObo(open("Data/go.obo", "r"))
Dict2 = {}


#Name of file containing the GO terms to serach
#Initializes the  wanted terms dictionary
def loadTerms(GOwanted):
    Data_in = open(GOwanted, "r")
    global Dict2
    counter = 0
    for line in Data_in:
        data_main = line.replace(" ", "").replace("\n", "")
        Dict2[data_main] = []


#Asocciates GO Identifiers with a second level parent and stores results y main Dictionary
def asocciate(in_file):
    in_file = open(in_file, "r")
    for line in in_file:
        contig_id = line.split(",")[0]
        if line.split(",")[1] == "NotFound" or line.split(",")[1] == "":
            pass
        gos = line.split(",")[1].replace(" ", "").split(";")
        for goid in gos:
            go_keys = Dict2.keys()
            for go_key in go_keys:
                if go_key in GoRelationalFunctions.getAncestors(OBOs, goid):
                    Dict2[go_key].append(contig_id)


#Write ready to plot tables
def writeTables(Counted_file):
    out_file = open(Counted_file, 'w')
    for go2 in Dict2.keys():
        out_file.write('%s\t%s\n' % (go2, str(len(Dict2[go2]))))
    return 0


#Write go 2 contigs associations
def writego2contigs(outgo2contigs):
    out_file = open(outgo2contigs, "w")
    for go2 in Dict2.keys():
        out_file.write('%s;%s\n' % (go2, ";".join(Dict2[go2])))
    return 0


#Another help function
def usage():
    print """
    GoDistribution.py contigs2go.csv GOswanted Counted_GOs.tab go2contigs.csv
    """
    exit()


def main():
    if len(sys.argv) != 5:
        usage()
    Counted_file = sys.argv[3]
    GOwanted = sys.argv[2]
    in_file = sys.argv[1]
    go2contigs_file = sys.argv[4]
    print "Loading terms to asocciate"
    loadTerms(GOwanted)
    print "Associating terms to contigs"
    asocciate(in_file)
    print "Writing outputs"
    writeTables(Counted_file)
    writego2contigs(go2contigs_file)


main()
