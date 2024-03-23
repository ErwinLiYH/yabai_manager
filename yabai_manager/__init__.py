__version__ = '1.1.0'

import logging
import os


logging.basicConfig(
    level=logging.CRITICAL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

LOGGER = logging.getLogger("Yabai Manager")
fh = logging.FileHandler(os.path.expanduser('~/yabai_manager.log'), mode='w', delay=True)
LOGGER.addHandler(fh)