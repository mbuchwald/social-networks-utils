from enum import IntEnum


class LogLevel(IntEnum):
    TRACE = 1
    DEBUG = 2
    INFO = 3
    WARN = 4
    ERROR = 5
    NOTHING = 6

    def __gt__(self, other):
        self.value


class Logger:
    def __init__(self, level):
        self.level = level

    def _loggear(self, wanted, msg):
        if wanted >= self.level:
            print(msg)

    def debug(self, msg):
        self._loggear(LogLevel.DEBUG, msg)

    def trace(self, msg):
        self._loggear(LogLevel.TRACE, msg)

    def info(self, msg):
        self._loggear(LogLevel.INFO, msg)

    def warn(self, msg):
        self._loggear(LogLevel.WARN, msg)

    def error(self, msg):
        self._loggear(LogLevel.ERROR, msg)