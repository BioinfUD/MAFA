#!/usr/bin/python2
#carojasq@correo.udistrital.edu.co
#GICOGE Research Group
#Udistrital

import sys
sys.path.append(os.path.split(sys.argv[0])[0])
from Bio.Blast import NCBIXML
##
def usage():
	"""  This script converts a XML input of BLAST to a custom CSV format ready to do the functional annotation with Gene Onlotogy
	BlastXML2CSVCustom.py blast_xml_input.xml querys2hits.csv
	"""
	exit()

def convertandwrite(in_file, outfile):
	csv_file=open(outfile,"w")
	xml_in=open(in_file,"w")
	count=0
	records=NCBIXML.parse(xml_in)
	for record in records:
		for alignment in record.alignments[0:1]:	
			#Solo toma la parte del query id que da el id del query real.
			query_id=record.query.split(" ")[0]
			hit_def=alignment.hit_def
			csv_file.write('"%s","%s"' % (query_id, hit_def))
			count=count+1
	return count

def main():
	if len(sys.argv)!=3:
		usage()
	input_xml=sys.argv[1]
	output_csv=sys.argv[2]
	counter=convertandwrite(input_xml, output_csv)
	print "%s hits has been wrote to %s " % (str(counter), output_csv)

main()
