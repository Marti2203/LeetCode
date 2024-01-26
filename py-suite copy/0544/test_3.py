
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


def test_3():
    assert solution.Solution().findContestMatch(99) == '((((((1,99),(49,51)),((24,76),(26,74))),(((12,88),(38,62)),((13,87),(37,63)))),((((6,94),(44,56)),((19,81),(31,69))),(((7,93),(43,57)),((18,82),(32,68))))),(((((3,97),(47,53)),((22,78),(28,72))),(((10,90),(40,60)),((15,85),(35,65)))),((((4,96),(46,54)),((21,79),(29,71))),(((9,91),(41,59)),((16,84),(34,66))))))'
