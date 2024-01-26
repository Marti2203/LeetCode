
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


def test_14():
    assert solution.Solution().subsets([83, 8, 79, 61, 100]) == [[], [83], [83, 8], [83, 8, 79], [83, 8, 79, 61], [83, 8, 79, 61, 100], [83, 8, 79, 100], [83, 8, 61], [83, 8, 61, 100], [83, 8, 100], [83, 79], [83, 79, 61], [83, 79, 61, 100], [83, 79, 100], [83, 61], [83, 61, 100], [83, 100], [8], [8, 79], [8, 79, 61], [8, 79, 61, 100], [8, 79, 100], [8, 61], [8, 61, 100], [8, 100], [79], [79, 61], [79, 61, 100], [79, 100], [61], [61, 100], [100]]
