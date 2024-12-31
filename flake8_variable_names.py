import ast
import importlib.metadata
from ast import NodeVisitor
from typing import Generator, Any


class Visitor(NodeVisitor):
    ...


class Plugin:
    name = __name__
    version = importlib.metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        yield 1, 1, "GVN001 - bad", type(self)
        # visitor = Visitor()
        # visitor.visit(self._tree)

        # for line, col, msg in visitor.errors:
        #     yield line, col, msg, type(self)
