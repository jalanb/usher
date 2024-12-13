"""Hand messages for Usher's back end

A "message" is a item in the queue
    It has a key and a status, and a (derived) project

>>> from usher.back.messages import Message
>>> message = Message("ABC-123", "in progress")
>>> assert message.key == "ABC-123"
>>> assert message.status == "in progress"
>>> assert message.project == "ABC"
"""

from dataclasses import dataclass


@dataclass
class Message:
    key: str
    status: str

    def __post__init__(self, key: str, status: str):
        self.key = key
        self.status = status
        if "-" in key:
            self.project = key.split("-")[0] if "-" in key else ""
        else:
            raise KeyError(f"No project in issue id: {key}")
