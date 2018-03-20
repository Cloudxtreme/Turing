# -*- coding: utf-8 -*-

from algo.stmts import BlockStmt
from .BaseStmt import *


class FuncStmt(BlockStmt):
    parameters = None

    def __init__(self, parameters: List[str], children: CodeBlock):
        super().__init__(children)
        self.parameters = parameters

    def __str__(self):
        return "[Func (%s) %s]" % (", ".join(self.parameters), super().__str__())