
from taskiq import TaskiqDepends
from taskiq_nats import NatsBroker

# Connect to NATS
broker = NatsBroker("nats://localhost:4222", queue="workers")


# Task 1: Convert string to uppercase
@broker.task
async def to_uppercase(msg: str) -> str:
    print(f"Worker received (to_uppercase): {msg}")
    return msg.upper()


# Task 2: Convert string to lowercase
@broker.task
async def to_lowercase(msg: str) -> str:
    print(f"Worker received (to_lowercase): {msg}")
    return msg.lower()


# Task 3: Reverse the string
@broker.task
async def reverse_string(msg: str) -> str:
    print(f"Worker received (reverse_string): {msg}")
    return msg[::-1]


# Task 4: Count number of characters
@broker.task
async def count_chars(msg: str) -> int:
    print(f"Worker received (count_chars): {msg}")
    return len(msg)


# Task 5: Repeat string twice
@broker.task
async def repeat_string(msg: str) -> str:
    print(f"Worker received (repeat_string): {msg}")
    return msg * 2
