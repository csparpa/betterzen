#!/usr/bin/env python

"""
A revised version of the Zen of Python
"""

from os import linesep as newline
from random import randrange

_header ="""
The Zen of Python, by Tim Peters

"""

_aphorisms = [ "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!" ]

def _to_lines(list_of_strings):
    return newline.join(list_of_strings)

def zen():
    """
    Prints the original Zen of Python by Tim Peters
    """
    print _header + _to_lines(_aphorisms)

def numbered_zen():
    """
    Prints the Zen of Python, numbering each aphorism
    """
    print _header + \
      _to_lines(['%d. %s' % (n, apho) for n, apho in enumerate(_aphorisms, 1)])

def aphorism(index):
    """
    Prints the aphorism that you want
    
    :param index: the reference number of the aphorism
    :type index: int
    """
    print _aphorisms[index+1]

def apropos(list_of_terms):
    """
    Prints the aphorisms that include at least one of the provided keywords.
    String matchings are exact and key insensitive
    
    :param list_of_terms: a list of keywords
    :type list_of_terms: list
    """
    matching_aphorisms = set()
    for aphorism in _aphorisms:
        for term in list_of_terms:
            if term.lower() in aphorism.lower():
                matching_aphorisms.add(aphorism)
    if matching_aphorisms:
        print _to_lines(list(matching_aphorisms))

def random():
    """
    Prints a random aphorism
    """
    print _aphorisms[randrange(0,len(_aphorisms)-1)]

# May the Zen be with you...
zen()