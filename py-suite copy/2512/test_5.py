
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
    assert solution.Solution().topStudents(['DLEUt1lEeA', 'q7JsCJOzUl', '4FtQ5xVBAz', '3Enky0vGUx', '7wQp020RY9', 'U7K8benbAP'], ['Q1kDpZdlYv', '9LeM43FHCN', 'QxpXxz3kgB', 'S3ttcUU5hd', 'U1UIOlssr0'], ['XorBvYzaLf', 'dezJmfnLHc'], [78, 59, 32, 64, 97, 51], 14) == [59, 78]
