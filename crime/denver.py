import datetime
import requests

from django.conf import settings
from crime.models import Crimes


DENVER_FEED_COLUMNS = [
    'INCIDENT_ID',
    'OFFENSE_ID',
    'OFFENSE_CODE',
    'OFFENSE_CODE_EXTENSION',
    'OFFENSE_TYPE_ID',
    'OFFENSE_CATEGORY_ID',
    'FIRST_OCCURRENCE_DATE',
    'LAST_OCCURRENCE_DATE',
    'REPORTED_DATE',
    'INCIDENT_ADDRESS',
    'GEO_X',
    'GEO_Y',
    'GEO_LON',
    'GEO_LAT',
    'DISTRICT_ID',
    'PRECINCT_ID',
    'NEIGHBORHOOD_ID',
]


def import_crime_feed():
    db_session = settings.SQLALCHEMY_SESSION()
    r = requests.get('http://data.denvergov.org/download/gis/crime/csv/crime.csv', stream=True)

    first_row = True
    for line in r.iter_lines():
        if line:
            csv_row = line.split(",")
            # Don't save the column headers
            if (first_row and csv_row[0] == "INCIDENT_ID") or csv_row == DENVER_FEED_COLUMNS:
                first_row = False
                continue

            dr = dict(zip(DENVER_FEED_COLUMNS, csv_row))
            model = csv_to_model(dr)

            if db_session.query(Crimes).filter_by(pd_incident=model.pd_incident).all():
                continue

            db_session.add(model)

    db_session.commit()


def csv_to_model(csv_row):
    kwargs = {'pd_id': 1,
              'pd_incident': int(float(csv_row.get('INCIDENT_ID'))),
              'pd_offense' : int(float(csv_row.get('OFFENSE_ID'))),
              'offense_code_id': int(float(csv_row.get('OFFENSE_CODE'))),
              'offense_code_ext_id': int(float(csv_row.get('OFFENSE_CODE_EXTENSION'))),
              'offense_type': int(float(csv_row.get('OFFENSE_TYPE_ID'))),
              'offense_category': csv_row.get('OFFENSE_CATEGORY_ID'),
              'first_occurrence': datetime.datetime.strptime(csv_row.get('FIRST_OCCURRENCE_DATE'), '%Y-%m-%d %H:%M:%S'),
              'last_occurrence': datetime.datetime.strptime(csv_row.get('LAST_OCCURRENCE_DATE'), '%Y-%m-%d %H:%M:%S') if csv_row.get('LAST_OCCURENCE_DATE') else None,
              'reported_date': datetime.datetime.strptime(csv_row.get('REPORTED_DATE'), '%Y-%m-%d %H:%M:%S'),
              'address': csv_row.get('INCIDENT_ADDRESS'),
              'geo_x': csv_row.get('GEO_X'),
              'geo_y': csv_row.get('GEO_Y'),
              'longitude': csv_row.get('GEO_LON'),
              'latitude': csv_row.get('GEO_LAT'),
              'pd_district': csv_row.get('DISTRICT_ID'),
              'pd_precinct': csv_row.get('PRECINCT_ID'),
              'neighborhood': csv_row.get('NEIGHBORHOOD_ID'),
    }

    return Crimes(**kwargs)
