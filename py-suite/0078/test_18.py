
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


def test_18():
    assert solution.Solution().subsets([19, 60, 56, 14, 27]) == [[], [19], [19, 60], [19, 60, 56], [19, 60, 56, 14], [19, 60, 56, 14, 27], [19, 60, 56, 27], [19, 60, 14], [19, 60, 14, 27], [19, 60, 27], [19, 56], [19, 56, 14], [19, 56, 14, 27], [19, 56, 27], [19, 14], [19, 14, 27], [19, 27], [60], [60, 56], [60, 56, 14], [60, 56, 14, 27], [60, 56, 27], [60, 14], [60, 14, 27], [60, 27], [56], [56, 14], [56, 14, 27], [56, 27], [14], [14, 27], [27]]
