class LiteralEvalError(Exception):
    """Raised when an error occurs during the literal evaluation of a string."""
    def __init__(self, message: str) -> None:
        super().__init__(message)