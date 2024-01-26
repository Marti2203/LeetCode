
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


def test_12():
    assert solution.Solution().spiralMatrixIII(71, 24, 49, 62) == [[49, 62], [70, 23], [69, 23], [68, 23], [67, 23], [66, 23], [65, 23], [64, 23], [63, 23], [62, 23], [61, 23], [60, 23], [59, 23], [58, 23], [57, 23], [56, 23], [55, 23], [54, 23], [53, 23], [52, 23], [51, 23], [50, 23], [49, 23], [48, 23], [47, 23], [46, 23], [45, 23], [44, 23], [43, 23], [42, 23], [41, 23], [40, 23], [39, 23], [38, 23], [37, 23], [36, 23], [35, 23], [34, 23], [33, 23], [32, 23], [31, 23], [30, 23], [29, 23], [28, 23], [27, 23], [26, 23], [25, 23], [24, 23], [23, 23], [22, 23], [21, 23], [20, 23], [19, 23], [18, 23], [17, 23], [16, 23], [15, 23], [14, 23], [13, 23], [12, 23], [11, 23], [10, 23], [70, 22], [69, 22], [68, 22], [67, 22], [66, 22], [65, 22], [64, 22], [63, 22], [62, 22], [61, 22], [60, 22], [59, 22], [58, 22], [57, 22], [56, 22], [55, 22], [54, 22], [53, 22], [52, 22], [51, 22], [50, 22], [49, 22], [48, 22], [47, 22], [46, 22], [45, 22], [44, 22], [43, 22], [42, 22], [41, 22], [40, 22], [39, 22], [38, 22], [37, 22], [36, 22], [35, 22], [34, 22], [33, 22], [32, 22], [31, 22], [30, 22], [29, 22], [28, 22], [27, 22], [26, 22], [25, 22], [24, 22], [23, 22], [22, 22], [21, 22], [20, 22], [19, 22], [18, 22], [17, 22], [16, 22], [15, 22], [14, 22], [13, 22], [12, 22], [11, 22], [10, 22], [9, 22], [9, 23], [70, 21], [69, 21], [68, 21], [67, 21], [66, 21], [65, 21], [64, 21], [63, 21], [62, 21], [61, 21], [60, 21], [59, 21], [58, 21], [57, 21], [56, 21], [55, 21], [54, 21], [53, 21], [52, 21], [51, 21], [50, 21], [49, 21], [48, 21], [47, 21], [46, 21], [45, 21], [44, 21], [43, 21], [42, 21], [41, 21], [40, 21], [39, 21], [38, 21], [37, 21], [36, 21], [35, 21], [34, 21], [33, 21], [32, 21], [31, 21], [30, 21], [29, 21], [28, 21], [27, 21], [26, 21], [25, 21], [24, 21], [23, 21], [22, 21], [21, 21], [20, 21], [19, 21], [18, 21], [17, 21], [16, 21], [15, 21], [14, 21], [13, 21], [12, 21], [11, 21], [10, 21], [9, 21], [8, 21], [8, 22], [8, 23], [70, 20], [69, 20], [68, 20], [67, 20], [66, 20], [65, 20], [64, 20], [63, 20], [62, 20], [61, 20], [60, 20], [59, 20], [58, 20], [57, 20], [56, 20], [55, 20], [54, 20], [53, 20], [52, 20], [51, 20], [50, 20], [49, 20], [48, 20], [47, 20], [46, 20], [45, 20], [44, 20], [43, 20], [42, 20], [41, 20], [40, 20], [39, 20], [38, 20], [37, 20], [36, 20], [35, 20], [34, 20], [33, 20], [32, 20], [31, 20], [30, 20], [29, 20], [28, 20], [27, 20], [26, 20], [25, 20], [24, 20], [23, 20], [22, 20], [21, 20], [20, 20], [19, 20], [18, 20], [17, 20], [16, 20], [15, 20], [14, 20], [13, 20], [12, 20], [11, 20], [10, 20], [9, 20], [8, 20], [7, 20], [7, 21], [7, 22], [7, 23], [70, 19], [69, 19], [68, 19], [67, 19], [66, 19], [65, 19], [64, 19], [63, 19], [62, 19], [61, 19], [60, 19], [59, 19], [58, 19], [57, 19], [56, 19], [55, 19], [54, 19], [53, 19], [52, 19], [51, 19], [50, 19], [49, 19], [48, 19], [47, 19], [46, 19], [45, 19], [44, 19], [43, 19], [42, 19], [41, 19], [40, 19], [39, 19], [38, 19], [37, 19], [36, 19], [35, 19], [34, 19], [33, 19], [32, 19], [31, 19], [30, 19], [29, 19], [28, 19], [27, 19], [26, 19], [25, 19], [24, 19], [23, 19], [22, 19], [21, 19], [20, 19], [19, 19], [18, 19], [17, 19], [16, 19], [15, 19], [14, 19], [13, 19], [12, 19], [11, 19], [10, 19], [9, 19], [8, 19], [7, 19], [6, 19], [6, 20], [6, 21], [6, 22], [6, 23], [70, 18], [69, 18], [68, 18], [67, 18], [66, 18], [65, 18], [64, 18], [63, 18], [62, 18], [61, 18], [60, 18], [59, 18], [58, 18], [57, 18], [56, 18], [55, 18], [54, 18], [53, 18], [52, 18], [51, 18], [50, 18], [49, 18], [48, 18], [47, 18], [46, 18], [45, 18], [44, 18], [43, 18], [42, 18], [41, 18], [40, 18], [39, 18], [38, 18], [37, 18], [36, 18], [35, 18], [34, 18], [33, 18], [32, 18], [31, 18], [30, 18], [29, 18], [28, 18], [27, 18], [26, 18], [25, 18], [24, 18], [23, 18], [22, 18], [21, 18], [20, 18], [19, 18], [18, 18], [17, 18], [16, 18], [15, 18], [14, 18], [13, 18], [12, 18], [11, 18], [10, 18], [9, 18], [8, 18], [7, 18], [6, 18], [5, 18], [5, 19], [5, 20], [5, 21], [5, 22], [5, 23], [70, 17], [69, 17], [68, 17], [67, 17], [66, 17], [65, 17], [64, 17], [63, 17], [62, 17], [61, 17], [60, 17], [59, 17], [58, 17], [57, 17], [56, 17], [55, 17], [54, 17], [53, 17], [52, 17], [51, 17], [50, 17], [49, 17], [48, 17], [47, 17], [46, 17], [45, 17], [44, 17], [43, 17], [42, 17], [41, 17], [40, 17], [39, 17], [38, 17], [37, 17], [36, 17], [35, 17], [34, 17], [33, 17], [32, 17], [31, 17], [30, 17], [29, 17], [28, 17], [27, 17], [26, 17], [25, 17], [24, 17], [23, 17], [22, 17], [21, 17], [20, 17], [19, 17], [18, 17], [17, 17], [16, 17], [15, 17], [14, 17], [13, 17], [12, 17], [11, 17], [10, 17], [9, 17], [8, 17], [7, 17], [6, 17], [5, 17], [4, 17], [4, 18], [4, 19], [4, 20], [4, 21], [4, 22], [4, 23], [70, 16], [69, 16], [68, 16], [67, 16], [66, 16], [65, 16], [64, 16], [63, 16], [62, 16], [61, 16], [60, 16], [59, 16], [58, 16], [57, 16], [56, 16], [55, 16], [54, 16], [53, 16], [52, 16], [51, 16], [50, 16], [49, 16], [48, 16], [47, 16], [46, 16], [45, 16], [44, 16], [43, 16], [42, 16], [41, 16], [40, 16], [39, 16], [38, 16], [37, 16], [36, 16], [35, 16], [34, 16], [33, 16], [32, 16], [31, 16], [30, 16], [29, 16], [28, 16], [27, 16], [26, 16], [25, 16], [24, 16], [23, 16], [22, 16], [21, 16], [20, 16], [19, 16], [18, 16], [17, 16], [16, 16], [15, 16], [14, 16], [13, 16], [12, 16], [11, 16], [10, 16], [9, 16], [8, 16], [7, 16], [6, 16], [5, 16], [4, 16], [3, 16], [3, 17], [3, 18], [3, 19], [3, 20], [3, 21], [3, 22], [3, 23], [70, 15], [69, 15], [68, 15], [67, 15], [66, 15], [65, 15], [64, 15], [63, 15], [62, 15], [61, 15], [60, 15], [59, 15], [58, 15], [57, 15], [56, 15], [55, 15], [54, 15], [53, 15], [52, 15], [51, 15], [50, 15], [49, 15], [48, 15], [47, 15], [46, 15], [45, 15], [44, 15], [43, 15], [42, 15], [41, 15], [40, 15], [39, 15], [38, 15], [37, 15], [36, 15], [35, 15], [34, 15], [33, 15], [32, 15], [31, 15], [30, 15], [29, 15], [28, 15], [27, 15], [26, 15], [25, 15], [24, 15], [23, 15], [22, 15], [21, 15], [20, 15], [19, 15], [18, 15], [17, 15], [16, 15], [15, 15], [14, 15], [13, 15], [12, 15], [11, 15], [10, 15], [9, 15], [8, 15], [7, 15], [6, 15], [5, 15], [4, 15], [3, 15], [2, 15], [2, 16], [2, 17], [2, 18], [2, 19], [2, 20], [2, 21], [2, 22], [2, 23], [70, 14], [69, 14], [68, 14], [67, 14], [66, 14], [65, 14], [64, 14], [63, 14], [62, 14], [61, 14], [60, 14], [59, 14], [58, 14], [57, 14], [56, 14], [55, 14], [54, 14], [53, 14], [52, 14], [51, 14], [50, 14], [49, 14], [48, 14], [47, 14], [46, 14], [45, 14], [44, 14], [43, 14], [42, 14], [41, 14], [40, 14], [39, 14], [38, 14], [37, 14], [36, 14], [35, 14], [34, 14], [33, 14], [32, 14], [31, 14], [30, 14], [29, 14], [28, 14], [27, 14], [26, 14], [25, 14], [24, 14], [23, 14], [22, 14], [21, 14], [20, 14], [19, 14], [18, 14], [17, 14], [16, 14], [15, 14], [14, 14], [13, 14], [12, 14], [11, 14], [10, 14], [9, 14], [8, 14], [7, 14], [6, 14], [5, 14], [4, 14], [3, 14], [2, 14], [1, 14], [1, 15], [1, 16], [1, 17], [1, 18], [1, 19], [1, 20], [1, 21], [1, 22], [1, 23], [70, 13], [69, 13], [68, 13], [67, 13], [66, 13], [65, 13], [64, 13], [63, 13], [62, 13], [61, 13], [60, 13], [59, 13], [58, 13], [57, 13], [56, 13], [55, 13], [54, 13], [53, 13], [52, 13], [51, 13], [50, 13], [49, 13], [48, 13], [47, 13], [46, 13], [45, 13], [44, 13], [43, 13], [42, 13], [41, 13], [40, 13], [39, 13], [38, 13], [37, 13], [36, 13], [35, 13], [34, 13], [33, 13], [32, 13], [31, 13], [30, 13], [29, 13], [28, 13], [27, 13], [26, 13], [25, 13], [24, 13], [23, 13], [22, 13], [21, 13], [20, 13], [19, 13], [18, 13], [17, 13], [16, 13], [15, 13], [14, 13], [13, 13], [12, 13], [11, 13], [10, 13], [9, 13], [8, 13], [7, 13], [6, 13], [5, 13], [4, 13], [3, 13], [2, 13], [1, 13], [0, 13], [0, 14], [0, 15], [0, 16], [0, 17], [0, 18], [0, 19], [0, 20], [0, 21], [0, 22], [0, 23], [70, 12], [69, 12], [68, 12], [67, 12], [66, 12], [65, 12], [64, 12], [63, 12], [62, 12], [61, 12], [60, 12], [59, 12], [58, 12], [57, 12], [56, 12], [55, 12], [54, 12], [53, 12], [52, 12], [51, 12], [50, 12], [49, 12], [48, 12], [47, 12], [46, 12], [45, 12], [44, 12], [43, 12], [42, 12], [41, 12], [40, 12], [39, 12], [38, 12], [37, 12], [36, 12], [35, 12], [34, 12], [33, 12], [32, 12], [31, 12], [30, 12], [29, 12], [28, 12], [27, 12], [26, 12], [25, 12], [24, 12], [23, 12], [22, 12], [21, 12], [20, 12], [19, 12], [18, 12], [17, 12], [16, 12], [15, 12], [14, 12], [13, 12], [12, 12], [11, 12], [10, 12], [9, 12], [8, 12], [7, 12], [6, 12], [5, 12], [4, 12], [3, 12], [2, 12], [1, 12], [0, 12], [70, 11], [69, 11], [68, 11], [67, 11], [66, 11], [65, 11], [64, 11], [63, 11], [62, 11], [61, 11], [60, 11], [59, 11], [58, 11], [57, 11], [56, 11], [55, 11], [54, 11], [53, 11], [52, 11], [51, 11], [50, 11], [49, 11], [48, 11], [47, 11], [46, 11], [45, 11], [44, 11], [43, 11], [42, 11], [41, 11], [40, 11], [39, 11], [38, 11], [37, 11], [36, 11], [35, 11], [34, 11], [33, 11], [32, 11], [31, 11], [30, 11], [29, 11], [28, 11], [27, 11], [26, 11], [25, 11], [24, 11], [23, 11], [22, 11], [21, 11], [20, 11], [19, 11], [18, 11], [17, 11], [16, 11], [15, 11], [14, 11], [13, 11], [12, 11], [11, 11], [10, 11], [9, 11], [8, 11], [7, 11], [6, 11], [5, 11], [4, 11], [3, 11], [2, 11], [1, 11], [0, 11], [70, 10], [69, 10], [68, 10], [67, 10], [66, 10], [65, 10], [64, 10], [63, 10], [62, 10], [61, 10], [60, 10], [59, 10], [58, 10], [57, 10], [56, 10], [55, 10], [54, 10], [53, 10], [52, 10], [51, 10], [50, 10], [49, 10], [48, 10], [47, 10], [46, 10], [45, 10], [44, 10], [43, 10], [42, 10], [41, 10], [40, 10], [39, 10], [38, 10], [37, 10], [36, 10], [35, 10], [34, 10], [33, 10], [32, 10], [31, 10], [30, 10], [29, 10], [28, 10], [27, 10], [26, 10], [25, 10], [24, 10], [23, 10], [22, 10], [21, 10], [20, 10], [19, 10], [18, 10], [17, 10], [16, 10], [15, 10], [14, 10], [13, 10], [12, 10], [11, 10], [10, 10], [9, 10], [8, 10], [7, 10], [6, 10], [5, 10], [4, 10], [3, 10], [2, 10], [1, 10], [0, 10], [70, 9], [69, 9], [68, 9], [67, 9], [66, 9], [65, 9], [64, 9], [63, 9], [62, 9], [61, 9], [60, 9], [59, 9], [58, 9], [57, 9], [56, 9], [55, 9], [54, 9], [53, 9], [52, 9], [51, 9], [50, 9], [49, 9], [48, 9], [47, 9], [46, 9], [45, 9], [44, 9], [43, 9], [42, 9], [41, 9], [40, 9], [39, 9], [38, 9], [37, 9], [36, 9], [35, 9], [34, 9], [33, 9], [32, 9], [31, 9], [30, 9], [29, 9], [28, 9], [27, 9], [26, 9], [25, 9], [24, 9], [23, 9], [22, 9], [21, 9], [20, 9], [19, 9], [18, 9], [17, 9], [16, 9], [15, 9], [14, 9], [13, 9], [12, 9], [11, 9], [10, 9], [9, 9], [8, 9], [7, 9], [6, 9], [5, 9], [4, 9], [3, 9], [2, 9], [1, 9], [0, 9], [70, 8], [69, 8], [68, 8], [67, 8], [66, 8], [65, 8], [64, 8], [63, 8], [62, 8], [61, 8], [60, 8], [59, 8], [58, 8], [57, 8], [56, 8], [55, 8], [54, 8], [53, 8], [52, 8], [51, 8], [50, 8], [49, 8], [48, 8], [47, 8], [46, 8], [45, 8], [44, 8], [43, 8], [42, 8], [41, 8], [40, 8], [39, 8], [38, 8], [37, 8], [36, 8], [35, 8], [34, 8], [33, 8], [32, 8], [31, 8], [30, 8], [29, 8], [28, 8], [27, 8], [26, 8], [25, 8], [24, 8], [23, 8], [22, 8], [21, 8], [20, 8], [19, 8], [18, 8], [17, 8], [16, 8], [15, 8], [14, 8], [13, 8], [12, 8], [11, 8], [10, 8], [9, 8], [8, 8], [7, 8], [6, 8], [5, 8], [4, 8], [3, 8], [2, 8], [1, 8], [0, 8], [70, 7], [69, 7], [68, 7], [67, 7], [66, 7], [65, 7], [64, 7], [63, 7], [62, 7], [61, 7], [60, 7], [59, 7], [58, 7], [57, 7], [56, 7], [55, 7], [54, 7], [53, 7], [52, 7], [51, 7], [50, 7], [49, 7], [48, 7], [47, 7], [46, 7], [45, 7], [44, 7], [43, 7], [42, 7], [41, 7], [40, 7], [39, 7], [38, 7], [37, 7], [36, 7], [35, 7], [34, 7], [33, 7], [32, 7], [31, 7], [30, 7], [29, 7], [28, 7], [27, 7], [26, 7], [25, 7], [24, 7], [23, 7], [22, 7], [21, 7], [20, 7], [19, 7], [18, 7], [17, 7], [16, 7], [15, 7], [14, 7], [13, 7], [12, 7], [11, 7], [10, 7], [9, 7], [8, 7], [7, 7], [6, 7], [5, 7], [4, 7], [3, 7], [2, 7], [1, 7], [0, 7], [70, 6], [69, 6], [68, 6], [67, 6], [66, 6], [65, 6], [64, 6], [63, 6], [62, 6], [61, 6], [60, 6], [59, 6], [58, 6], [57, 6], [56, 6], [55, 6], [54, 6], [53, 6], [52, 6], [51, 6], [50, 6], [49, 6], [48, 6], [47, 6], [46, 6], [45, 6], [44, 6], [43, 6], [42, 6], [41, 6], [40, 6], [39, 6], [38, 6], [37, 6], [36, 6], [35, 6], [34, 6], [33, 6], [32, 6], [31, 6], [30, 6], [29, 6], [28, 6], [27, 6], [26, 6], [25, 6], [24, 6], [23, 6], [22, 6], [21, 6], [20, 6], [19, 6], [18, 6], [17, 6], [16, 6], [15, 6], [14, 6], [13, 6], [12, 6], [11, 6], [10, 6], [9, 6], [8, 6], [7, 6], [6, 6], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6], [70, 5], [69, 5], [68, 5], [67, 5], [66, 5], [65, 5], [64, 5], [63, 5], [62, 5], [61, 5], [60, 5], [59, 5], [58, 5], [57, 5], [56, 5], [55, 5], [54, 5], [53, 5], [52, 5], [51, 5], [50, 5], [49, 5], [48, 5], [47, 5], [46, 5], [45, 5], [44, 5], [43, 5], [42, 5], [41, 5], [40, 5], [39, 5], [38, 5], [37, 5], [36, 5], [35, 5], [34, 5], [33, 5], [32, 5], [31, 5], [30, 5], [29, 5], [28, 5], [27, 5], [26, 5], [25, 5], [24, 5], [23, 5], [22, 5], [21, 5], [20, 5], [19, 5], [18, 5], [17, 5], [16, 5], [15, 5], [14, 5], [13, 5], [12, 5], [11, 5], [10, 5], [9, 5], [8, 5], [7, 5], [6, 5], [5, 5], [4, 5], [3, 5], [2, 5], [1, 5], [0, 5], [70, 4], [69, 4], [68, 4], [67, 4], [66, 4], [65, 4], [64, 4], [63, 4], [62, 4], [61, 4], [60, 4], [59, 4], [58, 4], [57, 4], [56, 4], [55, 4], [54, 4], [53, 4], [52, 4], [51, 4], [50, 4], [49, 4], [48, 4], [47, 4], [46, 4], [45, 4], [44, 4], [43, 4], [42, 4], [41, 4], [40, 4], [39, 4], [38, 4], [37, 4], [36, 4], [35, 4], [34, 4], [33, 4], [32, 4], [31, 4], [30, 4], [29, 4], [28, 4], [27, 4], [26, 4], [25, 4], [24, 4], [23, 4], [22, 4], [21, 4], [20, 4], [19, 4], [18, 4], [17, 4], [16, 4], [15, 4], [14, 4], [13, 4], [12, 4], [11, 4], [10, 4], [9, 4], [8, 4], [7, 4], [6, 4], [5, 4], [4, 4], [3, 4], [2, 4], [1, 4], [0, 4], [70, 3], [69, 3], [68, 3], [67, 3], [66, 3], [65, 3], [64, 3], [63, 3], [62, 3], [61, 3], [60, 3], [59, 3], [58, 3], [57, 3], [56, 3], [55, 3], [54, 3], [53, 3], [52, 3], [51, 3], [50, 3], [49, 3], [48, 3], [47, 3], [46, 3], [45, 3], [44, 3], [43, 3], [42, 3], [41, 3], [40, 3], [39, 3], [38, 3], [37, 3], [36, 3], [35, 3], [34, 3], [33, 3], [32, 3], [31, 3], [30, 3], [29, 3], [28, 3], [27, 3], [26, 3], [25, 3], [24, 3], [23, 3], [22, 3], [21, 3], [20, 3], [19, 3], [18, 3], [17, 3], [16, 3], [15, 3], [14, 3], [13, 3], [12, 3], [11, 3], [10, 3], [9, 3], [8, 3], [7, 3], [6, 3], [5, 3], [4, 3], [3, 3], [2, 3], [1, 3], [0, 3], [70, 2], [69, 2], [68, 2], [67, 2], [66, 2], [65, 2], [64, 2], [63, 2], [62, 2], [61, 2], [60, 2], [59, 2], [58, 2], [57, 2], [56, 2], [55, 2], [54, 2], [53, 2], [52, 2], [51, 2], [50, 2], [49, 2], [48, 2], [47, 2], [46, 2], [45, 2], [44, 2], [43, 2], [42, 2], [41, 2], [40, 2], [39, 2], [38, 2], [37, 2], [36, 2], [35, 2], [34, 2], [33, 2], [32, 2], [31, 2], [30, 2], [29, 2], [28, 2], [27, 2], [26, 2], [25, 2], [24, 2], [23, 2], [22, 2], [21, 2], [20, 2], [19, 2], [18, 2], [17, 2], [16, 2], [15, 2], [14, 2], [13, 2], [12, 2], [11, 2], [10, 2], [9, 2], [8, 2], [7, 2], [6, 2], [5, 2], [4, 2], [3, 2], [2, 2], [1, 2], [0, 2], [70, 1], [69, 1], [68, 1], [67, 1], [66, 1], [65, 1], [64, 1], [63, 1], [62, 1], [61, 1], [60, 1], [59, 1], [58, 1], [57, 1], [56, 1], [55, 1], [54, 1], [53, 1], [52, 1], [51, 1], [50, 1], [49, 1], [48, 1], [47, 1], [46, 1], [45, 1], [44, 1], [43, 1], [42, 1], [41, 1], [40, 1], [39, 1], [38, 1], [37, 1], [36, 1], [35, 1], [34, 1], [33, 1], [32, 1], [31, 1], [30, 1], [29, 1], [28, 1], [27, 1], [26, 1], [25, 1], [24, 1], [23, 1], [22, 1], [21, 1], [20, 1], [19, 1], [18, 1], [17, 1], [16, 1], [15, 1], [14, 1], [13, 1], [12, 1], [11, 1], [10, 1], [9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [70, 0], [69, 0], [68, 0], [67, 0], [66, 0], [65, 0], [64, 0], [63, 0], [62, 0], [61, 0], [60, 0], [59, 0], [58, 0], [57, 0], [56, 0], [55, 0], [54, 0], [53, 0], [52, 0], [51, 0], [50, 0], [49, 0], [48, 0], [47, 0], [46, 0], [45, 0], [44, 0], [43, 0], [42, 0], [41, 0], [40, 0], [39, 0], [38, 0], [37, 0], [36, 0], [35, 0], [34, 0], [33, 0], [32, 0], [31, 0], [30, 0], [29, 0], [28, 0], [27, 0], [26, 0], [25, 0], [24, 0], [23, 0], [22, 0], [21, 0], [20, 0], [19, 0], [18, 0], [17, 0], [16, 0], [15, 0], [14, 0], [13, 0], [12, 0], [11, 0], [10, 0], [9, 0], [8, 0], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
