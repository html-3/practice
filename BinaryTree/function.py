def BinaryTree(listInput):
  # (childNode, parentNode)
  # every child node is related to one parent,
  # every parent nodes can have at most two children,
  # and there is a parentNode who's a root

  
  # parsing the list of strings of pairs to
  # a list of strings of ids
  listNodes = []
  dictNodes = {}
  for i in listInput:
    listNodes += i[1:-1].split(',')

  
  length = len(listNodes)

  # parsing the list of strings of ids to
  # a dictionary of keys children ids and values parent ids
  j = 0
  while length > j:
    # defining parent and child nodes, they come in pairs, so...
    childNode = listNodes[j]
    parentNode = listNodes[j + 1]

    # one child node has two parents
    if dictNodes.get(childNode):
      return "false"

    dictNodes[childNode] = parentNode
    j += 2

  # list of parent nodes
  parentNodes = list(dictNodes.values())

  for k in parentNodes:
    # parent node with more than 2 children
    if parentNodes.count(k) > 2:
      return "false"
  
  return "true"