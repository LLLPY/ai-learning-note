# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/8/26 15:04  
from collections import deque

# what is depth first search ?
# It's a way that you burrow ahead in a single minded way.(一路向前)

'''
 Q: how can i find a way from S to G with dfs ? 
  
            C --- E
            |
            |
       ---- B
      |     |
      |     |
      S --- A --- D --- G
 
 A:
    1. initialize a Queue
        put the S on the Queue
    2. extend first path on the Queue and check to see if that first path is a winner
        2.1 take the first path off and extend it(and check,if win then over,or continue...)
        2.2 put the new paths on front of the Queue
            Q: why should i put the new path on the front of the Queue?
            A: because i want to keep going down in the step that i just generated,i have to put
               it on the first so that i can deal with it first.(i think that is the core of dfs:
               find the new way and deal with it at the first time)  
               
 Process of dfs with a Queue:
    1.initialize a Queue and put the S on the Queue.
    Q = () 
    (S)    2.put S on the Queue
                     3.take off the S     check
    (S-A),(S-B)      4.put (S-A),(S-B) on the front
                     5.take off the (S-A) check 
    (S-A-B),(S-A-D),(S-B)  6.put (S-A-B),(S-A-D) on the first,and (S-B) is still there
                     7.take off the (S-A-B) check
    (S-A-B-C),(S-A-D),(S-B) 8.put (S-A-B-C) on the first
    ......
'''

def find_path_in_dfs(start, target, graph):
    # 1.define the Q
    queue = deque()
    if target not in graph:
        return
    queue.append([start])

    while queue:
        # 1.take off the first path
        cur_path = queue.popleft()
        end = cur_path[-1]
        # check if we get to the target
        if end == target:
            return cur_path

        # 2.find the new paths we can get to and extend
        neighbor_nodes = graph[end]
        for new_node in neighbor_nodes:
            if new_node not in cur_path:
                new_path = list(cur_path)
                new_path.append(new_node)

                # 3.put on the new path
                queue.appendleft(new_path)


if __name__ == '__main__':
    # 邻接表法来表示
    graph = {
        'A': {'B', 'D', 'S'},
        'B': {'A', 'C', 'S'},
        'C': {'B', 'E'},
        'D': {'A', 'G'},
        'E': {'C'},
        'G': {'D'},
        'S': {'A', 'B'},
        'W':{}
    }

    start = 'S'
    target = 'W'

    path = find_path_in_dfs(start, target, graph)
    print(f'the way S to G is :{path}')
