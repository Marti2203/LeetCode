
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


def test_17():
    assert solution.Solution()._getSubToId('8wd1TmoPTr', 'vK5vwxafy5') == {'8': 0, 'w': 1, 'd': 2, '1': 3, 'T': 4, 'm': 5, 'o': 6, 'P': 7, 'r': 8, 'v': 9, 'K': 10, '5': 11, 'x': 12, 'a': 13, 'f': 14, 'y': 15}
