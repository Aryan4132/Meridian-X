import os
import sys
import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    # Retrieve logging level from environment
    log_level_str = os.environ.get("MERIDIAN_LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, log_level_str, logging.INFO)
    
    # Resolve log file path inside the workspace's .meridian directory
    # or fallback to user home .meridian directory
    from src.core.config import MERIDIAN_DATA_DIR
    meridian_dir = os.path.join(MERIDIAN_DATA_DIR, ".meridian")
    try:
        os.makedirs(meridian_dir, exist_ok=True)
    except Exception:
        # Fallback to home dir
        home_dir = os.path.expanduser("~")
        meridian_dir = os.path.join(home_dir, ".meridian")
        os.makedirs(meridian_dir, exist_ok=True)
        
    log_file = os.path.join(meridian_dir, "meridian.log")
    
    # Root logger setup
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    
    # Prevent duplicate handlers if re-initialized
    has_file_handler = any(isinstance(h, RotatingFileHandler) for h in root_logger.handlers)
    if not has_file_handler:
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Rotating File Handler (Max 10MB, keep 5 backups)
        file_handler = RotatingFileHandler(
            log_file, maxBytes=10 * 1024 * 1024, backupCount=5, encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_level)
        root_logger.addHandler(file_handler)
        
        # Console Handler (only if not already running under standard context that captures stderr/stdout)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(log_level)
        root_logger.addHandler(console_handler)
        
    logging.info(f"Structured logging initialized. Writing logs to: {log_file}")
    return log_file

def shutdown_logger():
    """Flushes and closes all root logging handlers to release file locks on shutdown."""
    root_logger = logging.getLogger()
    for handler in list(root_logger.handlers):
        try:
            handler.flush()
            handler.close()
            root_logger.removeHandler(handler)
        except Exception:
            pass
    try:
        logging.shutdown()
    except Exception:
        pass
