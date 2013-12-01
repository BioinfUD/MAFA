
#This script sends idmapping (tabular) file getting from ftp://ftp.pir.georgetown.edu/databases/idmapping/ to a table for easy #access.
#Cristian Alejandro Rojas
#carojasq@correo.udistrital.edu.co
import sys, os
sys.path.append(os.path.split(sys.argv[0])[0])
sys.path.append(os.path.split(sys.argv[0])[0]+"/Utilities")
sys.path.append("Utilities")
import Config
import QueryGenerator

	
def usage():
	print "python2 mappingsToDB.py idmapping.tb"
	exit()

def createtable(table):
	cursor=Config.connect()
	query="CREATE TABLE IF NOT EXISTS `mappings_e` (  `GI` varchar(30000) NOT NULL,  `UniprotAC` varchar(50) DEFAULT NULL, `RefSeq` varchar(50) DEFAULT NULL,  `GoId` varchar(10000) NOT NULL, `EntrezGene` varchar(1000) NOT NULL,  KEY `UniprotAC` (`UniprotAC`),  KEY `RefSeq` (`RefSeq`), KEY `EntrezGene` (`EntrezGene`)) ENGINE=MyISAM DEFAULT CHARSET=latin1"
	cursor.execute(query)

def insert(file, table):
	count=0
	cursor=Config.connect()
	row={}
	for line in file:
		tmp_array=line.split("\t")
		row['UniprotAC']=tmp_array[0]
		row['GI']=tmp_array[4]
		row['RefSeq']=tmp_array[3]
		row['EntrezGene']=tmp_array[2]
		row['GoId']=tmp_array[7]
		if tmp_array[7]=="":
			pass
		GI_data=tmp_array[4]
		refseq_data=tmp_array[3]
		if len(GI_data.split(";"))>1:
			tmp_GI=GI_data.split(";")
			for AC_GI in tmp_GI:
				row['GI']=AC_GI.replace(" ","")
				query=QueryGenerator.gen_insert(table, row)
				cursor.execute(query)
				count=count+1
		if len(refseq_data.split(";"))>1:
			tmp_refseq=refseq_data.split(";")
			for AC_RefSeq in tmp_refseq:
				row['RefSeq']=AC_RefSeq.replace(" ","")
				query=QueryGenerator.gen_insert(table, row)
				cursor.execute(query)
				count=count+1
		else:
			query=QueryGenerator.gen_insert(table, row)
			cursor.execute(query)
			count=count+1
	return count
def main():
	if len(sys.argv)!=2:
		usage()
	createtable("mappings")
	print "Tabla creada, insertando registros"
	inserted=insert(open(sys.argv[1], "r"), "mappings")
	print "%s registros fueron insertados" % str(inserted)


main()