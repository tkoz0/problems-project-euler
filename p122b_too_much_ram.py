import os,psutil

# similar to previous solution but represent the vertices as tree leaves
# a root to leaf path represents an exponent set

maxk = 200
m = [0]*(maxk+1)

class Node:
    def __init__(self,value,parent,children):
        self.value = value
        self.parent = parent
        self.children = children

root = Node(1,None,[]) # start with just exponent 1
layer_num = 0

# find all leaves and generate children
# root to leaf path represents an exponent set
def generate_next_layer(node):
    if node.children: # go to leaf nodes only
        for child in node.children:
            generate_next_layer(child)
    else: # generate larger exponents that can be made
        expset = []
        p = node
        while p: # collect the exponents in the set represented by this node
            expset.append(p.value)
            p = p.parent
        # use pairs to form a larger exponent
        for i in range(len(expset)):
            if expset[i] + expset[i] <= expset[0]: break # cant make larger
            for j in range(i,len(expset)):
                newexp = expset[i] + expset[j]
                if newexp <= expset[0]: break # cant make larger
                if newexp <= maxk:
                    node.children.append(Node(newexp,node,[]))
                    if m[newexp] == 0:
                        m[newexp] = len(expset)
                        #print('set m(%d)=%d'%(newexp,len(expset)))

while 0 in m[2:]: # loop until all values are generated
    layer_num += 1
    print(': generating layer %d'%layer_num)
    generate_next_layer(root)
    print(': done, memory = %dMiB'
        %(psutil.Process(os.getpid()).memory_info().rss>>20,))

print(sum(m))

