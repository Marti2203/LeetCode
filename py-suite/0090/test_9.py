
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


def test_9():
    assert solution.Solution().subsetsWithDup([31, 63, 15, 93]) == [[], [15], [15, 31], [15, 31, 63], [15, 31, 63, 93], [15, 31, 93], [15, 63], [15, 63, 93], [15, 93], [31], [31, 63], [31, 63, 93], [31, 93], [63], [63, 93], [93]]
