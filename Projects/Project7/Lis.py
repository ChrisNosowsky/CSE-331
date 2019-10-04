"""
Project 7: Chris Nosowsky
Project finds the longest increasing subsequence by using the verification functions
which verify if the sequence is a subsequence and if the sequence is increasing
Adds all possible sequences to a list and removes clones and one's with same length
then finally determines the longest length
"""


def verify_subseq(seq, subseq):
    """
    Verifies if a subsequence of seq.
    :param seq: sequence
    :param subseq: subsequence
    """
    it = iter(seq)
    return all(c in it for c in subseq)  # checks the seq bc iterator yields items that was not yielded in previous iter


def verify_increasing(seq):
    """
    Verifies if the seq is in sorted, increasing order.
    :param seq: sequence
    """
    largest_so_far = -69696969  # had to do it to em. sets really low # for initial test
    largest_string_so_far = ""  # largest string. smallest for initial test
    if not seq:  # if the sequence is empty, return true
        return True
    for item in seq:
        if isinstance(item, str):  # type checking
            if largest_string_so_far < item:  # if item is greater, then continue bc its so far increasing
                largest_string_so_far = item
                continue
            else:
                return False
        if isinstance(seq, int) or isinstance(item, int):  # type checking
            if item > largest_so_far:
                largest_so_far = item  # same as above, just int testing
            else:
                return False
        else:  # for chars
            if ord(item) > largest_so_far:
                largest_so_far = ord(item)
            else:
                return False
    return True


def find_lis(seq):
    """
    Finds the longest increasing subsequence. Doesn't even run in the tests unless increasing and subseq return True
    :param seq: sequence
    """
    list_of_sequences = [[seq[0]]]
    for item in seq:
        if item > list_of_sequences[-1][-1]:  # item larger then all seq
            new_string = list(list_of_sequences[-1])
            new_string.append(item)
            list_of_sequences.append(new_string)
        elif item < list_of_sequences[0][0]:  # item is smaller then all seq
            list_of_sequences[0][0] = item
        else:  # item in the middle
            list_of_sequences = remove_duplicates(item, list_of_sequences)

    return list_of_sequences[-1]


def remove_duplicates(item, list_of_sequences):
    """
    Remove any duplicate items in the sequence
    :param item: item in the sequence
    :param list_of_sequences: list of sequences to see if the item is a duplicate.
    """
    for seq in list_of_sequences[::-1]:  # removes any clones or same length sequences
        if item > seq[-1]:
            new_string = list(seq)
            new_string.append(item)
            index = list_of_sequences.index(seq)
            list_of_sequences = remove_same_length(new_string, list_of_sequences)
            list_of_sequences.insert(index+1, new_string)
            break
    return list_of_sequences  # new list of updated possible sequences


def remove_same_length(listing, lol):
    """
    Remove same length sequences from our list of possible longest sequences
    :param listing: list to check length for
    :param lol: all sequence lengths
    """
    check = list(lol)
    for l in lol:
        if len(listing) == len(l):  # if the list we are checking is same as a length in the list of lengths, remove it
            check.remove(l)
    return check  # returns the new list of updated possible longest lengths
