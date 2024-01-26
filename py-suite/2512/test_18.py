
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
    assert solution.Solution().topStudents(['qFufd9yEx8', 'CKlBakRsRI', '1ZyjPfv0qd', 'F3qLy50zqS', 'zfMvyXLMo6', 'rwYN59aPOc'], ['b537rYUpaE', 'H2JvQYMhC5', 'y9RB5A3J5E', 'sytDrJpy3k'], ['1nxJjSk95f', 'uXJzATlaP5', 'GrUpxL58U6', 'zd8LvwfQxw', 'SpdySsXsAX'], [73, 74, 95], 61) == [73, 74, 95]
