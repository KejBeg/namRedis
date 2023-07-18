#!/usr/bin/python3 -u

# Import Redis and asyncio
import aioredis
import asyncio

class RedisClient:
    """
    Redis client class to connect to the Redis server and setting/getting values
    """
    
    def __init__(self, host, port):
        """
        Constructor for RedisClient class

        Args:
            host (_type_): host name or IP address of the Redis server
            port (_type_): port number of the Redis server
        """

        self.host = host
        self.port = port
        self.redis = None

    async def connect(self):
        """
        Connect to the Redis server
        """
        
        try:
            self.redis = await aioredis.from_url(f'redis://{self.host}:{self.port}')
            await self.redis.ping()
        except aioredis.RedisError as e:
            print(f'Error connecting to Redis server: {e}')
            return

    async def disconnect(self):
        """
        Disconnect from the Redis server
        """

        try:
            await self.redis.close()
        except aioredis.RedisError as e:
            print(f'Error disconnecting from Redis server: {e}')
            return            
            
    async def get(self, key):
        """
        Get the value for the given key

        Args:
            key (_type_): key to get the value for

        Returns:
            _type_: depends on the value type
        """

        try:
            return await self.redis.get(key)
        except aioredis.RedisError as e:
            print(f'Error getting value for key {key}: {e}')
            return
        
    async def set(self, key, value):
        """
        Set the value for the given key

        Args:
            key (_type_): key to set the value for
            value (_type_): value to set
        """

        try:
            await self.redis.set(key, value)
        except aioredis.RedisError as e:
            print(f'Error setting value for key {key}, value {value}: {e}')
            return
        