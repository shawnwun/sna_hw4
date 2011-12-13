from networkx import *
import sys

def main():
	total_source = read_file('sna_hw4/data/hw4.graph.t1_complete_source')
	total_target = read_list_file('sna_hw4/data/hw4.graph.t1_complete_target')
	output = {}
	graph_path = 'sna_hw4/data/hw4.graph'
	graph = read_edgelist(graph_path)
	graph_list = []
	obs_list = []
	print total_target[0]
	for n in range(8):
		graph_list.append(read_edgelist(graph_path+'.year'+str(2000+n)))
	for n in range(44000, 66000): #len(total_source)):
		print n
		if len(graph.neighbors(total_source[n]))<5:
			count = 0
			for i in total_target[n]:
				if len(graph.neighbors(i))<5:
					if count ==0:
						output[total_source[n]] = []
						count+=1
					tmp = []
					for g in graph_list:
						check = 1
						if g.nodes().count(i)==0 or g.nodes().count(total_source[n])==0:
							tmp.append(0)
							continue
						for j in  g.neighbors(total_source[n]):
							if g.neighbors(i).count(j)>0:
								tmp.append(1)
								check = 0
								break
						if check == 1:
							tmp.append(0)
					obs_list.append(list(tmp))
					#if total_target[total_source.index(i)].count(total_target[n])>0:
					#	total_target[total_source.index(i)].remove(total_target[n])
	num=3
	write_file('sna_hw4/data/hw4.lpmodel'+str(num), obs_list)
	write_test('sna_hw4/data/hw4.lptest'+str(num), obs_list)

def write_file(path, data_fea):
	f = file(path, 'w')
	for i in range(len(data_fea)):
		f.write('%i ' % data_fea[i][7])
		for j in range(7):
			f.write('%i:%i ' % (j+1, data_fea[i][j]))
		f.write('\n')
	f.close()

def write_test(path, data_fea):
	f = file(path, 'w')
	for i in range(len(data_fea)):
		for j in range(1, 8):
			f.write('%i:%i ' % (j, data_fea[i][j]))
		f.write('\n')
	f.close()

def read_file(path):
	aList = []
	f = file(path, 'r')
	while True:
		r = f.readline()
		if r == '':
			break
		node = str(r.split()[0])
		aList.append(node)
	f.close()
	return aList

def read_list_file(path):
	mLists=[]
	f = file(path , 'r')
	while True:
		r = f.readline()
		if r =='':
			break
		tmp = []
		for i in r.split():
			tmp.append(i)
		mLists.append(tmp)
	f.close()
	return mLists

if __name__ == '__main__':
	sys.exit(main())
