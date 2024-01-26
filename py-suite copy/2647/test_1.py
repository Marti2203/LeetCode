
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


def test_1():
    assert solution.Solution().colorRed(41) == [[1, 1], [2, 1], [3, 3], [3, 5], [4, 2], [5, 1], [5, 3], [5, 5], [5, 7], [5, 9], [6, 1], [7, 3], [7, 5], [7, 7], [7, 9], [7, 11], [7, 13], [8, 2], [9, 1], [9, 3], [9, 5], [9, 7], [9, 9], [9, 11], [9, 13], [9, 15], [9, 17], [10, 1], [11, 3], [11, 5], [11, 7], [11, 9], [11, 11], [11, 13], [11, 15], [11, 17], [11, 19], [11, 21], [12, 2], [13, 1], [13, 3], [13, 5], [13, 7], [13, 9], [13, 11], [13, 13], [13, 15], [13, 17], [13, 19], [13, 21], [13, 23], [13, 25], [14, 1], [15, 3], [15, 5], [15, 7], [15, 9], [15, 11], [15, 13], [15, 15], [15, 17], [15, 19], [15, 21], [15, 23], [15, 25], [15, 27], [15, 29], [16, 2], [17, 1], [17, 3], [17, 5], [17, 7], [17, 9], [17, 11], [17, 13], [17, 15], [17, 17], [17, 19], [17, 21], [17, 23], [17, 25], [17, 27], [17, 29], [17, 31], [17, 33], [18, 1], [19, 3], [19, 5], [19, 7], [19, 9], [19, 11], [19, 13], [19, 15], [19, 17], [19, 19], [19, 21], [19, 23], [19, 25], [19, 27], [19, 29], [19, 31], [19, 33], [19, 35], [19, 37], [20, 2], [21, 1], [21, 3], [21, 5], [21, 7], [21, 9], [21, 11], [21, 13], [21, 15], [21, 17], [21, 19], [21, 21], [21, 23], [21, 25], [21, 27], [21, 29], [21, 31], [21, 33], [21, 35], [21, 37], [21, 39], [21, 41], [22, 1], [23, 3], [23, 5], [23, 7], [23, 9], [23, 11], [23, 13], [23, 15], [23, 17], [23, 19], [23, 21], [23, 23], [23, 25], [23, 27], [23, 29], [23, 31], [23, 33], [23, 35], [23, 37], [23, 39], [23, 41], [23, 43], [23, 45], [24, 2], [25, 1], [25, 3], [25, 5], [25, 7], [25, 9], [25, 11], [25, 13], [25, 15], [25, 17], [25, 19], [25, 21], [25, 23], [25, 25], [25, 27], [25, 29], [25, 31], [25, 33], [25, 35], [25, 37], [25, 39], [25, 41], [25, 43], [25, 45], [25, 47], [25, 49], [26, 1], [27, 3], [27, 5], [27, 7], [27, 9], [27, 11], [27, 13], [27, 15], [27, 17], [27, 19], [27, 21], [27, 23], [27, 25], [27, 27], [27, 29], [27, 31], [27, 33], [27, 35], [27, 37], [27, 39], [27, 41], [27, 43], [27, 45], [27, 47], [27, 49], [27, 51], [27, 53], [28, 2], [29, 1], [29, 3], [29, 5], [29, 7], [29, 9], [29, 11], [29, 13], [29, 15], [29, 17], [29, 19], [29, 21], [29, 23], [29, 25], [29, 27], [29, 29], [29, 31], [29, 33], [29, 35], [29, 37], [29, 39], [29, 41], [29, 43], [29, 45], [29, 47], [29, 49], [29, 51], [29, 53], [29, 55], [29, 57], [30, 1], [31, 3], [31, 5], [31, 7], [31, 9], [31, 11], [31, 13], [31, 15], [31, 17], [31, 19], [31, 21], [31, 23], [31, 25], [31, 27], [31, 29], [31, 31], [31, 33], [31, 35], [31, 37], [31, 39], [31, 41], [31, 43], [31, 45], [31, 47], [31, 49], [31, 51], [31, 53], [31, 55], [31, 57], [31, 59], [31, 61], [32, 2], [33, 1], [33, 3], [33, 5], [33, 7], [33, 9], [33, 11], [33, 13], [33, 15], [33, 17], [33, 19], [33, 21], [33, 23], [33, 25], [33, 27], [33, 29], [33, 31], [33, 33], [33, 35], [33, 37], [33, 39], [33, 41], [33, 43], [33, 45], [33, 47], [33, 49], [33, 51], [33, 53], [33, 55], [33, 57], [33, 59], [33, 61], [33, 63], [33, 65], [34, 1], [35, 3], [35, 5], [35, 7], [35, 9], [35, 11], [35, 13], [35, 15], [35, 17], [35, 19], [35, 21], [35, 23], [35, 25], [35, 27], [35, 29], [35, 31], [35, 33], [35, 35], [35, 37], [35, 39], [35, 41], [35, 43], [35, 45], [35, 47], [35, 49], [35, 51], [35, 53], [35, 55], [35, 57], [35, 59], [35, 61], [35, 63], [35, 65], [35, 67], [35, 69], [36, 2], [37, 1], [37, 3], [37, 5], [37, 7], [37, 9], [37, 11], [37, 13], [37, 15], [37, 17], [37, 19], [37, 21], [37, 23], [37, 25], [37, 27], [37, 29], [37, 31], [37, 33], [37, 35], [37, 37], [37, 39], [37, 41], [37, 43], [37, 45], [37, 47], [37, 49], [37, 51], [37, 53], [37, 55], [37, 57], [37, 59], [37, 61], [37, 63], [37, 65], [37, 67], [37, 69], [37, 71], [37, 73], [38, 1], [39, 3], [39, 5], [39, 7], [39, 9], [39, 11], [39, 13], [39, 15], [39, 17], [39, 19], [39, 21], [39, 23], [39, 25], [39, 27], [39, 29], [39, 31], [39, 33], [39, 35], [39, 37], [39, 39], [39, 41], [39, 43], [39, 45], [39, 47], [39, 49], [39, 51], [39, 53], [39, 55], [39, 57], [39, 59], [39, 61], [39, 63], [39, 65], [39, 67], [39, 69], [39, 71], [39, 73], [39, 75], [39, 77], [40, 2], [41, 1], [41, 3], [41, 5], [41, 7], [41, 9], [41, 11], [41, 13], [41, 15], [41, 17], [41, 19], [41, 21], [41, 23], [41, 25], [41, 27], [41, 29], [41, 31], [41, 33], [41, 35], [41, 37], [41, 39], [41, 41], [41, 43], [41, 45], [41, 47], [41, 49], [41, 51], [41, 53], [41, 55], [41, 57], [41, 59], [41, 61], [41, 63], [41, 65], [41, 67], [41, 69], [41, 71], [41, 73], [41, 75], [41, 77], [41, 79], [41, 81]]
