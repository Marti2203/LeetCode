
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
    assert solution.Solution().groupAnagrams(['N7KdcSCqt4', 'fSdbXU6hbK', 'vkdFPVEJVV', 'NV4fduiTk3', 'DCxxD9epgp', 'vvFVDsPIN0']) == dict_values([['N7KdcSCqt4'], ['fSdbXU6hbK'], ['vkdFPVEJVV'], ['NV4fduiTk3'], ['DCxxD9epgp'], ['vvFVDsPIN0']])