import sys
from networkx import *

def main():
	graph_path = sys.argv[1]
	output_path = sys.argv[2]
	graph = read_edgelist(graph_path)
	nodes = graph.nodes()
	source = {}
	test = []
	for i in nodes:
		if i[0]=='a' and graph.degree(i)>=5:			
			if source.keys().count(i)==0:
				#source[i]=[]
#			for j in range(1, 3):
				tmp = hop_neighbors(graph, i)
				if len(tmp)>0:
					source[i]=[]
					for k in tmp:
						source[i].append(k)
			
	
	file_path = output_path + '.t1_complete_source_hp'
	write_nodes(source.keys(), file_path)
	file_path = output_path + '.t1_complete_target_hp'
	write_nodelists(source.values(), file_path)
	
def write_edgelist(nodes, aList, output):
	f = file(output, 'w')
	for i in range(len(nodes)):
		for j in aList[i]:
			f.write('%s %s\n' % (nodes[i], j))
	f.close()

def write_nodes(aList, output):
	f = file(output, 'w')
	for i in range(len(aList)):
		f.write('%s\n' % aList[i])
	f.close()

def write_nodelists(aList, output):
	f = file(output, 'w')
	for i in range(len(aList)):
		for j in range(len(aList[i])-1):
			f.write('%s ' % aList[i][j])
		f.write('%s\n' % aList[i][len(aList[i])-1])
	f.close()

def hop_neighbors(graph, node):
	node_list = []
	stack = []
	for i in graph.neighbors(node):
		for j in graph.neighbors(i):
			if j[0]=='a' and node!=j:
				if node_list.count(j)==0:
					node_list.append(j)
					stack.append(j)
			#elif j[0]=='c':
	'''			
	for i in stack:
		for j in graph.neighbors(i):
			for k in graph.neighbors(j):
				if k[0]=='a':
					if node_list.count(k)==0 and graph.degree(k)>=3:
						node_list.append(k)
	'''
	return node_list

if __name__ == "__main__":
	sys.exit(main())
