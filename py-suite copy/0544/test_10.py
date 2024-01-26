
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


def test_10():
    assert solution.Solution().findContestMatch(95) == '((((((1,95),(47,49)),((23,73),(25,71))),(((11,85),(37,59)),((13,83),(35,61)))),((((5,91),(43,53)),((19,77),(29,67))),(((7,89),(41,55)),((17,79),(31,65))))),(((((2,94),(46,50)),((22,74),(26,70))),(((10,86),(38,58)),((14,82),(34,62)))),((((4,92),(44,52)),((20,76),(28,68))),(((8,88),(40,56)),((16,80),(32,64))))))'
