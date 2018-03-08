# -*- coding: utf-8 -*-

from .AstNode import *

class CallNode(AstNode):
	"""Function call node

	func -- function (AstNode)
	args -- arguments (list of AstNode)"""
	func = None
	args = None

	def __init__(self, func, args):
		self.func = func
		self.args = args

	def __str__(self):
		return "[Call (%s) with %s]" % (self.func, self.args)

	def __repr__(self):
		return "CallNode(%r, %r)" % (self.func, self.args)