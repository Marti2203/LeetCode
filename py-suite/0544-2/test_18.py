
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
    assert solution.Solution().findContestMatch(72) == '((((((1,72),(36,37)),((18,55),(19,54))),(((9,64),(28,45)),((10,63),(27,46)))),((((4,69),(33,40)),((15,58),(22,51))),(((6,67),(31,42)),((13,60),(24,49))))),(((((2,71),(35,38)),((17,56),(20,53))),(((8,65),(29,44)),((11,62),(26,47)))),((((3,70),(34,39)),((16,57),(21,52))),(((7,66),(30,43)),((12,61),(25,48))))))'
