
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


def test_4():
    assert solution.Solution().findContestMatch(71) == '((((((1,71),(35,37)),((17,55),(19,53))),(((8,64),(28,44)),((10,62),(26,46)))),((((4,68),(32,40)),((14,58),(22,50))),(((5,67),(31,41)),((13,59),(23,49))))),(((((2,70),(34,38)),((16,56),(20,52))),(((7,65),(29,43)),((11,61),(25,47)))),((((3,69),(33,39)),((15,57),(21,51))),(((6,66),(30,42)),((12,60),(24,48))))))'
