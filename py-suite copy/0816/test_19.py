
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


def test_19():
    assert solution.Solution().ambiguousCoordinates('cBUTMRx8gi') == ['(B, UTMRx8g)', '(B, U.TMRx8g)', '(B, UT.MRx8g)', '(B, UTM.Rx8g)', '(B, UTMR.x8g)', '(B, UTMRx.8g)', '(B, UTMRx8.g)', '(BU, TMRx8g)', '(BU, T.MRx8g)', '(BU, TM.Rx8g)', '(BU, TMR.x8g)', '(BU, TMRx.8g)', '(BU, TMRx8.g)', '(B.U, TMRx8g)', '(B.U, T.MRx8g)', '(B.U, TM.Rx8g)', '(B.U, TMR.x8g)', '(B.U, TMRx.8g)', '(B.U, TMRx8.g)', '(BUT, MRx8g)', '(BUT, M.Rx8g)', '(BUT, MR.x8g)', '(BUT, MRx.8g)', '(BUT, MRx8.g)', '(B.UT, MRx8g)', '(B.UT, M.Rx8g)', '(B.UT, MR.x8g)', '(B.UT, MRx.8g)', '(B.UT, MRx8.g)', '(BU.T, MRx8g)', '(BU.T, M.Rx8g)', '(BU.T, MR.x8g)', '(BU.T, MRx.8g)', '(BU.T, MRx8.g)', '(BUTM, Rx8g)', '(BUTM, R.x8g)', '(BUTM, Rx.8g)', '(BUTM, Rx8.g)', '(B.UTM, Rx8g)', '(B.UTM, R.x8g)', '(B.UTM, Rx.8g)', '(B.UTM, Rx8.g)', '(BU.TM, Rx8g)', '(BU.TM, R.x8g)', '(BU.TM, Rx.8g)', '(BU.TM, Rx8.g)', '(BUT.M, Rx8g)', '(BUT.M, R.x8g)', '(BUT.M, Rx.8g)', '(BUT.M, Rx8.g)', '(BUTMR, x8g)', '(BUTMR, x.8g)', '(BUTMR, x8.g)', '(B.UTMR, x8g)', '(B.UTMR, x.8g)', '(B.UTMR, x8.g)', '(BU.TMR, x8g)', '(BU.TMR, x.8g)', '(BU.TMR, x8.g)', '(BUT.MR, x8g)', '(BUT.MR, x.8g)', '(BUT.MR, x8.g)', '(BUTM.R, x8g)', '(BUTM.R, x.8g)', '(BUTM.R, x8.g)', '(BUTMRx, 8g)', '(BUTMRx, 8.g)', '(B.UTMRx, 8g)', '(B.UTMRx, 8.g)', '(BU.TMRx, 8g)', '(BU.TMRx, 8.g)', '(BUT.MRx, 8g)', '(BUT.MRx, 8.g)', '(BUTM.Rx, 8g)', '(BUTM.Rx, 8.g)', '(BUTMR.x, 8g)', '(BUTMR.x, 8.g)', '(BUTMRx8, g)', '(B.UTMRx8, g)', '(BU.TMRx8, g)', '(BUT.MRx8, g)', '(BUTM.Rx8, g)', '(BUTMR.x8, g)', '(BUTMRx.8, g)']
