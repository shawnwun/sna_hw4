import sys
import os
import networkx as nx
import operator

fturn = file(sys.argv[1],'r')
fname = file(sys.argv[2],'r')
fout = file(sys.argv[3],'w')

myprdt = {}
while True:
    name = fname.readline()
    if name=='':
	break

    prdt = float(fturn.readline())
    myprdt[name] = prdt

count = 0
for n in sorted(myprdt.iteritems(),key=operator.itemgetter(1),reverse=True):
    count +=1
    print  count, n[0], n[1]
    if count<=25000 and n[1]>=0:
	fout.write(n[0])


