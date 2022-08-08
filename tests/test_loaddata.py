import pytest
from FashionCloud.app import models
from FashionCloud.app.utils.LoadandMap import mapping, group_by, data_mapping, catalog_structure, _add_article_data, _add_variation_data, combine_columns


class TestLoadData:
    def test_mapping(self):
        mapping_values = [{
            "source": "EU|37|1",
            "destination": "Europe size 37 blue",
            "source_type": "size_group_code|size_code|color_code",
            "destination_type": "test_column"
        }]

        expected_output = {
            "size_group_code|size_code|color_code": {
                "name": "test_column",
                "EU|37|1": "Europe size 37 blue"
            }
        }

        assert mapping(mapping_values) == expected_output

    def test_combine_columns(self):
            combine_columns_merge_name = ["supplier", "brand", "collection"]
            combine_column_name = "supplier|brand|collection"
            values_data = [{
                "ean": "8719245200978",
                "supplier": "Rupesco BV",
                "brand": "Via Vai",
                "collection": "NW 17-18",
                "season": "winter",
                "article_structure_code": "10",
                "article_number": "15189-02",
                "article_number_2": "15189-02 Aviation Nero",
                "article_number_3": "Aviation",
                "color_code": "1",
                "size_group_code": "EU",
                "size_code": "38",
                "size_name": "38",
                "currency": "EUR",
                "price_buy_net": "58.5",
                "price_sell": "139.95",
                "material": "Aviation",
                "target_area": "Woman Shoes"
            }]

            expected_output = [{
                "ean": "8719245200978",
                "supplier_brand_collection": "Rupesco BV Via Vai NW 17-18",
                "season": "winter",
                "article_structure_code": "10",
                "article_number": "15189-02",
                "article_number_2": "15189-02 Aviation Nero",
                "article_number_3": "Aviation",
                "color_code": "1",
                "size_group_code": "EU",
                "size_code": "38",
                "size_name": "38",
                "currency": "EUR",
                "price_buy_net": "58.5",
                "price_sell": "139.95",
                "material": "Aviation",
                "target_area": "Woman Shoes"
            }]

            assert combine_columns(combine_columns_merge_name, combine_column_name, values_data) != expected_output
