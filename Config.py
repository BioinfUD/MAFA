import MySQLdb
import multiprocessing


#Cristian Alejandro Rojas
#carojasq@correo.udistrital.edu.co
#This script connect to a MySQL db and returns a cursor ready for querys

global nrdb,updb
nrdb="Reference_dbs/nr"
updb="Reference_dbs/uniprot_sprot.fasta"
global max_threads
max_threads=12
def connect():
	#DBSettings
	host="localhost"
	user="root"
	password="6nu"
	db_name="genetix"
	try:
		db=MySQLdb.connect(host=host,user=user,passwd=password,db=db_name)
		try: 
			db.autocommit(True)
		except:
			print "Autommit setting was not possible for this connection, please check the mysql settingss"
			quit()
	except:
		print "There was an error when creating de DB connection"
		quit()
	cursor = db.cursor(MySQLdb.cursors.DictCursor) 
	return cursor
