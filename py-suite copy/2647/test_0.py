
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


def test_0():
    assert solution.Solution().colorRed(40) == [[1, 1], [2, 3], [3, 2], [4, 1], [4, 3], [4, 5], [4, 7], [5, 1], [6, 3], [6, 5], [6, 7], [6, 9], [6, 11], [7, 2], [8, 1], [8, 3], [8, 5], [8, 7], [8, 9], [8, 11], [8, 13], [8, 15], [9, 1], [10, 3], [10, 5], [10, 7], [10, 9], [10, 11], [10, 13], [10, 15], [10, 17], [10, 19], [11, 2], [12, 1], [12, 3], [12, 5], [12, 7], [12, 9], [12, 11], [12, 13], [12, 15], [12, 17], [12, 19], [12, 21], [12, 23], [13, 1], [14, 3], [14, 5], [14, 7], [14, 9], [14, 11], [14, 13], [14, 15], [14, 17], [14, 19], [14, 21], [14, 23], [14, 25], [14, 27], [15, 2], [16, 1], [16, 3], [16, 5], [16, 7], [16, 9], [16, 11], [16, 13], [16, 15], [16, 17], [16, 19], [16, 21], [16, 23], [16, 25], [16, 27], [16, 29], [16, 31], [17, 1], [18, 3], [18, 5], [18, 7], [18, 9], [18, 11], [18, 13], [18, 15], [18, 17], [18, 19], [18, 21], [18, 23], [18, 25], [18, 27], [18, 29], [18, 31], [18, 33], [18, 35], [19, 2], [20, 1], [20, 3], [20, 5], [20, 7], [20, 9], [20, 11], [20, 13], [20, 15], [20, 17], [20, 19], [20, 21], [20, 23], [20, 25], [20, 27], [20, 29], [20, 31], [20, 33], [20, 35], [20, 37], [20, 39], [21, 1], [22, 3], [22, 5], [22, 7], [22, 9], [22, 11], [22, 13], [22, 15], [22, 17], [22, 19], [22, 21], [22, 23], [22, 25], [22, 27], [22, 29], [22, 31], [22, 33], [22, 35], [22, 37], [22, 39], [22, 41], [22, 43], [23, 2], [24, 1], [24, 3], [24, 5], [24, 7], [24, 9], [24, 11], [24, 13], [24, 15], [24, 17], [24, 19], [24, 21], [24, 23], [24, 25], [24, 27], [24, 29], [24, 31], [24, 33], [24, 35], [24, 37], [24, 39], [24, 41], [24, 43], [24, 45], [24, 47], [25, 1], [26, 3], [26, 5], [26, 7], [26, 9], [26, 11], [26, 13], [26, 15], [26, 17], [26, 19], [26, 21], [26, 23], [26, 25], [26, 27], [26, 29], [26, 31], [26, 33], [26, 35], [26, 37], [26, 39], [26, 41], [26, 43], [26, 45], [26, 47], [26, 49], [26, 51], [27, 2], [28, 1], [28, 3], [28, 5], [28, 7], [28, 9], [28, 11], [28, 13], [28, 15], [28, 17], [28, 19], [28, 21], [28, 23], [28, 25], [28, 27], [28, 29], [28, 31], [28, 33], [28, 35], [28, 37], [28, 39], [28, 41], [28, 43], [28, 45], [28, 47], [28, 49], [28, 51], [28, 53], [28, 55], [29, 1], [30, 3], [30, 5], [30, 7], [30, 9], [30, 11], [30, 13], [30, 15], [30, 17], [30, 19], [30, 21], [30, 23], [30, 25], [30, 27], [30, 29], [30, 31], [30, 33], [30, 35], [30, 37], [30, 39], [30, 41], [30, 43], [30, 45], [30, 47], [30, 49], [30, 51], [30, 53], [30, 55], [30, 57], [30, 59], [31, 2], [32, 1], [32, 3], [32, 5], [32, 7], [32, 9], [32, 11], [32, 13], [32, 15], [32, 17], [32, 19], [32, 21], [32, 23], [32, 25], [32, 27], [32, 29], [32, 31], [32, 33], [32, 35], [32, 37], [32, 39], [32, 41], [32, 43], [32, 45], [32, 47], [32, 49], [32, 51], [32, 53], [32, 55], [32, 57], [32, 59], [32, 61], [32, 63], [33, 1], [34, 3], [34, 5], [34, 7], [34, 9], [34, 11], [34, 13], [34, 15], [34, 17], [34, 19], [34, 21], [34, 23], [34, 25], [34, 27], [34, 29], [34, 31], [34, 33], [34, 35], [34, 37], [34, 39], [34, 41], [34, 43], [34, 45], [34, 47], [34, 49], [34, 51], [34, 53], [34, 55], [34, 57], [34, 59], [34, 61], [34, 63], [34, 65], [34, 67], [35, 2], [36, 1], [36, 3], [36, 5], [36, 7], [36, 9], [36, 11], [36, 13], [36, 15], [36, 17], [36, 19], [36, 21], [36, 23], [36, 25], [36, 27], [36, 29], [36, 31], [36, 33], [36, 35], [36, 37], [36, 39], [36, 41], [36, 43], [36, 45], [36, 47], [36, 49], [36, 51], [36, 53], [36, 55], [36, 57], [36, 59], [36, 61], [36, 63], [36, 65], [36, 67], [36, 69], [36, 71], [37, 1], [38, 3], [38, 5], [38, 7], [38, 9], [38, 11], [38, 13], [38, 15], [38, 17], [38, 19], [38, 21], [38, 23], [38, 25], [38, 27], [38, 29], [38, 31], [38, 33], [38, 35], [38, 37], [38, 39], [38, 41], [38, 43], [38, 45], [38, 47], [38, 49], [38, 51], [38, 53], [38, 55], [38, 57], [38, 59], [38, 61], [38, 63], [38, 65], [38, 67], [38, 69], [38, 71], [38, 73], [38, 75], [39, 2], [40, 1], [40, 3], [40, 5], [40, 7], [40, 9], [40, 11], [40, 13], [40, 15], [40, 17], [40, 19], [40, 21], [40, 23], [40, 25], [40, 27], [40, 29], [40, 31], [40, 33], [40, 35], [40, 37], [40, 39], [40, 41], [40, 43], [40, 45], [40, 47], [40, 49], [40, 51], [40, 53], [40, 55], [40, 57], [40, 59], [40, 61], [40, 63], [40, 65], [40, 67], [40, 69], [40, 71], [40, 73], [40, 75], [40, 77], [40, 79]]
