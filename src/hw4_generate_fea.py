from networkx import *
import sys
import hw4_topo_features

def main():
	data_fea = []
	test_fea = []
	graph_path = sys.argv[1]
	model_path = sys.argv[2]
	s = read_file('sna_hw4/data/hw4.graph.t1_complete_source_hp')
	t = read_list_file('sna_hw4/data/hw4.graph.t1_complete_target_hp')
	total_source = read_file('sna_hw4/data/hw4.graph.t1_complete_source')
	total_target = read_file('sna_hw4/data/hw4.graph.t1_complete_target')
	
	for n in range(1):
		aNum=6
		n = aNum
		print graph_path+str(2000+aNum)
		#if n ==0:
		graph_1 = read_edgelist(graph_path+'year'+str(2000+n))
		#else:
		#	graph_1 = graph_2.copy()
		#graph = read_edgelist(graph_path+'year'+str(2000+aNum))
		graph = read_edgelist(graph_path+'period'+str(2000+n)+'_'+str(2000+n+1))
		graph_2 = read_edgelist(graph_path+'year'+str(2000+n+1))
		#graph_3 = read_edgelist(graph_path+'year'+str(2000+n+2))
		checked = []
		node_list_1 = {}
		node_list_2 = {}
		node_list_3 = {}
		prop = {}
		count = 0
		source = []
		target = []
		for i in s:
			#print i
			if graph.nodes().count(i)>0:	
				source.append(i)
				target.append(t[s.index(i)])
		print 'source %d' % len(source)
		for i in source:
			#print count
			count+=1
			node_list_1[i]= hw4_topo_features.meta_paths(graph, i, 1)
			if graph_1.nodes().count(i)>0:
				node_list_2[i]= hw4_topo_features.meta_paths(graph_1, i, 1)
			if graph_2.nodes().count(i)>0:
				node_list_3[i]= hw4_topo_features.meta_paths(graph_2, i, 1)
			#prop[i] = hw4_topo_features.propflow(graph, i, 4)
		print 'source %d' % len(source)
		for i in range(len(source)):
			print i
			for j in target[i]:
				if checked.count(j)>0 or graph.nodes().count(j)==0:
					continue
				else:
					#print j
					pc_1 = [0, 0, 0, 0, 0]
					pc_2 = [0, 0, 0, 0, 0]
					if node_list_1.keys().count(j)>0:
						pc_1 = hw4_topo_features.pc(graph, node_list_1[source[i]], node_list_1[j], source[i], j, 1)
						pc_2 = hw4_topo_features.pc(graph, node_list_1[source[i]], node_list_1[j], source[i], j, 2)
					#pc_3 = topo_features.pc(graph, node_list_2[source[i]], node_list_2[j], source[i], j, 3)
					#prop = topo_features.propflow(graph, source[i], 4)
					tmp = hw4_topo_features.structural_feature(graph, source[i], j, [pc_1[0], pc_2[0]])#, prop[source[i]][j])
					#clu = hw4_topo_features.cluster_fea(target[i], total_source, total_target, source[i])
					feature = []
					feature.extend(pc_1)
					feature.extend(pc_2)
					#feature.append(pc_3)
					feature.extend(tmp)
					
					feature_dif = []
					feature_1 = []
					feature_2 = []
					
					if graph_1.nodes().count(source[i])>0 and graph_1.nodes().count(j)>0:
						pc_11 = [0, 0, 0, 0, 0]
						pc_12 = [0, 0, 0, 0, 0]
						if node_list_2.keys().count(j)>0:
							pc_11 = hw4_topo_features.pc(graph_1, node_list_2[source[i]], node_list_2[j], source[i], j, 1)
							pc_12 = hw4_topo_features.pc(graph_1, node_list_2[source[i]], node_list_2[j], source[i], j, 2)
						tmp = hw4_topo_features.structural_feature(graph_1, source[i], j, [pc_1[0], pc_2[0]])
						feature_1.extend(pc_11)
						feature_1.extend(pc_12)
						feature_1.extend(tmp)
					else:
						for k in range(len(feature)):
							feature_1.append(0)
						if graph_1.nodes().count(source[i])>0:
							feature_1[10]=(graph_1.degree(source[i]))
						elif graph_1.nodes().count(j)>0:
							feature_1[11]=(graph_1.degree(j))
					if graph_2.nodes().count(source[i])>0 and graph_2.nodes().count(j)>0:
						pc_11 = [0, 0, 0, 0, 0]
						pc_12 = [0, 0, 0, 0, 0]
						if node_list_3.keys().count(j)>0:
							pc_11 = hw4_topo_features.pc(graph_2, node_list_3[source[i]], node_list_3[j], source[i], j, 1)
							pc_12 = hw4_topo_features.pc(graph_2, node_list_3[source[i]], node_list_3[j], source[i], j, 2)
						tmp = hw4_topo_features.structural_feature(graph_2, source[i], j, [pc_1[0], pc_2[0]])
						feature_2.extend(pc_11)
						feature_2.extend(pc_12)
						feature_2.extend(tmp)
					else:
						for k in range(len(feature)):
							feature_2.append(0)
						if graph_2.nodes().count(source[i])>0:
							feature_2[10]=(graph_2.degree(source[i]))
						elif graph_2.nodes().count(j)>0:
							feature_2[11]=(graph_2.degree(j))
					for k in range(len(feature_1)):
						feature_dif.append(feature_2[k]-feature_1[k])
					
					#feature.append(clu)
					final = []
					connect = 0
					connect_1 = 0
					if n <=6:
						#if graph_3.nodes().count(source[i])>0 and graph_3.nodes().count(j)>0:
						#	for k in graph_3.neighbors(source[i]):
						#		if graph_3.neighbors(j).count(k)>0:
						#			connect = 1
						#			break
						for k in graph.neighbors(source[i]):
							if graph.neighbors(j).count(k)>0:
								connect_1 = 1
								break
						#final.append(connect)
						final.append(connect_1)
						final.extend(feature)
						final.extend(feature_dif)
						data_fea.append(final)	
					else:
						final.extend(feature)
						final.extend(feature_dif)
						test_fea.append(final)
					
			checked.append(source[i])
	
		#write_model(data_fea, model_path+'.'+str(aNum))
		write_model(test_fea, model_path+'.test')

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

def write_model(data_fea, path):
	f = file(path, 'w')
	for i in  range(len(data_fea)):
		for j in range(len(data_fea[i])):
			#if j ==0:
			#	f.write('%i ' % data_fea[i][j])
			#else:
			f.write('%i:%d ' % (j+2, data_fea[i][j]))
		f.write('\n')

if __name__ == '__main__':
	sys.exit(main())
