# flake8: noqa

from gendiff.formatters.engine import generate_diff

DIFF_JSON = """[{"key": "common", "value": [{"key": "follow", "value": false, "meta": "in_second"}, {"key": "setting1", "value": "Value 1", "meta": "in_both"}, {"key": "setting2", "value": 200, "meta": "in_first"}, {"key": "setting3", "value": true, "meta": "in_first"}, {"key": "setting3", "value": {"key": "value"}, "meta": "in_second"}, {"key": "setting4", "value": "blah blah", "meta": "in_second"}, {"key": "setting5", "value": {"key5": "value5"}, "meta": "in_second"}, {"key": "setting6", "value": [{"key": "doge", "value": [{"key": "wow", "value": "too much", "meta": "in_first"}, {"key": "wow", "value": "so much", "meta": "in_second"}], "meta": "in_both"}, {"key": "key", "value": "value", "meta": "in_both"}, {"key": "ops", "value": "vops", "meta": "in_second"}], "meta": "in_both"}], "meta": "in_both"}, {"key": "group1", "value": [{"key": "baz", "value": "bas", "meta": "in_first"}, {"key": "baz", "value": "bars", "meta": "in_second"}, {"key": "foo", "value": "bar", "meta": "in_both"}, {"key": "nest", "value": {"key": "value"}, "meta": "in_first"}, {"key": "nest", "value": "str", "meta": "in_second"}], "meta": "in_both"}, {"key": "group2", "value": {"abc": 12345, "deep": {"id": 45}}, "meta": "in_first"}, {"key": "group3", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}, "meta": "in_second"}, {"key": "group4", "value": [{"key": "default", "value": null, "meta": "in_first"}, {"key": "default", "value": "", "meta": "in_second"}, {"key": "foo", "value": 0, "meta": "in_first"}, {"key": "foo", "value": null, "meta": "in_second"}, {"key": "isNested", "value": false, "meta": "in_first"}, {"key": "isNested", "value": "none", "meta": "in_second"}, {"key": "key", "value": false, "meta": "in_second"}, {"key": "nest", "value": [{"key": "bar", "value": "", "meta": "in_first"}, {"key": "bar", "value": 0, "meta": "in_second"}, {"key": "isNested", "value": true, "meta": "in_first"}], "meta": "in_both"}, {"key": "someKey", "value": true, "meta": "in_second"}, {"key": "type", "value": "bas", "meta": "in_first"}, {"key": "type", "value": "bar", "meta": "in_second"}], "meta": "in_both"}]"""


def test_get_json_with_nested_yaml():
    file1 = 'tests/fixtures/file_nested1.yaml'
    file2 = 'tests/fixtures/file_nested2.yaml'
    assert generate_diff(file1, file2, 'json') == DIFF_JSON


def test_get_json_with_nested_json():
    file1 = 'tests/fixtures/file_nested1.json'
    file2 = 'tests/fixtures/file_nested2.json'
    assert generate_diff(file1, file2, 'json') == DIFF_JSON
