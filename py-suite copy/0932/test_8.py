
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


def test_8():
    assert solution.Solution().beautifulArray(97) == [63, 95, 31, 47, 79, 15, 55, 87, 23, 39, 71, 7, 59, 91, 27, 43, 75, 11, 51, 83, 19, 35, 67, 3, 61, 93, 29, 45, 77, 13, 53, 85, 21, 37, 69, 5, 57, 89, 25, 41, 73, 9, 49, 81, 17, 97, 33, 65, 1, 62, 94, 30, 46, 78, 14, 54, 86, 22, 38, 70, 6, 58, 90, 26, 42, 74, 10, 50, 82, 18, 34, 66, 2, 60, 92, 28, 44, 76, 12, 52, 84, 20, 36, 68, 4, 56, 88, 24, 40, 72, 8, 48, 80, 16, 96, 32, 64]
