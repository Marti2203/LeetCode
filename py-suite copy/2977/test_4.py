
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


def test_4():
    assert solution.Solution()._getSubToId('dd3Ntq69gw', 'xTzRk73Tbl') == {'d': 0, '3': 1, 'N': 2, 't': 3, 'q': 4, '6': 5, '9': 6, 'g': 7, 'w': 8, 'x': 9, 'T': 10, 'z': 11, 'R': 12, 'k': 13, '7': 14, 'b': 15, 'l': 16}
