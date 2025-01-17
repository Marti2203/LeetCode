
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


def test_8():
    assert solution.Solution().generateMatrix(16) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 17], [59, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 75, 18], [58, 111, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 125, 76, 19], [57, 110, 155, 192, 193, 194, 195, 196, 197, 198, 199, 200, 167, 126, 77, 20], [56, 109, 154, 191, 220, 221, 222, 223, 224, 225, 226, 201, 168, 127, 78, 21], [55, 108, 153, 190, 219, 240, 241, 242, 243, 244, 227, 202, 169, 128, 79, 22], [54, 107, 152, 189, 218, 239, 252, 253, 254, 245, 228, 203, 170, 129, 80, 23], [53, 106, 151, 188, 217, 238, 251, 256, 255, 246, 229, 204, 171, 130, 81, 24], [52, 105, 150, 187, 216, 237, 250, 249, 248, 247, 230, 205, 172, 131, 82, 25], [51, 104, 149, 186, 215, 236, 235, 234, 233, 232, 231, 206, 173, 132, 83, 26], [50, 103, 148, 185, 214, 213, 212, 211, 210, 209, 208, 207, 174, 133, 84, 27], [49, 102, 147, 184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 134, 85, 28], [48, 101, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 135, 86, 29], [47, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 30], [46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]]
