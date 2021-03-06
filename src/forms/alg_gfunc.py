# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from forms.inline_code_dialog import InlineCodeDialog
from forms.ui_alg_gfunc import Ui_AlgoGFuncStmt
from maths.nodes import *
from maths.parser import quick_parse as parse
from util.code import try_parse
from util.widgets import center_widget, msg_box_error

translate = QCoreApplication.translate


class AlgoGFuncStmt(QDialog):
    def __init__(self, parent, origcode=("x", "cos(x)", "", "", "0.1", '"red"')):
        super().__init__(parent)
        self.ui = Ui_AlgoGFuncStmt()
        self.ui.setupUi(self)
        self.setFixedWidth(self.width())
        self.adjustSize()
        self.setFixedSize(self.size())
        self.ui.txtVariable.setText(origcode[0])
        self.ui.txtFunction.setText(origcode[1])
        self.ui.txtStart.setText(origcode[2])
        self.ui.txtEnd.setText(origcode[3])
        self.ui.txtStep.setText(origcode[4])
        self.ui.txtColor.setText(origcode[5])

        self.ui.btnCodeFunction.clicked.connect(lambda: self.click(self.ui.txtFunction))
        self.ui.btnCodeStart.clicked.connect(lambda: self.click(self.ui.txtStart))
        self.ui.btnCodeEnd.clicked.connect(lambda: self.click(self.ui.txtEnd))
        self.ui.btnCodeStep.clicked.connect(lambda: self.click(self.ui.txtStep))
        self.ui.btnCodeColor.clicked.connect(self.change_color)

        center_widget(self, parent)

    def done(self, res):
        if res == QDialog.Accepted:
            name = self.ui.txtVariable.text()
            parsed = parse(name)

            if not isinstance(parsed, IdentifierNode):
                box = msg_box_error(translate("Algo",
                                              "Invalid variable name: {name}").format(
                    name=name), parent=self)
                box.exec_()
                return

            self.f_variable = name

            p = try_parse(self.ui.txtFunction.text(), self)

            if p is None:
                return

            self.f_function = p

            p = try_parse(self.ui.txtStart.text(), self)

            if p is None:
                return

            self.f_start = p

            p = try_parse(self.ui.txtEnd.text(), self)

            if p is None:
                return

            self.f_end = p

            p = try_parse(self.ui.txtStep.text(), self)

            if p is None:
                return

            self.f_step = p

            p = try_parse(self.ui.txtColor.text(), self)

            if p is None:
                return

            self.f_color = p

            self.ok = True

        super(AlgoGFuncStmt, self).done(res)

    def click(self, wgt):
        dlg = InlineCodeDialog(self, wgt.text())
        if dlg.run():
            wgt.setText(dlg.value())

    def change_color(self, _):
        dlg = QColorDialog(self)
        current = self.ui.txtColor.text()
        if current[0] == current[-1] == '"':
            current = current[1:-1]
        dlg.setCurrentColor(QColor(current))
        if dlg.exec_():
            self.ui.txtColor.setText('"%s"' % dlg.currentColor().name())

    def run(self):
        return self.exec_() == QDialog.Accepted and self.ok
