
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


def test_14():
    assert solution.Solution().ambiguousCoordinates('cZuK9rccrZ') == ['(Z, uK9rccr)', '(Z, u.K9rccr)', '(Z, uK.9rccr)', '(Z, uK9.rccr)', '(Z, uK9r.ccr)', '(Z, uK9rc.cr)', '(Z, uK9rcc.r)', '(Zu, K9rccr)', '(Zu, K.9rccr)', '(Zu, K9.rccr)', '(Zu, K9r.ccr)', '(Zu, K9rc.cr)', '(Zu, K9rcc.r)', '(Z.u, K9rccr)', '(Z.u, K.9rccr)', '(Z.u, K9.rccr)', '(Z.u, K9r.ccr)', '(Z.u, K9rc.cr)', '(Z.u, K9rcc.r)', '(ZuK, 9rccr)', '(ZuK, 9.rccr)', '(ZuK, 9r.ccr)', '(ZuK, 9rc.cr)', '(ZuK, 9rcc.r)', '(Z.uK, 9rccr)', '(Z.uK, 9.rccr)', '(Z.uK, 9r.ccr)', '(Z.uK, 9rc.cr)', '(Z.uK, 9rcc.r)', '(Zu.K, 9rccr)', '(Zu.K, 9.rccr)', '(Zu.K, 9r.ccr)', '(Zu.K, 9rc.cr)', '(Zu.K, 9rcc.r)', '(ZuK9, rccr)', '(ZuK9, r.ccr)', '(ZuK9, rc.cr)', '(ZuK9, rcc.r)', '(Z.uK9, rccr)', '(Z.uK9, r.ccr)', '(Z.uK9, rc.cr)', '(Z.uK9, rcc.r)', '(Zu.K9, rccr)', '(Zu.K9, r.ccr)', '(Zu.K9, rc.cr)', '(Zu.K9, rcc.r)', '(ZuK.9, rccr)', '(ZuK.9, r.ccr)', '(ZuK.9, rc.cr)', '(ZuK.9, rcc.r)', '(ZuK9r, ccr)', '(ZuK9r, c.cr)', '(ZuK9r, cc.r)', '(Z.uK9r, ccr)', '(Z.uK9r, c.cr)', '(Z.uK9r, cc.r)', '(Zu.K9r, ccr)', '(Zu.K9r, c.cr)', '(Zu.K9r, cc.r)', '(ZuK.9r, ccr)', '(ZuK.9r, c.cr)', '(ZuK.9r, cc.r)', '(ZuK9.r, ccr)', '(ZuK9.r, c.cr)', '(ZuK9.r, cc.r)', '(ZuK9rc, cr)', '(ZuK9rc, c.r)', '(Z.uK9rc, cr)', '(Z.uK9rc, c.r)', '(Zu.K9rc, cr)', '(Zu.K9rc, c.r)', '(ZuK.9rc, cr)', '(ZuK.9rc, c.r)', '(ZuK9.rc, cr)', '(ZuK9.rc, c.r)', '(ZuK9r.c, cr)', '(ZuK9r.c, c.r)', '(ZuK9rcc, r)', '(Z.uK9rcc, r)', '(Zu.K9rcc, r)', '(ZuK.9rcc, r)', '(ZuK9.rcc, r)', '(ZuK9r.cc, r)', '(ZuK9rc.c, r)']
