
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


def test_10():
    assert solution.Solution().permuteUnique([33, 25, 76, 53]) == [[25, 33, 53, 76], [25, 33, 76, 53], [25, 53, 33, 76], [25, 53, 76, 33], [25, 76, 33, 53], [25, 76, 53, 33], [33, 25, 53, 76], [33, 25, 76, 53], [33, 53, 25, 76], [33, 53, 76, 25], [33, 76, 25, 53], [33, 76, 53, 25], [53, 25, 33, 76], [53, 25, 76, 33], [53, 33, 25, 76], [53, 33, 76, 25], [53, 76, 25, 33], [53, 76, 33, 25], [76, 25, 33, 53], [76, 25, 53, 33], [76, 33, 25, 53], [76, 33, 53, 25], [76, 53, 25, 33], [76, 53, 33, 25]]
