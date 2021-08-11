import pytest
from utilities import get_regions, get_country_and_language, hash_language


def test_get_regions():
    regions_list = get_regions()
    assert regions_list


def test_get_country_and_language():
    country = get_country_and_language('Americas')
    assert country
    assert country['name']
    assert country['language']


def test_get_country_and_language_invalid_region():
    error = get_country_and_language('foo')
    assert error
    assert error['message'] == 'Not Found'
    assert error['status'] == 404


def test_hash_language():
    string_hash = hash_language('test')
    assert string_hash
    assert len(string_hash) == 40
