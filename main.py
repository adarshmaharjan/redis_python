import os

import redis
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Redis configuration from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_USER = os.getenv("REDIS_USER")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    username=REDIS_USER,
    password=REDIS_PASSWORD,
    decode_responses=True,
)
# Initialize Redis connection
try:
    # Basic operations
    r.set("foo", "bar")
    value = r.get("foo")
    print(f"Connected to Redis at {REDIS_HOST}:{REDIS_PORT}")
    print(f"Value of 'foo': {value}")

    r.hset(
        "user-session:123",
        mapping={
            "name": "adarsh",
            "email": "[EMAIL_ADDRESS]",
            "role": "admin",
            "last_login": "2022-01-01T00:00:00Z",
        },
    )

    user = r.hgetall("user-session:123")
    print(f"User session: {user}")

except redis.ConnectionError as e:
    print(f"Could not connect to Redis: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    r.close()
