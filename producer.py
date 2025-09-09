
import asyncio
from tasks import to_uppercase, to_lowercase, reverse_string, count_chars, repeat_string, broker

async def main():
    await broker.startup()
    
    # Send tasks
    await to_uppercase.kiq("Hello from Producer 🚀")
    await to_lowercase.kiq("HELLO WORLD🙌")
    await reverse_string.kiq("Python🐍")
    await count_chars.kiq("Count me!🔢")
    await repeat_string.kiq("RepeatMe🤖")
    
    await broker.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
