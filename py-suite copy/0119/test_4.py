
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


def test_4():
    assert solution.Solution().getRow(68) == [1, 68, 2278, 50116, 814385, 10424128, 109453344, 969443904, 7392009768, 49280065120, 290752384208, 1533058025824, 7282025622664, 31368725759168, 123234279768160, 443643407165376, 1469568786235308, 4495151581425648, 12736262814039336, 33516481089577200, 82115378669464140, 187692294101632320, 400978991944396320, 801957983888792640, 1503671219791486200, 2646461346833015712, 4376839919762295216, 6808417652963570336, 9969468706125227992, 13750991318793417920, 17876288714431443296, 21912870037044995008, 25336755980333275478, 27640097433090845976, 28453041475240576740, 27640097433090845976, 25336755980333275478, 21912870037044995008, 17876288714431443296, 13750991318793417920, 9969468706125227992, 6808417652963570336, 4376839919762295216, 2646461346833015712, 1503671219791486200, 801957983888792640, 400978991944396320, 187692294101632320, 82115378669464140, 33516481089577200, 12736262814039336, 4495151581425648, 1469568786235308, 443643407165376, 123234279768160, 31368725759168, 7282025622664, 1533058025824, 290752384208, 49280065120, 7392009768, 969443904, 109453344, 10424128, 814385, 50116, 2278, 68, 1]