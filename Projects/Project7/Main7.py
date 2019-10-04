from Lis import *


def read_file(filename):
    with open(filename, 'r') as reader:
        return [word for line in reader for word in line.split()]


def main(file):
    seq = read_file(file)
    lis = find_lis(seq)
    print('length:', len(lis))
    print(lis)

    if not verify_subseq(seq, lis):
        print('Warning: Not a subsequence!')
    if not verify_increasing(lis):
        print('Warning: Sequence not increasing!')


if __name__ == '__main__':
    #main('e.txt', 'pi.txt')
    #main('midsummer.txt', 'muchado.txt')
    #print(find_lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
    main('e.txt')