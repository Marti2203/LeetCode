
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


def test_3():
    assert solution.Solution().topStudents(['epX5L1MhtF', '5cbgBy87vj', 'waHVCTD3tO', '37K1RBsXJE', 'wt4l9PIZy0'], ['M1JwpHssR8', 'yK0Hm0cpLV'], ['If7ARb5kpB', 'cTBifQJkqG', 'aOJlmSGuVr', 'XoK4DK41av', 'L7ApPLO1U6', 'edCpPuHjsk'], [37, 27, 51, 55, 91, 31], 100) == [27, 31, 37, 51, 55, 91]
