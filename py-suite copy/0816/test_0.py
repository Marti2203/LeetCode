
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
    assert solution.Solution().ambiguousCoordinates('e7p33K9TZY') == ['(7, p33K9TZ)', '(7, p.33K9TZ)', '(7, p3.3K9TZ)', '(7, p33.K9TZ)', '(7, p33K.9TZ)', '(7, p33K9.TZ)', '(7, p33K9T.Z)', '(7p, 33K9TZ)', '(7p, 3.3K9TZ)', '(7p, 33.K9TZ)', '(7p, 33K.9TZ)', '(7p, 33K9.TZ)', '(7p, 33K9T.Z)', '(7.p, 33K9TZ)', '(7.p, 3.3K9TZ)', '(7.p, 33.K9TZ)', '(7.p, 33K.9TZ)', '(7.p, 33K9.TZ)', '(7.p, 33K9T.Z)', '(7p3, 3K9TZ)', '(7p3, 3.K9TZ)', '(7p3, 3K.9TZ)', '(7p3, 3K9.TZ)', '(7p3, 3K9T.Z)', '(7.p3, 3K9TZ)', '(7.p3, 3.K9TZ)', '(7.p3, 3K.9TZ)', '(7.p3, 3K9.TZ)', '(7.p3, 3K9T.Z)', '(7p.3, 3K9TZ)', '(7p.3, 3.K9TZ)', '(7p.3, 3K.9TZ)', '(7p.3, 3K9.TZ)', '(7p.3, 3K9T.Z)', '(7p33, K9TZ)', '(7p33, K.9TZ)', '(7p33, K9.TZ)', '(7p33, K9T.Z)', '(7.p33, K9TZ)', '(7.p33, K.9TZ)', '(7.p33, K9.TZ)', '(7.p33, K9T.Z)', '(7p.33, K9TZ)', '(7p.33, K.9TZ)', '(7p.33, K9.TZ)', '(7p.33, K9T.Z)', '(7p3.3, K9TZ)', '(7p3.3, K.9TZ)', '(7p3.3, K9.TZ)', '(7p3.3, K9T.Z)', '(7p33K, 9TZ)', '(7p33K, 9.TZ)', '(7p33K, 9T.Z)', '(7.p33K, 9TZ)', '(7.p33K, 9.TZ)', '(7.p33K, 9T.Z)', '(7p.33K, 9TZ)', '(7p.33K, 9.TZ)', '(7p.33K, 9T.Z)', '(7p3.3K, 9TZ)', '(7p3.3K, 9.TZ)', '(7p3.3K, 9T.Z)', '(7p33.K, 9TZ)', '(7p33.K, 9.TZ)', '(7p33.K, 9T.Z)', '(7p33K9, TZ)', '(7p33K9, T.Z)', '(7.p33K9, TZ)', '(7.p33K9, T.Z)', '(7p.33K9, TZ)', '(7p.33K9, T.Z)', '(7p3.3K9, TZ)', '(7p3.3K9, T.Z)', '(7p33.K9, TZ)', '(7p33.K9, T.Z)', '(7p33K.9, TZ)', '(7p33K.9, T.Z)', '(7p33K9T, Z)', '(7.p33K9T, Z)', '(7p.33K9T, Z)', '(7p3.3K9T, Z)', '(7p33.K9T, Z)', '(7p33K.9T, Z)', '(7p33K9.T, Z)']
