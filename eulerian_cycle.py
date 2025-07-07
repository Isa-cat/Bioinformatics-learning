"""
construction of an eulerian cycle
input: graph 
contains: ajacency list (format: node: node node node )
read from that into list of nodes and edges
regex to split at : and ' ' and \n ?
keeps track of unexplored edges: 
at start, add all edges to dictionary of edges (with key being the starting node)
define array of cycle
define starting position
while array isempty=False loop
go from one node to the next one

delete edge from 'unexplored' dict
and so on
if stuck:
define new start node, whose dict value is not null? smth like that
(=still has unused edges)
retrace cycle and add on from there

"""

from collections import defaultdict
import random
from collections import deque
import numpy as np
import re
from operator import methodcaller

def eulerian_cycle(adj_list):
    nodes,edges= read_adj_list(adj_list)
    graph_dict=defaultdict(list)
    for i in range(len(nodes)):
        graph_dict[nodes[i]]=edges[i]
    print(graph_dict)
    start_node=nodes[0]
    current_node=start_node
    last_node=start_node
    #paths=[]
    cycle_path=[start_node]
    while bool(graph_dict) == True:
        #cycle_dict=graph_dict
        print(graph_dict.values())
        if len(graph_dict[last_node])>1:
            current_node=graph_dict[last_node][random.randint(0,len(graph_dict[last_node])-1)]
        else:
            current_node=graph_dict[last_node]
        cycle_path.append(current_node)
        print(current_node)
    
        if graph_dict[last_node] is None:
            graph_dict.pop(last_node)
        if (graph_dict[last_node] is not None) and (current_node in graph_dict[last_node]):  
            graph_dict[last_node].remove(current_node)
        if current_node not in graph_dict.keys():
            #paths.append(cycle_path)
            index=random.randint(0,len(cycle_path))
            if start_node in graph_dict.keys():
                graph_dict[start_node]=graph_dict[start_node].append(cycle_path[cycle_path.index(start_node)+1])
            cycle_path=deque(cycle_path).rotate(-index)
        
    return cycle_path
            
        
    
def read_adj_list(adj_list):
    #nodes=[]
    #edges=[]
    nodes=[item.split(':')[0] for item in adj_list]
    #print(nodes)
    #nodes, edgelist=[node, edges for node, edges in adj_list.split(':')]
    edges=list(map(str.split,[item.split(':')[1] for item in adj_list]))
    
    #print(edges)
    return nodes,edges

    #re.split(r'\s+',edge.split(':')

f = open("adj_list.txt", 'r').read().strip().split('\n')
print(f)
print(eulerian_cycle(f))
