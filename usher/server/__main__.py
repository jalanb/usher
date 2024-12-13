"""Maintain a queue of status messages

Each message contains:
    1. An issue id (e.g. "ABC-123")
    2. A status (e.g. "in progress", "stage", "test", "beta", "done")

Provide a REST API to allow at least
    1. PUT to add messages to the queue
    2. GET to read messages from the queue
"""

import os
import sys

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}

def main() -> int:
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
