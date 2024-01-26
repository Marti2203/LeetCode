
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


def test_0():
    assert solution.Solution().subsetsWithDup([36, 23, 44, 22, 77]) == [[], [22], [22, 23], [22, 23, 36], [22, 23, 36, 44], [22, 23, 36, 44, 77], [22, 23, 36, 77], [22, 23, 44], [22, 23, 44, 77], [22, 23, 77], [22, 36], [22, 36, 44], [22, 36, 44, 77], [22, 36, 77], [22, 44], [22, 44, 77], [22, 77], [23], [23, 36], [23, 36, 44], [23, 36, 44, 77], [23, 36, 77], [23, 44], [23, 44, 77], [23, 77], [36], [36, 44], [36, 44, 77], [36, 77], [44], [44, 77], [77]]
