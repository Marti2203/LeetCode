
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
    assert solution.Solution().spiralMatrixIII(3, 59, 54, 97) == [[54, 97], [2, 45], [2, 46], [2, 47], [2, 48], [2, 49], [2, 50], [2, 51], [2, 52], [2, 53], [2, 54], [2, 55], [2, 56], [2, 57], [2, 58], [2, 44], [1, 44], [1, 45], [1, 46], [1, 47], [1, 48], [1, 49], [1, 50], [1, 51], [1, 52], [1, 53], [1, 54], [1, 55], [1, 56], [1, 57], [1, 58], [2, 43], [1, 43], [0, 43], [0, 44], [0, 45], [0, 46], [0, 47], [0, 48], [0, 49], [0, 50], [0, 51], [0, 52], [0, 53], [0, 54], [0, 55], [0, 56], [0, 57], [0, 58], [2, 42], [1, 42], [0, 42], [2, 41], [1, 41], [0, 41], [2, 40], [1, 40], [0, 40], [2, 39], [1, 39], [0, 39], [2, 38], [1, 38], [0, 38], [2, 37], [1, 37], [0, 37], [2, 36], [1, 36], [0, 36], [2, 35], [1, 35], [0, 35], [2, 34], [1, 34], [0, 34], [2, 33], [1, 33], [0, 33], [2, 32], [1, 32], [0, 32], [2, 31], [1, 31], [0, 31], [2, 30], [1, 30], [0, 30], [2, 29], [1, 29], [0, 29], [2, 28], [1, 28], [0, 28], [2, 27], [1, 27], [0, 27], [2, 26], [1, 26], [0, 26], [2, 25], [1, 25], [0, 25], [2, 24], [1, 24], [0, 24], [2, 23], [1, 23], [0, 23], [2, 22], [1, 22], [0, 22], [2, 21], [1, 21], [0, 21], [2, 20], [1, 20], [0, 20], [2, 19], [1, 19], [0, 19], [2, 18], [1, 18], [0, 18], [2, 17], [1, 17], [0, 17], [2, 16], [1, 16], [0, 16], [2, 15], [1, 15], [0, 15], [2, 14], [1, 14], [0, 14], [2, 13], [1, 13], [0, 13], [2, 12], [1, 12], [0, 12], [2, 11], [1, 11], [0, 11], [2, 10], [1, 10], [0, 10], [2, 9], [1, 9], [0, 9], [2, 8], [1, 8], [0, 8], [2, 7], [1, 7], [0, 7], [2, 6], [1, 6], [0, 6], [2, 5], [1, 5], [0, 5], [2, 4], [1, 4], [0, 4], [2, 3], [1, 3], [0, 3], [2, 2], [1, 2], [0, 2], [2, 1], [1, 1], [0, 1], [2, 0], [1, 0], [0, 0]]