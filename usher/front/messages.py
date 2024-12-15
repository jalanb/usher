"""Provide a message for use in the front end"""

from pydantic import BaseModel

from usher.back.messages import Message

class FrontMessage(BaseModel):
    """A message from a client

    Example:
        >>> message = Message(issue_id="ABC-123", status="test")
        >>> message.issue_id
        'ABC-123'
        >>> message.status
        'test'
    """
    issue_id: str
    status: str

    @property
    def back(self) -> Message:
        """Convert to a `Message`"""
        return Message(key=self.issue_id, status=self.status)
