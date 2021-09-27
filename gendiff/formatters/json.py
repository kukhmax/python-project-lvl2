#!/usr/bin/env python3

import json
from gendiff.difference import make_diff


def get_json(path_file1: str, path_file2: str) -> str:
    """Serialize 'diff' to a JSON formatted 'str' """
    diff = make_diff(path_file1, path_file2)
    return json.dumps(diff)
