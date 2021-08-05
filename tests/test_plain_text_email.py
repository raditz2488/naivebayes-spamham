import unittest
import io
import re
from email_object import EmailObject

class TestPlaintextEmailObject(unittest.TestCase):
    CLRF = '\n\n'

    def setUp(self):
        self.file_path = './tests/fixtures/plain.eml'
        self.file_io = io.open(self.file_path, 'r')
        self.text = self.file_io.read()
        self.file_io.seek(0)
        self.email_object = EmailObject(self.file_io)

    def test_parse_plain_body(self):
        # Seperate body from header in the plain email.
        # The header is the first element after splitting text with CLRF, followed by the body.
        body = self.CLRF.join(self.text.split(self.CLRF)[1:])
        self.assertEqual(self.email_object.body(), body)