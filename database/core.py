# from redis_om import get_redis_connection
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# redis = get_redis_connection(
#     host=str(getenv("REDIS_HOST")),
#     port=str(getenv("REDIS_PORT")),
#     password=str(getenv("REDIS_PASSWORD")),
#     decode_responses=True
# )
