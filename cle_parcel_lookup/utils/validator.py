""" Validator module contains methods for validation """

import re


def is_valid_parcel_string(parcel_string):
    """ Check if parcel string is in correct format """
    return re.match("[0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9]", parcel_string) is not None
