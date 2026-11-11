import unittest
from lisp import tokenize, parse

class TokenizeTests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(tokenize("(+ 1 2)"), ['(', '+', '1', '2', ')'])

    def test_nested(self):
        self.assertEqual(tokenize("(+ 1 (* 2 3))"),
                         ['(', '+', '1', '(', '*', '2', '3', ')', ')'])

    def test_extra_whitespace(self):
        self.assertEqual(tokenize("  ( +   1 2 ) "), ['(', '+', '1', '2', ')'])

class ParseTests(unittest.TestCase):
    def test_number(self):
        self.assertEqual(parse("42"), 42)

    def test_symbol(self):
        self.assertEqual(parse("x"), "x")

    def test_flat_list(self):
        self.assertEqual(parse("(+ 1 2)"), ["+", 1, 2])

    def test_nested_list(self):
        self.assertEqual(parse("(+ 1 (* 2 3))"), ["+", 1, ["*", 2, 3]])

    def test_missing_close_paren(self):
        with self.assertRaises(SyntaxError):
            parse("(+ 1 2")

    def test_unexpected_close_paren(self):
        with self.assertRaises(SyntaxError):
            parse(")")