
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


def test_14():
    assert solution.Solution().simplifiedFractions(15) == ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5', '1/6', '5/6', '1/7', '2/7', '3/7', '4/7', '5/7', '6/7', '1/8', '3/8', '5/8', '7/8', '1/9', '2/9', '4/9', '5/9', '7/9', '8/9', '1/10', '3/10', '7/10', '9/10', '1/11', '2/11', '3/11', '4/11', '5/11', '6/11', '7/11', '8/11', '9/11', '10/11', '1/12', '5/12', '7/12', '11/12', '1/13', '2/13', '3/13', '4/13', '5/13', '6/13', '7/13', '8/13', '9/13', '10/13', '11/13', '12/13', '1/14', '3/14', '5/14', '9/14', '11/14', '13/14', '1/15', '2/15', '4/15', '7/15', '8/15', '11/15', '13/15', '14/15']
