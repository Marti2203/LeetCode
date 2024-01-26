
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
    assert solution.Solution().findSubsequences([1, 11, 14, 89]) == [[1, 11], [1, 11, 14], [1, 11, 14, 89], [1, 11, 89], [1, 14], [1, 14, 89], [1, 89], [11, 14], [11, 14, 89], [11, 89], [14, 89]]
