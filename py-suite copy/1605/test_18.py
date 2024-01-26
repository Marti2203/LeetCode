
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
    assert solution.Solution().restoreMatrix([55, 49, 10, 50, 54], [44, 40, 21, 10, 9, 99]) == [[44, 11, 0, 0, 0, 0], [0, 29, 20, 0, 0, 0], [0, 0, 1, 9, 0, 0], [0, 0, 0, 1, 9, 40], [0, 0, 0, 0, 0, 54]]
