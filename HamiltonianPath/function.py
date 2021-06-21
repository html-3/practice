def HamiltonianPath(string):
  
  rawList = list(string)

  # string of the vertices or nodes
  vList = rawList[0]
  
  # string of the edges or conections
  cList = rawList[1]
  
  # string of the order in which the vertices are reached
  oList = rawList[2]

  # list of the path in the graph
  pList = oList[1]
  
  # i is the current step of the path order
  for i in range(3,len(oList),2):
    # step to compare with edges
    step = f"{oList[i-2]}-{oList[i]}"
    invstep = f"{oList[i]}-{oList[i-2]}"

    # must be a valid edge from the 
    if cList.find(step) == -1 and cList.find(invstep) == -1:
      return oList[i-2]

    # must not be crossed twice
    elif not pList.find(step[-1]):
      return oList[i]

    # add the current step to the path already taken
    else:
      pList = pList+step[-1]

  return "yes"

