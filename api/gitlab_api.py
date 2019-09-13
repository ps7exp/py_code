import os
from configuration.config import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, '../config.yml')

config = Config.load_config(CONFIG_PATH)
url = config['API_URL']


class GitlabApi:

    @staticmethod
    def load(path):
        return url + path
