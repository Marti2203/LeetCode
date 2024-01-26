
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
    assert solution.Solution().simplifiedFractions(50) == ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5', '1/6', '5/6', '1/7', '2/7', '3/7', '4/7', '5/7', '6/7', '1/8', '3/8', '5/8', '7/8', '1/9', '2/9', '4/9', '5/9', '7/9', '8/9', '1/10', '3/10', '7/10', '9/10', '1/11', '2/11', '3/11', '4/11', '5/11', '6/11', '7/11', '8/11', '9/11', '10/11', '1/12', '5/12', '7/12', '11/12', '1/13', '2/13', '3/13', '4/13', '5/13', '6/13', '7/13', '8/13', '9/13', '10/13', '11/13', '12/13', '1/14', '3/14', '5/14', '9/14', '11/14', '13/14', '1/15', '2/15', '4/15', '7/15', '8/15', '11/15', '13/15', '14/15', '1/16', '3/16', '5/16', '7/16', '9/16', '11/16', '13/16', '15/16', '1/17', '2/17', '3/17', '4/17', '5/17', '6/17', '7/17', '8/17', '9/17', '10/17', '11/17', '12/17', '13/17', '14/17', '15/17', '16/17', '1/18', '5/18', '7/18', '11/18', '13/18', '17/18', '1/19', '2/19', '3/19', '4/19', '5/19', '6/19', '7/19', '8/19', '9/19', '10/19', '11/19', '12/19', '13/19', '14/19', '15/19', '16/19', '17/19', '18/19', '1/20', '3/20', '7/20', '9/20', '11/20', '13/20', '17/20', '19/20', '1/21', '2/21', '4/21', '5/21', '8/21', '10/21', '11/21', '13/21', '16/21', '17/21', '19/21', '20/21', '1/22', '3/22', '5/22', '7/22', '9/22', '13/22', '15/22', '17/22', '19/22', '21/22', '1/23', '2/23', '3/23', '4/23', '5/23', '6/23', '7/23', '8/23', '9/23', '10/23', '11/23', '12/23', '13/23', '14/23', '15/23', '16/23', '17/23', '18/23', '19/23', '20/23', '21/23', '22/23', '1/24', '5/24', '7/24', '11/24', '13/24', '17/24', '19/24', '23/24', '1/25', '2/25', '3/25', '4/25', '6/25', '7/25', '8/25', '9/25', '11/25', '12/25', '13/25', '14/25', '16/25', '17/25', '18/25', '19/25', '21/25', '22/25', '23/25', '24/25', '1/26', '3/26', '5/26', '7/26', '9/26', '11/26', '15/26', '17/26', '19/26', '21/26', '23/26', '25/26', '1/27', '2/27', '4/27', '5/27', '7/27', '8/27', '10/27', '11/27', '13/27', '14/27', '16/27', '17/27', '19/27', '20/27', '22/27', '23/27', '25/27', '26/27', '1/28', '3/28', '5/28', '9/28', '11/28', '13/28', '15/28', '17/28', '19/28', '23/28', '25/28', '27/28', '1/29', '2/29', '3/29', '4/29', '5/29', '6/29', '7/29', '8/29', '9/29', '10/29', '11/29', '12/29', '13/29', '14/29', '15/29', '16/29', '17/29', '18/29', '19/29', '20/29', '21/29', '22/29', '23/29', '24/29', '25/29', '26/29', '27/29', '28/29', '1/30', '7/30', '11/30', '13/30', '17/30', '19/30', '23/30', '29/30', '1/31', '2/31', '3/31', '4/31', '5/31', '6/31', '7/31', '8/31', '9/31', '10/31', '11/31', '12/31', '13/31', '14/31', '15/31', '16/31', '17/31', '18/31', '19/31', '20/31', '21/31', '22/31', '23/31', '24/31', '25/31', '26/31', '27/31', '28/31', '29/31', '30/31', '1/32', '3/32', '5/32', '7/32', '9/32', '11/32', '13/32', '15/32', '17/32', '19/32', '21/32', '23/32', '25/32', '27/32', '29/32', '31/32', '1/33', '2/33', '4/33', '5/33', '7/33', '8/33', '10/33', '13/33', '14/33', '16/33', '17/33', '19/33', '20/33', '23/33', '25/33', '26/33', '28/33', '29/33', '31/33', '32/33', '1/34', '3/34', '5/34', '7/34', '9/34', '11/34', '13/34', '15/34', '19/34', '21/34', '23/34', '25/34', '27/34', '29/34', '31/34', '33/34', '1/35', '2/35', '3/35', '4/35', '6/35', '8/35', '9/35', '11/35', '12/35', '13/35', '16/35', '17/35', '18/35', '19/35', '22/35', '23/35', '24/35', '26/35', '27/35', '29/35', '31/35', '32/35', '33/35', '34/35', '1/36', '5/36', '7/36', '11/36', '13/36', '17/36', '19/36', '23/36', '25/36', '29/36', '31/36', '35/36', '1/37', '2/37', '3/37', '4/37', '5/37', '6/37', '7/37', '8/37', '9/37', '10/37', '11/37', '12/37', '13/37', '14/37', '15/37', '16/37', '17/37', '18/37', '19/37', '20/37', '21/37', '22/37', '23/37', '24/37', '25/37', '26/37', '27/37', '28/37', '29/37', '30/37', '31/37', '32/37', '33/37', '34/37', '35/37', '36/37', '1/38', '3/38', '5/38', '7/38', '9/38', '11/38', '13/38', '15/38', '17/38', '21/38', '23/38', '25/38', '27/38', '29/38', '31/38', '33/38', '35/38', '37/38', '1/39', '2/39', '4/39', '5/39', '7/39', '8/39', '10/39', '11/39', '14/39', '16/39', '17/39', '19/39', '20/39', '22/39', '23/39', '25/39', '28/39', '29/39', '31/39', '32/39', '34/39', '35/39', '37/39', '38/39', '1/40', '3/40', '7/40', '9/40', '11/40', '13/40', '17/40', '19/40', '21/40', '23/40', '27/40', '29/40', '31/40', '33/40', '37/40', '39/40', '1/41', '2/41', '3/41', '4/41', '5/41', '6/41', '7/41', '8/41', '9/41', '10/41', '11/41', '12/41', '13/41', '14/41', '15/41', '16/41', '17/41', '18/41', '19/41', '20/41', '21/41', '22/41', '23/41', '24/41', '25/41', '26/41', '27/41', '28/41', '29/41', '30/41', '31/41', '32/41', '33/41', '34/41', '35/41', '36/41', '37/41', '38/41', '39/41', '40/41', '1/42', '5/42', '11/42', '13/42', '17/42', '19/42', '23/42', '25/42', '29/42', '31/42', '37/42', '41/42', '1/43', '2/43', '3/43', '4/43', '5/43', '6/43', '7/43', '8/43', '9/43', '10/43', '11/43', '12/43', '13/43', '14/43', '15/43', '16/43', '17/43', '18/43', '19/43', '20/43', '21/43', '22/43', '23/43', '24/43', '25/43', '26/43', '27/43', '28/43', '29/43', '30/43', '31/43', '32/43', '33/43', '34/43', '35/43', '36/43', '37/43', '38/43', '39/43', '40/43', '41/43', '42/43', '1/44', '3/44', '5/44', '7/44', '9/44', '13/44', '15/44', '17/44', '19/44', '21/44', '23/44', '25/44', '27/44', '29/44', '31/44', '35/44', '37/44', '39/44', '41/44', '43/44', '1/45', '2/45', '4/45', '7/45', '8/45', '11/45', '13/45', '14/45', '16/45', '17/45', '19/45', '22/45', '23/45', '26/45', '28/45', '29/45', '31/45', '32/45', '34/45', '37/45', '38/45', '41/45', '43/45', '44/45', '1/46', '3/46', '5/46', '7/46', '9/46', '11/46', '13/46', '15/46', '17/46', '19/46', '21/46', '25/46', '27/46', '29/46', '31/46', '33/46', '35/46', '37/46', '39/46', '41/46', '43/46', '45/46', '1/47', '2/47', '3/47', '4/47', '5/47', '6/47', '7/47', '8/47', '9/47', '10/47', '11/47', '12/47', '13/47', '14/47', '15/47', '16/47', '17/47', '18/47', '19/47', '20/47', '21/47', '22/47', '23/47', '24/47', '25/47', '26/47', '27/47', '28/47', '29/47', '30/47', '31/47', '32/47', '33/47', '34/47', '35/47', '36/47', '37/47', '38/47', '39/47', '40/47', '41/47', '42/47', '43/47', '44/47', '45/47', '46/47', '1/48', '5/48', '7/48', '11/48', '13/48', '17/48', '19/48', '23/48', '25/48', '29/48', '31/48', '35/48', '37/48', '41/48', '43/48', '47/48', '1/49', '2/49', '3/49', '4/49', '5/49', '6/49', '8/49', '9/49', '10/49', '11/49', '12/49', '13/49', '15/49', '16/49', '17/49', '18/49', '19/49', '20/49', '22/49', '23/49', '24/49', '25/49', '26/49', '27/49', '29/49', '30/49', '31/49', '32/49', '33/49', '34/49', '36/49', '37/49', '38/49', '39/49', '40/49', '41/49', '43/49', '44/49', '45/49', '46/49', '47/49', '48/49', '1/50', '3/50', '7/50', '9/50', '11/50', '13/50', '17/50', '19/50', '21/50', '23/50', '27/50', '29/50', '31/50', '33/50', '37/50', '39/50', '41/50', '43/50', '47/50', '49/50']
