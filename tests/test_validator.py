import pytest
from cle_parcel_lookup.utils.validator import is_valid_parcel_string

def test_is_valid_parcel_string_has_valid_format():
    assert is_valid_parcel_string('123-12-123') == True

def test_is_valid_parcel_string_has_invalid_format():
    assert is_valid_parcel_string('lorem ipsum') == False
    with pytest.raises(TypeError):
        assert is_valid_parcel_string(object()) == False
