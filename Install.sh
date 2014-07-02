function download_ref_dbs {
#Descarga NR
	mkdir Reference_dbs
	cd Reference_dbs
	echo Downloading Non-redundant database from NCBI server
	wget ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nr.gz
	echo uncompressing file
	gunzip nr.gz  	
	echo Creating index
	makeblastdb -in nr -dbtype prot
	#Descarga uniprot
	echo Downloading Uniprot database from Uniprot server
	wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
	gunzip  uniprot_sprot.fasta.gz
	echo Creating index
	makeblastdb -in uniprot_sprot.fasta -dbtype prot
}

#Descarga Mapeos
echo Downloading mapping file
wget ftp://ftp.pir.georgetown.edu/databases/idmapping/idmapping.tb.gz
echo Uncompressing idmapping.tb
gunzip idmapping.tb.gz
echo Writing mapping file to database 
python MappingsToDB.py idmapping.tb &
echo The process has been sended to background
echo Bringing mapping2db process to foregroung
fg 1
fg 1
