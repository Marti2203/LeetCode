
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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other is None:
            return False
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"




class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_nums = sum(nums)
        max_value = 0
        for i in range(n):
            rotation_sum = 0
            for j in range(n):
                rotation_sum += nums[(j+i)%n]
            max_value = max(max_value, rotation_sum)
        return max_value
