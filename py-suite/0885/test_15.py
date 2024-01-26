
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
    assert solution.Solution().spiralMatrixIII(81, 16, 2, 16) == [[2, 16], [3, 15], [2, 15], [1, 15], [4, 15], [4, 14], [3, 14], [2, 14], [1, 14], [0, 14], [0, 15], [5, 15], [5, 14], [5, 13], [4, 13], [3, 13], [2, 13], [1, 13], [0, 13], [6, 15], [6, 14], [6, 13], [6, 12], [5, 12], [4, 12], [3, 12], [2, 12], [1, 12], [0, 12], [7, 15], [7, 14], [7, 13], [7, 12], [7, 11], [6, 11], [5, 11], [4, 11], [3, 11], [2, 11], [1, 11], [0, 11], [8, 15], [8, 14], [8, 13], [8, 12], [8, 11], [8, 10], [7, 10], [6, 10], [5, 10], [4, 10], [3, 10], [2, 10], [1, 10], [0, 10], [9, 15], [9, 14], [9, 13], [9, 12], [9, 11], [9, 10], [9, 9], [8, 9], [7, 9], [6, 9], [5, 9], [4, 9], [3, 9], [2, 9], [1, 9], [0, 9], [10, 15], [10, 14], [10, 13], [10, 12], [10, 11], [10, 10], [10, 9], [10, 8], [9, 8], [8, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8], [11, 15], [11, 14], [11, 13], [11, 12], [11, 11], [11, 10], [11, 9], [11, 8], [11, 7], [10, 7], [9, 7], [8, 7], [7, 7], [6, 7], [5, 7], [4, 7], [3, 7], [2, 7], [1, 7], [0, 7], [12, 15], [12, 14], [12, 13], [12, 12], [12, 11], [12, 10], [12, 9], [12, 8], [12, 7], [12, 6], [11, 6], [10, 6], [9, 6], [8, 6], [7, 6], [6, 6], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6], [13, 15], [13, 14], [13, 13], [13, 12], [13, 11], [13, 10], [13, 9], [13, 8], [13, 7], [13, 6], [13, 5], [12, 5], [11, 5], [10, 5], [9, 5], [8, 5], [7, 5], [6, 5], [5, 5], [4, 5], [3, 5], [2, 5], [1, 5], [0, 5], [14, 15], [14, 14], [14, 13], [14, 12], [14, 11], [14, 10], [14, 9], [14, 8], [14, 7], [14, 6], [14, 5], [14, 4], [13, 4], [12, 4], [11, 4], [10, 4], [9, 4], [8, 4], [7, 4], [6, 4], [5, 4], [4, 4], [3, 4], [2, 4], [1, 4], [0, 4], [15, 15], [15, 14], [15, 13], [15, 12], [15, 11], [15, 10], [15, 9], [15, 8], [15, 7], [15, 6], [15, 5], [15, 4], [15, 3], [14, 3], [13, 3], [12, 3], [11, 3], [10, 3], [9, 3], [8, 3], [7, 3], [6, 3], [5, 3], [4, 3], [3, 3], [2, 3], [1, 3], [0, 3], [16, 15], [16, 14], [16, 13], [16, 12], [16, 11], [16, 10], [16, 9], [16, 8], [16, 7], [16, 6], [16, 5], [16, 4], [16, 3], [16, 2], [15, 2], [14, 2], [13, 2], [12, 2], [11, 2], [10, 2], [9, 2], [8, 2], [7, 2], [6, 2], [5, 2], [4, 2], [3, 2], [2, 2], [1, 2], [0, 2], [17, 15], [17, 14], [17, 13], [17, 12], [17, 11], [17, 10], [17, 9], [17, 8], [17, 7], [17, 6], [17, 5], [17, 4], [17, 3], [17, 2], [17, 1], [16, 1], [15, 1], [14, 1], [13, 1], [12, 1], [11, 1], [10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [18, 15], [18, 14], [18, 13], [18, 12], [18, 11], [18, 10], [18, 9], [18, 8], [18, 7], [18, 6], [18, 5], [18, 4], [18, 3], [18, 2], [18, 1], [18, 0], [17, 0], [16, 0], [15, 0], [14, 0], [13, 0], [12, 0], [11, 0], [10, 0], [9, 0], [8, 0], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0], [19, 15], [19, 14], [19, 13], [19, 12], [19, 11], [19, 10], [19, 9], [19, 8], [19, 7], [19, 6], [19, 5], [19, 4], [19, 3], [19, 2], [19, 1], [19, 0], [20, 15], [20, 14], [20, 13], [20, 12], [20, 11], [20, 10], [20, 9], [20, 8], [20, 7], [20, 6], [20, 5], [20, 4], [20, 3], [20, 2], [20, 1], [20, 0], [21, 15], [21, 14], [21, 13], [21, 12], [21, 11], [21, 10], [21, 9], [21, 8], [21, 7], [21, 6], [21, 5], [21, 4], [21, 3], [21, 2], [21, 1], [21, 0], [22, 15], [22, 14], [22, 13], [22, 12], [22, 11], [22, 10], [22, 9], [22, 8], [22, 7], [22, 6], [22, 5], [22, 4], [22, 3], [22, 2], [22, 1], [22, 0], [23, 15], [23, 14], [23, 13], [23, 12], [23, 11], [23, 10], [23, 9], [23, 8], [23, 7], [23, 6], [23, 5], [23, 4], [23, 3], [23, 2], [23, 1], [23, 0], [24, 15], [24, 14], [24, 13], [24, 12], [24, 11], [24, 10], [24, 9], [24, 8], [24, 7], [24, 6], [24, 5], [24, 4], [24, 3], [24, 2], [24, 1], [24, 0], [25, 15], [25, 14], [25, 13], [25, 12], [25, 11], [25, 10], [25, 9], [25, 8], [25, 7], [25, 6], [25, 5], [25, 4], [25, 3], [25, 2], [25, 1], [25, 0], [26, 15], [26, 14], [26, 13], [26, 12], [26, 11], [26, 10], [26, 9], [26, 8], [26, 7], [26, 6], [26, 5], [26, 4], [26, 3], [26, 2], [26, 1], [26, 0], [27, 15], [27, 14], [27, 13], [27, 12], [27, 11], [27, 10], [27, 9], [27, 8], [27, 7], [27, 6], [27, 5], [27, 4], [27, 3], [27, 2], [27, 1], [27, 0], [28, 15], [28, 14], [28, 13], [28, 12], [28, 11], [28, 10], [28, 9], [28, 8], [28, 7], [28, 6], [28, 5], [28, 4], [28, 3], [28, 2], [28, 1], [28, 0], [29, 15], [29, 14], [29, 13], [29, 12], [29, 11], [29, 10], [29, 9], [29, 8], [29, 7], [29, 6], [29, 5], [29, 4], [29, 3], [29, 2], [29, 1], [29, 0], [30, 15], [30, 14], [30, 13], [30, 12], [30, 11], [30, 10], [30, 9], [30, 8], [30, 7], [30, 6], [30, 5], [30, 4], [30, 3], [30, 2], [30, 1], [30, 0], [31, 15], [31, 14], [31, 13], [31, 12], [31, 11], [31, 10], [31, 9], [31, 8], [31, 7], [31, 6], [31, 5], [31, 4], [31, 3], [31, 2], [31, 1], [31, 0], [32, 15], [32, 14], [32, 13], [32, 12], [32, 11], [32, 10], [32, 9], [32, 8], [32, 7], [32, 6], [32, 5], [32, 4], [32, 3], [32, 2], [32, 1], [32, 0], [33, 15], [33, 14], [33, 13], [33, 12], [33, 11], [33, 10], [33, 9], [33, 8], [33, 7], [33, 6], [33, 5], [33, 4], [33, 3], [33, 2], [33, 1], [33, 0], [34, 15], [34, 14], [34, 13], [34, 12], [34, 11], [34, 10], [34, 9], [34, 8], [34, 7], [34, 6], [34, 5], [34, 4], [34, 3], [34, 2], [34, 1], [34, 0], [35, 15], [35, 14], [35, 13], [35, 12], [35, 11], [35, 10], [35, 9], [35, 8], [35, 7], [35, 6], [35, 5], [35, 4], [35, 3], [35, 2], [35, 1], [35, 0], [36, 15], [36, 14], [36, 13], [36, 12], [36, 11], [36, 10], [36, 9], [36, 8], [36, 7], [36, 6], [36, 5], [36, 4], [36, 3], [36, 2], [36, 1], [36, 0], [37, 15], [37, 14], [37, 13], [37, 12], [37, 11], [37, 10], [37, 9], [37, 8], [37, 7], [37, 6], [37, 5], [37, 4], [37, 3], [37, 2], [37, 1], [37, 0], [38, 15], [38, 14], [38, 13], [38, 12], [38, 11], [38, 10], [38, 9], [38, 8], [38, 7], [38, 6], [38, 5], [38, 4], [38, 3], [38, 2], [38, 1], [38, 0], [39, 15], [39, 14], [39, 13], [39, 12], [39, 11], [39, 10], [39, 9], [39, 8], [39, 7], [39, 6], [39, 5], [39, 4], [39, 3], [39, 2], [39, 1], [39, 0], [40, 15], [40, 14], [40, 13], [40, 12], [40, 11], [40, 10], [40, 9], [40, 8], [40, 7], [40, 6], [40, 5], [40, 4], [40, 3], [40, 2], [40, 1], [40, 0], [41, 15], [41, 14], [41, 13], [41, 12], [41, 11], [41, 10], [41, 9], [41, 8], [41, 7], [41, 6], [41, 5], [41, 4], [41, 3], [41, 2], [41, 1], [41, 0], [42, 15], [42, 14], [42, 13], [42, 12], [42, 11], [42, 10], [42, 9], [42, 8], [42, 7], [42, 6], [42, 5], [42, 4], [42, 3], [42, 2], [42, 1], [42, 0], [43, 15], [43, 14], [43, 13], [43, 12], [43, 11], [43, 10], [43, 9], [43, 8], [43, 7], [43, 6], [43, 5], [43, 4], [43, 3], [43, 2], [43, 1], [43, 0], [44, 15], [44, 14], [44, 13], [44, 12], [44, 11], [44, 10], [44, 9], [44, 8], [44, 7], [44, 6], [44, 5], [44, 4], [44, 3], [44, 2], [44, 1], [44, 0], [45, 15], [45, 14], [45, 13], [45, 12], [45, 11], [45, 10], [45, 9], [45, 8], [45, 7], [45, 6], [45, 5], [45, 4], [45, 3], [45, 2], [45, 1], [45, 0], [46, 15], [46, 14], [46, 13], [46, 12], [46, 11], [46, 10], [46, 9], [46, 8], [46, 7], [46, 6], [46, 5], [46, 4], [46, 3], [46, 2], [46, 1], [46, 0], [47, 15], [47, 14], [47, 13], [47, 12], [47, 11], [47, 10], [47, 9], [47, 8], [47, 7], [47, 6], [47, 5], [47, 4], [47, 3], [47, 2], [47, 1], [47, 0], [48, 15], [48, 14], [48, 13], [48, 12], [48, 11], [48, 10], [48, 9], [48, 8], [48, 7], [48, 6], [48, 5], [48, 4], [48, 3], [48, 2], [48, 1], [48, 0], [49, 15], [49, 14], [49, 13], [49, 12], [49, 11], [49, 10], [49, 9], [49, 8], [49, 7], [49, 6], [49, 5], [49, 4], [49, 3], [49, 2], [49, 1], [49, 0], [50, 15], [50, 14], [50, 13], [50, 12], [50, 11], [50, 10], [50, 9], [50, 8], [50, 7], [50, 6], [50, 5], [50, 4], [50, 3], [50, 2], [50, 1], [50, 0], [51, 15], [51, 14], [51, 13], [51, 12], [51, 11], [51, 10], [51, 9], [51, 8], [51, 7], [51, 6], [51, 5], [51, 4], [51, 3], [51, 2], [51, 1], [51, 0], [52, 15], [52, 14], [52, 13], [52, 12], [52, 11], [52, 10], [52, 9], [52, 8], [52, 7], [52, 6], [52, 5], [52, 4], [52, 3], [52, 2], [52, 1], [52, 0], [53, 15], [53, 14], [53, 13], [53, 12], [53, 11], [53, 10], [53, 9], [53, 8], [53, 7], [53, 6], [53, 5], [53, 4], [53, 3], [53, 2], [53, 1], [53, 0], [54, 15], [54, 14], [54, 13], [54, 12], [54, 11], [54, 10], [54, 9], [54, 8], [54, 7], [54, 6], [54, 5], [54, 4], [54, 3], [54, 2], [54, 1], [54, 0], [55, 15], [55, 14], [55, 13], [55, 12], [55, 11], [55, 10], [55, 9], [55, 8], [55, 7], [55, 6], [55, 5], [55, 4], [55, 3], [55, 2], [55, 1], [55, 0], [56, 15], [56, 14], [56, 13], [56, 12], [56, 11], [56, 10], [56, 9], [56, 8], [56, 7], [56, 6], [56, 5], [56, 4], [56, 3], [56, 2], [56, 1], [56, 0], [57, 15], [57, 14], [57, 13], [57, 12], [57, 11], [57, 10], [57, 9], [57, 8], [57, 7], [57, 6], [57, 5], [57, 4], [57, 3], [57, 2], [57, 1], [57, 0], [58, 15], [58, 14], [58, 13], [58, 12], [58, 11], [58, 10], [58, 9], [58, 8], [58, 7], [58, 6], [58, 5], [58, 4], [58, 3], [58, 2], [58, 1], [58, 0], [59, 15], [59, 14], [59, 13], [59, 12], [59, 11], [59, 10], [59, 9], [59, 8], [59, 7], [59, 6], [59, 5], [59, 4], [59, 3], [59, 2], [59, 1], [59, 0], [60, 15], [60, 14], [60, 13], [60, 12], [60, 11], [60, 10], [60, 9], [60, 8], [60, 7], [60, 6], [60, 5], [60, 4], [60, 3], [60, 2], [60, 1], [60, 0], [61, 15], [61, 14], [61, 13], [61, 12], [61, 11], [61, 10], [61, 9], [61, 8], [61, 7], [61, 6], [61, 5], [61, 4], [61, 3], [61, 2], [61, 1], [61, 0], [62, 15], [62, 14], [62, 13], [62, 12], [62, 11], [62, 10], [62, 9], [62, 8], [62, 7], [62, 6], [62, 5], [62, 4], [62, 3], [62, 2], [62, 1], [62, 0], [63, 15], [63, 14], [63, 13], [63, 12], [63, 11], [63, 10], [63, 9], [63, 8], [63, 7], [63, 6], [63, 5], [63, 4], [63, 3], [63, 2], [63, 1], [63, 0], [64, 15], [64, 14], [64, 13], [64, 12], [64, 11], [64, 10], [64, 9], [64, 8], [64, 7], [64, 6], [64, 5], [64, 4], [64, 3], [64, 2], [64, 1], [64, 0], [65, 15], [65, 14], [65, 13], [65, 12], [65, 11], [65, 10], [65, 9], [65, 8], [65, 7], [65, 6], [65, 5], [65, 4], [65, 3], [65, 2], [65, 1], [65, 0], [66, 15], [66, 14], [66, 13], [66, 12], [66, 11], [66, 10], [66, 9], [66, 8], [66, 7], [66, 6], [66, 5], [66, 4], [66, 3], [66, 2], [66, 1], [66, 0], [67, 15], [67, 14], [67, 13], [67, 12], [67, 11], [67, 10], [67, 9], [67, 8], [67, 7], [67, 6], [67, 5], [67, 4], [67, 3], [67, 2], [67, 1], [67, 0], [68, 15], [68, 14], [68, 13], [68, 12], [68, 11], [68, 10], [68, 9], [68, 8], [68, 7], [68, 6], [68, 5], [68, 4], [68, 3], [68, 2], [68, 1], [68, 0], [69, 15], [69, 14], [69, 13], [69, 12], [69, 11], [69, 10], [69, 9], [69, 8], [69, 7], [69, 6], [69, 5], [69, 4], [69, 3], [69, 2], [69, 1], [69, 0], [70, 15], [70, 14], [70, 13], [70, 12], [70, 11], [70, 10], [70, 9], [70, 8], [70, 7], [70, 6], [70, 5], [70, 4], [70, 3], [70, 2], [70, 1], [70, 0], [71, 15], [71, 14], [71, 13], [71, 12], [71, 11], [71, 10], [71, 9], [71, 8], [71, 7], [71, 6], [71, 5], [71, 4], [71, 3], [71, 2], [71, 1], [71, 0], [72, 15], [72, 14], [72, 13], [72, 12], [72, 11], [72, 10], [72, 9], [72, 8], [72, 7], [72, 6], [72, 5], [72, 4], [72, 3], [72, 2], [72, 1], [72, 0], [73, 15], [73, 14], [73, 13], [73, 12], [73, 11], [73, 10], [73, 9], [73, 8], [73, 7], [73, 6], [73, 5], [73, 4], [73, 3], [73, 2], [73, 1], [73, 0], [74, 15], [74, 14], [74, 13], [74, 12], [74, 11], [74, 10], [74, 9], [74, 8], [74, 7], [74, 6], [74, 5], [74, 4], [74, 3], [74, 2], [74, 1], [74, 0], [75, 15], [75, 14], [75, 13], [75, 12], [75, 11], [75, 10], [75, 9], [75, 8], [75, 7], [75, 6], [75, 5], [75, 4], [75, 3], [75, 2], [75, 1], [75, 0], [76, 15], [76, 14], [76, 13], [76, 12], [76, 11], [76, 10], [76, 9], [76, 8], [76, 7], [76, 6], [76, 5], [76, 4], [76, 3], [76, 2], [76, 1], [76, 0], [77, 15], [77, 14], [77, 13], [77, 12], [77, 11], [77, 10], [77, 9], [77, 8], [77, 7], [77, 6], [77, 5], [77, 4], [77, 3], [77, 2], [77, 1], [77, 0], [78, 15], [78, 14], [78, 13], [78, 12], [78, 11], [78, 10], [78, 9], [78, 8], [78, 7], [78, 6], [78, 5], [78, 4], [78, 3], [78, 2], [78, 1], [78, 0], [79, 15], [79, 14], [79, 13], [79, 12], [79, 11], [79, 10], [79, 9], [79, 8], [79, 7], [79, 6], [79, 5], [79, 4], [79, 3], [79, 2], [79, 1], [79, 0], [80, 15], [80, 14], [80, 13], [80, 12], [80, 11], [80, 10], [80, 9], [80, 8], [80, 7], [80, 6], [80, 5], [80, 4], [80, 3], [80, 2], [80, 1], [80, 0]]