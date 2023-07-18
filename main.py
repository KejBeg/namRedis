#!/usr/bin/python3 -u

# Import Redis and asyncio
import aioredis
import asyncio

# Import redisClient class
from redisClient import RedisClient

# Import relevant variables from config.py
from config import redisPort, redisHost


# Main function just for testing
async def main():
    redis = RedisClient(redisHost, redisPort)
    await redis.connect()
    await redis.set('foo', 'bar')

    # Value is returned with data type bytes and so we need to decode it
    gottenValue = await redis.get('foo')

    print(gottenValue.decode('utf-8'))
    await redis.disconnect()

# Execute main function with asyncio
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())