
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


def test_12():
    assert solution.Solution().subsetsWithDup([31, 93, 77, 61, 20]) == [[], [20], [20, 31], [20, 31, 61], [20, 31, 61, 77], [20, 31, 61, 77, 93], [20, 31, 61, 93], [20, 31, 77], [20, 31, 77, 93], [20, 31, 93], [20, 61], [20, 61, 77], [20, 61, 77, 93], [20, 61, 93], [20, 77], [20, 77, 93], [20, 93], [31], [31, 61], [31, 61, 77], [31, 61, 77, 93], [31, 61, 93], [31, 77], [31, 77, 93], [31, 93], [61], [61, 77], [61, 77, 93], [61, 93], [77], [77, 93], [93]]
