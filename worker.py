
import asyncio
from taskiq import TaskiqScheduler
from tasks import (
    broker,
    to_uppercase,
    to_lowercase,
    reverse_string,
    count_chars,
    repeat_string
)

if __name__ == "__main__":
    scheduler = TaskiqScheduler(broker=broker)
    asyncio.run(scheduler.startup())
