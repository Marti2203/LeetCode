
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


def test_3():
    assert solution.Solution().ambiguousCoordinates('ZPTZ91cmUg') == ['(P, TZ91cmU)', '(P, T.Z91cmU)', '(P, TZ.91cmU)', '(P, TZ9.1cmU)', '(P, TZ91.cmU)', '(P, TZ91c.mU)', '(P, TZ91cm.U)', '(PT, Z91cmU)', '(PT, Z.91cmU)', '(PT, Z9.1cmU)', '(PT, Z91.cmU)', '(PT, Z91c.mU)', '(PT, Z91cm.U)', '(P.T, Z91cmU)', '(P.T, Z.91cmU)', '(P.T, Z9.1cmU)', '(P.T, Z91.cmU)', '(P.T, Z91c.mU)', '(P.T, Z91cm.U)', '(PTZ, 91cmU)', '(PTZ, 9.1cmU)', '(PTZ, 91.cmU)', '(PTZ, 91c.mU)', '(PTZ, 91cm.U)', '(P.TZ, 91cmU)', '(P.TZ, 9.1cmU)', '(P.TZ, 91.cmU)', '(P.TZ, 91c.mU)', '(P.TZ, 91cm.U)', '(PT.Z, 91cmU)', '(PT.Z, 9.1cmU)', '(PT.Z, 91.cmU)', '(PT.Z, 91c.mU)', '(PT.Z, 91cm.U)', '(PTZ9, 1cmU)', '(PTZ9, 1.cmU)', '(PTZ9, 1c.mU)', '(PTZ9, 1cm.U)', '(P.TZ9, 1cmU)', '(P.TZ9, 1.cmU)', '(P.TZ9, 1c.mU)', '(P.TZ9, 1cm.U)', '(PT.Z9, 1cmU)', '(PT.Z9, 1.cmU)', '(PT.Z9, 1c.mU)', '(PT.Z9, 1cm.U)', '(PTZ.9, 1cmU)', '(PTZ.9, 1.cmU)', '(PTZ.9, 1c.mU)', '(PTZ.9, 1cm.U)', '(PTZ91, cmU)', '(PTZ91, c.mU)', '(PTZ91, cm.U)', '(P.TZ91, cmU)', '(P.TZ91, c.mU)', '(P.TZ91, cm.U)', '(PT.Z91, cmU)', '(PT.Z91, c.mU)', '(PT.Z91, cm.U)', '(PTZ.91, cmU)', '(PTZ.91, c.mU)', '(PTZ.91, cm.U)', '(PTZ9.1, cmU)', '(PTZ9.1, c.mU)', '(PTZ9.1, cm.U)', '(PTZ91c, mU)', '(PTZ91c, m.U)', '(P.TZ91c, mU)', '(P.TZ91c, m.U)', '(PT.Z91c, mU)', '(PT.Z91c, m.U)', '(PTZ.91c, mU)', '(PTZ.91c, m.U)', '(PTZ9.1c, mU)', '(PTZ9.1c, m.U)', '(PTZ91.c, mU)', '(PTZ91.c, m.U)', '(PTZ91cm, U)', '(P.TZ91cm, U)', '(PT.Z91cm, U)', '(PTZ.91cm, U)', '(PTZ9.1cm, U)', '(PTZ91.cm, U)', '(PTZ91c.m, U)']
