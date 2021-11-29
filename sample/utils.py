import os
from pathlib import Path

# Constants

ROOT_DIR = Path(__file__).parent.parent
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')

MAX_PASS_LEN = 10

# Variables

path_to_archive = ''
found_password = 'PLACEHOLDER'

# Methods

def get_resource(name):
    return os.path.join(RESOURCES_DIR, name)