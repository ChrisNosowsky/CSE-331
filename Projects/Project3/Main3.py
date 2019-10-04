from TreeSet import TreeSet


def natural_order(x, y):
    if x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 1


def case_insensitive_order(x, y):
    return natural_order(x.lower(), y.lower())


def main(filename):
    with open(filename, 'r') as reader:
        tree = TreeSet(case_insensitive_order)
        # tree = TreeSet(natural_order)
        for line in reader:
            line = line.strip()
            if line == 'clear':
                tree.clear()
            elif line.startswith('+'):
                tree.insert(line[1:])
            elif line.startswith('-'):
                tree.remove(line[1:])
            else:
                raise Exception('Bad input: {0}'.format(line))

        print(tree)
        print('length:', len(tree))
        print('first:', tree.first())
        print('last:', tree.last())


if __name__ == '__main__':
    main('phonetic.txt')

