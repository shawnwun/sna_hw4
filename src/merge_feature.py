import sys
import os
import networkx as nx
import operator

flst = file(sys.argv[1],'r')
fout = file(sys.argv[2],'w')
merge_size = int(sys.argv[3])

files = []
while True:
    line = flst.readline()
    if line=='':
	break
    fs = line.split()
    fs[-1] = fs[-1].replace('\n','')
    files.append( tuple(fs) )
    print fs

nf_pairs = []

for i in range(len(files)-1,-1,-1):
    fture = file(files[i][0],'r')
    fname = file(files[i][1],'r')
    pair = []
    while True:
	name = fname.readline()
	if name=='':
	    break
	fe = fture.readline().replace('\n','')
	pair.append( [name,fe] )
    nf_pairs.append( pair )
    fname.close()
    fture.close()

merged_fe = {}
for i in range(0,len(nf_pairs)-merge_size+1,1):
    for l in nf_pairs[i]:
	fe = l[1].split()
	merged_fe[ (l[0],i) ]=fe
    for l in nf_pairs[i+1]:
	fe_tail = l[1].split()
	del fe_tail[0]
	if merged_fe.has_key( (l[0],i) ):
	    for j in range(len(fe_tail)):
		pair = fe_tail[j].split(':')
		pair[0] = str(36+j+1)
		fe_tail[j] = ':'.join(pair)
	    merged_fe[ (l[0],i) ].extend( fe_tail )
    print i

fo1 = file('feature/03+04+05.fe','w')
fo2 = file('feature/02+03+04.fe','w')
fo3 = file('feature/01+02+03.fe','w')
fo4 = file('feature/00+01+02.fe','w')

for key, fe in merged_fe.iteritems():
    fout.write(' '.join( fe )+'\n')
    if key[1]==0:
	fo1.write(' '.join( fe )+'\n')
    elif key[1]==1:
	fo2.write(' '.join( fe )+'\n')
    elif key[1]==2:
	fo3.write(' '.join( fe )+'\n')
    else:
	fo4.write(' '.join( fe )+'\n')






