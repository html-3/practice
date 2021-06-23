from function import HamiltonianPath

# hypothetical list to test the function.
testset = [
            ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C,A,D,B)"],
            ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(D,A,B,C)"],
            ["(A,B,C)","(B-A,C-B)","(C,B,A)"],
            ["(X,Y,Z,Q)","(X-Y,Y-Q,Y-Z)","(Z,Y,Q,X)"],
            ["(X,Y,Z,Q)","(X-Y,Y-Q,Y-Z,X-Q)","(Z,Y,Q,X)"],
            ["(X,Y,Z,Q)","(X-Y,Y-Q,Y-Z,X-Q)","(Q,Y,Z,X)"],
            ["(X,Y,Z,Q)","(X-Y,Y-Q,Y-Z,X-Q)","(Q,X,Y,Z)"],
            ["(A,B,C,D,E,F)","(A-B,A-D,B-D,B-C,C-F,E-D)","(F,C,B,A,D,E)"],
            ["(A,B,C,D,E,F)","(A-B,A-D,B-D,B-C,C-F,E-D)","(E,F,C,B,D,A)"],
            ["(A,B,C,D,E,F,G)","(A-B,A-D,B-D,B-C,C-F,E-D,F-E,G-F)","(G,F,E,D,B,C,A)"]
          ]

          # Correct outputs
          # yes
          # B  
          # yes
          # Q  
          # yes
          # Z  
          # yes
          # yes
          # E  
          # C  

# testing every string in the list
for i in testset:
    print(HamiltonianPath(i))