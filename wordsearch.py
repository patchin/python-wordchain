file = open("word_graph.txt", 'r')
word_graph = eval(file.read())
#print(word_graph)

def find_chain(startword, endword, maxlevel=5):
    if maxlevel == 0:
        return (False, [])
    if endword in word_graph[startword]:
        return (True, [startword,endword])
    else:
        for nextstep in word_graph[startword]:
            (success, path) = find_chain(nextstep, endword, maxlevel-1)
            if success:
                return (True, [startword] + path)
    return (False, [])

print(find_chain("HATE", "LOVE"))