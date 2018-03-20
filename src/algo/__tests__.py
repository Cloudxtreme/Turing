# -*- coding: utf-8 -*-

import maths.nodes as nodes
from algo.stmts import *
from algo.stmts.BreakStmt import BreakStmt
from algo.stmts.ContinueStmt import ContinueStmt
from algo.worker import Worker
from tests.framework import expect

tests = [
    (
        [
            AssignStmt("sum", nodes.NumberNode(0)),
            InputStmt("N"),
            ForStmt("i", nodes.NumberNode(1), nodes.IdentifierNode("N"), [
                AssignStmt("sum", nodes.BinOpNode(nodes.IdentifierNode("sum"), nodes.IdentifierNode("i"), "+"))
            ]),
            DisplayStmt(nodes.BinOpNode(nodes.StringNode("Result="), nodes.IdentifierNode("sum"), "+"))
        ],
        "5",
        [
            "Variable N = 5",
            "Result=15"
        ]
    ),
    (
        [
            ForStmt("i", nodes.NumberNode(1), nodes.NumberNode(3), [
                ForStmt("i", nodes.NumberNode(1), nodes.NumberNode(3), [
                    DisplayStmt(nodes.IdentifierNode("i"))
                ])
            ])
        ],
        "",
        [
            "1",
            "2",
            "3",
            "1",
            "2",
            "3",
            "1",
            "2",
            "3",
        ]
    ),
    (
        [
            AssignStmt("i", nodes.NumberNode(42)),
            ForStmt("i", nodes.NumberNode(1), nodes.NumberNode(10), [
                IfStmt(nodes.NumberNode(1), [
                    IfStmt(nodes.BinOpNode(nodes.IdentifierNode("i"), nodes.NumberNode(2), "%"), [
                        ContinueStmt()
                    ]),
                    IfStmt(nodes.BinOpNode(nodes.IdentifierNode("i"), nodes.NumberNode(5), ">"), [
                        DisplayStmt(nodes.StringNode("break")),
                        DisplayStmt(nodes.IdentifierNode("i")),
                        BreakStmt()
                    ]),
                    DisplayStmt(nodes.IdentifierNode("i")),
                ])
            ]),
            DisplayStmt(nodes.IdentifierNode("i"))
        ],
        "",
        [
            "2",
            "4",
            "break",
            "6",
            "42"
        ]
    )
]


def run_tests():
    for algo, input, exp_output in tests:
        worker = Worker(algo)

        output = ""

        def buffer_print(*args, end="\n"):
            nonlocal output
            output += " ".join(str(arg) for arg in args) + end

        worker.callback_print = buffer_print

        iter_input = iter(input.split("\n"))

        def buffer_input(prompt=""):
            result = next(iter_input)
            buffer_print(prompt + result)
            return result

        worker.callback_input = buffer_input

        worker.evaluator.strict_typing = True
        worker.run()

        expect(output, "".join(x + "\n" for x in exp_output))
