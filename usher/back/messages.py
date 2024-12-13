"""Hand messages for Usher's back end

A "message" is a item in the queue
    It has a key and a status

>>> from usher.back.messages import Message
>>> message = Message("ABC-123", "in progress")
>>> assert message.key == "ABC-123"
>>> assert message.status == "in progress"

It conveniently also derives a project
    Per Jira: the project is before the "-" in the key

>>> assert message.project == "ABC"

Less conveniently it raises an exception if there is no project in the key

>>> try:
>>>     Message("ABC", "in progress")
>>> except KeyError:
>>>     print("Fail")
Fail

"""

from dataclasses import dataclass


@dataclass
class Message:
    key: str
    status: str

    def __post__init__(self):
        """Set the project from the key"""
        if "-" in self.key:
            self.project = key.split("-")[0] if "-" in key else ""
        else:
            raise KeyError(f"No project in issue id: {key}")
