from collections import defaultdict,deque

def creat_graph(edges): # unweighted, undirected
	graph = defaultdict(list)
	for edge in edges:
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])
	return graph

def bfs(graph,start):
	status = dict()
	q = deque()
	for key in graph.iterkeys():
		status[key] = False
	q.append(start)
	status[start] = True
	while q:
		parent = q.popleft()
		for vertice in graph[parent]:
			if not status[vertice]:
				q.append(vertice)
				status[vertice] = True

if __name__ == '__main__':
	graph = creat_graph([[1,2],[2,3],[2,4],[1,3],[3,5],[4,5]])
	print graph
	bfs(graph,1)