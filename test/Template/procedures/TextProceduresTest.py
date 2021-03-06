import unittest
from ...BaseTestCase import BaseTestCase
from kombi.Template import Template

class TextProceduresTest(BaseTestCase):
    """Test Text template procedures."""

    def testUpper(self):
        """
        Test that the upper procedure works properly.
        """
        result = Template.runProcedure("upper", "boop")
        self.assertEqual(result, "BOOP")

    def testConcat(self):
        """
        Test that concat procedure works properly.
        """
        result = Template.runProcedure("concat", "BOOP", " ", "FOO")
        self.assertEqual(result, "BOOP FOO")

    def testLower(self):
        """
        Test that the lower procedure works properly.
        """
        result = Template.runProcedure("lower", "BOOP")
        self.assertEqual(result, "boop")

    def testReplace(self):
        """
        Test that the replace procedure works properly.
        """
        result = Template.runProcedure("replace", "Boop", "o", "e")
        self.assertEqual(result, "Beep")

    def testRemove(self):
        """
        Test that the remove procedure works properly.
        """
        result = Template.runProcedure("remove", "boop", "p")
        self.assertEqual(result, "boo")


if __name__ == "__main__":
    unittest.main()
