
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
    assert solution.Solution().countOfPairs(94, 39, 83) == [188, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 252, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 186, 180, 174, 168, 162, 156, 150, 144, 138, 132, 126, 120, 118, 116, 114, 112, 110, 106, 100, 94, 88, 82, 76, 70, 64, 58, 52, 46, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
