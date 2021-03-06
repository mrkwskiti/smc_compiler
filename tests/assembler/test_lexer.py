import unittest
from smc.assembler import TokenType
from smc.assembler import Lexer

class TestLexer(unittest.TestCase):
  def test_tokens(self):
    records = (
      ('1234', TokenType.INT, 1234),
      ('add', TokenType.ADD, 'add'),
      ('.fill', TokenType.FILL, '.fill'),
      ('mark', TokenType.WORD, 'mark'),
      ('(', TokenType.SPC, '('),
      ('+', TokenType.PLUS, '+'),
      ('-', TokenType.MINUS, '-')
    )

    for text, token_type, token_value in records:
      lexer = Lexer(text)
      token = lexer.get_next_token()
      self.assertEqual(token.type, token_type)
      self.assertEqual(token.value, token_value)