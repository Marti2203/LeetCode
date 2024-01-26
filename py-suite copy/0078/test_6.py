
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
    assert solution.Solution().subsets([3, 61, 82, 32, 71]) == [[], [3], [3, 61], [3, 61, 82], [3, 61, 82, 32], [3, 61, 82, 32, 71], [3, 61, 82, 71], [3, 61, 32], [3, 61, 32, 71], [3, 61, 71], [3, 82], [3, 82, 32], [3, 82, 32, 71], [3, 82, 71], [3, 32], [3, 32, 71], [3, 71], [61], [61, 82], [61, 82, 32], [61, 82, 32, 71], [61, 82, 71], [61, 32], [61, 32, 71], [61, 71], [82], [82, 32], [82, 32, 71], [82, 71], [32], [32, 71], [71]]
