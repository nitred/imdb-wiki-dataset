"""General Utilities."""
import os

from nr_common.configreader import config_from_path

print(config_from_path(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../config.yaml"))))
