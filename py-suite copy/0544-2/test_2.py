
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
    assert solution.Solution().findContestMatch(89) == '((((((1,89),(44,46)),((22,68),(23,67))),(((11,79),(34,56)),((12,78),(33,57)))),((((5,85),(40,50)),((18,72),(27,63))),(((7,83),(38,52)),((16,74),(29,61))))),(((((2,88),(43,47)),((21,69),(24,66))),(((10,80),(35,55)),((13,77),(32,58)))),((((4,86),(41,49)),((19,71),(26,64))),(((8,82),(37,53)),((15,75),(30,60))))))'
