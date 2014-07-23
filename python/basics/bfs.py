from collections import defaultdict,deque

def creat_graph(edges): # unweighted, undirected
	graph = defaultdict(list)
	for edge in edges:
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])
	return graph

def bfs(graph,start):
	status = dict()
	parents = {start:-1}
	q = deque()
	for key in graph.iterkeys():
		status[key] = False
	q.append(start)
	status[start] = True
	while q:
		parent = q.popleft()
		print "Processed vertex %d" % (parent)
		for vertice in graph[parent]:
			print "Processed edge %d -> %d" % (parent, vertice)
			if not status[vertice]:
				q.append(vertice)
				status[vertice] = True
				parents[vertice] = parent
	return parents

def find_path(start,end,parents):
	if (start == end) or (end == -1):
		print start
	else:
		find_path(start,parents[end],parents)
		print end

if __name__ == '__main__':
	graph = creat_graph([[1,2],[1,5],[1,6],[2,3],[2,5],[3,4],[5,4]])
	print graph
	parents = bfs(graph,1)
	find_path(1,4,parents)