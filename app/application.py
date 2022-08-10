from typing import List, Dict, Tuple, Union
from FashionCloud.app.utils.loaddata import ExtractData, Mapping, MapData, CatalogStructure
import copy, json


def extract_data() -> Tuple[List[Dict[str, str]], List[Dict[str, str]]]:
    price_file = "/Users/vivekreddyvari/opt/anaconda/NewLearning/FashionCloud/app/models/pricat.csv"
    mapping_file = "/Users/vivekreddyvari/opt/anaconda/NewLearning/FashionCloud/app/models/mappings.csv"

    price_catalog = ExtractData(price_file, None)
    map_file = ExtractData(mapping_file, None)
    price_catalog_values = price_catalog.return_from_file()
    mapping_file_values = map_file.return_from_file()

    return (price_catalog_values, mapping_file_values) \
        if price_catalog_values and mapping_file_values else (None, None)


def mapping(mapping_file_values: List[Dict[str, str]]) -> Dict[str, dict]:
    map_data_retrieved = Mapping(mapping_file_values, map_data={})
    map_data = map_data_retrieved.return_map_data()

    return map_data


def group_by(price_catalog_values: List[Dict[str, str]],
             mapping_file_values: Dict[str, Union[str, dict]]) -> List[Dict[str, str]]:
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


def map_data(grouping_data: List[Dict[str, str]], mapping_file_values: Dict[str, dict]) -> List[Dict[str, str]]:
    data_retrieved = MapData(grouping_data, mapping_file_values)
    map_data_retrieved = data_retrieved.map_data_output()
    return map_data_retrieved


def catalog_structure(map_data_ret: List[Dict[str, str]]) -> Dict[str, Union[str, dict]]:
    cat_str = CatalogStructure(map_data_ret)
    cat_str_data = cat_str.catalog_structure()
    return cat_str_data
    pass


def main():
    price_cat_values, mapping_file_values = extract_data()
    print(price_cat_values)
    print(mapping_file_values, end='\n\n')
    if price_cat_values and mapping_file_values:
        map = mapping(mapping_file_values)
        print(f" Mapping Values : {map}", end='\n\n')
        grouping = group_by(price_cat_values, map)
        print(grouping, end='\n\n')
        map_data_ret = map_data(grouping, map)
        print(f" mapped data retrieve: {map_data_ret}", end='\n\n')
        catalog_struct = catalog_structure(map_data_ret=map_data_ret)
        print(f" Catalog Structure : {catalog_struct}", end='\n\n')

        # Make JSON - file:
        with open("/Users/vivekreddyvari/opt/anaconda/NewLearning/FashionCloud/app/output/catalog_structured.json", "w") \
                as json_file: json.dump(catalog_struct, json_file)


if __name__ == "__main__":
    main()
