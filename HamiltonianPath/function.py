def HamiltonianPath(stringInput):
  # parsing string
  rawList = list(stringInput)

  # string of the vertices or nodes
  nodesList = rawList[0]
  
  # string of the edges or conections
  conectionsList = rawList[1]
  
  # string of the order in which the vertices are reached
  orderList = rawList[2]

  # list of the path in the graph
  pathList = orderList[1]
  
  # i is the current step of the path order
  for i in range(3,len(orderList),2):
    # step to compare with edges
    step = f"{orderList[i-2]}-{orderList[i]}"
    invstep = f"{orderList[i]}-{orderList[i-2]}"

    # must be a valid edge from the 
    if conectionsList.find(step) == -1 and conectionsList.find(invstep) == -1:
      return orderList[i-2]

    # must not be crossed twice
    elif not pathList.find(step[-1]):
      return orderList[i]

    # add the current step to the path already taken
    else:
      pathList = pathList+step[-1]

  return "yes"

