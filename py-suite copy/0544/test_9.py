
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


def test_9():
    assert solution.Solution().findContestMatch(88) == '((((((1,88),(44,45)),((22,67),(23,66))),(((11,78),(34,55)),((12,77),(33,56)))),((((5,84),(40,49)),((18,71),(27,62))),(((7,82),(38,51)),((16,73),(29,60))))),(((((2,87),(43,46)),((21,68),(24,65))),(((10,79),(35,54)),((13,76),(32,57)))),((((4,85),(41,48)),((19,70),(26,63))),(((8,81),(37,52)),((15,74),(30,59))))))'
