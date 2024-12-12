from functools import wraps
import time
import logging

logger = logging.getLogger(__name__)

def monitor_performance(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        duration = time.time() - start
        logger.info(f"{f.__name__} took {duration:.2f} seconds to execute")
        return result
    return wrapper