import unittest
import app
import test_config
import json

STATUS_CODE_MSG = "Status code not OK"


class AppTestMethods(unittest.TestCase):
    """
    Tests for each endpoint of the flask application.

    This relies on a "test_config.py" being setup in the same folder
    as this file. Its contents should match that of config.py, but
    should point towards a local database instead of the production
    database.

    IMPORTANT: The local database should be an import of the test_data.sql
    that is on the github repo at database/test_data.sql. This is needed so
    that the results of data related tests are predictable.

    As of writing this, the test_data.sql contains a trimmed version of a
    dump of the production database on April 5th 2021. In order to keep the
    size down, only 9 stations and data going back 2 weeks were kept.

    A change to the production database structure (including new stored
    procedures) may necessitate a change to the test data as well as
    the tests.
    """

    def setUp(self):
        app.app.testing = True
        app.init_db(test_config.CONNECTION_STRING)
        self.app = app.app.test_client()

    def test_title_icon(self):
        response = self.app.get("/favicon.ico")
        self.assertEqual(response.status_code, 200, STATUS_CODE_MSG)

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200, STATUS_CODE_MSG)

    def test_stations_static(self):

        response = self.app.get("/stations/static")
        self.assertEqual(response.status_code, 200, STATUS_CODE_MSG)

        data = json.loads(response.get_data("application/json"))

        # Check rowcount
        self.assertEqual(data["rowcount"], 9, "Unexpected number of rows")

        # Check the first two rows of data.
        checks = [
            ["address", ['Christchurch Place', 'Exchequer Street']],
            ["latitude", [53.343368, 53.343034]],
            ["longitude", [-6.27012, -6.263578]],
            ["name", ['CHRISTCHURCH PLACE', 'EXCHEQUER STREET']],
            ["number", [6, 9]],
        ]

        for name, values in checks:
            message = "Unexpected data for column: " + name
            self.assertListEqual(data[name][:2], values, message)

    def test_stations_latest(self):

        response = self.app.get("/stations/latest")
        self.assertEqual(response.status_code, 200, STATUS_CODE_MSG)

        data = json.loads(response.get_data("application/json"))

        # Check rowcount
        self.assertEqual(data["rowcount"], 9, "Unexpected number of rows")

        # Check the first two rows of data.
        checks = [
            # Columns from the static station table
            ["address", ['Christchurch Place', 'Exchequer Street']],
            ["latitude", [53.343368, 53.343034]],
            ["longitude", [-6.27012, -6.263578]],
            ["name", ['CHRISTCHURCH PLACE', 'EXCHEQUER STREET']],
            ["number", [6, 9]],
            # Columns from the station_update table
            ["available_bikes", [2, 11]],
            ["banking", [0, 0]],
            ["bike_stands", [20, 24]],
            ["bonus", [0, 0]],
            ["last_update", [None, None]],
            ["retrieved", [1617614878000000000, 1617614878000000000]],
            ["status", ['OPEN', 'OPEN']],
        ]

        for name, values in checks:
            message = "Unexpected data for column: " + name
            self.assertListEqual(data[name][:2], values, message)

    def test_stations_template(self):
        response = self.app.get("/stations/template")
        self.assertEqual(response.status_code, 200, STATUS_CODE_MSG)

    def test_weather_data(self):
        response = self.app.get("/weather/data")
        self.assertEqual(response.status_code, 200, STATUS_CODE_MSG)

        data = json.loads(response.get_data("application/json"))
        self.assertTrue(5 <= len(data.keys()) <= 6)
        self.assertIsInstance(data, dict, "Expected return object of type dict")
        self.assertEqual(data['0']['description'], "Clouds", "Expected description 'Clouds'")

    def test_weather_icons(self):
        response = self.app.get("/weather/icons/blah")
        self.assertEqual(response.status_code, 200, STATUS_CODE_MSG)

    def test_station_prediction(self):
        response = self.app.get("/stations/prediction?date=2021-04-13&hour=4")
        with self.subTest():
            self.assertEqual(response.status_code, 200, STATUS_CODE_MSG), "Bad response status"

        with self.subTest():
            data = json.loads(response.get_data("application/json"))
            self.assertIsInstance(data, dict, "Expected return object of type dict")
            self.assertEqual(len(data.keys()), 109, "Expected 109 entries in return object")

    def test_search(self):
        response = self.app.get("/search?q=Talbot")
        self.assertEqual(response.status_code, 200, STATUS_CODE_MSG)
