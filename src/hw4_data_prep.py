from networkx import *
import sys

def main():
	graph_data = sys.argv[1]
	output_path = sys.argv[2]
	years = []#[0]
	for i in range(2000, 2008):
		years.append(i)
	data = read_data(graph_data, years)
	'''
	print len(data[0])
	print len(data[0][0:100])
	print data[0][0:100]
	graph = parse_edgelist(data[0][0:100])
	print len(graph.nodes())
	print graph.nodes()
	print len(graph.edges())
	print graph.edges()
	'''

	for i in range(len(years)-1):
		graph = parse_edgelist(data[i])
		print len(graph.nodes())
		file_path = output_path
		if years[i]!=0:
			file_path = file_path+'.period'+str(years[i])+'_'+str(years[i+1])
		write_edgelist(graph, file_path, data=False)

def write_data(edge_list, path):
	f = file(path, 'w')
	for i in range(len(edge_list)):
		f.write('%s %s\n' % (edge_list[i][0], edge_list[i][1]))
	f.close()

def read_data(path, year):
	data = []
	for i in range(len(year)-1):
		data.append([])
	f = file(path, 'r')
	line = f.readline()
	while(True):
		line = f.readline()
		if line == '':
			break
		index = year.index(int(line.split()[3]))
		tmp = ""
		for i in range(2):
			tmp= tmp+line.split()[i]+" "
		#data[0].append(tmp)
		if index<7:
			data[index].append(tmp)
		if index>0:
			data[index-1].append(tmp)			
	f.close()
	return data

if __name__ == '__main__':
	sys.exit(main())
