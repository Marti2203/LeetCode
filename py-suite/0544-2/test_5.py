
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


def test_5():
    assert solution.Solution().findContestMatch(90) == '((((((1,90),(45,46)),((22,69),(24,67))),(((11,80),(35,56)),((12,79),(34,57)))),((((5,86),(41,50)),((18,73),(28,63))),(((7,84),(39,52)),((16,75),(30,61))))),(((((2,89),(44,47)),((21,70),(25,66))),(((10,81),(36,55)),((13,78),(33,58)))),((((4,87),(42,49)),((19,72),(27,64))),(((8,83),(38,53)),((15,76),(31,60))))))'
