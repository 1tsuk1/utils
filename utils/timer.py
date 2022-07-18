"""
ref: https://qiita.com/kaggle_grandmaster-arai-san/items/d59b2fb7142ec7e270a5#timer
"""
import logging
import time
from contextlib import contextmanager
from typing import Optional


@contextmanager
def timer(name: str, logger: Optional[logging.Logger] = None):
    t0 = time.time()
    yield
    msg = f"[{name}] done in {time.time()-t0:.0f} s"
    if logger:
        logger.info(msg)
    else:
        print(msg)
