
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
    assert solution.Solution().ambiguousCoordinates('71qu4gZ08L') == ['(1, qu4gZ08)', '(1, q.u4gZ08)', '(1, qu.4gZ08)', '(1, qu4.gZ08)', '(1, qu4g.Z08)', '(1, qu4gZ.08)', '(1, qu4gZ0.8)', '(1q, u4gZ08)', '(1q, u.4gZ08)', '(1q, u4.gZ08)', '(1q, u4g.Z08)', '(1q, u4gZ.08)', '(1q, u4gZ0.8)', '(1.q, u4gZ08)', '(1.q, u.4gZ08)', '(1.q, u4.gZ08)', '(1.q, u4g.Z08)', '(1.q, u4gZ.08)', '(1.q, u4gZ0.8)', '(1qu, 4gZ08)', '(1qu, 4.gZ08)', '(1qu, 4g.Z08)', '(1qu, 4gZ.08)', '(1qu, 4gZ0.8)', '(1.qu, 4gZ08)', '(1.qu, 4.gZ08)', '(1.qu, 4g.Z08)', '(1.qu, 4gZ.08)', '(1.qu, 4gZ0.8)', '(1q.u, 4gZ08)', '(1q.u, 4.gZ08)', '(1q.u, 4g.Z08)', '(1q.u, 4gZ.08)', '(1q.u, 4gZ0.8)', '(1qu4, gZ08)', '(1qu4, g.Z08)', '(1qu4, gZ.08)', '(1qu4, gZ0.8)', '(1.qu4, gZ08)', '(1.qu4, g.Z08)', '(1.qu4, gZ.08)', '(1.qu4, gZ0.8)', '(1q.u4, gZ08)', '(1q.u4, g.Z08)', '(1q.u4, gZ.08)', '(1q.u4, gZ0.8)', '(1qu.4, gZ08)', '(1qu.4, g.Z08)', '(1qu.4, gZ.08)', '(1qu.4, gZ0.8)', '(1qu4g, Z08)', '(1qu4g, Z.08)', '(1qu4g, Z0.8)', '(1.qu4g, Z08)', '(1.qu4g, Z.08)', '(1.qu4g, Z0.8)', '(1q.u4g, Z08)', '(1q.u4g, Z.08)', '(1q.u4g, Z0.8)', '(1qu.4g, Z08)', '(1qu.4g, Z.08)', '(1qu.4g, Z0.8)', '(1qu4.g, Z08)', '(1qu4.g, Z.08)', '(1qu4.g, Z0.8)', '(1qu4gZ, 0.8)', '(1.qu4gZ, 0.8)', '(1q.u4gZ, 0.8)', '(1qu.4gZ, 0.8)', '(1qu4.gZ, 0.8)', '(1qu4g.Z, 0.8)', '(1qu4gZ0, 8)']
