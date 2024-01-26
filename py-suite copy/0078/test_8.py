
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
    assert solution.Solution().subsets([42, 61, 57, 11, 48, 71]) == [[], [42], [42, 61], [42, 61, 57], [42, 61, 57, 11], [42, 61, 57, 11, 48], [42, 61, 57, 11, 48, 71], [42, 61, 57, 11, 71], [42, 61, 57, 48], [42, 61, 57, 48, 71], [42, 61, 57, 71], [42, 61, 11], [42, 61, 11, 48], [42, 61, 11, 48, 71], [42, 61, 11, 71], [42, 61, 48], [42, 61, 48, 71], [42, 61, 71], [42, 57], [42, 57, 11], [42, 57, 11, 48], [42, 57, 11, 48, 71], [42, 57, 11, 71], [42, 57, 48], [42, 57, 48, 71], [42, 57, 71], [42, 11], [42, 11, 48], [42, 11, 48, 71], [42, 11, 71], [42, 48], [42, 48, 71], [42, 71], [61], [61, 57], [61, 57, 11], [61, 57, 11, 48], [61, 57, 11, 48, 71], [61, 57, 11, 71], [61, 57, 48], [61, 57, 48, 71], [61, 57, 71], [61, 11], [61, 11, 48], [61, 11, 48, 71], [61, 11, 71], [61, 48], [61, 48, 71], [61, 71], [57], [57, 11], [57, 11, 48], [57, 11, 48, 71], [57, 11, 71], [57, 48], [57, 48, 71], [57, 71], [11], [11, 48], [11, 48, 71], [11, 71], [48], [48, 71], [71]]
