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
import numpy as np

def eulerian_cycle(adj_list):
    graph_dict= read_adj_list(adj_list)
    #graph_dict=defaultdict(list)
    #for i in range(len(nodes)):
       # graph_dict[nodes[i]]=edges[i]
    print(graph_dict)
    nodes=list(graph_dict.keys())
    start_node=nodes[0]
    current_node=start_node
    last_node=start_node
    #paths=[]
    cycle_path=deque(current_node)
    
    while bool(graph_dict) == True:
        #cycle_dict=graph_dict
        #print(graph_dict.values())
        #if last_node in graph_dict.keys():
        if (last_node in graph_dict.keys()) and (len(graph_dict[last_node])>1): 
            current_node=str(graph_dict[last_node][random.randint(0,len(graph_dict[last_node])-1)]).strip("'[]'")
            graph_dict[last_node].remove(current_node)
        elif (last_node in graph_dict.keys()) and (len(graph_dict[last_node])==1):
            current_node=str(graph_dict[last_node]).strip("'['']'")
            graph_dict.pop(last_node)
        elif (last_node in graph_dict.keys()) and (graph_dict[last_node] is None):
            graph_dict.pop(last_node)
            #assign new curren_node to a value shown in the edge list of the dictionary
        #else:
            
            
        print(current_node)
        cycle_path.append(current_node)
        last_node=current_node
        #print(cycle_path)
        #print(graph_dict)    
                
        if current_node not in graph_dict.keys():
            #if the graph dict has had current_node removed (-> no way to go further)
            #decide new starting point (index)
            #paths.append(cycle_path)
            new_index=random.randint(0,len(cycle_path)-1)
            if start_node in graph_dict.keys():
                graph_dict[start_node].append(cycle_path[cycle_path.index(start_node)+1])
                #if the start node is still available as transit point: add the edge to second node again
                #so that cycle when start point is changed can go that edge again
            elif start_node not in graph_dict.keys():
                graph_dict[start_node]=list(cycle_path[1])
            current_node= int(cycle_path[new_index])
            cycle_path.rotate(-current_node)
            start_node=cycle_path[0]
            current_node=cycle_path[-1]
            last_node=cycle_path[-2]
            print(cycle_path)
            
        #cycle_path.append(current_node)
        
    return cycle_path
            
        
    
def read_adj_list(adj_list):
    #nodes=[]
    #edges=[]
    nodes=[item.split(':')[0] for item in adj_list]
    #print(nodes)
    #nodes, edgelist=[node, edges for node, edges in adj_list.split(':')]
    
    edges=map(str.split,[item.split(':')[1] for item in adj_list])
    graph_dict=dict(zip(nodes,edges))
    #print(edges)
    return graph_dict

    #re.split(r'\s+',edge.split(':')

f = open("dataset_30187_2.txt", 'r').read().strip().split('\n')
#print(f)
print(" ".join(eulerian_cycle(f)))
