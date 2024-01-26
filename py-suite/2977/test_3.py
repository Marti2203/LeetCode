
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


def test_3():
    assert solution.Solution()._getSubToId('FNG5lrBf4Z', 'a9nF5RQl8L') == {'F': 0, 'N': 1, 'G': 2, '5': 3, 'l': 4, 'r': 5, 'B': 6, 'f': 7, '4': 8, 'Z': 9, 'a': 10, '9': 11, 'n': 12, 'R': 13, 'Q': 14, '8': 15, 'L': 16}
