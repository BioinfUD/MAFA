import sys
global data
data={}


def loaddata(archivo):
	global data
	archivo=open(archivo,"r")
	for line in archivo:
		line=line.replace("\n","")
		tmp_array=line.split(";",1)
		GoId=tmp_array[0]
		contigs=tmp_array[1]
		data[GoId]=set(tmp_array[1].split(";"))

def searchIntersection(goids):	
	result=set(data[goids[0]]).intersection(set(data[goids[1]]))
	for goid in goids[2:]:
		result=result.intersection(set(data[goid]))
	return result

def usage():
	print """
	CrossedGOSearch.py go2Sequences.csv GO:002112,GO:0127983,GO:01231
	"""
	exit()

def main():
	if len(sys.argv)!=3:
		usage()
	GoWanted=sys.argv[2]
	File_in=sys.argv[1]
	loaddata(File_in)
	GoWanted=GoWanted.split(",")
	print "The terms that are part of %s are:" % ",".join(GoWanted)
	print "\n".join(list(searchIntersection(GoWanted)))

main()