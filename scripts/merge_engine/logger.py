"""
Logging services for the CRM Dataset Build Framework.

This module provides a centralized logging service used by all merge engine
components. It wraps the Python standard logging package behind a consistent
framework API.

Responsibilities:
    - Console logging
    - Optional file logging
    - Section headings
    - Success messages
    - Build timing
"""

from __future__ import annotations

import logging
from pathlib import Path
from time import perf_counter
from typing import Final


DEFAULT_LOGGER_NAME: Final[str] = "CRM Dataset Builder"

DEFAULT_CONSOLE_FORMAT: Final[str] = (
    "%(levelname)-8s %(message)s"
)

DEFAULT_FILE_FORMAT: Final[str] = (
    "%(asctime)s | %(levelname)s | %(message)s"
)


class BuildLogger:
    """
    Central logging service for the CRM Dataset Build Framework.

    A single BuildLogger instance should be shared across all framework
    components instead of creating multiple logger instances.
    """

    def __init__(
        self,
        *,
        name: str = DEFAULT_LOGGER_NAME,
        log_file: Path | None = None,
        verbose: bool = True,
    ) -> None:
        """
        Initialize the logging service.

        Args:
            name:
                Name of the underlying logger.

            log_file:
                Optional log file.

            verbose:
                Enable console logging.
        """

        self._name = name
        self._log_file = log_file
        self._verbose = verbose

        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)
        self._logger.propagate = False

        self._start_time: float | None = None

        self._configure_logger()

    @property
    def name(self) -> str:
        """
        Return the logger name.
        """

        return self._name
    @property
    def log_file(self) -> Path | None:
        """
        Return the configured log file.
        """

        return self._log_file

    @property
    def verbose(self) -> bool:
        """
        Return whether console logging is enabled.
        """

        return self._verbose

    def _configure_logger(self) -> None:
        """
        Configure the underlying Python logger.

        Existing handlers are removed before new handlers are added to
        prevent duplicate log messages.
        """

        self._logger.handlers.clear()

        formatter = self._create_formatter()

        if self._verbose:
            console_handler = self._create_console_handler(formatter)
            self._logger.addHandler(console_handler)

        if self._log_file is not None:
            self._log_file.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            file_handler = self._create_file_handler()

            self._logger.addHandler(file_handler)

    def _create_formatter(self) -> logging.Formatter:
        """
        Create the console formatter.

        Returns:
            Configured logging formatter.
        """

        return logging.Formatter(
            DEFAULT_CONSOLE_FORMAT,
        )

    def _create_console_handler(
        self,
        formatter: logging.Formatter,
    ) -> logging.Handler:
        """
        Create a console log handler.

        Args:
            formatter:
                Formatter applied to the console output.

        Returns:
            Configured console handler.
        """

        handler = logging.StreamHandler()

        handler.setLevel(logging.INFO)

        handler.setFormatter(
            formatter,
        )

        return handler

    def _create_file_handler(
        self,
    ) -> logging.Handler:
        """
        Create a file log handler.

        Returns:
            Configured file handler.
        """

        if self._log_file is None:
            raise ValueError(
                "log_file must not be None."
            )

        formatter = logging.Formatter(
            DEFAULT_FILE_FORMAT,
        )

        handler = logging.FileHandler(
            self._log_file,
            encoding="utf-8",
        )

        handler.setLevel(
            logging.INFO,
        )

        handler.setFormatter(
            formatter,
        )

        return handler
    # ==========================================================
    # Public Logging API
    # ==========================================================

    def info(
        self,
        message: str,
    ) -> None:
        """
        Log an informational message.

        Args:
            message:
                Message to write.
        """

        self._log(
            logging.INFO,
            message,
        )

    def warning(
        self,
        message: str,
    ) -> None:
        """
        Log a warning message.

        Args:
            message:
                Message to write.
        """

        self._log(
            logging.WARNING,
            message,
        )

    def error(
        self,
        message: str,
    ) -> None:
        """
        Log an error message.

        Args:
            message:
                Message to write.
        """

        self._log(
            logging.ERROR,
            message,
        )

    def success(
        self,
        message: str,
    ) -> None:
        """
        Log a success message.

        Success messages are written using the INFO logging level
        with a success prefix.

        Args:
            message:
                Message to write.
        """

        self._log(
            logging.INFO,
            f"SUCCESS  {message}",
        )

    def section(
        self,
        title: str,
    ) -> None:
        """
        Write a formatted section heading.

        Args:
            title:
                Section title.
        """

        separator = "=" * 72

        self.blank()

        self._logger.info(separator)
        self._logger.info(title)
        self._logger.info(separator)

        self.blank()

    def blank(
        self,
    ) -> None:
        """
        Write a blank line.
        """

        if self._verbose:
            print()

    def start_timer(
        self,
    ) -> None:
        """
        Start the elapsed timer.
        """

        self._start_time = perf_counter()

    def elapsed_time(
        self,
    ) -> float:
        """
        Return the elapsed execution time.

        Returns:
            Elapsed time in seconds.
        """

        if self._start_time is None:
            return 0.0

        return perf_counter() - self._start_time
    # ==========================================================
    # Private Methods
    # ==========================================================

    def _log(
        self,
        level: int,
        message: str,
    ) -> None:
        """
        Write a log message using the configured logger.

        Args:
            level:
                Logging level.

            message:
                Message to log.
        """

        self._logger.log(
            level,
            message,
        )

    def reset_timer(
        self,
    ) -> None:
        """
        Reset the elapsed timer.
        """

        self._start_time = None

    def stop_timer(
        self,
    ) -> float:
        """
        Stop the timer and return the elapsed time.

        Returns:
            Elapsed time in seconds.
        """

        elapsed = self.elapsed_time()

        self.reset_timer()

        return elapsed

    def log_elapsed_time(
        self,
        operation: str,
    ) -> float:
        """
        Log the elapsed execution time.

        Args:
            operation:
                Operation description.

        Returns:
            Elapsed time in seconds.
        """

        elapsed = self.stop_timer()

        self.info(
            f"{operation} completed in {elapsed:.3f} seconds."
        )

        return elapsed

    def exception(
        self,
        message: str,
        *,
        exc_info: bool = True,
    ) -> None:
        """
        Log an exception.

        Args:
            message:
                Exception message.

            exc_info:
                Include traceback information.
        """

        self._logger.exception(
            message,
            exc_info=exc_info,
        )

    def set_level(
        self,
        level: int,
    ) -> None:
        """
        Change the logger level.

        Args:
            level:
                New logging level.
        """

        self._logger.setLevel(
            level,
        )

        for handler in self._logger.handlers:
            handler.setLevel(
                level,
            )

    def has_file_logging(
        self,
    ) -> bool:
        """
        Return True when file logging is enabled.
        """

        return self._log_file is not None

    def handler_count(
        self,
    ) -> int:
        """
        Return the number of registered handlers.
        """

        return len(
            self._logger.handlers,
        )