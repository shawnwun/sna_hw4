import sys
import os
import networkx as nx



fin = file(sys.argv[1],'r')
fturn = file(sys.argv[2],'r')
fname = file(sys.argv[3],'r')
fout = file(sys.argv[4],'w')

G = nx.Graph()
while True:
    line = fin.readline()
    if line=='':
	break
    pair = line.split('\n')[0].split()
    G.add_edge(pair[0],pair[1])

while True:
    line = fname.readline()
    if line=='':
	break
    pair = line.split('\n')[0].split()

    label = '-1'
    if pair[0] in G:
	neineis = []
	for nei in G.neighbors(pair[0]):
	    neineis.extend( G.neighbors(nei) )
    
	if pair[1] in neineis:
	    label = '1'

    feature = fturn.readline()
    fout.write(label+' '+feature)


