
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


def test_16():
    assert solution.Solution()._getSubToId('t5ZK7mXeQB', '2409CpgZKD') == {'t': 0, '5': 1, 'Z': 2, 'K': 3, '7': 4, 'm': 5, 'X': 6, 'e': 7, 'Q': 8, 'B': 9, '2': 10, '4': 11, '0': 12, '9': 13, 'C': 14, 'p': 15, 'g': 16, 'D': 17}
