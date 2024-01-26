
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


def test_19():
    assert solution.Solution()._getSubToId('RBQeqHmtwE', 'YmuTHDR1Dg') == {'R': 0, 'B': 1, 'Q': 2, 'e': 3, 'q': 4, 'H': 5, 'm': 6, 't': 7, 'w': 8, 'E': 9, 'Y': 10, 'u': 11, 'T': 12, 'D': 13, '1': 14, 'g': 15}
