import csv
from typing import Dict, List, Union
import copy


class ExtractData:

    def __init__(self, file, file_values):
        self._file = file
        self._file_values = file_values

    def return_from_file(self):
        self._file_values = []
        try:
            with open(self._file, newline="") as csvfile:
                data = csv.DictReader(csvfile, delimiter=";")
                for row in data:
                    self._file_values.append(row)
        except FileNotFoundError:
            print(f"{self._file} Not found")

        return self._file_values


class Mapping:
    def __init__(self, mapping_file_data, map_data):
        self.mapping_file_data = mapping_file_data
        self._map_data = map_data

    def return_map_data(self):
        self._map_data = {}
        for row in self.mapping_file_data:
            if row['source_type'] not in self._map_data.keys():
                self._map_data[row['source_type']] = {}
            self._map_data[row['source_type']]['name'] = row['destination_type']
            self._map_data[row['source_type']][row['source']] = row['destination']
        print(f" map_data after mapping {self._map_data}")
        return self._map_data


class MapData:

    def __init__(self, grouping_data: List[Dict[str, str]], mapping_file_values: Dict[str, dict]):
        self.grouping_data = grouping_data
        self.mapping_file_values = mapping_file_values

    def map_data_output(self) -> List[Dict[str, str]]:
        self._map_data = []
        for row in self.grouping_data:
            mapped_row = {}
            for key, value in row.items():
                if not value:
                    continue
                if key in self.mapping_file_values.keys():
                    column_name = self.mapping_file_values[key]['name']
                    column_value = self.mapping_file_values[key][value]
                    mapped_row[column_name] = column_value
                else:
                    mapped_row[key] = value
                self._map_data.append(mapped_row)
            return self._map_data


class CatalogStructure:

    def __init__(self, map_data_ret: List[Dict[str, str]]):
        self.map_data_incoming = map_data_ret

    def catalog_structure(self) -> Dict[str, Union[str, dict]]:
        self._catalog_structure_format = {
            "brand": " ",
            "supplier": " ",
            "collection": "",
            "season": "",
            "article": {},
        }

        for row in self.map_data_incoming:
            self._catalog_structure_format['brand'] = row['brand']
            self._catalog_structure_format['supplier'] = row['supplier']
            self._catalog_structure_format['collection'] = row['collection']
            self._catalog_structure_format['season'] = row['season']
            if not row['article_number'] in self._catalog_structure_format['article'].keys():
                self._catalog_structure_format = \
                    _add_article_data(self._catalog_structure_format, row)

            # if row['ean'] in self._catalog_structure_format['article'][row['article_number']]['variation'].keys():
                # continue
            else:
                self._catalog_structure_format = \
                    _add_variation_data(self._catalog_structure_format, row)

        return self._catalog_structure_format


def _add_article_data(catalog_structure_format: dict, row: Dict[str, str]) -> dict:
    catalog_structure_format = copy.deepcopy(catalog_structure_format)
    catalog_structure_format['article'][row['article_number']] = {}
    catalog_structure_format['article'][row['article_number']]['article_structure'] = row[
        'article_structure']
    catalog_structure_format['article'][row['article_number']]['article_number_2'] = row['article_number_2']
    catalog_structure_format['article'][row['article_number']]['article_number_3'] = row['article_number_3']
    catalog_structure_format['article'][row['article_number']]['target_area'] = row['target_area']
    catalog_structure_format['article'][row['article_number']]['variation'] = {}

    return catalog_structure_format


def _add_variation_data(catalog_structure_format: dict, row: Dict[str, str]) -> dict:
    catalog_structure_format = copy.deepcopy(catalog_structure_format)
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']] = {}
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['color'] = \
        row['color']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['size_code'] = \
        row['size_code']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['size_name'] = \
        row['size_name']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['currency'] = \
        row['currency']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['price_buy_net'] = \
        row['price_buy_net']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['price_sell'] = \
        row['price_sell']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['material'] = \
        row['material']

    return catalog_structure_format