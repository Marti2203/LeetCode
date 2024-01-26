
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


def test_10():
    assert solution.Solution().minReverseOperations(86, 3, [15, 3, 95, 30, 78, 67], 5) == [-1, 1, -1, 0, -1, 1, -1, 1, -1, 2, -1, 2, -1, 3, -1, -1, -1, 4, -1, 5, -1, 5, -1, 6, -1, 6, -1, 7, -1, 7, -1, 8, -1, 8, -1, 9, -1, 9, -1, 10, -1, 10, -1, 11, -1, 11, -1, 12, -1, 12, -1, 13, -1, 13, -1, 14, -1, 14, -1, 15, -1, 15, -1, 16, -1, 16, -1, -1, -1, 17, -1, 18, -1, 18, -1, 19, -1, 19, -1, 20, -1, 20, -1, 21, -1, 21]
