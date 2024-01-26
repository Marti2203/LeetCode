
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
    assert solution.Solution().findContestMatch(81) == '((((((1,81),(40,42)),((20,62),(21,61))),(((10,72),(31,51)),((11,71),(30,52)))),((((5,77),(36,46)),((16,66),(25,57))),(((6,76),(35,47)),((15,67),(26,56))))),(((((2,80),(39,43)),((19,63),(22,60))),(((9,73),(32,50)),((12,70),(29,53)))),((((4,78),(37,45)),((17,65),(24,58))),(((7,75),(34,48)),((14,68),(27,55))))))'
