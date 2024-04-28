from quasarpy.utils.errors import LiteralEvalError
from quasarpy.utils.logger import logger
from quasarpy.utils.redis_server import RedisConfig


# Test the logger
def test_logger() -> None:
    logger.info('test')
    logger.error('test')
    logger.warning('test')
    logger.debug('test')


# Error tests
def test_literal_eval_error() -> None:
    try:
        raise LiteralEvalError('test')
    except LiteralEvalError as e:
        assert str(e) == 'test'


# Redis server tests
def test_redis_config_valid() -> None:
    config = RedisConfig()
    assert config.host == 'localhost'
    assert config.port == 6379
    assert config.db == 0
