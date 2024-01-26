
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


def test_16():
    assert solution.Solution().ambiguousCoordinates('uKxUS8xGNo') == ['(K, xUS8xGN)', '(K, x.US8xGN)', '(K, xU.S8xGN)', '(K, xUS.8xGN)', '(K, xUS8.xGN)', '(K, xUS8x.GN)', '(K, xUS8xG.N)', '(Kx, US8xGN)', '(Kx, U.S8xGN)', '(Kx, US.8xGN)', '(Kx, US8.xGN)', '(Kx, US8x.GN)', '(Kx, US8xG.N)', '(K.x, US8xGN)', '(K.x, U.S8xGN)', '(K.x, US.8xGN)', '(K.x, US8.xGN)', '(K.x, US8x.GN)', '(K.x, US8xG.N)', '(KxU, S8xGN)', '(KxU, S.8xGN)', '(KxU, S8.xGN)', '(KxU, S8x.GN)', '(KxU, S8xG.N)', '(K.xU, S8xGN)', '(K.xU, S.8xGN)', '(K.xU, S8.xGN)', '(K.xU, S8x.GN)', '(K.xU, S8xG.N)', '(Kx.U, S8xGN)', '(Kx.U, S.8xGN)', '(Kx.U, S8.xGN)', '(Kx.U, S8x.GN)', '(Kx.U, S8xG.N)', '(KxUS, 8xGN)', '(KxUS, 8.xGN)', '(KxUS, 8x.GN)', '(KxUS, 8xG.N)', '(K.xUS, 8xGN)', '(K.xUS, 8.xGN)', '(K.xUS, 8x.GN)', '(K.xUS, 8xG.N)', '(Kx.US, 8xGN)', '(Kx.US, 8.xGN)', '(Kx.US, 8x.GN)', '(Kx.US, 8xG.N)', '(KxU.S, 8xGN)', '(KxU.S, 8.xGN)', '(KxU.S, 8x.GN)', '(KxU.S, 8xG.N)', '(KxUS8, xGN)', '(KxUS8, x.GN)', '(KxUS8, xG.N)', '(K.xUS8, xGN)', '(K.xUS8, x.GN)', '(K.xUS8, xG.N)', '(Kx.US8, xGN)', '(Kx.US8, x.GN)', '(Kx.US8, xG.N)', '(KxU.S8, xGN)', '(KxU.S8, x.GN)', '(KxU.S8, xG.N)', '(KxUS.8, xGN)', '(KxUS.8, x.GN)', '(KxUS.8, xG.N)', '(KxUS8x, GN)', '(KxUS8x, G.N)', '(K.xUS8x, GN)', '(K.xUS8x, G.N)', '(Kx.US8x, GN)', '(Kx.US8x, G.N)', '(KxU.S8x, GN)', '(KxU.S8x, G.N)', '(KxUS.8x, GN)', '(KxUS.8x, G.N)', '(KxUS8.x, GN)', '(KxUS8.x, G.N)', '(KxUS8xG, N)', '(K.xUS8xG, N)', '(Kx.US8xG, N)', '(KxU.S8xG, N)', '(KxUS.8xG, N)', '(KxUS8.xG, N)', '(KxUS8x.G, N)']
