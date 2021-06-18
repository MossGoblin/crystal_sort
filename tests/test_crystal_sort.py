from crystal_sort import __version__
from crystal_sort import crystal_sort

def test_version():
    assert __version__ == '0.1.0'

def test_sort_flag_false():
    bucket = [3, 5, 7, 1, 5, 9, 8, 4, 6, 2]
    ordered_bucket = crystal_sort.sort(bucket)
    assert ordered_bucket == sorted(bucket)

def test_sort_flag_false():
    bucket = [3, 5, 7, 1, 5, 9, 8, 4, 6, 2]
    ordered_bucket = crystal_sort.sort(bucket, True)
    assert ordered_bucket == sorted(bucket)