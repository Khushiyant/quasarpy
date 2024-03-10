import redis
import os
from quasar.utils.logger import logger
import pydantic


class RedisConfig(pydantic.BaseModel):
    host: str = os.getenv('LOCALHOST', 'localhost')
    port: int = os.getenv('DB_PORT', 6379)
    db: int = os.getenv('DB', 0)

    @pydantic.validator('port')
    def check_port(cls, v):
        if v < 0 or v > 65535:
            raise ValueError('Port number must be between 0 and 65535')
        return v

    @pydantic.validator('db')
    def check_db(cls, v):
        if v < 0 or v > 15:
            raise ValueError('Database number must be between 0 and 15')
        return v

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class RedisServer:
    logger = logger

    def __init__(self):
        self.logger.info('RedisServer initialized.')
        try:
            self.config = RedisConfig()
        except pydantic.ValidationError as e:
            self.logger.error(e)
            raise e
        self.server = redis.Redis(
            host=self.config.host, port=self.config.port, db=self.config.db)

    def set_value(self, key, value):
        self.server.set(key, value)

    def get_value(self, key):
        return self.server.get(key)

    def delete_value(self, key):
        self.server.delete(key)

    def get_all_keys(self):
        return self.server.keys()


if __name__ == '__main__':
    server = RedisServer()
    print(server.server)
