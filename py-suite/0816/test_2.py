
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


def test_2():
    assert solution.Solution().ambiguousCoordinates('a202SiGs9l') == ['(2, 0.2SiGs9)', '(20, 2SiGs9)', '(20, 2.SiGs9)', '(20, 2S.iGs9)', '(20, 2Si.Gs9)', '(20, 2SiG.s9)', '(20, 2SiGs.9)', '(202, SiGs9)', '(202, S.iGs9)', '(202, Si.Gs9)', '(202, SiG.s9)', '(202, SiGs.9)', '(2.02, SiGs9)', '(2.02, S.iGs9)', '(2.02, Si.Gs9)', '(2.02, SiG.s9)', '(2.02, SiGs.9)', '(20.2, SiGs9)', '(20.2, S.iGs9)', '(20.2, Si.Gs9)', '(20.2, SiG.s9)', '(20.2, SiGs.9)', '(202S, iGs9)', '(202S, i.Gs9)', '(202S, iG.s9)', '(202S, iGs.9)', '(2.02S, iGs9)', '(2.02S, i.Gs9)', '(2.02S, iG.s9)', '(2.02S, iGs.9)', '(20.2S, iGs9)', '(20.2S, i.Gs9)', '(20.2S, iG.s9)', '(20.2S, iGs.9)', '(202.S, iGs9)', '(202.S, i.Gs9)', '(202.S, iG.s9)', '(202.S, iGs.9)', '(202Si, Gs9)', '(202Si, G.s9)', '(202Si, Gs.9)', '(2.02Si, Gs9)', '(2.02Si, G.s9)', '(2.02Si, Gs.9)', '(20.2Si, Gs9)', '(20.2Si, G.s9)', '(20.2Si, Gs.9)', '(202.Si, Gs9)', '(202.Si, G.s9)', '(202.Si, Gs.9)', '(202S.i, Gs9)', '(202S.i, G.s9)', '(202S.i, Gs.9)', '(202SiG, s9)', '(202SiG, s.9)', '(2.02SiG, s9)', '(2.02SiG, s.9)', '(20.2SiG, s9)', '(20.2SiG, s.9)', '(202.SiG, s9)', '(202.SiG, s.9)', '(202S.iG, s9)', '(202S.iG, s.9)', '(202Si.G, s9)', '(202Si.G, s.9)', '(202SiGs, 9)', '(2.02SiGs, 9)', '(20.2SiGs, 9)', '(202.SiGs, 9)', '(202S.iGs, 9)', '(202Si.Gs, 9)', '(202SiG.s, 9)']
