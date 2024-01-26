
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


def test_11():
    assert solution.Solution().spiralMatrixIII(78, 18, 24, 1) == [[24, 1], [24, 2], [25, 2], [25, 1], [25, 0], [24, 0], [23, 0], [23, 1], [23, 2], [23, 3], [24, 3], [25, 3], [26, 3], [26, 2], [26, 1], [26, 0], [22, 0], [22, 1], [22, 2], [22, 3], [22, 4], [23, 4], [24, 4], [25, 4], [26, 4], [27, 4], [27, 3], [27, 2], [27, 1], [27, 0], [21, 0], [21, 1], [21, 2], [21, 3], [21, 4], [21, 5], [22, 5], [23, 5], [24, 5], [25, 5], [26, 5], [27, 5], [28, 5], [28, 4], [28, 3], [28, 2], [28, 1], [28, 0], [20, 0], [20, 1], [20, 2], [20, 3], [20, 4], [20, 5], [20, 6], [21, 6], [22, 6], [23, 6], [24, 6], [25, 6], [26, 6], [27, 6], [28, 6], [29, 6], [29, 5], [29, 4], [29, 3], [29, 2], [29, 1], [29, 0], [19, 0], [19, 1], [19, 2], [19, 3], [19, 4], [19, 5], [19, 6], [19, 7], [20, 7], [21, 7], [22, 7], [23, 7], [24, 7], [25, 7], [26, 7], [27, 7], [28, 7], [29, 7], [30, 7], [30, 6], [30, 5], [30, 4], [30, 3], [30, 2], [30, 1], [30, 0], [18, 0], [18, 1], [18, 2], [18, 3], [18, 4], [18, 5], [18, 6], [18, 7], [18, 8], [19, 8], [20, 8], [21, 8], [22, 8], [23, 8], [24, 8], [25, 8], [26, 8], [27, 8], [28, 8], [29, 8], [30, 8], [31, 8], [31, 7], [31, 6], [31, 5], [31, 4], [31, 3], [31, 2], [31, 1], [31, 0], [17, 0], [17, 1], [17, 2], [17, 3], [17, 4], [17, 5], [17, 6], [17, 7], [17, 8], [17, 9], [18, 9], [19, 9], [20, 9], [21, 9], [22, 9], [23, 9], [24, 9], [25, 9], [26, 9], [27, 9], [28, 9], [29, 9], [30, 9], [31, 9], [32, 9], [32, 8], [32, 7], [32, 6], [32, 5], [32, 4], [32, 3], [32, 2], [32, 1], [32, 0], [16, 0], [16, 1], [16, 2], [16, 3], [16, 4], [16, 5], [16, 6], [16, 7], [16, 8], [16, 9], [16, 10], [17, 10], [18, 10], [19, 10], [20, 10], [21, 10], [22, 10], [23, 10], [24, 10], [25, 10], [26, 10], [27, 10], [28, 10], [29, 10], [30, 10], [31, 10], [32, 10], [33, 10], [33, 9], [33, 8], [33, 7], [33, 6], [33, 5], [33, 4], [33, 3], [33, 2], [33, 1], [33, 0], [15, 0], [15, 1], [15, 2], [15, 3], [15, 4], [15, 5], [15, 6], [15, 7], [15, 8], [15, 9], [15, 10], [15, 11], [16, 11], [17, 11], [18, 11], [19, 11], [20, 11], [21, 11], [22, 11], [23, 11], [24, 11], [25, 11], [26, 11], [27, 11], [28, 11], [29, 11], [30, 11], [31, 11], [32, 11], [33, 11], [34, 11], [34, 10], [34, 9], [34, 8], [34, 7], [34, 6], [34, 5], [34, 4], [34, 3], [34, 2], [34, 1], [34, 0], [14, 0], [14, 1], [14, 2], [14, 3], [14, 4], [14, 5], [14, 6], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [15, 12], [16, 12], [17, 12], [18, 12], [19, 12], [20, 12], [21, 12], [22, 12], [23, 12], [24, 12], [25, 12], [26, 12], [27, 12], [28, 12], [29, 12], [30, 12], [31, 12], [32, 12], [33, 12], [34, 12], [35, 12], [35, 11], [35, 10], [35, 9], [35, 8], [35, 7], [35, 6], [35, 5], [35, 4], [35, 3], [35, 2], [35, 1], [35, 0], [13, 0], [13, 1], [13, 2], [13, 3], [13, 4], [13, 5], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13], [14, 13], [15, 13], [16, 13], [17, 13], [18, 13], [19, 13], [20, 13], [21, 13], [22, 13], [23, 13], [24, 13], [25, 13], [26, 13], [27, 13], [28, 13], [29, 13], [30, 13], [31, 13], [32, 13], [33, 13], [34, 13], [35, 13], [36, 13], [36, 12], [36, 11], [36, 10], [36, 9], [36, 8], [36, 7], [36, 6], [36, 5], [36, 4], [36, 3], [36, 2], [36, 1], [36, 0], [12, 0], [12, 1], [12, 2], [12, 3], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [12, 12], [12, 13], [12, 14], [13, 14], [14, 14], [15, 14], [16, 14], [17, 14], [18, 14], [19, 14], [20, 14], [21, 14], [22, 14], [23, 14], [24, 14], [25, 14], [26, 14], [27, 14], [28, 14], [29, 14], [30, 14], [31, 14], [32, 14], [33, 14], [34, 14], [35, 14], [36, 14], [37, 14], [37, 13], [37, 12], [37, 11], [37, 10], [37, 9], [37, 8], [37, 7], [37, 6], [37, 5], [37, 4], [37, 3], [37, 2], [37, 1], [37, 0], [11, 0], [11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10], [11, 11], [11, 12], [11, 13], [11, 14], [11, 15], [12, 15], [13, 15], [14, 15], [15, 15], [16, 15], [17, 15], [18, 15], [19, 15], [20, 15], [21, 15], [22, 15], [23, 15], [24, 15], [25, 15], [26, 15], [27, 15], [28, 15], [29, 15], [30, 15], [31, 15], [32, 15], [33, 15], [34, 15], [35, 15], [36, 15], [37, 15], [38, 15], [38, 14], [38, 13], [38, 12], [38, 11], [38, 10], [38, 9], [38, 8], [38, 7], [38, 6], [38, 5], [38, 4], [38, 3], [38, 2], [38, 1], [38, 0], [10, 0], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10], [10, 11], [10, 12], [10, 13], [10, 14], [10, 15], [10, 16], [11, 16], [12, 16], [13, 16], [14, 16], [15, 16], [16, 16], [17, 16], [18, 16], [19, 16], [20, 16], [21, 16], [22, 16], [23, 16], [24, 16], [25, 16], [26, 16], [27, 16], [28, 16], [29, 16], [30, 16], [31, 16], [32, 16], [33, 16], [34, 16], [35, 16], [36, 16], [37, 16], [38, 16], [39, 16], [39, 15], [39, 14], [39, 13], [39, 12], [39, 11], [39, 10], [39, 9], [39, 8], [39, 7], [39, 6], [39, 5], [39, 4], [39, 3], [39, 2], [39, 1], [39, 0], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9], [9, 10], [9, 11], [9, 12], [9, 13], [9, 14], [9, 15], [9, 16], [9, 17], [10, 17], [11, 17], [12, 17], [13, 17], [14, 17], [15, 17], [16, 17], [17, 17], [18, 17], [19, 17], [20, 17], [21, 17], [22, 17], [23, 17], [24, 17], [25, 17], [26, 17], [27, 17], [28, 17], [29, 17], [30, 17], [31, 17], [32, 17], [33, 17], [34, 17], [35, 17], [36, 17], [37, 17], [38, 17], [39, 17], [40, 17], [40, 16], [40, 15], [40, 14], [40, 13], [40, 12], [40, 11], [40, 10], [40, 9], [40, 8], [40, 7], [40, 6], [40, 5], [40, 4], [40, 3], [40, 2], [40, 1], [40, 0], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [8, 10], [8, 11], [8, 12], [8, 13], [8, 14], [8, 15], [8, 16], [8, 17], [41, 17], [41, 16], [41, 15], [41, 14], [41, 13], [41, 12], [41, 11], [41, 10], [41, 9], [41, 8], [41, 7], [41, 6], [41, 5], [41, 4], [41, 3], [41, 2], [41, 1], [41, 0], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [7, 14], [7, 15], [7, 16], [7, 17], [42, 17], [42, 16], [42, 15], [42, 14], [42, 13], [42, 12], [42, 11], [42, 10], [42, 9], [42, 8], [42, 7], [42, 6], [42, 5], [42, 4], [42, 3], [42, 2], [42, 1], [42, 0], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [6, 15], [6, 16], [6, 17], [43, 17], [43, 16], [43, 15], [43, 14], [43, 13], [43, 12], [43, 11], [43, 10], [43, 9], [43, 8], [43, 7], [43, 6], [43, 5], [43, 4], [43, 3], [43, 2], [43, 1], [43, 0], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [5, 15], [5, 16], [5, 17], [44, 17], [44, 16], [44, 15], [44, 14], [44, 13], [44, 12], [44, 11], [44, 10], [44, 9], [44, 8], [44, 7], [44, 6], [44, 5], [44, 4], [44, 3], [44, 2], [44, 1], [44, 0], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12], [4, 13], [4, 14], [4, 15], [4, 16], [4, 17], [45, 17], [45, 16], [45, 15], [45, 14], [45, 13], [45, 12], [45, 11], [45, 10], [45, 9], [45, 8], [45, 7], [45, 6], [45, 5], [45, 4], [45, 3], [45, 2], [45, 1], [45, 0], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [3, 15], [3, 16], [3, 17], [46, 17], [46, 16], [46, 15], [46, 14], [46, 13], [46, 12], [46, 11], [46, 10], [46, 9], [46, 8], [46, 7], [46, 6], [46, 5], [46, 4], [46, 3], [46, 2], [46, 1], [46, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [2, 14], [2, 15], [2, 16], [2, 17], [47, 17], [47, 16], [47, 15], [47, 14], [47, 13], [47, 12], [47, 11], [47, 10], [47, 9], [47, 8], [47, 7], [47, 6], [47, 5], [47, 4], [47, 3], [47, 2], [47, 1], [47, 0], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15], [1, 16], [1, 17], [48, 17], [48, 16], [48, 15], [48, 14], [48, 13], [48, 12], [48, 11], [48, 10], [48, 9], [48, 8], [48, 7], [48, 6], [48, 5], [48, 4], [48, 3], [48, 2], [48, 1], [48, 0], [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [0, 15], [0, 16], [0, 17], [49, 17], [49, 16], [49, 15], [49, 14], [49, 13], [49, 12], [49, 11], [49, 10], [49, 9], [49, 8], [49, 7], [49, 6], [49, 5], [49, 4], [49, 3], [49, 2], [49, 1], [49, 0], [50, 17], [50, 16], [50, 15], [50, 14], [50, 13], [50, 12], [50, 11], [50, 10], [50, 9], [50, 8], [50, 7], [50, 6], [50, 5], [50, 4], [50, 3], [50, 2], [50, 1], [50, 0], [51, 17], [51, 16], [51, 15], [51, 14], [51, 13], [51, 12], [51, 11], [51, 10], [51, 9], [51, 8], [51, 7], [51, 6], [51, 5], [51, 4], [51, 3], [51, 2], [51, 1], [51, 0], [52, 17], [52, 16], [52, 15], [52, 14], [52, 13], [52, 12], [52, 11], [52, 10], [52, 9], [52, 8], [52, 7], [52, 6], [52, 5], [52, 4], [52, 3], [52, 2], [52, 1], [52, 0], [53, 17], [53, 16], [53, 15], [53, 14], [53, 13], [53, 12], [53, 11], [53, 10], [53, 9], [53, 8], [53, 7], [53, 6], [53, 5], [53, 4], [53, 3], [53, 2], [53, 1], [53, 0], [54, 17], [54, 16], [54, 15], [54, 14], [54, 13], [54, 12], [54, 11], [54, 10], [54, 9], [54, 8], [54, 7], [54, 6], [54, 5], [54, 4], [54, 3], [54, 2], [54, 1], [54, 0], [55, 17], [55, 16], [55, 15], [55, 14], [55, 13], [55, 12], [55, 11], [55, 10], [55, 9], [55, 8], [55, 7], [55, 6], [55, 5], [55, 4], [55, 3], [55, 2], [55, 1], [55, 0], [56, 17], [56, 16], [56, 15], [56, 14], [56, 13], [56, 12], [56, 11], [56, 10], [56, 9], [56, 8], [56, 7], [56, 6], [56, 5], [56, 4], [56, 3], [56, 2], [56, 1], [56, 0], [57, 17], [57, 16], [57, 15], [57, 14], [57, 13], [57, 12], [57, 11], [57, 10], [57, 9], [57, 8], [57, 7], [57, 6], [57, 5], [57, 4], [57, 3], [57, 2], [57, 1], [57, 0], [58, 17], [58, 16], [58, 15], [58, 14], [58, 13], [58, 12], [58, 11], [58, 10], [58, 9], [58, 8], [58, 7], [58, 6], [58, 5], [58, 4], [58, 3], [58, 2], [58, 1], [58, 0], [59, 17], [59, 16], [59, 15], [59, 14], [59, 13], [59, 12], [59, 11], [59, 10], [59, 9], [59, 8], [59, 7], [59, 6], [59, 5], [59, 4], [59, 3], [59, 2], [59, 1], [59, 0], [60, 17], [60, 16], [60, 15], [60, 14], [60, 13], [60, 12], [60, 11], [60, 10], [60, 9], [60, 8], [60, 7], [60, 6], [60, 5], [60, 4], [60, 3], [60, 2], [60, 1], [60, 0], [61, 17], [61, 16], [61, 15], [61, 14], [61, 13], [61, 12], [61, 11], [61, 10], [61, 9], [61, 8], [61, 7], [61, 6], [61, 5], [61, 4], [61, 3], [61, 2], [61, 1], [61, 0], [62, 17], [62, 16], [62, 15], [62, 14], [62, 13], [62, 12], [62, 11], [62, 10], [62, 9], [62, 8], [62, 7], [62, 6], [62, 5], [62, 4], [62, 3], [62, 2], [62, 1], [62, 0], [63, 17], [63, 16], [63, 15], [63, 14], [63, 13], [63, 12], [63, 11], [63, 10], [63, 9], [63, 8], [63, 7], [63, 6], [63, 5], [63, 4], [63, 3], [63, 2], [63, 1], [63, 0], [64, 17], [64, 16], [64, 15], [64, 14], [64, 13], [64, 12], [64, 11], [64, 10], [64, 9], [64, 8], [64, 7], [64, 6], [64, 5], [64, 4], [64, 3], [64, 2], [64, 1], [64, 0], [65, 17], [65, 16], [65, 15], [65, 14], [65, 13], [65, 12], [65, 11], [65, 10], [65, 9], [65, 8], [65, 7], [65, 6], [65, 5], [65, 4], [65, 3], [65, 2], [65, 1], [65, 0], [66, 17], [66, 16], [66, 15], [66, 14], [66, 13], [66, 12], [66, 11], [66, 10], [66, 9], [66, 8], [66, 7], [66, 6], [66, 5], [66, 4], [66, 3], [66, 2], [66, 1], [66, 0], [67, 17], [67, 16], [67, 15], [67, 14], [67, 13], [67, 12], [67, 11], [67, 10], [67, 9], [67, 8], [67, 7], [67, 6], [67, 5], [67, 4], [67, 3], [67, 2], [67, 1], [67, 0], [68, 17], [68, 16], [68, 15], [68, 14], [68, 13], [68, 12], [68, 11], [68, 10], [68, 9], [68, 8], [68, 7], [68, 6], [68, 5], [68, 4], [68, 3], [68, 2], [68, 1], [68, 0], [69, 17], [69, 16], [69, 15], [69, 14], [69, 13], [69, 12], [69, 11], [69, 10], [69, 9], [69, 8], [69, 7], [69, 6], [69, 5], [69, 4], [69, 3], [69, 2], [69, 1], [69, 0], [70, 17], [70, 16], [70, 15], [70, 14], [70, 13], [70, 12], [70, 11], [70, 10], [70, 9], [70, 8], [70, 7], [70, 6], [70, 5], [70, 4], [70, 3], [70, 2], [70, 1], [70, 0], [71, 17], [71, 16], [71, 15], [71, 14], [71, 13], [71, 12], [71, 11], [71, 10], [71, 9], [71, 8], [71, 7], [71, 6], [71, 5], [71, 4], [71, 3], [71, 2], [71, 1], [71, 0], [72, 17], [72, 16], [72, 15], [72, 14], [72, 13], [72, 12], [72, 11], [72, 10], [72, 9], [72, 8], [72, 7], [72, 6], [72, 5], [72, 4], [72, 3], [72, 2], [72, 1], [72, 0], [73, 17], [73, 16], [73, 15], [73, 14], [73, 13], [73, 12], [73, 11], [73, 10], [73, 9], [73, 8], [73, 7], [73, 6], [73, 5], [73, 4], [73, 3], [73, 2], [73, 1], [73, 0], [74, 17], [74, 16], [74, 15], [74, 14], [74, 13], [74, 12], [74, 11], [74, 10], [74, 9], [74, 8], [74, 7], [74, 6], [74, 5], [74, 4], [74, 3], [74, 2], [74, 1], [74, 0], [75, 17], [75, 16], [75, 15], [75, 14], [75, 13], [75, 12], [75, 11], [75, 10], [75, 9], [75, 8], [75, 7], [75, 6], [75, 5], [75, 4], [75, 3], [75, 2], [75, 1], [75, 0], [76, 17], [76, 16], [76, 15], [76, 14], [76, 13], [76, 12], [76, 11], [76, 10], [76, 9], [76, 8], [76, 7], [76, 6], [76, 5], [76, 4], [76, 3], [76, 2], [76, 1], [76, 0], [77, 17], [77, 16], [77, 15], [77, 14], [77, 13], [77, 12], [77, 11], [77, 10], [77, 9], [77, 8], [77, 7], [77, 6], [77, 5], [77, 4], [77, 3], [77, 2], [77, 1], [77, 0]]
