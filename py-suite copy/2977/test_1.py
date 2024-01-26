
import solution

import random
import typing
from typing import *
import collections
from collections import *
import functools
from functools import *
import math
from math import *
import string
from string import *
import bisect
import heapq
from heapq import *
import itertools
from itertools import *
import re
from re import *
import operator
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if other is None:
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"


def test_1():
    assert solution.Solution()._getSubToId('U7wiOPOdJe', 'qAublbzUn2') == {'U': 0, '7': 1, 'w': 2, 'i': 3, 'O': 4, 'P': 5, 'd': 6, 'J': 7, 'e': 8, 'q': 9, 'A': 10, 'u': 11, 'b': 12, 'l': 13, 'z': 14, 'n': 15, '2': 16}
