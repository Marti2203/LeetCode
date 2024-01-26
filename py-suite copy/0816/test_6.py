
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


def test_6():
    assert solution.Solution().ambiguousCoordinates('uEx5dLXDd4') == ['(E, x5dLXDd)', '(E, x.5dLXDd)', '(E, x5.dLXDd)', '(E, x5d.LXDd)', '(E, x5dL.XDd)', '(E, x5dLX.Dd)', '(E, x5dLXD.d)', '(Ex, 5dLXDd)', '(Ex, 5.dLXDd)', '(Ex, 5d.LXDd)', '(Ex, 5dL.XDd)', '(Ex, 5dLX.Dd)', '(Ex, 5dLXD.d)', '(E.x, 5dLXDd)', '(E.x, 5.dLXDd)', '(E.x, 5d.LXDd)', '(E.x, 5dL.XDd)', '(E.x, 5dLX.Dd)', '(E.x, 5dLXD.d)', '(Ex5, dLXDd)', '(Ex5, d.LXDd)', '(Ex5, dL.XDd)', '(Ex5, dLX.Dd)', '(Ex5, dLXD.d)', '(E.x5, dLXDd)', '(E.x5, d.LXDd)', '(E.x5, dL.XDd)', '(E.x5, dLX.Dd)', '(E.x5, dLXD.d)', '(Ex.5, dLXDd)', '(Ex.5, d.LXDd)', '(Ex.5, dL.XDd)', '(Ex.5, dLX.Dd)', '(Ex.5, dLXD.d)', '(Ex5d, LXDd)', '(Ex5d, L.XDd)', '(Ex5d, LX.Dd)', '(Ex5d, LXD.d)', '(E.x5d, LXDd)', '(E.x5d, L.XDd)', '(E.x5d, LX.Dd)', '(E.x5d, LXD.d)', '(Ex.5d, LXDd)', '(Ex.5d, L.XDd)', '(Ex.5d, LX.Dd)', '(Ex.5d, LXD.d)', '(Ex5.d, LXDd)', '(Ex5.d, L.XDd)', '(Ex5.d, LX.Dd)', '(Ex5.d, LXD.d)', '(Ex5dL, XDd)', '(Ex5dL, X.Dd)', '(Ex5dL, XD.d)', '(E.x5dL, XDd)', '(E.x5dL, X.Dd)', '(E.x5dL, XD.d)', '(Ex.5dL, XDd)', '(Ex.5dL, X.Dd)', '(Ex.5dL, XD.d)', '(Ex5.dL, XDd)', '(Ex5.dL, X.Dd)', '(Ex5.dL, XD.d)', '(Ex5d.L, XDd)', '(Ex5d.L, X.Dd)', '(Ex5d.L, XD.d)', '(Ex5dLX, Dd)', '(Ex5dLX, D.d)', '(E.x5dLX, Dd)', '(E.x5dLX, D.d)', '(Ex.5dLX, Dd)', '(Ex.5dLX, D.d)', '(Ex5.dLX, Dd)', '(Ex5.dLX, D.d)', '(Ex5d.LX, Dd)', '(Ex5d.LX, D.d)', '(Ex5dL.X, Dd)', '(Ex5dL.X, D.d)', '(Ex5dLXD, d)', '(E.x5dLXD, d)', '(Ex.5dLXD, d)', '(Ex5.dLXD, d)', '(Ex5d.LXD, d)', '(Ex5dL.XD, d)', '(Ex5dLX.D, d)']
