
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


def test_7():
    assert solution.Solution().countOfPairs(61, 31, 44) == [122, 126, 132, 138, 144, 150, 142, 130, 128, 126, 124, 122, 120, 118, 116, 114, 112, 110, 106, 100, 94, 88, 82, 76, 72, 70, 68, 66, 64, 62, 60, 56, 50, 44, 38, 32, 26, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
