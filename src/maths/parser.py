# -*- coding: utf-8 -*-

class TokenType:
	"""Token types used during the lexing process"""
	OPERATOR, STRING, NUMBER, IDENTIFIER, COMMA, PAREN, BRACK = range(7)

class Operators:
	"""Availaboe operators"""
	math = ["+", "-", "*", "/", "%", "^", "&", "|", "XOR"]       # Mathematical (numeric) operators
	comp = ["==", "!=", "<=", "<", ">", ">="]                    # Relational (comparison) operators
	boolean = ["ET", "OU", "NON"]                                # Boolean operators
	ops = math + comp + boolean                                  # All operators

class AstNode:
	"""Base node class"""
	def __init__(self):
		pass

class BinOpNode(AstNode):
	"""Binary (two operands) operator node

	left   -- left operand (AstNode)
	right  -- right operand (AstNode)
	opType -- which binary operator (str)"""
	left = None
	right = None
	opType = None

	def __init__(self, left, right, opType):
		self.left = left
		self.right = right
		self.opType = opType

class UnaryOpNode(AstNode):
	"""Unary operator node

	value  -- value (AstNode)
	opType -- which unary operator (str)"""
	value = None
	opType = None

	def __init__(self, value, opType):
		self.value = value
		self.opType = opType

class CallNode(AstNode):
	"""Function call node

	func -- function name (str)
	args -- arguments (list)"""
	func = None
	args = None

	def __init__(self, func, args):
		self.func = func
		self.args = args

class ArrayAccessNode(AstNode):
	"""Array access node

	array -- array (AstNode)
	index -- index (AstNode)"""
	array = None
	index = None

	def __init__(self, array, index):
		self.array = array
		self.index = index

class NumberNode(AstNode):
	"""Number node

	value -- value (float)"""
	value = None

	def __init__(self, value):
		self.value = value

class StringNode(AstNode):
	"""String node

	value -- value (str)"""
	value = None

	def __init__(self, value):
		self.value = value

class IdentifierNode(AstNode):
	"""Identifier node

	value -- value (str)"""
	value = None

	def __init__(self, value):
		self.value = value

class ListNode(AstNode):
	"""Identifier node

	value -- value (list)"""
	value = None

	def __init__(self, value):
		self.value = value

class Parser:
	"""Main parser class. Transforms a string into an AST tree."""

	expression = None
	tokens = None
	idx = None

	def __init__(self, expr):
		"""Initializes the Parser instance.

		expr -- the expression to be parsed"""
		self.expression = expr
		self.tokens = []
		self.idx = 0
		self.fix_mul()

	def fix_mul(self):
		"""Fixes the multiplication syntax by adding starts (*) between numbers and identifies.

		Example: 2pi becomes 2*pi"""
		for i in range(1, len(self.expression)):
			if self.expression[i - 1].isdigit() and self.expression[i].isalpha():
				self.expression = self.expression[:i] + "*" + self.expression[i:]

	def error(msg, dat=None):
		"""Quick-and-dirty logger. Remove this in production."""
		print("parser: " + msg)

	def nextToken(self):
		"""Reads the next token and advances the position."""
		self.idx += 1
		return self.tokens[self.idx - 1]

	def peekToken(self):
		"""Reads the next token without affecting position."""
		return self.tokens[self.idx]

	def match(self, tokType, value=None):
		"""Checks if the next token matches the specified token type and (optional) value."""
		return self.canRead() and self.peekToken()[0] == tokType and ((not value) or self.peekToken()[1] in (value if type(value) == list else [value]))

	def accept(self, tokType, value=None):
		"""If the next token matches, advance and return True, otherwise return False without advancing."""
		if self.match(tokType, value):
			self.idx += 1
			return True

		return False

	def acceptOp(self, opType):
		"""Wrapper for accept(OPERATOR, opType)."""
		return self.accept(TokenType.OPERATOR, opType)

	def expect(self, opType, value=None):
		"""Asserts the next token is of the specified type and (optional) value. Explodes otherwise."""
		if not self.match(opType, value):
			print("'%s' attendu" % value)
			return None

		return self.nextToken()

	def canRead(self):
		"""Checks if there is still anything to read."""
		return self.idx < len(self.tokens)

	def tokenize(self):
		"""Converts the expression string into a linear list of tokens."""
		import re
		regex = re.compile(r'(\+|-|\*|/|%|\^|==|!=|<=|<|>|>=|\(|\)|\[|\]|\bET\b|\bOU\b|\bXOR\b|\bNON\b|&|\||,)')
		tok = [x.strip() for x in regex.split(self.expression) if x.strip()]

		for token in tok:
			if token.upper() in Operators.ops:
				self.tokens.append((TokenType.OPERATOR, token.upper()))
			elif token == ",":
				self.tokens.append((TokenType.COMMA, ","))
			elif token in ["(", ")"]:
				self.tokens.append((TokenType.PAREN, token))
			elif token in ["[", "]"]:
				self.tokens.append((TokenType.BRACK, token))
			else:
				if token[0] == token[-1] == '"':
					self.tokens.append((TokenType.STRING, token[1:-1]))
				else:
					try:
						num = float(token)
						self.tokens.append((TokenType.NUMBER, num))
					except:
						if re.search('^[a-zA-Z_0-9]+$', token):
							self.tokens.append((TokenType.IDENTIFIER, token))
						else:
							self.tokens.append((None, token))

	def peekOp(self, expected):
		"""Checks if any of the specified operators are to be found."""
		for x in expected:
			if self.acceptOp(x):
				return x

	def parse(self):
		"""Main parsing routine."""
		self.tokenize()
		return self.parseExpr()

	def parseExpr(self):
		"""Parses an expression."""
		return self.parseOr()

	def parseOr(self):
		"""Parses an OR operation."""
		expr = self.parseXor()

		while self.match(TokenType.OPERATOR):
			op = self.peekOp(["OU", "|"])
			if op:
				self.accept(TokenType.OPERATOR)
				expr = BinOpNode(expr, self.parseXor(), "|")
				continue
			break

		return expr

	def parseXor(self):
		"""Parses a XOR operation."""
		expr = self.parseAnd()

		while self.match(TokenType.OPERATOR):
			op = self.peekOp(["XOR"])
			if op:
				self.accept(TokenType.OPERATOR)
				expr = BinOpNode(expr, self.parseAnd(), "XOR")
				continue
			break

		return expr

	def parseAnd(self):
		"""Parses an AND operation."""
		expr = self.parseEquality()

		while self.match(TokenType.OPERATOR):
			op = self.peekOp(["ET", "&"])
			if op:
				self.accept(TokenType.OPERATOR)
				expr = BinOpNode(expr, self.parseEquality(), "&")
				continue
			break

		return expr

	def parseEquality(self):
		"""Parses a comparison/equality."""
		expr = self.parseAdditive()

		while self.match(TokenType.OPERATOR):
			op = self.peekOp(Operators.comp)
			if op:
				self.accept(TokenType.OPERATOR)
				expr = BinOpNode(expr, self.parseAdditive(), op)
				continue
			break

		return expr

	def parseAdditive(self):
		"""Parses an addition or subtraction."""
		expr = self.parseMultiplicative()

		while self.match(TokenType.OPERATOR):
			op = self.peekOp(["+", "-"])
			if op:
				self.accept(TokenType.OPERATOR)
				expr = BinOpNode(expr, self.parseMultiplicative(), op)
				continue
			break

		return expr

	def parseMultiplicative(self):
		"""Parses a product, division, exponentiation or modulus."""
		expr = self.parseUnary()

		while self.match(TokenType.OPERATOR):
			op = self.peekOp(["^", "*", "/", "%"])
			if op:
				self.accept(TokenType.OPERATOR)
				expr = BinOpNode(expr, self.parseUnary(), op)
				continue
			break

		return expr

	def parseUnary(self):
		"""Parses an unary operation."""
		op = self.peekOp(["-", "NON"])
		if op:
			self.accept(TokenType.OPERATOR)
			return UnaryOpNode(self.parseUnary(), op)

		return self.parseCallPre()

	def parseCallPre(self):
		"""Parses a function call (1)."""
		return self.parseCall(self.parseTerm())

	def parseArgList(self, array = False):
		"""Parses an argument list."""
		ret = []

		if array:
			ttype = TokenType.BRACK
			topen = "["
			tend = "]"
		else:
			ttype = TokenType.PAREN
			topen = "("
			tend = ")"

		self.expect(ttype, topen)

		while not self.match(ttype, tend):
			ret.append(self.parseExpr())
			if not self.accept(TokenType.COMMA):
				break

		self.expect(ttype, tend)

		return ret

	def parseIndexer(self):
		"""Parses an indexer expression."""
		self.expect(TokenType.BRACK, "[")

		expr = self.parseExpr()

		self.expect(TokenType.BRACK, "]")

		return expr

	def parseCall(self, left):
		"""Parses a function call (2)."""
		if type(left) == IdentifierNode and self.match(TokenType.PAREN, "("):
			return self.parseCall(CallNode(left.value, self.parseArgList()))
		elif self.match(TokenType.BRACK, "["):
			return self.parseCall(ArrayAccessNode(left, self.parseIndexer()))
		else:
			return left

	def parseTerm(self):
		"""Parses an atomic term."""
		if self.match(TokenType.NUMBER):
			return NumberNode(float(self.nextToken()[1]))
		elif self.accept(TokenType.PAREN, "("):
			stmt = self.parseExpr()
			self.expect(TokenType.PAREN, ")")
			return stmt
		elif self.match(TokenType.BRACK, "["):
			stmt = ListNode(self.parseArgList(True))
			return stmt
		elif self.match(TokenType.STRING):
			return StringNode(self.nextToken()[1])
		elif self.match(TokenType.IDENTIFIER):
			return IdentifierNode(self.nextToken()[1])
		else:
			error("pk tu fais ça")
			return None
