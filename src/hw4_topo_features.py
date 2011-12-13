from networkx import *
import math

def meta_paths(graph, source, meta):
	
	tmp_nodes=[{},{},{},{},{}]
	count = 0
	count_1 = 0
	
	for i in graph.neighbors(source):
		if tmp_nodes[1].keys().count(i)==0:
			tmp_nodes[1][i]=1
	for i in tmp_nodes[1].keys():
		for j in graph.neighbors(i):
			if ((meta==1 and j[0]=='a') or (meta==2 and j[0]=='c')) and j!=source:
				if tmp_nodes[2].keys().count(j)==0:
					tmp_nodes[2][j]=1
				else:
					tmp_nodes[2][j]+=1
	for i in tmp_nodes[2].keys():
		for j in graph.neighbors(i):
			if tmp_nodes[3].keys().count(j)==0:
				tmp_nodes[3][j]=tmp_nodes[2][i]
			else:
				tmp_nodes[3][j]+=tmp_nodes[2][i]
	for i in tmp_nodes[3].keys():
		for j in graph.neighbors(i):
			if (meta==1 and j[0]=='a') or (meta==2 and j[0]=='c'):
				if tmp_nodes[4].keys().count(j)==0:
					tmp_nodes[4][j]=tmp_nodes[3][i]
					count+=tmp_nodes[3][i]
				else:
					tmp_nodes[4][j]+=tmp_nodes[3][i]
					count+=tmp_nodes[3][i]

	for i in tmp_nodes[2].keys():
		count-=(tmp_nodes[2][i])*(tmp_nodes[2][i])
		count_1+=(tmp_nodes[2][i])
	tmp_nodes[0]['score1']=count
	tmp_nodes[0]['score2'] = count_1
	return tmp_nodes


def pc(graph, source_nodes, target_nodes, source, target, meta):
	paths = 0
	st_pc = 0
	ts_pc = 0
	if meta ==1:
		if source_nodes[2].keys().count(target)>0:
			paths = source_nodes[2][target]
		st_pc = source_nodes[0]['score2']
		ts_pc = target_nodes[0]['score2']
	elif meta==2:
		if source_nodes[2].keys().count(target)==0 and source_nodes[4].keys().count(target)>0:
			paths = source_nodes[4][target]
		elif source_nodes[2].keys().count(target)>0 and source_nodes[4].keys().count(target)>0:
			paths = source_nodes[4][target]-source_nodes[2][target]*source_nodes[2][target]
		st_pc = source_nodes[0]['score1']
		ts_pc = target_nodes[0]['score1']
	elif meta==3:
		if source_nodes[2].keys().count(target)==0 and source_nodes[4].keys().count(target)>0:
			paths = source_nodes[4][target]
		elif source_nodes[2].keys().count(target)>0 and source_nodes[4].keys().count(target)>0:
			paths = source_nodes[4][target]-source_nodes[2][target]*source_nodes[2][target]
		st_pc = source_nodes[0]['score1']
		ts_pc = target_nodes[0]['score1']
	npc_p = 0
	rw_st_p = 0
	rw_ts_p = 0
	if st_pc >0:
		rw_st_p = paths/st_pc
	if ts_pc >0:
		rw_ts_p = paths/ts_pc
	if not(st_pc ==0 and ts_pc ==0):
		npc_p = paths*2/(st_pc+ts_pc)
	srw_p = rw_st_p+rw_ts_p
	return [paths, npc_p, rw_st_p, rw_ts_p, srw_p]


def structural_feature(graph, source, target, path_count):#, prop):

	feature = []
	neighbors_s = graph.neighbors(source)
	neighbors_t = graph.neighbors(target)
	common_neighbors = []
	union_neighbors = neighbors_s
	for i in neighbors_s:
		if neighbors_t.count(i)>0:
			common_neighbors.append(i)
	for i in neighbors_t:
		if union_neighbors.count(i)==0:
			union_neighbors.append(i)
	adamic = 0
	for i in common_neighbors:
		adamic+=1/math.log(len(graph.neighbors(i)))
	feature.append(len(neighbors_s)) # neighbors(source)
	feature.append(len(neighbors_t)) # neighbors(target)
	feature.append(len(common_neighbors)) #common neighbors(source, target)
	feature.append(len(common_neighbors)/len(union_neighbors)) #Jaccard measure
	feature.append(adamic) #adamic/adar measure
	feature.append(len(neighbors_s)*len(neighbors_t)) #preferential attachment
	#feature.append(max_flow(graph, source, target)) #max flow
	feature.append(path_count[0]+path_count[1])#+path_count[2]) # shortest path, l<=4
	feature.append(0.005*path_count[0]+0.005*0.005*(path_count[1]))#+path_count[2])) #Katz, l=4, beta=sqrt(0.05)
	#feature.append(prop) #propflow predictor

	return list(feature)

def propflow (graph, source, length):

	score = {}
	found = [source]
	new_search = [source]
	score[source]=1
	old_search = []
	for deg in range(length):
		old_search = new_search
		new_search = []
		while len(old_search)>0:
			v = old_search.pop()
			node_input = score[v]
			sum_output = graph.degree(v)
			flow = 0
			for i in graph.neighbors(v):
				flow = node_input/sum_output
				score[i] = flow
				if found.count(i)==0:
					found.append(i)
					new_search.append(i)
				
	return score

def cluster_fea(aList, tsList, ttList, source):
	
	count = 0
	for i in aList:
		for j in aList:
			if j!=i and ttList[tsList.index(i)].count(j)>0:
				count+=1
	score = (count/(len(aList)*(len(aList)-1)))
		
	return score

def temporal_feature(feature_1, feature_2):
	
	feature = []
	for i in range(len(feature_1)):
		feature.append(feature_2[i]-feature_1[i])
	return feature

