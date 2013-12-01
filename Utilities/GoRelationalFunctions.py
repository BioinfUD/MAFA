def getDescendents(terms, goid):
  recursiveArray = [goid]
  if terms.has_key(goid):
    children = terms[goid]['c']
    if len(children) > 0:
      for child in children:
        recursiveArray.extend(getDescendents(child))
  return set(recursiveArray)


#Get First Parent (GO Category)

def getAncestors(terms ,goid):
  recursiveArray = [goid]
  if terms.has_key(goid):
    parents = terms[goid]['p']
    if len(parents) > 0:
      for parent in parents:
        recursiveArray.extend(getAncestors(terms, parent))
  return set(recursiveArray)

def isParent(terms, parent, goid):
  if parent in getAncestors(terms, goid):
      return True
  else:
      return False