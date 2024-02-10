import redis
import os
from dataclasses import dataclass

LOCALHOST = os.getenv('LOCALHOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', 6379)
DB = os.getenv('DB', 0)

r = redis.Redis(host=LOCALHOST, port=DB_PORT, db=DB)


@dataclass
class RedisServer:
    r = redis.Redis(host=LOCALHOST, port=DB_PORT, db=DB)

    def set_value(self, key, value):
        self.r.set(key, value)

    def get_value(self, key):
        return self.r.get(key)

    def delete_value(self, key):
        self.r.delete(key)

    def get_all_keys(self):
        return self.r.keys()


if __name__ == '__main__':
    server = RedisServer()
    server.set_value('key', 'value')
    # server.set_value('key', 'value')
    # print(timeit.timeit(lambda: server.get_value('key'), number=10000)) #
    # 1.0435702909890097
