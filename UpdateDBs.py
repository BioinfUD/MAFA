import os
import Config

def usage():
    print "This script updates the mappings table, also the Non-redundant database and Uniprot database "
    exit()
def rmandupdate():
    cursor=Config.connect()
    print "Deleting mappings"
    query="DROP TABLE mappings_e"
    cursor.execute(query)
    print "Removing local database files"
    os.system("rm -rf idmapp* Referen*")
    print "Reinstalling everything"
    os.system("bash Install.sh")

def main():
    if len(sys.argv)!=1:
        usage()
    rmandupdate()
main()