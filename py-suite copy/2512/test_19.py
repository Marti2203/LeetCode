
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


def test_19():
    assert solution.Solution().topStudents(['ZIVdBwpHOa', 'gHH1F8vEXD', '4EO3qyihYE'], ['6ysUvszJA6', 'XYONd5JEwz', 'iec8uuKFil', '0OoOUPcv4Q'], ['ksB3Dy5DYo', 'qyZUz93kXE', 'Vj085UpwK2', 'EajFDIGp8M', 'Y54vApdUCt'], [7, 81, 99, 93, 68, 69], 49) == [7, 68, 81, 93, 99]
