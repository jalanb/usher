"""Add message from an issue tracker to the queue

Provide a REST API to add messages to the queue
    It can be called by an issue tracker which will send a POST request with
        1. An issue id (e.g. "ABC-123")
        2. A status (e.g. "in progress", "stage", "test", "beta", "done")

"""

import asyncio
import random
import time

import httpx


async def call_health_check():
    """Call the server's health check endpoint.

    Temp function to get up and testable
    """
    async with httpx.AsyncClient() as client:
        while True:
            try:
                response = await client.get("http://usher_server:8000/health")
                print(f"Health check response: {response.json()}")
            except Exception as e:
                print(f"Error calling health check: {e}")
            await asyncio.sleep(1)


async def main():
    """Run the health check for one minute."""
    start_time = time.time()
    max_calls = random.randint(1, 5)
    while time.time() - start_time < max_calls:  # Run for 1 minute
        await call_health_check()


if __name__ == "__main__":
    asyncio.run(main())
