import asyncio
import unittest

from usher.queue import UsherQueueTest as UsherQueue

import pytest

class TestUsherQueue(unittest.TestCase):
    """Test the UsherQueue class"""

    def test_read_empty_queue(self):
        """Test that consuming from an empty queue rises an exception"""
        queue = UsherQueue()
        with pytest.raises(asyncio.QueueEmpty):
            queue.consume_sync()
