
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


def test_6():
    assert solution.Solution()._getSubToId('qjGsf52rDj', 'IJpScsyBpA') == {'q': 0, 'j': 1, 'G': 2, 's': 3, 'f': 4, '5': 5, '2': 6, 'r': 7, 'D': 8, 'I': 9, 'J': 10, 'p': 11, 'S': 12, 'c': 13, 'y': 14, 'B': 15, 'A': 16}
