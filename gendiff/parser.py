import json
import yaml
import ini
import pathlib


def parse(filepath):
    ext = pathlib.Path(filepath).suffix
    if ext == '.json':
        return json.load(open(filepath))
    elif ext == '.yml' or ext == '.yaml':
        return yaml.safe_load(open(filepath))
    elif ext == '.ini':
        return ini.load(open(filepath))
    else:
        raise Exception('{} file format not supported'.format(ext))