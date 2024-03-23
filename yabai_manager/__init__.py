__version__ = '1.1.0'

import logging
import os


logging.basicConfig(
    level=logging.INFO,
    filename=os.path.expanduser('~/yabai_manager.log'),
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

LOGGER = logging.getLogger("Yabai Manager")