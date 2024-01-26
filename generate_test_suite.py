import os
import os.path
import sys
import shutil
import random
from typing import *
from copy import deepcopy
import inspect


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


generators = {
    str: lambda _: "".join(
        random.choice("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVXYZ")
        for _ in range(10)
    ),
    int: lambda _: random.randint(1, 100),
    List: lambda x: [generators[get_args(x)[0]](get_args(x)[0]) for _ in range(10)],
    List[int]: lambda x: [generators[int](int) for _ in range(random.randint(1,6))],
    List[str]: lambda _: [generators[str](str) for _ in range(random.randint(1,6))],
    Tuple: lambda x: tuple([generators[arg](arg) for arg in get_args(x)]),
    Optional: lambda x: None
    if random.random() < 0.3
    else generators[get_args(x)](get_args(x)),
}


def generate_list_node(arg, first=True):
    if not first and random.random() < 0.5:
        return None
    else:
        return ListNode(generators[int](int), generate_list_node(None, False))


def generate_tree_node(arg, first=True):
    if not first and random.random() < 0.5:
        return None
    else:
        return TreeNode(
            generators[int](int),
            generate_tree_node(None, False),
            generate_tree_node(None, False),
        )


generators[ListNode] = generate_list_node
imports = """
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
"""

test_template = """
import solution
{prerequisites}
def test_{id}():
    assert solution.Solution().{method}({args}) == {output}
"""

"""
Problems that are not supported due to tough constraints
"""
black_list = [
    "0013",
    "0022",
    "0038",
    "0019",
    "0043",
    "0051",
    "0052",
    "0077",
    "0089",
    "0095",
    "0247",
    "0339",
    "0339-2",
    "0458",
    "0479",
    "0726",
    "0753",
    "0786",
    "0894",
    "0964",
    "1030",
    "1079",
    "1238",
    "1240",
    "1363",
    "1415",
    "1441",
    "1659",
    "1718",
    "1837",
    "1931",
    "1998",
    "2081",
    "2172",
    "2235",
    "2243",
    "2305",
    "2609",
    "2645",
    "2709",
    "2992",
]
os.makedirs("./py-suite", exist_ok=True)
for file in sorted(os.listdir("./py")):
    problem_name = file[:-3]
    if problem_name in black_list:
        continue
    print("Problem name: ", problem_name)
    shutil.rmtree("./py-suite/" + problem_name, ignore_errors=True)
    os.makedirs("./py-suite/" + problem_name, exist_ok=False)

    with open(os.path.join("py", file)) as reference:
        reference_source_code = imports + reference.read()
        print(reference_source_code)
        if "NestedInteger" in reference_source_code:
            continue
        exec(reference_source_code, globals())
        Solution: Any
        target_method_name = [
            x
            for x in dir(Solution)
            if not x.startswith("__") and callable(getattr(Solution, x))
        ][0]
        target_method: Callable = getattr(Solution, target_method_name)
        print("Target method: ", target_method_name)
        # Get types of arguments for function
        generated_args = True
        arg_constructors = []
        for k, v in target_method.__annotations__.items():
            print(f" Name = {k}, Type = {v}")
            if k == "return":
                continue
            # print(get_args(v))
            if v not in generators:
                print("Skip argument", v)
                generated_args = False
                break
            generator = generators[v]
            arg_constructors.append((v, generator))
        if not generated_args:
            shutil.rmtree("./py-suite/" + problem_name, ignore_errors=True)
            continue

        arg_constructor = lambda: [generator(t) for t, generator in arg_constructors]

        test_index = 0
        failures = 0
        print("Starting input generation for ", problem_name)
        while test_index < 20:
            inputs = arg_constructor()
            original_input = deepcopy(inputs)
            # print("Inputs", inputs)
            try:
                output = getattr(Solution(), target_method_name)(*inputs)
            except Exception as e:
                print("Exception", problem_name, e)
                failures += 1
                if failures > 10:
                    break
                # input()
                continue
            failures = 0
            # print("Output", output)

            with open(
                os.path.join("py-suite", problem_name, f"test_{test_index}.py"), "w"
            ) as test_file:
                test_file.write(
                    test_template.format(
                        id=test_index,
                        method=target_method_name,
                        args=", ".join(repr(arg) for arg in original_input),
                        output=repr(output),
                        prerequisites=imports + inspect.getsource(ListNode) + "\n",
                    )
                )
            test_index += 1
            # input()
        if failures > 10:
            shutil.rmtree("./py-suite/" + problem_name, ignore_errors=True)

    # input()
