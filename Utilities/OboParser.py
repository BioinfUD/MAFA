
#This is a OBO parser.
#This parser has been adapted by Cristian Rojas carojasq@correo.udistrital.edu.co
#Credits to Damian Kao from http://blog.nextgenetics.net/?e=6

def getTerm(stream):
  block = []
  for line in stream:
    if line.strip() == "[Term]" or line.strip() == "[Typedef]":
      break
    else:
      if line.strip() != "":
        block.append(line.strip())

  return block

def parseTagValue(term):
  data = {}
  for line in term:
    tag = line.split(': ',1)[0]
    value = line.split(': ',1)[1]
    if not data.has_key(tag):
      data[tag] = []

    data[tag].append(value)

  return data



def parseObo(oboFile):
  terms = {}
  #skip the file header lines
  getTerm(oboFile)
  #infinite loop to go through the obo file.
  #Breaks when the term returned is empty, indicating end of file
  while 1:
    #get the term using the two parsing functions
    term = parseTagValue(getTerm(oboFile))
    if len(term) != 0:
      termID = term['id'][0]

      #only add to the structure if the term has a is_a tag
      #the is_a value contain GOID and term definition
      #we only want the GOID
      if term.has_key('is_a'):
        termParents = [p.split()[0] for p in term['is_a']]
      #Part_of ADDED
#      if term.has_key('relationship'):
#        for el in term['relationship']:
#            if "part_of" in term['relationship']:
#                termParents.append(term['relationship'].split(" ")[0])
        if not terms.has_key(termID):
          #each goid will have two arrays of parents and children
          terms[termID] = {'p':[],'c':[]}

        #append parents of the current term
        terms[termID]['p'] = termParents

        #for every parent term, add this current term as children
        for termParent in termParents:
          if not terms.has_key(termParent):
            terms[termParent] = {'p':[],'c':[]}
          terms[termParent]['c'].append(termID)
    else:
      break
  return terms
def __init__(self):
  print "Inicializado"