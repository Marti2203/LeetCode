
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


def test_17():
    assert solution.Solution().ambiguousCoordinates('QdGy7tY3kM') == ['(d, Gy7tY3k)', '(d, G.y7tY3k)', '(d, Gy.7tY3k)', '(d, Gy7.tY3k)', '(d, Gy7t.Y3k)', '(d, Gy7tY.3k)', '(d, Gy7tY3.k)', '(dG, y7tY3k)', '(dG, y.7tY3k)', '(dG, y7.tY3k)', '(dG, y7t.Y3k)', '(dG, y7tY.3k)', '(dG, y7tY3.k)', '(d.G, y7tY3k)', '(d.G, y.7tY3k)', '(d.G, y7.tY3k)', '(d.G, y7t.Y3k)', '(d.G, y7tY.3k)', '(d.G, y7tY3.k)', '(dGy, 7tY3k)', '(dGy, 7.tY3k)', '(dGy, 7t.Y3k)', '(dGy, 7tY.3k)', '(dGy, 7tY3.k)', '(d.Gy, 7tY3k)', '(d.Gy, 7.tY3k)', '(d.Gy, 7t.Y3k)', '(d.Gy, 7tY.3k)', '(d.Gy, 7tY3.k)', '(dG.y, 7tY3k)', '(dG.y, 7.tY3k)', '(dG.y, 7t.Y3k)', '(dG.y, 7tY.3k)', '(dG.y, 7tY3.k)', '(dGy7, tY3k)', '(dGy7, t.Y3k)', '(dGy7, tY.3k)', '(dGy7, tY3.k)', '(d.Gy7, tY3k)', '(d.Gy7, t.Y3k)', '(d.Gy7, tY.3k)', '(d.Gy7, tY3.k)', '(dG.y7, tY3k)', '(dG.y7, t.Y3k)', '(dG.y7, tY.3k)', '(dG.y7, tY3.k)', '(dGy.7, tY3k)', '(dGy.7, t.Y3k)', '(dGy.7, tY.3k)', '(dGy.7, tY3.k)', '(dGy7t, Y3k)', '(dGy7t, Y.3k)', '(dGy7t, Y3.k)', '(d.Gy7t, Y3k)', '(d.Gy7t, Y.3k)', '(d.Gy7t, Y3.k)', '(dG.y7t, Y3k)', '(dG.y7t, Y.3k)', '(dG.y7t, Y3.k)', '(dGy.7t, Y3k)', '(dGy.7t, Y.3k)', '(dGy.7t, Y3.k)', '(dGy7.t, Y3k)', '(dGy7.t, Y.3k)', '(dGy7.t, Y3.k)', '(dGy7tY, 3k)', '(dGy7tY, 3.k)', '(d.Gy7tY, 3k)', '(d.Gy7tY, 3.k)', '(dG.y7tY, 3k)', '(dG.y7tY, 3.k)', '(dGy.7tY, 3k)', '(dGy.7tY, 3.k)', '(dGy7.tY, 3k)', '(dGy7.tY, 3.k)', '(dGy7t.Y, 3k)', '(dGy7t.Y, 3.k)', '(dGy7tY3, k)', '(d.Gy7tY3, k)', '(dG.y7tY3, k)', '(dGy.7tY3, k)', '(dGy7.tY3, k)', '(dGy7t.Y3, k)', '(dGy7tY.3, k)']
