import sys
import os 
import networkx

fturn = file(sys.argv[1],'r')
fout = file(sys.argv[2],'w')

while True:
    feature = fturn.readline()
    if feature=='':
	break
    tokens = feature.split()
    if tokens[0]=='0':
	tokens[0]='-1'
	
    fout.write(' '.join(tokens)+'\n')







