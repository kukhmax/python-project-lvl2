from gendiff.formatters.stylish import get_stylish



DIFF_OF_NESTED_FILES = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


def test_generate_diff_with_nested_yaml():
    file1 = 'tests/fixtures/file_nested1.yaml'
    file2 = 'tests/fixtures/file_nested2.yaml'
    assert get_stylish(file1, file2) == DIFF_OF_NESTED_FILES


def test_generate_diff_with_nested_json():
    file1 = 'tests/fixtures/file_nested1.json'
    file2 = 'tests/fixtures/file_nested2.json'
    assert get_stylish(file1, file2) == DIFF_OF_NESTED_FILES