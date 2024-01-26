
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
    assert solution.Solution().minReverseOperations(64, 35, [40, 22, 54, 15], 4) == [13, 12, 11, 12, 11, 10, 11, 10, 9, 10, 9, 8, 9, 8, 7, -1, 7, 6, 7, 6, 5, 6, -1, 4, 5, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 1, 2, -1, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, -1, 8, 7, 8, 9, 8, 9, 10, 9, 10]
