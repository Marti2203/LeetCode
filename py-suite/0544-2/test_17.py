
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
    assert solution.Solution().findContestMatch(65) == '((((((1,65),(32,34)),((16,50),(17,49))),(((8,58),(25,41)),((9,57),(24,42)))),((((4,62),(29,37)),((13,53),(20,46))),(((5,61),(28,38)),((12,54),(21,45))))),(((((2,64),(31,35)),((15,51),(18,48))),(((7,59),(26,40)),((10,56),(23,43)))),((((3,63),(30,36)),((14,52),(19,47))),(((6,60),(27,39)),((11,55),(22,44))))))'
