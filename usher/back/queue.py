"""Provide a queue for use in usher

Queue derives from asyncio.Queue for use with FastAPI apps.

Usher's apps will use a queue of messages
These messages are stored in an `UsherQueue`, derived from `asyncio.Queue`.
For this sake of this example we'll use a test class

>>> from usher.back.queue import UsherQueueSync as UsherQueue
>>> queue = UsherQueue()

Once we have the queue we can put messages in it

>>> message = {"issue_id": "ABC-123", "status": "in progress"}
>>> queue.publish_sync(message)

And then we can read messages back from it

>>> message = queue.consume_sync()
>>> assert message
>>> assert message["issue_id"] == "ABC-123"
>>> assert message["status"] == "in progress"
"""

import asyncio
import doctest


class UsherQueue(asyncio.Queue):
    """Provide an interface to allow

    1. [publish](cci:1://file:///opt/clones/github/jalanb/ushers/usher/usher/queue.py:24:4-26:31) to read messages from the queue # noqa
    2. [consume](cci:1://file:///opt/clones/github/jalanb/ushers/usher/usher/queue.py:28:4-30:62) to add messages to the queue # noqa
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def publish(self, message: dict) -> None:
        """Publish a message to the queue"""
        await self.put(message)

    async def consume(self) -> dict:
        """Consume a single message from the queue"""
        return await self.get()


class UsherQueueSync(UsherQueue):
    """Provide a test class for UsherQueue

    Allows synchronous access to the queue for testing
    """

    def publish_sync(self, message: dict) -> None:
        """Synchronous wrapper for publish"""
        asyncio.run(self.publish(message))

    def assert_full(self) -> None:
        """Assert that the queue is has some items"""
        if self.empty():
            raise asyncio.QueueEmpty

    def consume_sync(self) -> dict:
        """Synchronous wrapper for consume"""
        self.assert_full()
        return asyncio.run(self.consume())


if __name__ == "__main__":
    doctest.testmod(verbose=True, raise_on_error=True)
