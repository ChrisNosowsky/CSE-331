"""
Project 1: Chris Nosowsky
"""
class Person:
    """Person Class"""
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def __str__(self):
        return '{0} {1} <{2}>'.format(self.first, self.last, self.email)

    def __repr__(self):
        return '({0}, {1}, {2})'.format(self.first, self.last, self.email)

    def __eq__(self, other):
        return self.first == other.first and self.last == other.last and self.email == other.email
def order_first_name(a, b):
    """
    Orders two people by their first names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    t = 0
    for i in a.first:
        if t < len(b.first):
            if i < b.first[t]:
                return True
            if i > b.first[t]:
                return False
        t = t + 1
    if a == b:
        return False
    if order_last_name(a, b):
        return True
    return False
def order_last_name(a, b):
    """
    Orders two people by their last names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    t = 0
    for i in a.last:
        if t < len(b.last):
            if i < b.last[t]:
                return True
            if i > b.last[t]:
                return False
        t = t + 1
    if a == b:
        return False
    if order_first_name(a, b):
        return True
    return False

def is_alphabetized(roster, ordering):
    """
    Checks whether the roster of names is alphabetized in the given order
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: True if the roster is alphabetized and False otherwise
    """
    for i in range(len(roster) - 1):
        if roster[i] == roster[i + 1]:
            continue
        if ordering(roster[i], roster[i + 1]) != 1:
            return False
    return True
