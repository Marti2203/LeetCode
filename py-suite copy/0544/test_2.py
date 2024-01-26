
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


def test_2():
    assert solution.Solution().findContestMatch(87) == '((((((1,87),(43,45)),((21,67),(23,65))),(((10,78),(34,54)),((12,76),(32,56)))),((((5,83),(39,49)),((17,71),(27,61))),(((6,82),(38,50)),((16,72),(28,60))))),(((((2,86),(42,46)),((20,68),(24,64))),(((9,79),(35,53)),((13,75),(31,57)))),((((4,84),(40,48)),((18,70),(26,62))),(((7,81),(37,51)),((15,73),(29,59))))))'
