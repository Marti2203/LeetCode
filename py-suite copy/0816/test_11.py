
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


def test_11():
    assert solution.Solution().ambiguousCoordinates('Qnu1kVt7l8') == ['(n, u1kVt7l)', '(n, u.1kVt7l)', '(n, u1.kVt7l)', '(n, u1k.Vt7l)', '(n, u1kV.t7l)', '(n, u1kVt.7l)', '(n, u1kVt7.l)', '(nu, 1kVt7l)', '(nu, 1.kVt7l)', '(nu, 1k.Vt7l)', '(nu, 1kV.t7l)', '(nu, 1kVt.7l)', '(nu, 1kVt7.l)', '(n.u, 1kVt7l)', '(n.u, 1.kVt7l)', '(n.u, 1k.Vt7l)', '(n.u, 1kV.t7l)', '(n.u, 1kVt.7l)', '(n.u, 1kVt7.l)', '(nu1, kVt7l)', '(nu1, k.Vt7l)', '(nu1, kV.t7l)', '(nu1, kVt.7l)', '(nu1, kVt7.l)', '(n.u1, kVt7l)', '(n.u1, k.Vt7l)', '(n.u1, kV.t7l)', '(n.u1, kVt.7l)', '(n.u1, kVt7.l)', '(nu.1, kVt7l)', '(nu.1, k.Vt7l)', '(nu.1, kV.t7l)', '(nu.1, kVt.7l)', '(nu.1, kVt7.l)', '(nu1k, Vt7l)', '(nu1k, V.t7l)', '(nu1k, Vt.7l)', '(nu1k, Vt7.l)', '(n.u1k, Vt7l)', '(n.u1k, V.t7l)', '(n.u1k, Vt.7l)', '(n.u1k, Vt7.l)', '(nu.1k, Vt7l)', '(nu.1k, V.t7l)', '(nu.1k, Vt.7l)', '(nu.1k, Vt7.l)', '(nu1.k, Vt7l)', '(nu1.k, V.t7l)', '(nu1.k, Vt.7l)', '(nu1.k, Vt7.l)', '(nu1kV, t7l)', '(nu1kV, t.7l)', '(nu1kV, t7.l)', '(n.u1kV, t7l)', '(n.u1kV, t.7l)', '(n.u1kV, t7.l)', '(nu.1kV, t7l)', '(nu.1kV, t.7l)', '(nu.1kV, t7.l)', '(nu1.kV, t7l)', '(nu1.kV, t.7l)', '(nu1.kV, t7.l)', '(nu1k.V, t7l)', '(nu1k.V, t.7l)', '(nu1k.V, t7.l)', '(nu1kVt, 7l)', '(nu1kVt, 7.l)', '(n.u1kVt, 7l)', '(n.u1kVt, 7.l)', '(nu.1kVt, 7l)', '(nu.1kVt, 7.l)', '(nu1.kVt, 7l)', '(nu1.kVt, 7.l)', '(nu1k.Vt, 7l)', '(nu1k.Vt, 7.l)', '(nu1kV.t, 7l)', '(nu1kV.t, 7.l)', '(nu1kVt7, l)', '(n.u1kVt7, l)', '(nu.1kVt7, l)', '(nu1.kVt7, l)', '(nu1k.Vt7, l)', '(nu1kV.t7, l)', '(nu1kVt.7, l)']
