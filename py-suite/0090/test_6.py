
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


def test_6():
    assert solution.Solution().subsetsWithDup([13, 12, 18, 33, 43, 60]) == [[], [12], [12, 13], [12, 13, 18], [12, 13, 18, 33], [12, 13, 18, 33, 43], [12, 13, 18, 33, 43, 60], [12, 13, 18, 33, 60], [12, 13, 18, 43], [12, 13, 18, 43, 60], [12, 13, 18, 60], [12, 13, 33], [12, 13, 33, 43], [12, 13, 33, 43, 60], [12, 13, 33, 60], [12, 13, 43], [12, 13, 43, 60], [12, 13, 60], [12, 18], [12, 18, 33], [12, 18, 33, 43], [12, 18, 33, 43, 60], [12, 18, 33, 60], [12, 18, 43], [12, 18, 43, 60], [12, 18, 60], [12, 33], [12, 33, 43], [12, 33, 43, 60], [12, 33, 60], [12, 43], [12, 43, 60], [12, 60], [13], [13, 18], [13, 18, 33], [13, 18, 33, 43], [13, 18, 33, 43, 60], [13, 18, 33, 60], [13, 18, 43], [13, 18, 43, 60], [13, 18, 60], [13, 33], [13, 33, 43], [13, 33, 43, 60], [13, 33, 60], [13, 43], [13, 43, 60], [13, 60], [18], [18, 33], [18, 33, 43], [18, 33, 43, 60], [18, 33, 60], [18, 43], [18, 43, 60], [18, 60], [33], [33, 43], [33, 43, 60], [33, 60], [43], [43, 60], [60]]
