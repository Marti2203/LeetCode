
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
    assert solution.Solution().findContestMatch(60) == '(((((1,60),(30,31)),((15,46),(16,45))),(((7,54),(24,37)),((9,52),(22,39)))),((((3,58),(28,33)),((13,48),(18,43))),(((5,56),(26,35)),((11,50),(20,41)))))'