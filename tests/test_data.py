from FashionCloud.app.utils.loaddata import ExtractData
from FashionCloud.app.application import extract_data
import pytest


class TestData:

    def test_extract_data(self):
        mappings_file_name = "../mappings.csv"
        price_catalog_name = "../pricat.csv"

        mappings_file_data = ExtractData(mappings_file_name, file_values=None)
        price_catalog_data = ExtractData(price_catalog_name, file_values=None)

        # with pytest.raises(FileNotFoundError):
            # ExtractData('../vivek.exe', file_values=None)

    def test_extract_data_application(self):
        extract_data()

test = TestData
print(test.test_extract_data)



