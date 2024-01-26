
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


def test_1():
    assert solution.Solution().subsets([21, 83, 32, 40, 30, 71]) == [[], [21], [21, 83], [21, 83, 32], [21, 83, 32, 40], [21, 83, 32, 40, 30], [21, 83, 32, 40, 30, 71], [21, 83, 32, 40, 71], [21, 83, 32, 30], [21, 83, 32, 30, 71], [21, 83, 32, 71], [21, 83, 40], [21, 83, 40, 30], [21, 83, 40, 30, 71], [21, 83, 40, 71], [21, 83, 30], [21, 83, 30, 71], [21, 83, 71], [21, 32], [21, 32, 40], [21, 32, 40, 30], [21, 32, 40, 30, 71], [21, 32, 40, 71], [21, 32, 30], [21, 32, 30, 71], [21, 32, 71], [21, 40], [21, 40, 30], [21, 40, 30, 71], [21, 40, 71], [21, 30], [21, 30, 71], [21, 71], [83], [83, 32], [83, 32, 40], [83, 32, 40, 30], [83, 32, 40, 30, 71], [83, 32, 40, 71], [83, 32, 30], [83, 32, 30, 71], [83, 32, 71], [83, 40], [83, 40, 30], [83, 40, 30, 71], [83, 40, 71], [83, 30], [83, 30, 71], [83, 71], [32], [32, 40], [32, 40, 30], [32, 40, 30, 71], [32, 40, 71], [32, 30], [32, 30, 71], [32, 71], [40], [40, 30], [40, 30, 71], [40, 71], [30], [30, 71], [71]]
