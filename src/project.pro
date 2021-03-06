

CODECFORTR = UTF-8
CODECFORSRC = UTF-8

RESOURCES += \
    turing.qrc

SOURCES += \
    turing_rc.py \
    editor_backend.py \
    main.py \
    algo\__tests__.py \
    algo\worker.py \
    algo\__init__.py \
    algo\backends\texas.py \
    algo\backends\__init__.py \
    algo\stmts\FuncStmt.py \
    algo\stmts\AssignStmt.py \
    algo\stmts\GPointStmt.py \
    algo\stmts\DisplayStmt.py \
    algo\stmts\__init__.py \
    algo\stmts\ElseStmt.py \
    algo\stmts\CallStmt.py \
    algo\stmts\BlockStmt.py \
    algo\stmts\InputStmt.py \
    algo\stmts\GClearStmt.py \
    algo\stmts\GLineStmt.py \
    algo\stmts\ContinueStmt.py \
    algo\stmts\ForStmt.py \
    algo\stmts\BaseStmt.py \
    algo\stmts\SleepStmt.py \
    algo\stmts\GWindowStmt.py \
    algo\stmts\IfStmt.py \
    algo\stmts\StopStmt.py \
    algo\stmts\WhileStmt.py \
    algo\stmts\BreakStmt.py \
    algo\stmts\ReturnStmt.py \
    algo\stmts\CommentStmt.py \
    algo\stmts\GFuncStmt.py \
    algo\frontends\algobox.py \
    algo\frontends\__init__.py \
    forms\ui_alg_sleep.py \
    forms\alg_func.py \
    forms\alg_define.py \
    forms\alg_gline.py \
    forms\calculator.py \
    forms\ui_inline_code.py \
    forms\ui_alg_comment.py \
    forms\ui_alg_gline.py \
    forms\__init__.py \
    forms\ui_alg_for.py \
    forms\alg_for.py \
    forms\alg_sleep.py \
    forms\ui_alg_call.py \
    forms\w_inline_code.py \
    forms\ui_alg_return.py \
    forms\inline_code_dialog.py \
    forms\alg_stop.py \
    forms\alg_comment.py \
    forms\alg_gpoint.py \
    forms\changtheme.py \
    forms\mainwindow.py \
    forms\alg_while.py \
    forms\ui_about.py \
    forms\ui_mainwindow.py \
    forms\alg_gwindow.py \
    forms\ui_alg_gpoint.py \
    forms\ui_changtheme.py \
    forms\ui_alg_input.py \
    forms\ui_alg_gwindow.py \
    forms\ui_alg_gfunc.py \
    forms\ui_alg_func.py \
    forms\alg_return.py \
    forms\about.py \
    forms\ui_alg_if.py \
    forms\ui_calculator.py \
    forms\ui_alg_display.py \
    forms\inline_code_editor.py \
    forms\alg_if.py \
    forms\ui_alg_stop.py \
    forms\ui_alg_while.py \
    forms\alg_display.py \
    forms\alg_call.py \
    forms\ui_help.py \
    forms\alg_input.py \
    forms\ui_alg_define.py \
    forms\alg_gfunc.py \
    forms\help.py \
    maths\evaluator.py \
    maths\parser.py \
    maths\__init__.py \
    maths\__tests__.py \
    maths\nodes\UnaryOpNode.py \
    maths\nodes\NumberNode.py \
    maths\nodes\ListNode.py \
    maths\nodes\ArrayAccessNode.py \
    maths\nodes\IdentifierNode.py \
    maths\nodes\LambdaNode.py \
    maths\nodes\BinOpNode.py \
    maths\nodes\AstNode.py \
    maths\nodes\__init__.py \
    maths\nodes\StringNode.py \
    maths\nodes\CallNode.py \
    maths\lib\stats.py \
    maths\lib\geom.py \
    maths\lib\const.py \
    maths\lib\algobox.py \
    maths\lib\physics.py \
    maths\lib\cast.py \
    maths\lib\docs.py \
    maths\lib\basic.py \
    maths\lib\trig.py \
    maths\lib\__init__.py \
    tools\docgen.py \
    tools\build.py \
    tools\progen.py \
    util\log.py \
    util\code.py \
    util\widgets.py \
    util\undoredo.py \
    util\theming.py \
    util\math.py \
    util\profiler.py \
    util\html.py \
    util\__init__.py \
    lang\__init__.py \
    lang\translator.py \
    tests\framework.py \
    tests\chat.py \
    tests\__init__.py
    
FORMS += \
    forms\ui_help.ui \
    forms\ui_alg_define.ui \
    forms\ui_calculator.ui \
    forms\ui_alg_if.ui \
    forms\ui_alg_while.ui \
    forms\ui_alg_display.ui \
    forms\ui_alg_stop.ui \
    forms\ui_alg_input.ui \
    forms\ui_alg_gwindow.ui \
    forms\ui_alg_gfunc.ui \
    forms\ui_alg_func.ui \
    forms\ui_about.ui \
    forms\ui_alg_gpoint.ui \
    forms\ui_changtheme.ui \
    forms\ui_mainwindow.ui \
    forms\ui_alg_comment.ui \
    forms\ui_alg_gline.ui \
    forms\ui_alg_call.ui \
    forms\w_inline_code.ui \
    forms\ui_alg_return.ui \
    forms\ui_alg_for.ui \
    forms\ui_inline_code.ui \
    forms\ui_alg_sleep.ui
    
TRANSLATIONS += \
    lang\it.ts \
    lang\fr.ts \
    lang\zh-CN.ts \
    lang\de.ts \
    lang\es.ts