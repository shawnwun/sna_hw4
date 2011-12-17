import sys
import os
import networkx as nx
import operator

fname = file(sys.argv[1],'r')
fout = file(sys.argv[2],'w')

argc = len(sys.argv)

myprdt = {}
pname = []

while True:
    name = fname.readline()
    if name=='':
	break
    pname.append(name)
    myprdt[name] = 0
fname.close()

for i in range(3,argc):
    fturn = file(sys.argv[i])
    for name in pname:
	prdt = float(fturn.readline())
	myprdt[name] += prdt
    fturn.close()

count = 0
for n in sorted(myprdt.iteritems(),key=operator.itemgetter(1),reverse=True):
    count +=1
    #print  count, n[0], n[1]
    if count<=25000 and n[1]>=0:
	fout.write(n[0])


