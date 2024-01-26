
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


def test_1():
    assert solution.Solution().findContestMatch(96) == '((((((1,96),(48,49)),((24,73),(25,72))),(((12,85),(37,60)),((13,84),(36,61)))),((((6,91),(43,54)),((19,78),(30,67))),(((7,90),(42,55)),((18,79),(31,66))))),(((((3,94),(46,51)),((22,75),(27,70))),(((10,87),(39,58)),((15,82),(34,63)))),((((4,93),(45,52)),((21,76),(28,69))),(((9,88),(40,57)),((16,81),(33,64))))))'
