
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


def test_7():
    assert solution.Solution().spiralMatrixIII(13, 98, 24, 52) == [[24, 52], [12, 40], [12, 41], [12, 42], [12, 43], [12, 44], [12, 45], [12, 46], [12, 47], [12, 48], [12, 49], [12, 50], [12, 51], [12, 52], [12, 53], [12, 54], [12, 55], [12, 56], [12, 57], [12, 58], [12, 59], [12, 60], [12, 61], [12, 62], [12, 63], [12, 64], [12, 65], [12, 39], [11, 39], [11, 40], [11, 41], [11, 42], [11, 43], [11, 44], [11, 45], [11, 46], [11, 47], [11, 48], [11, 49], [11, 50], [11, 51], [11, 52], [11, 53], [11, 54], [11, 55], [11, 56], [11, 57], [11, 58], [11, 59], [11, 60], [11, 61], [11, 62], [11, 63], [11, 64], [11, 65], [11, 66], [12, 66], [12, 38], [11, 38], [10, 38], [10, 39], [10, 40], [10, 41], [10, 42], [10, 43], [10, 44], [10, 45], [10, 46], [10, 47], [10, 48], [10, 49], [10, 50], [10, 51], [10, 52], [10, 53], [10, 54], [10, 55], [10, 56], [10, 57], [10, 58], [10, 59], [10, 60], [10, 61], [10, 62], [10, 63], [10, 64], [10, 65], [10, 66], [10, 67], [11, 67], [12, 67], [12, 37], [11, 37], [10, 37], [9, 37], [9, 38], [9, 39], [9, 40], [9, 41], [9, 42], [9, 43], [9, 44], [9, 45], [9, 46], [9, 47], [9, 48], [9, 49], [9, 50], [9, 51], [9, 52], [9, 53], [9, 54], [9, 55], [9, 56], [9, 57], [9, 58], [9, 59], [9, 60], [9, 61], [9, 62], [9, 63], [9, 64], [9, 65], [9, 66], [9, 67], [9, 68], [10, 68], [11, 68], [12, 68], [12, 36], [11, 36], [10, 36], [9, 36], [8, 36], [8, 37], [8, 38], [8, 39], [8, 40], [8, 41], [8, 42], [8, 43], [8, 44], [8, 45], [8, 46], [8, 47], [8, 48], [8, 49], [8, 50], [8, 51], [8, 52], [8, 53], [8, 54], [8, 55], [8, 56], [8, 57], [8, 58], [8, 59], [8, 60], [8, 61], [8, 62], [8, 63], [8, 64], [8, 65], [8, 66], [8, 67], [8, 68], [8, 69], [9, 69], [10, 69], [11, 69], [12, 69], [12, 35], [11, 35], [10, 35], [9, 35], [8, 35], [7, 35], [7, 36], [7, 37], [7, 38], [7, 39], [7, 40], [7, 41], [7, 42], [7, 43], [7, 44], [7, 45], [7, 46], [7, 47], [7, 48], [7, 49], [7, 50], [7, 51], [7, 52], [7, 53], [7, 54], [7, 55], [7, 56], [7, 57], [7, 58], [7, 59], [7, 60], [7, 61], [7, 62], [7, 63], [7, 64], [7, 65], [7, 66], [7, 67], [7, 68], [7, 69], [7, 70], [8, 70], [9, 70], [10, 70], [11, 70], [12, 70], [12, 34], [11, 34], [10, 34], [9, 34], [8, 34], [7, 34], [6, 34], [6, 35], [6, 36], [6, 37], [6, 38], [6, 39], [6, 40], [6, 41], [6, 42], [6, 43], [6, 44], [6, 45], [6, 46], [6, 47], [6, 48], [6, 49], [6, 50], [6, 51], [6, 52], [6, 53], [6, 54], [6, 55], [6, 56], [6, 57], [6, 58], [6, 59], [6, 60], [6, 61], [6, 62], [6, 63], [6, 64], [6, 65], [6, 66], [6, 67], [6, 68], [6, 69], [6, 70], [6, 71], [7, 71], [8, 71], [9, 71], [10, 71], [11, 71], [12, 71], [12, 33], [11, 33], [10, 33], [9, 33], [8, 33], [7, 33], [6, 33], [5, 33], [5, 34], [5, 35], [5, 36], [5, 37], [5, 38], [5, 39], [5, 40], [5, 41], [5, 42], [5, 43], [5, 44], [5, 45], [5, 46], [5, 47], [5, 48], [5, 49], [5, 50], [5, 51], [5, 52], [5, 53], [5, 54], [5, 55], [5, 56], [5, 57], [5, 58], [5, 59], [5, 60], [5, 61], [5, 62], [5, 63], [5, 64], [5, 65], [5, 66], [5, 67], [5, 68], [5, 69], [5, 70], [5, 71], [5, 72], [6, 72], [7, 72], [8, 72], [9, 72], [10, 72], [11, 72], [12, 72], [12, 32], [11, 32], [10, 32], [9, 32], [8, 32], [7, 32], [6, 32], [5, 32], [4, 32], [4, 33], [4, 34], [4, 35], [4, 36], [4, 37], [4, 38], [4, 39], [4, 40], [4, 41], [4, 42], [4, 43], [4, 44], [4, 45], [4, 46], [4, 47], [4, 48], [4, 49], [4, 50], [4, 51], [4, 52], [4, 53], [4, 54], [4, 55], [4, 56], [4, 57], [4, 58], [4, 59], [4, 60], [4, 61], [4, 62], [4, 63], [4, 64], [4, 65], [4, 66], [4, 67], [4, 68], [4, 69], [4, 70], [4, 71], [4, 72], [4, 73], [5, 73], [6, 73], [7, 73], [8, 73], [9, 73], [10, 73], [11, 73], [12, 73], [12, 31], [11, 31], [10, 31], [9, 31], [8, 31], [7, 31], [6, 31], [5, 31], [4, 31], [3, 31], [3, 32], [3, 33], [3, 34], [3, 35], [3, 36], [3, 37], [3, 38], [3, 39], [3, 40], [3, 41], [3, 42], [3, 43], [3, 44], [3, 45], [3, 46], [3, 47], [3, 48], [3, 49], [3, 50], [3, 51], [3, 52], [3, 53], [3, 54], [3, 55], [3, 56], [3, 57], [3, 58], [3, 59], [3, 60], [3, 61], [3, 62], [3, 63], [3, 64], [3, 65], [3, 66], [3, 67], [3, 68], [3, 69], [3, 70], [3, 71], [3, 72], [3, 73], [3, 74], [4, 74], [5, 74], [6, 74], [7, 74], [8, 74], [9, 74], [10, 74], [11, 74], [12, 74], [12, 30], [11, 30], [10, 30], [9, 30], [8, 30], [7, 30], [6, 30], [5, 30], [4, 30], [3, 30], [2, 30], [2, 31], [2, 32], [2, 33], [2, 34], [2, 35], [2, 36], [2, 37], [2, 38], [2, 39], [2, 40], [2, 41], [2, 42], [2, 43], [2, 44], [2, 45], [2, 46], [2, 47], [2, 48], [2, 49], [2, 50], [2, 51], [2, 52], [2, 53], [2, 54], [2, 55], [2, 56], [2, 57], [2, 58], [2, 59], [2, 60], [2, 61], [2, 62], [2, 63], [2, 64], [2, 65], [2, 66], [2, 67], [2, 68], [2, 69], [2, 70], [2, 71], [2, 72], [2, 73], [2, 74], [2, 75], [3, 75], [4, 75], [5, 75], [6, 75], [7, 75], [8, 75], [9, 75], [10, 75], [11, 75], [12, 75], [12, 29], [11, 29], [10, 29], [9, 29], [8, 29], [7, 29], [6, 29], [5, 29], [4, 29], [3, 29], [2, 29], [1, 29], [1, 30], [1, 31], [1, 32], [1, 33], [1, 34], [1, 35], [1, 36], [1, 37], [1, 38], [1, 39], [1, 40], [1, 41], [1, 42], [1, 43], [1, 44], [1, 45], [1, 46], [1, 47], [1, 48], [1, 49], [1, 50], [1, 51], [1, 52], [1, 53], [1, 54], [1, 55], [1, 56], [1, 57], [1, 58], [1, 59], [1, 60], [1, 61], [1, 62], [1, 63], [1, 64], [1, 65], [1, 66], [1, 67], [1, 68], [1, 69], [1, 70], [1, 71], [1, 72], [1, 73], [1, 74], [1, 75], [1, 76], [2, 76], [3, 76], [4, 76], [5, 76], [6, 76], [7, 76], [8, 76], [9, 76], [10, 76], [11, 76], [12, 76], [12, 28], [11, 28], [10, 28], [9, 28], [8, 28], [7, 28], [6, 28], [5, 28], [4, 28], [3, 28], [2, 28], [1, 28], [0, 28], [0, 29], [0, 30], [0, 31], [0, 32], [0, 33], [0, 34], [0, 35], [0, 36], [0, 37], [0, 38], [0, 39], [0, 40], [0, 41], [0, 42], [0, 43], [0, 44], [0, 45], [0, 46], [0, 47], [0, 48], [0, 49], [0, 50], [0, 51], [0, 52], [0, 53], [0, 54], [0, 55], [0, 56], [0, 57], [0, 58], [0, 59], [0, 60], [0, 61], [0, 62], [0, 63], [0, 64], [0, 65], [0, 66], [0, 67], [0, 68], [0, 69], [0, 70], [0, 71], [0, 72], [0, 73], [0, 74], [0, 75], [0, 76], [0, 77], [1, 77], [2, 77], [3, 77], [4, 77], [5, 77], [6, 77], [7, 77], [8, 77], [9, 77], [10, 77], [11, 77], [12, 77], [12, 27], [11, 27], [10, 27], [9, 27], [8, 27], [7, 27], [6, 27], [5, 27], [4, 27], [3, 27], [2, 27], [1, 27], [0, 27], [0, 78], [1, 78], [2, 78], [3, 78], [4, 78], [5, 78], [6, 78], [7, 78], [8, 78], [9, 78], [10, 78], [11, 78], [12, 78], [12, 26], [11, 26], [10, 26], [9, 26], [8, 26], [7, 26], [6, 26], [5, 26], [4, 26], [3, 26], [2, 26], [1, 26], [0, 26], [0, 79], [1, 79], [2, 79], [3, 79], [4, 79], [5, 79], [6, 79], [7, 79], [8, 79], [9, 79], [10, 79], [11, 79], [12, 79], [12, 25], [11, 25], [10, 25], [9, 25], [8, 25], [7, 25], [6, 25], [5, 25], [4, 25], [3, 25], [2, 25], [1, 25], [0, 25], [0, 80], [1, 80], [2, 80], [3, 80], [4, 80], [5, 80], [6, 80], [7, 80], [8, 80], [9, 80], [10, 80], [11, 80], [12, 80], [12, 24], [11, 24], [10, 24], [9, 24], [8, 24], [7, 24], [6, 24], [5, 24], [4, 24], [3, 24], [2, 24], [1, 24], [0, 24], [0, 81], [1, 81], [2, 81], [3, 81], [4, 81], [5, 81], [6, 81], [7, 81], [8, 81], [9, 81], [10, 81], [11, 81], [12, 81], [12, 23], [11, 23], [10, 23], [9, 23], [8, 23], [7, 23], [6, 23], [5, 23], [4, 23], [3, 23], [2, 23], [1, 23], [0, 23], [0, 82], [1, 82], [2, 82], [3, 82], [4, 82], [5, 82], [6, 82], [7, 82], [8, 82], [9, 82], [10, 82], [11, 82], [12, 82], [12, 22], [11, 22], [10, 22], [9, 22], [8, 22], [7, 22], [6, 22], [5, 22], [4, 22], [3, 22], [2, 22], [1, 22], [0, 22], [0, 83], [1, 83], [2, 83], [3, 83], [4, 83], [5, 83], [6, 83], [7, 83], [8, 83], [9, 83], [10, 83], [11, 83], [12, 83], [12, 21], [11, 21], [10, 21], [9, 21], [8, 21], [7, 21], [6, 21], [5, 21], [4, 21], [3, 21], [2, 21], [1, 21], [0, 21], [0, 84], [1, 84], [2, 84], [3, 84], [4, 84], [5, 84], [6, 84], [7, 84], [8, 84], [9, 84], [10, 84], [11, 84], [12, 84], [12, 20], [11, 20], [10, 20], [9, 20], [8, 20], [7, 20], [6, 20], [5, 20], [4, 20], [3, 20], [2, 20], [1, 20], [0, 20], [0, 85], [1, 85], [2, 85], [3, 85], [4, 85], [5, 85], [6, 85], [7, 85], [8, 85], [9, 85], [10, 85], [11, 85], [12, 85], [12, 19], [11, 19], [10, 19], [9, 19], [8, 19], [7, 19], [6, 19], [5, 19], [4, 19], [3, 19], [2, 19], [1, 19], [0, 19], [0, 86], [1, 86], [2, 86], [3, 86], [4, 86], [5, 86], [6, 86], [7, 86], [8, 86], [9, 86], [10, 86], [11, 86], [12, 86], [12, 18], [11, 18], [10, 18], [9, 18], [8, 18], [7, 18], [6, 18], [5, 18], [4, 18], [3, 18], [2, 18], [1, 18], [0, 18], [0, 87], [1, 87], [2, 87], [3, 87], [4, 87], [5, 87], [6, 87], [7, 87], [8, 87], [9, 87], [10, 87], [11, 87], [12, 87], [12, 17], [11, 17], [10, 17], [9, 17], [8, 17], [7, 17], [6, 17], [5, 17], [4, 17], [3, 17], [2, 17], [1, 17], [0, 17], [0, 88], [1, 88], [2, 88], [3, 88], [4, 88], [5, 88], [6, 88], [7, 88], [8, 88], [9, 88], [10, 88], [11, 88], [12, 88], [12, 16], [11, 16], [10, 16], [9, 16], [8, 16], [7, 16], [6, 16], [5, 16], [4, 16], [3, 16], [2, 16], [1, 16], [0, 16], [0, 89], [1, 89], [2, 89], [3, 89], [4, 89], [5, 89], [6, 89], [7, 89], [8, 89], [9, 89], [10, 89], [11, 89], [12, 89], [12, 15], [11, 15], [10, 15], [9, 15], [8, 15], [7, 15], [6, 15], [5, 15], [4, 15], [3, 15], [2, 15], [1, 15], [0, 15], [0, 90], [1, 90], [2, 90], [3, 90], [4, 90], [5, 90], [6, 90], [7, 90], [8, 90], [9, 90], [10, 90], [11, 90], [12, 90], [12, 14], [11, 14], [10, 14], [9, 14], [8, 14], [7, 14], [6, 14], [5, 14], [4, 14], [3, 14], [2, 14], [1, 14], [0, 14], [0, 91], [1, 91], [2, 91], [3, 91], [4, 91], [5, 91], [6, 91], [7, 91], [8, 91], [9, 91], [10, 91], [11, 91], [12, 91], [12, 13], [11, 13], [10, 13], [9, 13], [8, 13], [7, 13], [6, 13], [5, 13], [4, 13], [3, 13], [2, 13], [1, 13], [0, 13], [0, 92], [1, 92], [2, 92], [3, 92], [4, 92], [5, 92], [6, 92], [7, 92], [8, 92], [9, 92], [10, 92], [11, 92], [12, 92], [12, 12], [11, 12], [10, 12], [9, 12], [8, 12], [7, 12], [6, 12], [5, 12], [4, 12], [3, 12], [2, 12], [1, 12], [0, 12], [0, 93], [1, 93], [2, 93], [3, 93], [4, 93], [5, 93], [6, 93], [7, 93], [8, 93], [9, 93], [10, 93], [11, 93], [12, 93], [12, 11], [11, 11], [10, 11], [9, 11], [8, 11], [7, 11], [6, 11], [5, 11], [4, 11], [3, 11], [2, 11], [1, 11], [0, 11], [0, 94], [1, 94], [2, 94], [3, 94], [4, 94], [5, 94], [6, 94], [7, 94], [8, 94], [9, 94], [10, 94], [11, 94], [12, 94], [12, 10], [11, 10], [10, 10], [9, 10], [8, 10], [7, 10], [6, 10], [5, 10], [4, 10], [3, 10], [2, 10], [1, 10], [0, 10], [0, 95], [1, 95], [2, 95], [3, 95], [4, 95], [5, 95], [6, 95], [7, 95], [8, 95], [9, 95], [10, 95], [11, 95], [12, 95], [12, 9], [11, 9], [10, 9], [9, 9], [8, 9], [7, 9], [6, 9], [5, 9], [4, 9], [3, 9], [2, 9], [1, 9], [0, 9], [0, 96], [1, 96], [2, 96], [3, 96], [4, 96], [5, 96], [6, 96], [7, 96], [8, 96], [9, 96], [10, 96], [11, 96], [12, 96], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8], [0, 97], [1, 97], [2, 97], [3, 97], [4, 97], [5, 97], [6, 97], [7, 97], [8, 97], [9, 97], [10, 97], [11, 97], [12, 97], [12, 7], [11, 7], [10, 7], [9, 7], [8, 7], [7, 7], [6, 7], [5, 7], [4, 7], [3, 7], [2, 7], [1, 7], [0, 7], [12, 6], [11, 6], [10, 6], [9, 6], [8, 6], [7, 6], [6, 6], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6], [12, 5], [11, 5], [10, 5], [9, 5], [8, 5], [7, 5], [6, 5], [5, 5], [4, 5], [3, 5], [2, 5], [1, 5], [0, 5], [12, 4], [11, 4], [10, 4], [9, 4], [8, 4], [7, 4], [6, 4], [5, 4], [4, 4], [3, 4], [2, 4], [1, 4], [0, 4], [12, 3], [11, 3], [10, 3], [9, 3], [8, 3], [7, 3], [6, 3], [5, 3], [4, 3], [3, 3], [2, 3], [1, 3], [0, 3], [12, 2], [11, 2], [10, 2], [9, 2], [8, 2], [7, 2], [6, 2], [5, 2], [4, 2], [3, 2], [2, 2], [1, 2], [0, 2], [12, 1], [11, 1], [10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [12, 0], [11, 0], [10, 0], [9, 0], [8, 0], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
