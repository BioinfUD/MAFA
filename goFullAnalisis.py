import os
import sys
import Config
def usage():
	print """ This is the wrapper to get the GO distribution from a BLAST result
	goFullAnalisis.py in_file.fasta wanted_gos out_dir refseq|uniprot
	"""
	exit()
#	GoDistribution.py contigs2go.csv GOswanted Counted_GOs.tab go2contigs.csv
# 	hits2go.py querys2hits.csv hits2terms.csv


def main():
	if len(sys.argv)!=5:
		usage()
	in_file=sys.argv[1]
	out_dir=sys.argv[3]
	gos_buscados=sys.argv[2]
	db_blast=sys.argv[4]
	if db_blast=="refseq":
		db_blast=Config.nrdb
	elif db_blast=="uniprot":
		db_blast=Config.nrdb
	else:
		usage()
	hit2terms_file="%s/hits2terms.csv" % out_dir
	counted_GOs="%s/Counted_GOs.tab" % out_dir
	go2contigs_file="%s/go2contigs.csv" % out_dir
	out_img="%s/output.png" % out_dir
	out_pdf="%s/Report.pdf" % out_dir
	salida_csv='%s/query2hits.csv' % out_dir
	salida_xml='%s/query2hits.xml' % out_dir
	archivo_entrada=salida_csv
	print "The output dir is: %s" % out_dir
	print "The  XML output of blast will be on %s" % salida_xml
	print "The  CSV output of blast will be on %s" % salida_csv
	print "The GO terms wanted are in: %s" % gos_buscados
	print "The input file is: %s" % archivo_entrada
	print "The file containing relation bettwen sequences and terms is: %s" % hit2terms_file
	print "The GO terms to Sequences file is: %s" % go2contigs_file
	print "The count file of wanted GO terms is: %s" % counted_GOs
	print "The pie char will be generated to: %s" % out_img
	print "The PDF report will be generated on: %s" % out_pdf
	print "*************************Running process******************"
	print "Creating output directory..."
	mkdir_c=os.system('mkdir %s' % out_dir)
	print "Executing BLAST"
	print "Getting top hits and writing csv file"
	convert_c=os.system("python Utilities/BlastXML2CSVCustom.py %s %s" % (salida_xml, salida_csv ))
	print "Doing associations bettwen hits and gos...."
	hit2go_c=os.system("python hits2go.py"+" "+archivo_entrada+" "+hit2terms_file)
	print "Generating distribution......"
	goDis_c=os.system("python2 GoDistribution.py"+ " "+ hit2terms_file+" "+gos_buscados+" "+counted_GOs+" "+go2contigs_file)
	print "Generating Pie Char"
	charPie=os.system("python2 Utilities/GraphPie.py "+ counted_GOs +" "+ out_img)
	print "Generating PDF report"
	genPDF=os.system("python2  Utilities/PdfGen.py "+ counted_GOs +" "+ out_pdf+" "+out_img)

main()


