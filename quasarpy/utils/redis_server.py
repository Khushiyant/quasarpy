import redis
import os
from quasarpy.utils.logger import logger
import pydantic
import datetime
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa


class RedisConfig(pydantic.BaseModel):
    """
    Configuration model for Redis server.
    """

    model_config = pydantic.ConfigDict(env_file=".env", env_file_encoding="utf-8")
    host: str = os.getenv("LOCALHOST", "localhost")
    port: int = os.getenv("DB_PORT", 6379)
    db: int = os.getenv("DB", 0)

    @pydantic.field_validator("port")
    def check_port(cls, v):
        if v < 0 or v > 65535:
            raise ValueError("Port number must be between 0 and 65535")
        return v

    @pydantic.field_validator("db")
    def check_db(cls, v):
        if v < 0 or v > 15:
            raise ValueError("Database number must be between 0 and 15")
        return v


class RedisServer:
    """
    A class representing a Redis server.

    This class provides methods to interact with a Redis server, such as setting a value,
    getting a value, deleting a value, and retrieving all keys.

    Attributes:
        logger: The logger instance used for logging.
        config: The RedisConfig instance containing the configuration for the Redis server.
        server: The Redis server connection.

    Methods:
        __init__: Initializes the RedisServer instance.
        set_value: Sets a value in the Redis server.
        get_value: Retrieves a value from the Redis server.
        delete_value: Deletes a value from the Redis server.
        get_all_keys: Retrieves all keys from the Redis server.
    """

    logger = logger

    def __init__(self, config: RedisConfig):
        self.logger.info("RedisServer initialized.")
        try:
            self.config = config
        except pydantic.ValidationError as e:
            self.logger.error(e)
            raise e
        self.server = redis.Redis(
            host=self.config.host, port=self.config.port, db=self.config.db
        )

    def set_value(self, key, value):
        """
        Sets a value in the Redis server.

        Args:
            key: The key to set.
            value: The value to set.

        Returns:
            None
        """
        self.server.set(key, value)

    def get_value(self, key):
        """
        Retrieves a value from the Redis server.

        Args:
            key: The key to retrieve.

        Returns:
            The value associated with the key, or None if the key does not exist.
        """
        return self.server.get(key)

    def delete_value(self, key):
        """
        Deletes a value from the Redis server.

        Args:
            key: The key to delete.

        Returns:
            None
        """
        self.server.delete(key)

    def get_all_keys(self):
        """
        Retrieves all keys from the Redis server.

        Returns:
            A list of all keys in the Redis server.
        """
        return self.server.keys()


def generate_report(
    config: RedisConfig, format: str, data: dict | str, report_path: str
) -> None:
    def convert_html_to_pdf(source_html, output_filename):
        result_file = open(output_filename, "w+b")
        pisa_status = pisa.CreatePDF(source_html, dest=result_file)
        result_file.close()
        return pisa_status.err

    """
    Generates a report of all keys in the Redis server.

    Args:
        config (RedisConfig): The configuration object for the Redis server.
        format (str): The format in which the report should be generated.

    Returns:
        Union[Dict[str, Any], AnyStr]: The generated report. The return type can be either a dictionary or a string,
        depending on the specified format.

    """

    logger.info("Generating report")

    env = Environment(loader=FileSystemLoader("quasarpy/utils/templates"))
    template = env.get_template("report_template.html")
    report_path_html = f"{report_path}.html"

    html = template.render(time_now=datetime.datetime.now(), files=data)
    with open(report_path_html, "w") as f:
        f.write(html)

    if format == "pdf":
        if not convert_html_to_pdf(html, f"{report_path}.{format}"):
            logger.info("PDF report generated successfully.")

        if os.path.exists(report_path_html):
            os.remove(report_path_html)
            logger.info("HTML report deleted successfully.")
        else:
            logger.error("HTML report not found.")

    logger.info("Report generated successfully.")
