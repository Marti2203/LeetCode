
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


def test_7():
    assert solution.Solution().simplifiedFractions(21) == ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5', '1/6', '5/6', '1/7', '2/7', '3/7', '4/7', '5/7', '6/7', '1/8', '3/8', '5/8', '7/8', '1/9', '2/9', '4/9', '5/9', '7/9', '8/9', '1/10', '3/10', '7/10', '9/10', '1/11', '2/11', '3/11', '4/11', '5/11', '6/11', '7/11', '8/11', '9/11', '10/11', '1/12', '5/12', '7/12', '11/12', '1/13', '2/13', '3/13', '4/13', '5/13', '6/13', '7/13', '8/13', '9/13', '10/13', '11/13', '12/13', '1/14', '3/14', '5/14', '9/14', '11/14', '13/14', '1/15', '2/15', '4/15', '7/15', '8/15', '11/15', '13/15', '14/15', '1/16', '3/16', '5/16', '7/16', '9/16', '11/16', '13/16', '15/16', '1/17', '2/17', '3/17', '4/17', '5/17', '6/17', '7/17', '8/17', '9/17', '10/17', '11/17', '12/17', '13/17', '14/17', '15/17', '16/17', '1/18', '5/18', '7/18', '11/18', '13/18', '17/18', '1/19', '2/19', '3/19', '4/19', '5/19', '6/19', '7/19', '8/19', '9/19', '10/19', '11/19', '12/19', '13/19', '14/19', '15/19', '16/19', '17/19', '18/19', '1/20', '3/20', '7/20', '9/20', '11/20', '13/20', '17/20', '19/20', '1/21', '2/21', '4/21', '5/21', '8/21', '10/21', '11/21', '13/21', '16/21', '17/21', '19/21', '20/21']
