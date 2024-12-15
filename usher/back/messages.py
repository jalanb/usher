"""Hand messages for Usher's back end

A "message" is a item in the queue
    It has a key and a status

>>> from usher.back.messages import Message
>>> message = Message("ABC-123", "in progress")
>>> assert message.key == "ABC-123"
>>> assert message.status == "in progress"

It conveniently also derives a project

>>> assert message.project == "ABC"

Less conveniently it raises an KeyError if there is no project in the issue key
    Per Jira: a project is before an "-" in the key

>>> try:
...     Message("fred", "beta")
... except KeyError:
...     print("Fail")
Fail

"""

from dataclasses import dataclass


@dataclass
class Message:
    key: str
    status: str

    def __post_init__(self):
        """Set the project from the key"""
        if "-" in self.key:
            self.project = self.key.split("-")[0] if "-" in self.key else ""
        else:
            raise KeyError(f"No project in issue id: {self.key}")
