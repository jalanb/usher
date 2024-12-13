from unittest import TestCase

from usher.back.messages import Message


class TestMessage(TestCase):
    def test_message_with_project(self):
        """Check we can construct a message

        And that attribute `project` is set correctly
        """
        message = Message("ABC-123", "in progress")
        assert message.project == "ABC"

    def test_missing_project(self):
        """If the project name is missing from key, should raise an exception"""
        with self.assertRaises(KeyError):
            Message("123", "in progress")
