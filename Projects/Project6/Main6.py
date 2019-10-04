#!/usr/bin/python3

from Graph import Graph


def read_graph(filename):
    with open(filename, 'r') as reader:
        g = Graph(int(reader.readline()))
        for line in reader:
            (u, v, w) = line.split()
            g.insert_edge(int(u), int(v), float(w))
        return g


def main(filename):
    g = read_graph(filename)
    s = int(input('Source vertex?'))
    d = int(input('Dest vertex?'))
    print('Degree(s):', g.degree(s))
    print('Degree(d):', g.degree(d))
    if g.does_path_exist(s, d):
        p = g.find_min_weight_path(s, d)
        print('Path with', len(p) - 1, 'edges exists')
        print(p)
        if g.is_path_valid(p):
            print('Path weight:', g.path_weight(p))
        else:
            print('But your path is no good!')
    else:
        print('No path exists')


if __name__ == '__main__':
    main('g1.txt')
