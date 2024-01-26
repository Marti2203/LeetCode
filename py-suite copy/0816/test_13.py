
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


def test_13():
    assert solution.Solution().ambiguousCoordinates('tcfZZrA0tr') == ['(c, fZZrA0t)', '(c, f.ZZrA0t)', '(c, fZ.ZrA0t)', '(c, fZZ.rA0t)', '(c, fZZr.A0t)', '(c, fZZrA.0t)', '(c, fZZrA0.t)', '(cf, ZZrA0t)', '(cf, Z.ZrA0t)', '(cf, ZZ.rA0t)', '(cf, ZZr.A0t)', '(cf, ZZrA.0t)', '(cf, ZZrA0.t)', '(c.f, ZZrA0t)', '(c.f, Z.ZrA0t)', '(c.f, ZZ.rA0t)', '(c.f, ZZr.A0t)', '(c.f, ZZrA.0t)', '(c.f, ZZrA0.t)', '(cfZ, ZrA0t)', '(cfZ, Z.rA0t)', '(cfZ, Zr.A0t)', '(cfZ, ZrA.0t)', '(cfZ, ZrA0.t)', '(c.fZ, ZrA0t)', '(c.fZ, Z.rA0t)', '(c.fZ, Zr.A0t)', '(c.fZ, ZrA.0t)', '(c.fZ, ZrA0.t)', '(cf.Z, ZrA0t)', '(cf.Z, Z.rA0t)', '(cf.Z, Zr.A0t)', '(cf.Z, ZrA.0t)', '(cf.Z, ZrA0.t)', '(cfZZ, rA0t)', '(cfZZ, r.A0t)', '(cfZZ, rA.0t)', '(cfZZ, rA0.t)', '(c.fZZ, rA0t)', '(c.fZZ, r.A0t)', '(c.fZZ, rA.0t)', '(c.fZZ, rA0.t)', '(cf.ZZ, rA0t)', '(cf.ZZ, r.A0t)', '(cf.ZZ, rA.0t)', '(cf.ZZ, rA0.t)', '(cfZ.Z, rA0t)', '(cfZ.Z, r.A0t)', '(cfZ.Z, rA.0t)', '(cfZ.Z, rA0.t)', '(cfZZr, A0t)', '(cfZZr, A.0t)', '(cfZZr, A0.t)', '(c.fZZr, A0t)', '(c.fZZr, A.0t)', '(c.fZZr, A0.t)', '(cf.ZZr, A0t)', '(cf.ZZr, A.0t)', '(cf.ZZr, A0.t)', '(cfZ.Zr, A0t)', '(cfZ.Zr, A.0t)', '(cfZ.Zr, A0.t)', '(cfZZ.r, A0t)', '(cfZZ.r, A.0t)', '(cfZZ.r, A0.t)', '(cfZZrA, 0.t)', '(c.fZZrA, 0.t)', '(cf.ZZrA, 0.t)', '(cfZ.ZrA, 0.t)', '(cfZZ.rA, 0.t)', '(cfZZr.A, 0.t)', '(cfZZrA0, t)']
