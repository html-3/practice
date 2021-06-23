## Prompt
#### Medium
---
Have the function `HamiltonianPath(stringInput)` take the `stringInput` which will be an array of length three containing `lists` within `str`. The first part of the array will be a list of nodes or vertices of the graph. The second part of the array will be the edges or conections between the vertices,  where each edge is bidirectional. Finally, the part of the array will be a set path of edges and your program will have to determine whether or not the set of vertices given forms a Hamiltonian path on the graph which means that every vertex in the graph is visited only once in the order given. 

For example: if `stringInput` is ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C,A,D,B)"] then the vertices (C,A,D,B) in this order do in fact form a Hamiltonian path on the graph so your program should return the string yes. If for example the last part of the array was (D,A,B,C) then this doesn't form a Hamiltonian path because once you get to B you can't get to C in the graph without passing through the visited vertices again. Here your program should return the vertex where the path had to terminate, in this case your program should return B. 

The graph will have at least 2 vertices and all the vertices in the graph will be connected.
The function should return `yes` if the set path is possible and Hamiltonian, else it should return the last valid node of the set path.

## Analyze the problem

## Algorith design