
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


def test_18():
    assert solution.Solution().ambiguousCoordinates('PPzNGzr53G') == ['(P, zNGzr53)', '(P, z.NGzr53)', '(P, zN.Gzr53)', '(P, zNG.zr53)', '(P, zNGz.r53)', '(P, zNGzr.53)', '(P, zNGzr5.3)', '(Pz, NGzr53)', '(Pz, N.Gzr53)', '(Pz, NG.zr53)', '(Pz, NGz.r53)', '(Pz, NGzr.53)', '(Pz, NGzr5.3)', '(P.z, NGzr53)', '(P.z, N.Gzr53)', '(P.z, NG.zr53)', '(P.z, NGz.r53)', '(P.z, NGzr.53)', '(P.z, NGzr5.3)', '(PzN, Gzr53)', '(PzN, G.zr53)', '(PzN, Gz.r53)', '(PzN, Gzr.53)', '(PzN, Gzr5.3)', '(P.zN, Gzr53)', '(P.zN, G.zr53)', '(P.zN, Gz.r53)', '(P.zN, Gzr.53)', '(P.zN, Gzr5.3)', '(Pz.N, Gzr53)', '(Pz.N, G.zr53)', '(Pz.N, Gz.r53)', '(Pz.N, Gzr.53)', '(Pz.N, Gzr5.3)', '(PzNG, zr53)', '(PzNG, z.r53)', '(PzNG, zr.53)', '(PzNG, zr5.3)', '(P.zNG, zr53)', '(P.zNG, z.r53)', '(P.zNG, zr.53)', '(P.zNG, zr5.3)', '(Pz.NG, zr53)', '(Pz.NG, z.r53)', '(Pz.NG, zr.53)', '(Pz.NG, zr5.3)', '(PzN.G, zr53)', '(PzN.G, z.r53)', '(PzN.G, zr.53)', '(PzN.G, zr5.3)', '(PzNGz, r53)', '(PzNGz, r.53)', '(PzNGz, r5.3)', '(P.zNGz, r53)', '(P.zNGz, r.53)', '(P.zNGz, r5.3)', '(Pz.NGz, r53)', '(Pz.NGz, r.53)', '(Pz.NGz, r5.3)', '(PzN.Gz, r53)', '(PzN.Gz, r.53)', '(PzN.Gz, r5.3)', '(PzNG.z, r53)', '(PzNG.z, r.53)', '(PzNG.z, r5.3)', '(PzNGzr, 53)', '(PzNGzr, 5.3)', '(P.zNGzr, 53)', '(P.zNGzr, 5.3)', '(Pz.NGzr, 53)', '(Pz.NGzr, 5.3)', '(PzN.Gzr, 53)', '(PzN.Gzr, 5.3)', '(PzNG.zr, 53)', '(PzNG.zr, 5.3)', '(PzNGz.r, 53)', '(PzNGz.r, 5.3)', '(PzNGzr5, 3)', '(P.zNGzr5, 3)', '(Pz.NGzr5, 3)', '(PzN.Gzr5, 3)', '(PzNG.zr5, 3)', '(PzNGz.r5, 3)', '(PzNGzr.5, 3)']
