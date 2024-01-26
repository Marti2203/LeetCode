
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
    assert solution.Solution().findContestMatch(64) == '((((((1,64),(32,33)),((16,49),(17,48))),(((8,57),(25,40)),((9,56),(24,41)))),((((4,61),(29,36)),((13,52),(20,45))),(((5,60),(28,37)),((12,53),(21,44))))),(((((2,63),(31,34)),((15,50),(18,47))),(((7,58),(26,39)),((10,55),(23,42)))),((((3,62),(30,35)),((14,51),(19,46))),(((6,59),(27,38)),((11,54),(22,43))))))'
