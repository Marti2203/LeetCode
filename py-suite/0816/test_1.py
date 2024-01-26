
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


def test_1():
    assert solution.Solution().ambiguousCoordinates('MBOtoy31Kz') == ['(B, Otoy31K)', '(B, O.toy31K)', '(B, Ot.oy31K)', '(B, Oto.y31K)', '(B, Otoy.31K)', '(B, Otoy3.1K)', '(B, Otoy31.K)', '(BO, toy31K)', '(BO, t.oy31K)', '(BO, to.y31K)', '(BO, toy.31K)', '(BO, toy3.1K)', '(BO, toy31.K)', '(B.O, toy31K)', '(B.O, t.oy31K)', '(B.O, to.y31K)', '(B.O, toy.31K)', '(B.O, toy3.1K)', '(B.O, toy31.K)', '(BOt, oy31K)', '(BOt, o.y31K)', '(BOt, oy.31K)', '(BOt, oy3.1K)', '(BOt, oy31.K)', '(B.Ot, oy31K)', '(B.Ot, o.y31K)', '(B.Ot, oy.31K)', '(B.Ot, oy3.1K)', '(B.Ot, oy31.K)', '(BO.t, oy31K)', '(BO.t, o.y31K)', '(BO.t, oy.31K)', '(BO.t, oy3.1K)', '(BO.t, oy31.K)', '(BOto, y31K)', '(BOto, y.31K)', '(BOto, y3.1K)', '(BOto, y31.K)', '(B.Oto, y31K)', '(B.Oto, y.31K)', '(B.Oto, y3.1K)', '(B.Oto, y31.K)', '(BO.to, y31K)', '(BO.to, y.31K)', '(BO.to, y3.1K)', '(BO.to, y31.K)', '(BOt.o, y31K)', '(BOt.o, y.31K)', '(BOt.o, y3.1K)', '(BOt.o, y31.K)', '(BOtoy, 31K)', '(BOtoy, 3.1K)', '(BOtoy, 31.K)', '(B.Otoy, 31K)', '(B.Otoy, 3.1K)', '(B.Otoy, 31.K)', '(BO.toy, 31K)', '(BO.toy, 3.1K)', '(BO.toy, 31.K)', '(BOt.oy, 31K)', '(BOt.oy, 3.1K)', '(BOt.oy, 31.K)', '(BOto.y, 31K)', '(BOto.y, 3.1K)', '(BOto.y, 31.K)', '(BOtoy3, 1K)', '(BOtoy3, 1.K)', '(B.Otoy3, 1K)', '(B.Otoy3, 1.K)', '(BO.toy3, 1K)', '(BO.toy3, 1.K)', '(BOt.oy3, 1K)', '(BOt.oy3, 1.K)', '(BOto.y3, 1K)', '(BOto.y3, 1.K)', '(BOtoy.3, 1K)', '(BOtoy.3, 1.K)', '(BOtoy31, K)', '(B.Otoy31, K)', '(BO.toy31, K)', '(BOt.oy31, K)', '(BOto.y31, K)', '(BOtoy.31, K)', '(BOtoy3.1, K)']
