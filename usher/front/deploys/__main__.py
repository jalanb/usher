"""Prepare deploy commands from the queue

Read messages in the queue
    If message has status of  stage/test/beta then prepare a deploy command
    If not: discard the message
"""

import os
import sys


def main() -> int:
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
