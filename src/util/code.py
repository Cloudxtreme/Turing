# -*- coding: utf-8 -*-
import re

from maths.parser import Parser
from . import translate
from .widgets import msg_box_error

wrapper = """# -*- coding: utf-8 -*-
def __turing_loader__():
    import maths.lib
    import types
    for n, x in maths.lib.__dict__.items():
        if type(x) == types.ModuleType and "maths.lib." in x.__name__:
            module = __import__(x.__name__, globals(), locals(), ["*"], 0)
            for k, i in module.__dict__.items():
                if type(i) == types.FunctionType:
                    globals()[k] = getattr(module, k)
                elif k.startswith("c_"):
                    globals()[k[2:]] = getattr(module, k)
__turing_loader__()
del __turing_loader__

__input__ = input
def input(prompt="", **kwargs):
    return __input__(prompt, globals=globals(), locals=locals(), **kwargs)

%s
"""

line_offset = len(wrapper.split("\n")) - 2


def python_wrapper(input: str) -> str:
    return wrapper % input


def try_parse(txt, parent=None):
    p = Parser(txt)

    ret = None

    try:
        ret = p.parse()
    except:
        ret = None

    msgs = p.log.get_messages()

    if msgs:
        box = msg_box_error(
            translate("Algo", "The following errors occured while parsing the expression:\n\n") + "\n".join(
                x[1] for x in msgs), parent=parent)
        box.exec_()
        ret = None

    return ret


def is_id(txt):
    return bool(re.search('^[a-zA-Z_0-9]+$', txt))
