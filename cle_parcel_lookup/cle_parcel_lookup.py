""" cle_parcel_lookup module defines routes for index and parcel """

import json
from string import Template
import xmltodict
import requests
from flask import Blueprint, render_template, Response
from .utils.validator import is_valid_parcel_string

bp = Blueprint('cle_parcel_lookup', __name__)


@bp.route('/')
def index():
    """ Main route that renders the homepage """
    return render_template('cle_parcel_lookup/index.html')


@bp.route('/parcel/<parcel_string>')
def parcel(parcel_string):
    """ Endpoint that converts XML response to JSON for any given parcel string """
    if not is_valid_parcel_string(parcel_string):
        return Response(f"Parcel string {parcel_string} does not conform to format NNN-NN-NNN",
            status=400)

    template=Template('http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=$parcel')
    endpoint=template.substitute(parcel=parcel_string)
    response = requests.get(endpoint)
    if response.status_code == 200:
        xml = response.text.strip()
        return f'{json.dumps(xmltodict.parse(xml))}'

    return Response(f'Invalid response code returned for parcel {parcel_string}:'
        f'{response.status_code}', status=400)
