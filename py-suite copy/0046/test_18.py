
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
    assert solution.Solution().permute([81, 12, 55, 71, 4, 90]) == [[81, 12, 55, 71, 4, 90], [81, 12, 55, 71, 90, 4], [81, 12, 55, 4, 71, 90], [81, 12, 55, 4, 90, 71], [81, 12, 55, 90, 71, 4], [81, 12, 55, 90, 4, 71], [81, 12, 71, 55, 4, 90], [81, 12, 71, 55, 90, 4], [81, 12, 71, 4, 55, 90], [81, 12, 71, 4, 90, 55], [81, 12, 71, 90, 55, 4], [81, 12, 71, 90, 4, 55], [81, 12, 4, 55, 71, 90], [81, 12, 4, 55, 90, 71], [81, 12, 4, 71, 55, 90], [81, 12, 4, 71, 90, 55], [81, 12, 4, 90, 55, 71], [81, 12, 4, 90, 71, 55], [81, 12, 90, 55, 71, 4], [81, 12, 90, 55, 4, 71], [81, 12, 90, 71, 55, 4], [81, 12, 90, 71, 4, 55], [81, 12, 90, 4, 55, 71], [81, 12, 90, 4, 71, 55], [81, 55, 12, 71, 4, 90], [81, 55, 12, 71, 90, 4], [81, 55, 12, 4, 71, 90], [81, 55, 12, 4, 90, 71], [81, 55, 12, 90, 71, 4], [81, 55, 12, 90, 4, 71], [81, 55, 71, 12, 4, 90], [81, 55, 71, 12, 90, 4], [81, 55, 71, 4, 12, 90], [81, 55, 71, 4, 90, 12], [81, 55, 71, 90, 12, 4], [81, 55, 71, 90, 4, 12], [81, 55, 4, 12, 71, 90], [81, 55, 4, 12, 90, 71], [81, 55, 4, 71, 12, 90], [81, 55, 4, 71, 90, 12], [81, 55, 4, 90, 12, 71], [81, 55, 4, 90, 71, 12], [81, 55, 90, 12, 71, 4], [81, 55, 90, 12, 4, 71], [81, 55, 90, 71, 12, 4], [81, 55, 90, 71, 4, 12], [81, 55, 90, 4, 12, 71], [81, 55, 90, 4, 71, 12], [81, 71, 12, 55, 4, 90], [81, 71, 12, 55, 90, 4], [81, 71, 12, 4, 55, 90], [81, 71, 12, 4, 90, 55], [81, 71, 12, 90, 55, 4], [81, 71, 12, 90, 4, 55], [81, 71, 55, 12, 4, 90], [81, 71, 55, 12, 90, 4], [81, 71, 55, 4, 12, 90], [81, 71, 55, 4, 90, 12], [81, 71, 55, 90, 12, 4], [81, 71, 55, 90, 4, 12], [81, 71, 4, 12, 55, 90], [81, 71, 4, 12, 90, 55], [81, 71, 4, 55, 12, 90], [81, 71, 4, 55, 90, 12], [81, 71, 4, 90, 12, 55], [81, 71, 4, 90, 55, 12], [81, 71, 90, 12, 55, 4], [81, 71, 90, 12, 4, 55], [81, 71, 90, 55, 12, 4], [81, 71, 90, 55, 4, 12], [81, 71, 90, 4, 12, 55], [81, 71, 90, 4, 55, 12], [81, 4, 12, 55, 71, 90], [81, 4, 12, 55, 90, 71], [81, 4, 12, 71, 55, 90], [81, 4, 12, 71, 90, 55], [81, 4, 12, 90, 55, 71], [81, 4, 12, 90, 71, 55], [81, 4, 55, 12, 71, 90], [81, 4, 55, 12, 90, 71], [81, 4, 55, 71, 12, 90], [81, 4, 55, 71, 90, 12], [81, 4, 55, 90, 12, 71], [81, 4, 55, 90, 71, 12], [81, 4, 71, 12, 55, 90], [81, 4, 71, 12, 90, 55], [81, 4, 71, 55, 12, 90], [81, 4, 71, 55, 90, 12], [81, 4, 71, 90, 12, 55], [81, 4, 71, 90, 55, 12], [81, 4, 90, 12, 55, 71], [81, 4, 90, 12, 71, 55], [81, 4, 90, 55, 12, 71], [81, 4, 90, 55, 71, 12], [81, 4, 90, 71, 12, 55], [81, 4, 90, 71, 55, 12], [81, 90, 12, 55, 71, 4], [81, 90, 12, 55, 4, 71], [81, 90, 12, 71, 55, 4], [81, 90, 12, 71, 4, 55], [81, 90, 12, 4, 55, 71], [81, 90, 12, 4, 71, 55], [81, 90, 55, 12, 71, 4], [81, 90, 55, 12, 4, 71], [81, 90, 55, 71, 12, 4], [81, 90, 55, 71, 4, 12], [81, 90, 55, 4, 12, 71], [81, 90, 55, 4, 71, 12], [81, 90, 71, 12, 55, 4], [81, 90, 71, 12, 4, 55], [81, 90, 71, 55, 12, 4], [81, 90, 71, 55, 4, 12], [81, 90, 71, 4, 12, 55], [81, 90, 71, 4, 55, 12], [81, 90, 4, 12, 55, 71], [81, 90, 4, 12, 71, 55], [81, 90, 4, 55, 12, 71], [81, 90, 4, 55, 71, 12], [81, 90, 4, 71, 12, 55], [81, 90, 4, 71, 55, 12], [12, 81, 55, 71, 4, 90], [12, 81, 55, 71, 90, 4], [12, 81, 55, 4, 71, 90], [12, 81, 55, 4, 90, 71], [12, 81, 55, 90, 71, 4], [12, 81, 55, 90, 4, 71], [12, 81, 71, 55, 4, 90], [12, 81, 71, 55, 90, 4], [12, 81, 71, 4, 55, 90], [12, 81, 71, 4, 90, 55], [12, 81, 71, 90, 55, 4], [12, 81, 71, 90, 4, 55], [12, 81, 4, 55, 71, 90], [12, 81, 4, 55, 90, 71], [12, 81, 4, 71, 55, 90], [12, 81, 4, 71, 90, 55], [12, 81, 4, 90, 55, 71], [12, 81, 4, 90, 71, 55], [12, 81, 90, 55, 71, 4], [12, 81, 90, 55, 4, 71], [12, 81, 90, 71, 55, 4], [12, 81, 90, 71, 4, 55], [12, 81, 90, 4, 55, 71], [12, 81, 90, 4, 71, 55], [12, 55, 81, 71, 4, 90], [12, 55, 81, 71, 90, 4], [12, 55, 81, 4, 71, 90], [12, 55, 81, 4, 90, 71], [12, 55, 81, 90, 71, 4], [12, 55, 81, 90, 4, 71], [12, 55, 71, 81, 4, 90], [12, 55, 71, 81, 90, 4], [12, 55, 71, 4, 81, 90], [12, 55, 71, 4, 90, 81], [12, 55, 71, 90, 81, 4], [12, 55, 71, 90, 4, 81], [12, 55, 4, 81, 71, 90], [12, 55, 4, 81, 90, 71], [12, 55, 4, 71, 81, 90], [12, 55, 4, 71, 90, 81], [12, 55, 4, 90, 81, 71], [12, 55, 4, 90, 71, 81], [12, 55, 90, 81, 71, 4], [12, 55, 90, 81, 4, 71], [12, 55, 90, 71, 81, 4], [12, 55, 90, 71, 4, 81], [12, 55, 90, 4, 81, 71], [12, 55, 90, 4, 71, 81], [12, 71, 81, 55, 4, 90], [12, 71, 81, 55, 90, 4], [12, 71, 81, 4, 55, 90], [12, 71, 81, 4, 90, 55], [12, 71, 81, 90, 55, 4], [12, 71, 81, 90, 4, 55], [12, 71, 55, 81, 4, 90], [12, 71, 55, 81, 90, 4], [12, 71, 55, 4, 81, 90], [12, 71, 55, 4, 90, 81], [12, 71, 55, 90, 81, 4], [12, 71, 55, 90, 4, 81], [12, 71, 4, 81, 55, 90], [12, 71, 4, 81, 90, 55], [12, 71, 4, 55, 81, 90], [12, 71, 4, 55, 90, 81], [12, 71, 4, 90, 81, 55], [12, 71, 4, 90, 55, 81], [12, 71, 90, 81, 55, 4], [12, 71, 90, 81, 4, 55], [12, 71, 90, 55, 81, 4], [12, 71, 90, 55, 4, 81], [12, 71, 90, 4, 81, 55], [12, 71, 90, 4, 55, 81], [12, 4, 81, 55, 71, 90], [12, 4, 81, 55, 90, 71], [12, 4, 81, 71, 55, 90], [12, 4, 81, 71, 90, 55], [12, 4, 81, 90, 55, 71], [12, 4, 81, 90, 71, 55], [12, 4, 55, 81, 71, 90], [12, 4, 55, 81, 90, 71], [12, 4, 55, 71, 81, 90], [12, 4, 55, 71, 90, 81], [12, 4, 55, 90, 81, 71], [12, 4, 55, 90, 71, 81], [12, 4, 71, 81, 55, 90], [12, 4, 71, 81, 90, 55], [12, 4, 71, 55, 81, 90], [12, 4, 71, 55, 90, 81], [12, 4, 71, 90, 81, 55], [12, 4, 71, 90, 55, 81], [12, 4, 90, 81, 55, 71], [12, 4, 90, 81, 71, 55], [12, 4, 90, 55, 81, 71], [12, 4, 90, 55, 71, 81], [12, 4, 90, 71, 81, 55], [12, 4, 90, 71, 55, 81], [12, 90, 81, 55, 71, 4], [12, 90, 81, 55, 4, 71], [12, 90, 81, 71, 55, 4], [12, 90, 81, 71, 4, 55], [12, 90, 81, 4, 55, 71], [12, 90, 81, 4, 71, 55], [12, 90, 55, 81, 71, 4], [12, 90, 55, 81, 4, 71], [12, 90, 55, 71, 81, 4], [12, 90, 55, 71, 4, 81], [12, 90, 55, 4, 81, 71], [12, 90, 55, 4, 71, 81], [12, 90, 71, 81, 55, 4], [12, 90, 71, 81, 4, 55], [12, 90, 71, 55, 81, 4], [12, 90, 71, 55, 4, 81], [12, 90, 71, 4, 81, 55], [12, 90, 71, 4, 55, 81], [12, 90, 4, 81, 55, 71], [12, 90, 4, 81, 71, 55], [12, 90, 4, 55, 81, 71], [12, 90, 4, 55, 71, 81], [12, 90, 4, 71, 81, 55], [12, 90, 4, 71, 55, 81], [55, 81, 12, 71, 4, 90], [55, 81, 12, 71, 90, 4], [55, 81, 12, 4, 71, 90], [55, 81, 12, 4, 90, 71], [55, 81, 12, 90, 71, 4], [55, 81, 12, 90, 4, 71], [55, 81, 71, 12, 4, 90], [55, 81, 71, 12, 90, 4], [55, 81, 71, 4, 12, 90], [55, 81, 71, 4, 90, 12], [55, 81, 71, 90, 12, 4], [55, 81, 71, 90, 4, 12], [55, 81, 4, 12, 71, 90], [55, 81, 4, 12, 90, 71], [55, 81, 4, 71, 12, 90], [55, 81, 4, 71, 90, 12], [55, 81, 4, 90, 12, 71], [55, 81, 4, 90, 71, 12], [55, 81, 90, 12, 71, 4], [55, 81, 90, 12, 4, 71], [55, 81, 90, 71, 12, 4], [55, 81, 90, 71, 4, 12], [55, 81, 90, 4, 12, 71], [55, 81, 90, 4, 71, 12], [55, 12, 81, 71, 4, 90], [55, 12, 81, 71, 90, 4], [55, 12, 81, 4, 71, 90], [55, 12, 81, 4, 90, 71], [55, 12, 81, 90, 71, 4], [55, 12, 81, 90, 4, 71], [55, 12, 71, 81, 4, 90], [55, 12, 71, 81, 90, 4], [55, 12, 71, 4, 81, 90], [55, 12, 71, 4, 90, 81], [55, 12, 71, 90, 81, 4], [55, 12, 71, 90, 4, 81], [55, 12, 4, 81, 71, 90], [55, 12, 4, 81, 90, 71], [55, 12, 4, 71, 81, 90], [55, 12, 4, 71, 90, 81], [55, 12, 4, 90, 81, 71], [55, 12, 4, 90, 71, 81], [55, 12, 90, 81, 71, 4], [55, 12, 90, 81, 4, 71], [55, 12, 90, 71, 81, 4], [55, 12, 90, 71, 4, 81], [55, 12, 90, 4, 81, 71], [55, 12, 90, 4, 71, 81], [55, 71, 81, 12, 4, 90], [55, 71, 81, 12, 90, 4], [55, 71, 81, 4, 12, 90], [55, 71, 81, 4, 90, 12], [55, 71, 81, 90, 12, 4], [55, 71, 81, 90, 4, 12], [55, 71, 12, 81, 4, 90], [55, 71, 12, 81, 90, 4], [55, 71, 12, 4, 81, 90], [55, 71, 12, 4, 90, 81], [55, 71, 12, 90, 81, 4], [55, 71, 12, 90, 4, 81], [55, 71, 4, 81, 12, 90], [55, 71, 4, 81, 90, 12], [55, 71, 4, 12, 81, 90], [55, 71, 4, 12, 90, 81], [55, 71, 4, 90, 81, 12], [55, 71, 4, 90, 12, 81], [55, 71, 90, 81, 12, 4], [55, 71, 90, 81, 4, 12], [55, 71, 90, 12, 81, 4], [55, 71, 90, 12, 4, 81], [55, 71, 90, 4, 81, 12], [55, 71, 90, 4, 12, 81], [55, 4, 81, 12, 71, 90], [55, 4, 81, 12, 90, 71], [55, 4, 81, 71, 12, 90], [55, 4, 81, 71, 90, 12], [55, 4, 81, 90, 12, 71], [55, 4, 81, 90, 71, 12], [55, 4, 12, 81, 71, 90], [55, 4, 12, 81, 90, 71], [55, 4, 12, 71, 81, 90], [55, 4, 12, 71, 90, 81], [55, 4, 12, 90, 81, 71], [55, 4, 12, 90, 71, 81], [55, 4, 71, 81, 12, 90], [55, 4, 71, 81, 90, 12], [55, 4, 71, 12, 81, 90], [55, 4, 71, 12, 90, 81], [55, 4, 71, 90, 81, 12], [55, 4, 71, 90, 12, 81], [55, 4, 90, 81, 12, 71], [55, 4, 90, 81, 71, 12], [55, 4, 90, 12, 81, 71], [55, 4, 90, 12, 71, 81], [55, 4, 90, 71, 81, 12], [55, 4, 90, 71, 12, 81], [55, 90, 81, 12, 71, 4], [55, 90, 81, 12, 4, 71], [55, 90, 81, 71, 12, 4], [55, 90, 81, 71, 4, 12], [55, 90, 81, 4, 12, 71], [55, 90, 81, 4, 71, 12], [55, 90, 12, 81, 71, 4], [55, 90, 12, 81, 4, 71], [55, 90, 12, 71, 81, 4], [55, 90, 12, 71, 4, 81], [55, 90, 12, 4, 81, 71], [55, 90, 12, 4, 71, 81], [55, 90, 71, 81, 12, 4], [55, 90, 71, 81, 4, 12], [55, 90, 71, 12, 81, 4], [55, 90, 71, 12, 4, 81], [55, 90, 71, 4, 81, 12], [55, 90, 71, 4, 12, 81], [55, 90, 4, 81, 12, 71], [55, 90, 4, 81, 71, 12], [55, 90, 4, 12, 81, 71], [55, 90, 4, 12, 71, 81], [55, 90, 4, 71, 81, 12], [55, 90, 4, 71, 12, 81], [71, 81, 12, 55, 4, 90], [71, 81, 12, 55, 90, 4], [71, 81, 12, 4, 55, 90], [71, 81, 12, 4, 90, 55], [71, 81, 12, 90, 55, 4], [71, 81, 12, 90, 4, 55], [71, 81, 55, 12, 4, 90], [71, 81, 55, 12, 90, 4], [71, 81, 55, 4, 12, 90], [71, 81, 55, 4, 90, 12], [71, 81, 55, 90, 12, 4], [71, 81, 55, 90, 4, 12], [71, 81, 4, 12, 55, 90], [71, 81, 4, 12, 90, 55], [71, 81, 4, 55, 12, 90], [71, 81, 4, 55, 90, 12], [71, 81, 4, 90, 12, 55], [71, 81, 4, 90, 55, 12], [71, 81, 90, 12, 55, 4], [71, 81, 90, 12, 4, 55], [71, 81, 90, 55, 12, 4], [71, 81, 90, 55, 4, 12], [71, 81, 90, 4, 12, 55], [71, 81, 90, 4, 55, 12], [71, 12, 81, 55, 4, 90], [71, 12, 81, 55, 90, 4], [71, 12, 81, 4, 55, 90], [71, 12, 81, 4, 90, 55], [71, 12, 81, 90, 55, 4], [71, 12, 81, 90, 4, 55], [71, 12, 55, 81, 4, 90], [71, 12, 55, 81, 90, 4], [71, 12, 55, 4, 81, 90], [71, 12, 55, 4, 90, 81], [71, 12, 55, 90, 81, 4], [71, 12, 55, 90, 4, 81], [71, 12, 4, 81, 55, 90], [71, 12, 4, 81, 90, 55], [71, 12, 4, 55, 81, 90], [71, 12, 4, 55, 90, 81], [71, 12, 4, 90, 81, 55], [71, 12, 4, 90, 55, 81], [71, 12, 90, 81, 55, 4], [71, 12, 90, 81, 4, 55], [71, 12, 90, 55, 81, 4], [71, 12, 90, 55, 4, 81], [71, 12, 90, 4, 81, 55], [71, 12, 90, 4, 55, 81], [71, 55, 81, 12, 4, 90], [71, 55, 81, 12, 90, 4], [71, 55, 81, 4, 12, 90], [71, 55, 81, 4, 90, 12], [71, 55, 81, 90, 12, 4], [71, 55, 81, 90, 4, 12], [71, 55, 12, 81, 4, 90], [71, 55, 12, 81, 90, 4], [71, 55, 12, 4, 81, 90], [71, 55, 12, 4, 90, 81], [71, 55, 12, 90, 81, 4], [71, 55, 12, 90, 4, 81], [71, 55, 4, 81, 12, 90], [71, 55, 4, 81, 90, 12], [71, 55, 4, 12, 81, 90], [71, 55, 4, 12, 90, 81], [71, 55, 4, 90, 81, 12], [71, 55, 4, 90, 12, 81], [71, 55, 90, 81, 12, 4], [71, 55, 90, 81, 4, 12], [71, 55, 90, 12, 81, 4], [71, 55, 90, 12, 4, 81], [71, 55, 90, 4, 81, 12], [71, 55, 90, 4, 12, 81], [71, 4, 81, 12, 55, 90], [71, 4, 81, 12, 90, 55], [71, 4, 81, 55, 12, 90], [71, 4, 81, 55, 90, 12], [71, 4, 81, 90, 12, 55], [71, 4, 81, 90, 55, 12], [71, 4, 12, 81, 55, 90], [71, 4, 12, 81, 90, 55], [71, 4, 12, 55, 81, 90], [71, 4, 12, 55, 90, 81], [71, 4, 12, 90, 81, 55], [71, 4, 12, 90, 55, 81], [71, 4, 55, 81, 12, 90], [71, 4, 55, 81, 90, 12], [71, 4, 55, 12, 81, 90], [71, 4, 55, 12, 90, 81], [71, 4, 55, 90, 81, 12], [71, 4, 55, 90, 12, 81], [71, 4, 90, 81, 12, 55], [71, 4, 90, 81, 55, 12], [71, 4, 90, 12, 81, 55], [71, 4, 90, 12, 55, 81], [71, 4, 90, 55, 81, 12], [71, 4, 90, 55, 12, 81], [71, 90, 81, 12, 55, 4], [71, 90, 81, 12, 4, 55], [71, 90, 81, 55, 12, 4], [71, 90, 81, 55, 4, 12], [71, 90, 81, 4, 12, 55], [71, 90, 81, 4, 55, 12], [71, 90, 12, 81, 55, 4], [71, 90, 12, 81, 4, 55], [71, 90, 12, 55, 81, 4], [71, 90, 12, 55, 4, 81], [71, 90, 12, 4, 81, 55], [71, 90, 12, 4, 55, 81], [71, 90, 55, 81, 12, 4], [71, 90, 55, 81, 4, 12], [71, 90, 55, 12, 81, 4], [71, 90, 55, 12, 4, 81], [71, 90, 55, 4, 81, 12], [71, 90, 55, 4, 12, 81], [71, 90, 4, 81, 12, 55], [71, 90, 4, 81, 55, 12], [71, 90, 4, 12, 81, 55], [71, 90, 4, 12, 55, 81], [71, 90, 4, 55, 81, 12], [71, 90, 4, 55, 12, 81], [4, 81, 12, 55, 71, 90], [4, 81, 12, 55, 90, 71], [4, 81, 12, 71, 55, 90], [4, 81, 12, 71, 90, 55], [4, 81, 12, 90, 55, 71], [4, 81, 12, 90, 71, 55], [4, 81, 55, 12, 71, 90], [4, 81, 55, 12, 90, 71], [4, 81, 55, 71, 12, 90], [4, 81, 55, 71, 90, 12], [4, 81, 55, 90, 12, 71], [4, 81, 55, 90, 71, 12], [4, 81, 71, 12, 55, 90], [4, 81, 71, 12, 90, 55], [4, 81, 71, 55, 12, 90], [4, 81, 71, 55, 90, 12], [4, 81, 71, 90, 12, 55], [4, 81, 71, 90, 55, 12], [4, 81, 90, 12, 55, 71], [4, 81, 90, 12, 71, 55], [4, 81, 90, 55, 12, 71], [4, 81, 90, 55, 71, 12], [4, 81, 90, 71, 12, 55], [4, 81, 90, 71, 55, 12], [4, 12, 81, 55, 71, 90], [4, 12, 81, 55, 90, 71], [4, 12, 81, 71, 55, 90], [4, 12, 81, 71, 90, 55], [4, 12, 81, 90, 55, 71], [4, 12, 81, 90, 71, 55], [4, 12, 55, 81, 71, 90], [4, 12, 55, 81, 90, 71], [4, 12, 55, 71, 81, 90], [4, 12, 55, 71, 90, 81], [4, 12, 55, 90, 81, 71], [4, 12, 55, 90, 71, 81], [4, 12, 71, 81, 55, 90], [4, 12, 71, 81, 90, 55], [4, 12, 71, 55, 81, 90], [4, 12, 71, 55, 90, 81], [4, 12, 71, 90, 81, 55], [4, 12, 71, 90, 55, 81], [4, 12, 90, 81, 55, 71], [4, 12, 90, 81, 71, 55], [4, 12, 90, 55, 81, 71], [4, 12, 90, 55, 71, 81], [4, 12, 90, 71, 81, 55], [4, 12, 90, 71, 55, 81], [4, 55, 81, 12, 71, 90], [4, 55, 81, 12, 90, 71], [4, 55, 81, 71, 12, 90], [4, 55, 81, 71, 90, 12], [4, 55, 81, 90, 12, 71], [4, 55, 81, 90, 71, 12], [4, 55, 12, 81, 71, 90], [4, 55, 12, 81, 90, 71], [4, 55, 12, 71, 81, 90], [4, 55, 12, 71, 90, 81], [4, 55, 12, 90, 81, 71], [4, 55, 12, 90, 71, 81], [4, 55, 71, 81, 12, 90], [4, 55, 71, 81, 90, 12], [4, 55, 71, 12, 81, 90], [4, 55, 71, 12, 90, 81], [4, 55, 71, 90, 81, 12], [4, 55, 71, 90, 12, 81], [4, 55, 90, 81, 12, 71], [4, 55, 90, 81, 71, 12], [4, 55, 90, 12, 81, 71], [4, 55, 90, 12, 71, 81], [4, 55, 90, 71, 81, 12], [4, 55, 90, 71, 12, 81], [4, 71, 81, 12, 55, 90], [4, 71, 81, 12, 90, 55], [4, 71, 81, 55, 12, 90], [4, 71, 81, 55, 90, 12], [4, 71, 81, 90, 12, 55], [4, 71, 81, 90, 55, 12], [4, 71, 12, 81, 55, 90], [4, 71, 12, 81, 90, 55], [4, 71, 12, 55, 81, 90], [4, 71, 12, 55, 90, 81], [4, 71, 12, 90, 81, 55], [4, 71, 12, 90, 55, 81], [4, 71, 55, 81, 12, 90], [4, 71, 55, 81, 90, 12], [4, 71, 55, 12, 81, 90], [4, 71, 55, 12, 90, 81], [4, 71, 55, 90, 81, 12], [4, 71, 55, 90, 12, 81], [4, 71, 90, 81, 12, 55], [4, 71, 90, 81, 55, 12], [4, 71, 90, 12, 81, 55], [4, 71, 90, 12, 55, 81], [4, 71, 90, 55, 81, 12], [4, 71, 90, 55, 12, 81], [4, 90, 81, 12, 55, 71], [4, 90, 81, 12, 71, 55], [4, 90, 81, 55, 12, 71], [4, 90, 81, 55, 71, 12], [4, 90, 81, 71, 12, 55], [4, 90, 81, 71, 55, 12], [4, 90, 12, 81, 55, 71], [4, 90, 12, 81, 71, 55], [4, 90, 12, 55, 81, 71], [4, 90, 12, 55, 71, 81], [4, 90, 12, 71, 81, 55], [4, 90, 12, 71, 55, 81], [4, 90, 55, 81, 12, 71], [4, 90, 55, 81, 71, 12], [4, 90, 55, 12, 81, 71], [4, 90, 55, 12, 71, 81], [4, 90, 55, 71, 81, 12], [4, 90, 55, 71, 12, 81], [4, 90, 71, 81, 12, 55], [4, 90, 71, 81, 55, 12], [4, 90, 71, 12, 81, 55], [4, 90, 71, 12, 55, 81], [4, 90, 71, 55, 81, 12], [4, 90, 71, 55, 12, 81], [90, 81, 12, 55, 71, 4], [90, 81, 12, 55, 4, 71], [90, 81, 12, 71, 55, 4], [90, 81, 12, 71, 4, 55], [90, 81, 12, 4, 55, 71], [90, 81, 12, 4, 71, 55], [90, 81, 55, 12, 71, 4], [90, 81, 55, 12, 4, 71], [90, 81, 55, 71, 12, 4], [90, 81, 55, 71, 4, 12], [90, 81, 55, 4, 12, 71], [90, 81, 55, 4, 71, 12], [90, 81, 71, 12, 55, 4], [90, 81, 71, 12, 4, 55], [90, 81, 71, 55, 12, 4], [90, 81, 71, 55, 4, 12], [90, 81, 71, 4, 12, 55], [90, 81, 71, 4, 55, 12], [90, 81, 4, 12, 55, 71], [90, 81, 4, 12, 71, 55], [90, 81, 4, 55, 12, 71], [90, 81, 4, 55, 71, 12], [90, 81, 4, 71, 12, 55], [90, 81, 4, 71, 55, 12], [90, 12, 81, 55, 71, 4], [90, 12, 81, 55, 4, 71], [90, 12, 81, 71, 55, 4], [90, 12, 81, 71, 4, 55], [90, 12, 81, 4, 55, 71], [90, 12, 81, 4, 71, 55], [90, 12, 55, 81, 71, 4], [90, 12, 55, 81, 4, 71], [90, 12, 55, 71, 81, 4], [90, 12, 55, 71, 4, 81], [90, 12, 55, 4, 81, 71], [90, 12, 55, 4, 71, 81], [90, 12, 71, 81, 55, 4], [90, 12, 71, 81, 4, 55], [90, 12, 71, 55, 81, 4], [90, 12, 71, 55, 4, 81], [90, 12, 71, 4, 81, 55], [90, 12, 71, 4, 55, 81], [90, 12, 4, 81, 55, 71], [90, 12, 4, 81, 71, 55], [90, 12, 4, 55, 81, 71], [90, 12, 4, 55, 71, 81], [90, 12, 4, 71, 81, 55], [90, 12, 4, 71, 55, 81], [90, 55, 81, 12, 71, 4], [90, 55, 81, 12, 4, 71], [90, 55, 81, 71, 12, 4], [90, 55, 81, 71, 4, 12], [90, 55, 81, 4, 12, 71], [90, 55, 81, 4, 71, 12], [90, 55, 12, 81, 71, 4], [90, 55, 12, 81, 4, 71], [90, 55, 12, 71, 81, 4], [90, 55, 12, 71, 4, 81], [90, 55, 12, 4, 81, 71], [90, 55, 12, 4, 71, 81], [90, 55, 71, 81, 12, 4], [90, 55, 71, 81, 4, 12], [90, 55, 71, 12, 81, 4], [90, 55, 71, 12, 4, 81], [90, 55, 71, 4, 81, 12], [90, 55, 71, 4, 12, 81], [90, 55, 4, 81, 12, 71], [90, 55, 4, 81, 71, 12], [90, 55, 4, 12, 81, 71], [90, 55, 4, 12, 71, 81], [90, 55, 4, 71, 81, 12], [90, 55, 4, 71, 12, 81], [90, 71, 81, 12, 55, 4], [90, 71, 81, 12, 4, 55], [90, 71, 81, 55, 12, 4], [90, 71, 81, 55, 4, 12], [90, 71, 81, 4, 12, 55], [90, 71, 81, 4, 55, 12], [90, 71, 12, 81, 55, 4], [90, 71, 12, 81, 4, 55], [90, 71, 12, 55, 81, 4], [90, 71, 12, 55, 4, 81], [90, 71, 12, 4, 81, 55], [90, 71, 12, 4, 55, 81], [90, 71, 55, 81, 12, 4], [90, 71, 55, 81, 4, 12], [90, 71, 55, 12, 81, 4], [90, 71, 55, 12, 4, 81], [90, 71, 55, 4, 81, 12], [90, 71, 55, 4, 12, 81], [90, 71, 4, 81, 12, 55], [90, 71, 4, 81, 55, 12], [90, 71, 4, 12, 81, 55], [90, 71, 4, 12, 55, 81], [90, 71, 4, 55, 81, 12], [90, 71, 4, 55, 12, 81], [90, 4, 81, 12, 55, 71], [90, 4, 81, 12, 71, 55], [90, 4, 81, 55, 12, 71], [90, 4, 81, 55, 71, 12], [90, 4, 81, 71, 12, 55], [90, 4, 81, 71, 55, 12], [90, 4, 12, 81, 55, 71], [90, 4, 12, 81, 71, 55], [90, 4, 12, 55, 81, 71], [90, 4, 12, 55, 71, 81], [90, 4, 12, 71, 81, 55], [90, 4, 12, 71, 55, 81], [90, 4, 55, 81, 12, 71], [90, 4, 55, 81, 71, 12], [90, 4, 55, 12, 81, 71], [90, 4, 55, 12, 71, 81], [90, 4, 55, 71, 81, 12], [90, 4, 55, 71, 12, 81], [90, 4, 71, 81, 12, 55], [90, 4, 71, 81, 55, 12], [90, 4, 71, 12, 81, 55], [90, 4, 71, 12, 55, 81], [90, 4, 71, 55, 81, 12], [90, 4, 71, 55, 12, 81]]