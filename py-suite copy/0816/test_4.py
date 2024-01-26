
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


def test_4():
    assert solution.Solution().ambiguousCoordinates('jI5BseeaRX') == ['(I, 5BseeaR)', '(I, 5.BseeaR)', '(I, 5B.seeaR)', '(I, 5Bs.eeaR)', '(I, 5Bse.eaR)', '(I, 5Bsee.aR)', '(I, 5Bseea.R)', '(I5, BseeaR)', '(I5, B.seeaR)', '(I5, Bs.eeaR)', '(I5, Bse.eaR)', '(I5, Bsee.aR)', '(I5, Bseea.R)', '(I.5, BseeaR)', '(I.5, B.seeaR)', '(I.5, Bs.eeaR)', '(I.5, Bse.eaR)', '(I.5, Bsee.aR)', '(I.5, Bseea.R)', '(I5B, seeaR)', '(I5B, s.eeaR)', '(I5B, se.eaR)', '(I5B, see.aR)', '(I5B, seea.R)', '(I.5B, seeaR)', '(I.5B, s.eeaR)', '(I.5B, se.eaR)', '(I.5B, see.aR)', '(I.5B, seea.R)', '(I5.B, seeaR)', '(I5.B, s.eeaR)', '(I5.B, se.eaR)', '(I5.B, see.aR)', '(I5.B, seea.R)', '(I5Bs, eeaR)', '(I5Bs, e.eaR)', '(I5Bs, ee.aR)', '(I5Bs, eea.R)', '(I.5Bs, eeaR)', '(I.5Bs, e.eaR)', '(I.5Bs, ee.aR)', '(I.5Bs, eea.R)', '(I5.Bs, eeaR)', '(I5.Bs, e.eaR)', '(I5.Bs, ee.aR)', '(I5.Bs, eea.R)', '(I5B.s, eeaR)', '(I5B.s, e.eaR)', '(I5B.s, ee.aR)', '(I5B.s, eea.R)', '(I5Bse, eaR)', '(I5Bse, e.aR)', '(I5Bse, ea.R)', '(I.5Bse, eaR)', '(I.5Bse, e.aR)', '(I.5Bse, ea.R)', '(I5.Bse, eaR)', '(I5.Bse, e.aR)', '(I5.Bse, ea.R)', '(I5B.se, eaR)', '(I5B.se, e.aR)', '(I5B.se, ea.R)', '(I5Bs.e, eaR)', '(I5Bs.e, e.aR)', '(I5Bs.e, ea.R)', '(I5Bsee, aR)', '(I5Bsee, a.R)', '(I.5Bsee, aR)', '(I.5Bsee, a.R)', '(I5.Bsee, aR)', '(I5.Bsee, a.R)', '(I5B.see, aR)', '(I5B.see, a.R)', '(I5Bs.ee, aR)', '(I5Bs.ee, a.R)', '(I5Bse.e, aR)', '(I5Bse.e, a.R)', '(I5Bseea, R)', '(I.5Bseea, R)', '(I5.Bseea, R)', '(I5B.seea, R)', '(I5Bs.eea, R)', '(I5Bse.ea, R)', '(I5Bsee.a, R)']
