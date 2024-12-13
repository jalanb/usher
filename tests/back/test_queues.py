import asyncio
import unittest

from usher.back.messages import Message
from usher.back.queues import UsherQueueSync as UsherQueue

import pytest

class TestUsherQueue(unittest.TestCase):
    """Test the UsherQueue class"""

    def test_assert_full(self):
        """Test that asserting an empty queue raises an exception"""
        queue = UsherQueue()
        with pytest.raises(asyncio.QueueEmpty):
            queue.assert_full()

    def test_assert_not_full(self):
        """Test that asserting a full queue does not raise an exception"""
        queue = UsherQueue()
        message = Message("ABC-123", "in progress")
        queue.publish_sync(message)
        queue.assert_full()

    def test_read_empty_queue(self):
        """Test that consuming from an empty queue rises an exception"""
        queue = UsherQueue()
        with pytest.raises(asyncio.QueueEmpty):
            # breakpoint()
            queue.consume_sync()
