from platformdirs import *
import json
import sys
import os

class Config_Manager:
    def __init__(self, app_name, default_config, folders_to_create):
        self.app_name = app_name
        self.data_dir = user_data_dir(app_name)
        self.config_path = os.path.join(self.data_dir, "config.json")
        self.default_config = default_config
        self.folders_to_create = folders_to_create

    def load_config(self):
        try:
            with open(self.config_path,"r") as f:
                return json.load(f)
        except:
            print("No (or corrupt) config file found. Default config file created at {0}. Please edit it and rerun.".format(self.config_path))
            os.makedirs(self.data_dir, exist_ok=True)
            for folder in self.folders_to_create:
                os.makedirs(os.path.join(self.data_dir, folder), exist_ok=True)
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.default_config, f, ensure_ascii=False, indent=4)
            sys.exit("No (or corrupt) config")

    def print_config_path(self):
        print(self.config_path)
