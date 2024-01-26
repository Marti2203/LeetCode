
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
    assert solution.Solution().findContestMatch(83) == '((((((1,83),(41,43)),((20,64),(22,62))),(((10,74),(32,52)),((11,73),(31,53)))),((((5,79),(37,47)),((16,68),(26,58))),(((6,78),(36,48)),((15,69),(27,57))))),(((((2,82),(40,44)),((19,65),(23,61))),(((9,75),(33,51)),((12,72),(30,54)))),((((4,80),(38,46)),((17,67),(25,59))),(((7,77),(35,49)),((14,70),(28,56))))))'
