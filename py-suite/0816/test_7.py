
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


def test_7():
    assert solution.Solution().ambiguousCoordinates('XdSTbsgFMq') == ['(d, STbsgFM)', '(d, S.TbsgFM)', '(d, ST.bsgFM)', '(d, STb.sgFM)', '(d, STbs.gFM)', '(d, STbsg.FM)', '(d, STbsgF.M)', '(dS, TbsgFM)', '(dS, T.bsgFM)', '(dS, Tb.sgFM)', '(dS, Tbs.gFM)', '(dS, Tbsg.FM)', '(dS, TbsgF.M)', '(d.S, TbsgFM)', '(d.S, T.bsgFM)', '(d.S, Tb.sgFM)', '(d.S, Tbs.gFM)', '(d.S, Tbsg.FM)', '(d.S, TbsgF.M)', '(dST, bsgFM)', '(dST, b.sgFM)', '(dST, bs.gFM)', '(dST, bsg.FM)', '(dST, bsgF.M)', '(d.ST, bsgFM)', '(d.ST, b.sgFM)', '(d.ST, bs.gFM)', '(d.ST, bsg.FM)', '(d.ST, bsgF.M)', '(dS.T, bsgFM)', '(dS.T, b.sgFM)', '(dS.T, bs.gFM)', '(dS.T, bsg.FM)', '(dS.T, bsgF.M)', '(dSTb, sgFM)', '(dSTb, s.gFM)', '(dSTb, sg.FM)', '(dSTb, sgF.M)', '(d.STb, sgFM)', '(d.STb, s.gFM)', '(d.STb, sg.FM)', '(d.STb, sgF.M)', '(dS.Tb, sgFM)', '(dS.Tb, s.gFM)', '(dS.Tb, sg.FM)', '(dS.Tb, sgF.M)', '(dST.b, sgFM)', '(dST.b, s.gFM)', '(dST.b, sg.FM)', '(dST.b, sgF.M)', '(dSTbs, gFM)', '(dSTbs, g.FM)', '(dSTbs, gF.M)', '(d.STbs, gFM)', '(d.STbs, g.FM)', '(d.STbs, gF.M)', '(dS.Tbs, gFM)', '(dS.Tbs, g.FM)', '(dS.Tbs, gF.M)', '(dST.bs, gFM)', '(dST.bs, g.FM)', '(dST.bs, gF.M)', '(dSTb.s, gFM)', '(dSTb.s, g.FM)', '(dSTb.s, gF.M)', '(dSTbsg, FM)', '(dSTbsg, F.M)', '(d.STbsg, FM)', '(d.STbsg, F.M)', '(dS.Tbsg, FM)', '(dS.Tbsg, F.M)', '(dST.bsg, FM)', '(dST.bsg, F.M)', '(dSTb.sg, FM)', '(dSTb.sg, F.M)', '(dSTbs.g, FM)', '(dSTbs.g, F.M)', '(dSTbsgF, M)', '(d.STbsgF, M)', '(dS.TbsgF, M)', '(dST.bsgF, M)', '(dSTb.sgF, M)', '(dSTbs.gF, M)', '(dSTbsg.F, M)']
