
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


def test_5():
    assert solution.Solution()._getSubToId('CHN4zzR4FH', 'upLHSUKmpy') == {'C': 0, 'H': 1, 'N': 2, '4': 3, 'z': 4, 'R': 5, 'F': 6, 'u': 7, 'p': 8, 'L': 9, 'S': 10, 'U': 11, 'K': 12, 'm': 13, 'y': 14}
