
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
    assert solution.Solution().subsets([64, 16, 19, 7, 77]) == [[], [64], [64, 16], [64, 16, 19], [64, 16, 19, 7], [64, 16, 19, 7, 77], [64, 16, 19, 77], [64, 16, 7], [64, 16, 7, 77], [64, 16, 77], [64, 19], [64, 19, 7], [64, 19, 7, 77], [64, 19, 77], [64, 7], [64, 7, 77], [64, 77], [16], [16, 19], [16, 19, 7], [16, 19, 7, 77], [16, 19, 77], [16, 7], [16, 7, 77], [16, 77], [19], [19, 7], [19, 7, 77], [19, 77], [7], [7, 77], [77]]
