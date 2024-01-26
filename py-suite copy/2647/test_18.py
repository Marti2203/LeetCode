
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


def test_18():
    assert solution.Solution().colorRed(13) == [[1, 1], [2, 1], [3, 3], [3, 5], [4, 2], [5, 1], [5, 3], [5, 5], [5, 7], [5, 9], [6, 1], [7, 3], [7, 5], [7, 7], [7, 9], [7, 11], [7, 13], [8, 2], [9, 1], [9, 3], [9, 5], [9, 7], [9, 9], [9, 11], [9, 13], [9, 15], [9, 17], [10, 1], [11, 3], [11, 5], [11, 7], [11, 9], [11, 11], [11, 13], [11, 15], [11, 17], [11, 19], [11, 21], [12, 2], [13, 1], [13, 3], [13, 5], [13, 7], [13, 9], [13, 11], [13, 13], [13, 15], [13, 17], [13, 19], [13, 21], [13, 23], [13, 25]]
