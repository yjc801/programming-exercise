from collections import defaultdict

def creat_graph(edges): # unweighted, undirected
	graph = defaultdict(list)
	for edge in edges:
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])
	return graph

def dfs(graph,v,path=[]):
	path.append(v)
	for item in graph[v]:
		if item not in path:
			path = dfs(graph,item,path)
	return path

if __name__ == '__main__':
	graph = creat_graph([[1,2],[1,3],[2,4],[2,5],[3,6],[4,7],[3,8],[7,9]])
	print graph
	print dfs(graph,1)
	