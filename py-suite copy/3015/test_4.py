
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
    assert solution.Solution().countOfPairs(85, 16, 44) == [170, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 194, 192, 188, 182, 176, 170, 164, 158, 152, 146, 140, 134, 128, 122, 116, 110, 108, 106, 104, 102, 100, 98, 96, 94, 92, 90, 88, 86, 82, 76, 70, 64, 58, 52, 46, 40, 34, 28, 22, 16, 10, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
