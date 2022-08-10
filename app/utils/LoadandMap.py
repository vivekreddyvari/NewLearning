import csv
import copy
import json
from typing import List, Dict, Tuple, Union


def extract_data() -> Tuple[List[Dict[str, str]], List[Dict[str, str]]]:
    map_file = "/Users/vivekreddyvari/opt/anaconda/NewLearning/FashionCloud/app/models/mappings.csv"
    price_file = "/Users/vivekreddyvari/opt/anaconda/NewLearning/FashionCloud/app/models/pricat.csv"
    price_catalog_values = []
    mapping_file_values = []
    try:
        with open(price_file, newline="") as csvfile:
            data = csv.DictReader(csvfile, delimiter=";")
            for row in data:
                price_catalog_values.append(row)
    except FileNotFoundError:
        print(f"{price_file} not found, please specify the path")

    try:
        with open(map_file, newline="") as csvfile:
            data = csv.DictReader(csvfile, delimiter=";")
            for row in data:
                mapping_file_values.append(row)
    except FileNotFoundError:
        print(f"{map_file} not found, please specify the path")

    return (price_catalog_values, mapping_file_values) if price_catalog_values and mapping_file_values \
        else (None, None)


def mapping(mapping_file_values: List[Dict[str, str]]) -> Dict[str, dict]:
    map_data = {}
    for row in mapping_file_values:
        if row['source_type'] not in map_data.keys():
            map_data[row['source_type']] = {}
        map_data[row['source_type']]['name'] = row['destination_type']
        map_data[row['source_type']][row['source']] = row['destination']

    return map_data


def group_by(price_catalog_values: List[Dict[str, str]], mapping_file_values: Dict[str, Union[str, dict]]) -> \
List[Dict[str, str]]:
    price_catalog_values = copy.deepcopy(price_catalog_values)
    merge_cols = []
    for key in mapping_file_values.keys():
        if '|' in key:
            merge_cols.append(key)

        if merge_cols:
            for row in price_catalog_values:
                for merge_col_name in merge_cols:
                    columns = merge_col_name.split('|')
                    merge_col_values = [row[col_name] for col_name in columns]
                    row[merge_col_name] = '|'.join(merge_col_values)
                    for column_name in columns:
                        del row[column_name]
        return price_catalog_values


def data_mapping(grouping_data: List[Dict[str, str]], mapping_file_values: Dict[str, dict]) -> List[
    Dict[str, str]]:
    map_data = []
    for row in grouping_data:
        mapped_row = {}
        for key, value in row.items():
            if not value:
                continue
            if key in mapping_file_values.keys():
                column_name = mapping_file_values[key]['name']
                column_value = mapping_file_values[key][value]
                mapped_row[column_name] = column_value
            else:
                mapped_row[key] = value
        map_data.append(mapped_row)
    return map_data


def catalog_structure(map_data: List[Dict[str, str]]) -> Dict[str, Union[str, dict]]:
    catalog_structure_format = {
        "brand": " ",
        "supplier": " ",
        "collection": "",
        "season": "",
        "article": {},
    }

    for row in map_data:
        catalog_structure_format['brand'] = row['brand']
        catalog_structure_format['supplier'] = row['supplier']
        catalog_structure_format['collection'] = row['collection']
        catalog_structure_format['season'] = row['season']
        if not row['article_number'] in catalog_structure_format['article'].keys():
            catalog_structure_format = _add_article_data(catalog_structure_format, row)
        # if row['ean'] in catalog_structure_format['article'][row['article_number']]['variation'].keys():
         #   continue
        else:
            catalog_structure_format = _add_variation_data(catalog_structure_format, row)

    return catalog_structure_format


def _add_article_data(catalog_structure_format: dict, row: Dict[str, str]) -> dict:
    catalog_structure_format = copy.deepcopy(catalog_structure_format)
    catalog_structure_format['article'][row['article_number']] = {}
    catalog_structure_format['article'][row['article_number']]['article_structure'] = row['article_structure']
    catalog_structure_format['article'][row['article_number']]['article_number_2'] = row['article_number_2']
    catalog_structure_format['article'][row['article_number']]['article_number_3'] = row['article_number_3']
    catalog_structure_format['article'][row['article_number']]['target_area'] = row['target_area']
    catalog_structure_format['article'][row['article_number']]['variation'] = {}

    return catalog_structure_format


def _add_variation_data(catalog_structure_format: dict, row: Dict[str, str]) -> dict:
    catalog_structure_format = copy.deepcopy(catalog_structure_format)
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']] = {}
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['color'] = row['color']
    # catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['size'] = row['size']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['size_name'] = row['size_name']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['currency'] = row['currency']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['price_buy_net'] = row[
        'price_buy_net']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['price_sell'] = row[
        'price_sell']
    catalog_structure_format['article'][row['article_number']]['variation'][row['ean']]['material'] = row['material']

    return catalog_structure_format


# Configurable Option: combine multiple fields
def combine_columns(columns_to_merge_name: List[str], merged_column_name: str, values_data: List[Dict[str, str]]) \
        -> List[Dict[str, str]]:
    values_data = copy.deepcopy(values_data)
    for row in values_data:
        merged_column_values = [f"{row[column_name]}" for column_name in columns_to_merge_name]
        row[merged_column_name] = ' '.join(merged_column_values)
        for merge_column_name in columns_to_merge_name:
            del row[merge_column_name]

    return values_data


def main():
    price_catalog_values, mapping_file_values = extract_data()
    if price_catalog_values and mapping_file_values:
        mapping_file_values = mapping(mapping_file_values)
        grouping_data = group_by(price_catalog_values, mapping_file_values)
        mapped_data = data_mapping(grouping_data, mapping_file_values)
        catalog_structure_data = catalog_structure(mapped_data)

        with open("/Users/vivekreddyvari/opt/anaconda/NewLearning/FashionCloud/app/output/structure.json", "w") \
                as json_file : json.dump(catalog_structure_data, json_file)


if __name__ == '__main__':
    main()