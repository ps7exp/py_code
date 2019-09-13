import yaml


class Config:
    @staticmethod
    def load_config(config_file):
        with open(config_file, 'r') as ymlfile:
            try:
                return yaml.safe_load(ymlfile)
            except yaml.YAMLError as exc:
                print(exc)
