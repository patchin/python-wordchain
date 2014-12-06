word_graph = {}

def build_node(word):
    word_graph[word] = []
    for word2 in word_list:
        if neighbour(word, word2):
            word_graph[word].append(word2)

def neighbour(word1, word2):
    if len(word1) != len(word2):
        return False
    diffcount = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diffcount += 1
            if diffcount > 1:
                return False
    return True

#print(neighbour("hate", "hite"))
#print(neighbour("hate", "hitf"))

file = open("input.txt", 'r')

word_list = []
for line in file:
    for word in line.split():
        word_list.append(word)
file.close()

for word in word_list:
    build_node(word)

# write word graph to file
outfile = open("word_graph.txt", 'w')
outfile.write(str(word_graph))
#for node in word_graph:
#    outfile.write(str(node))
outfile.close()

print "Done generating word_graph."
