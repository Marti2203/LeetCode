
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


def test_15():
    assert solution.Solution().findReplaceString('raFcd16YDh', [36, 62], ['oMKfg3PlUk', '7NND9pK2vi', '5Rnc8eDdx8'], ['CCuJ9BJmQT', '6FvSH1fYcn', 'lwNoVjv5I2', 'GXlKlin28Z', 'ucM1B6f6C9', 'i1Mflb3NZx']) == 'raFcd16YDh'
