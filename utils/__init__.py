"""Init file to declares any default variables"""

import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_FILES = os.path.join(PROJECT_ROOT, "data_files")

# Default input json file if user is not giving data file
DEFAULT_INPUT_FILE = os.path.join(DATA_FILES, "input_data.json")

# Default log directory
DEFAULT_LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
