import logging
from datetime import datetime
from utils.paths import LOG_DIR


def cleanup_old_logs(max_logs: int = 20):
    log_files = sorted(LOG_DIR.glob("*.log"), key=lambda f: f.stat().st_mtime)

    if len(log_files) > max_logs:
        for old_file in log_files[:len(log_files) - max_logs]:
            old_file.unlink()


def setup_logger(name = "mytests", level = "INFO"):
    cleanup_old_logs()
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = LOG_DIR / f"{name}_{timestamp}.log"

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    handler_mytests = logging.FileHandler(log_file, encoding="utf-8")
    handler_mytests.setFormatter(formatter)

    handler_selenium = logging.FileHandler(LOG_DIR / f"selenium_{timestamp}.log", encoding="utf-8")
    handler_selenium.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    logger.addHandler(handler_mytests)

    selenium_logger = logging.getLogger("selenium")
    selenium_logger.setLevel(logging.DEBUG)
    selenium_logger.addHandler(handler_selenium)

    return logger

logger = setup_logger("mytests", level="DEBUG")