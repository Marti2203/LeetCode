
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


def test_15():
    assert solution.Solution().ambiguousCoordinates('e8IszeU4lJ') == ['(8, IszeU4l)', '(8, I.szeU4l)', '(8, Is.zeU4l)', '(8, Isz.eU4l)', '(8, Isze.U4l)', '(8, IszeU.4l)', '(8, IszeU4.l)', '(8I, szeU4l)', '(8I, s.zeU4l)', '(8I, sz.eU4l)', '(8I, sze.U4l)', '(8I, szeU.4l)', '(8I, szeU4.l)', '(8.I, szeU4l)', '(8.I, s.zeU4l)', '(8.I, sz.eU4l)', '(8.I, sze.U4l)', '(8.I, szeU.4l)', '(8.I, szeU4.l)', '(8Is, zeU4l)', '(8Is, z.eU4l)', '(8Is, ze.U4l)', '(8Is, zeU.4l)', '(8Is, zeU4.l)', '(8.Is, zeU4l)', '(8.Is, z.eU4l)', '(8.Is, ze.U4l)', '(8.Is, zeU.4l)', '(8.Is, zeU4.l)', '(8I.s, zeU4l)', '(8I.s, z.eU4l)', '(8I.s, ze.U4l)', '(8I.s, zeU.4l)', '(8I.s, zeU4.l)', '(8Isz, eU4l)', '(8Isz, e.U4l)', '(8Isz, eU.4l)', '(8Isz, eU4.l)', '(8.Isz, eU4l)', '(8.Isz, e.U4l)', '(8.Isz, eU.4l)', '(8.Isz, eU4.l)', '(8I.sz, eU4l)', '(8I.sz, e.U4l)', '(8I.sz, eU.4l)', '(8I.sz, eU4.l)', '(8Is.z, eU4l)', '(8Is.z, e.U4l)', '(8Is.z, eU.4l)', '(8Is.z, eU4.l)', '(8Isze, U4l)', '(8Isze, U.4l)', '(8Isze, U4.l)', '(8.Isze, U4l)', '(8.Isze, U.4l)', '(8.Isze, U4.l)', '(8I.sze, U4l)', '(8I.sze, U.4l)', '(8I.sze, U4.l)', '(8Is.ze, U4l)', '(8Is.ze, U.4l)', '(8Is.ze, U4.l)', '(8Isz.e, U4l)', '(8Isz.e, U.4l)', '(8Isz.e, U4.l)', '(8IszeU, 4l)', '(8IszeU, 4.l)', '(8.IszeU, 4l)', '(8.IszeU, 4.l)', '(8I.szeU, 4l)', '(8I.szeU, 4.l)', '(8Is.zeU, 4l)', '(8Is.zeU, 4.l)', '(8Isz.eU, 4l)', '(8Isz.eU, 4.l)', '(8Isze.U, 4l)', '(8Isze.U, 4.l)', '(8IszeU4, l)', '(8.IszeU4, l)', '(8I.szeU4, l)', '(8Is.zeU4, l)', '(8Isz.eU4, l)', '(8Isze.U4, l)', '(8IszeU.4, l)']
