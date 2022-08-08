from FashionCloud.app.utils import LoadandMap


class Main:
    """
    This Procedure is Main that runs step by step of all procedure below creates a json dump
    procedures:
        1. load data
        2. mapping data
        3. group data
        4. map_data
        5. catalog_data

    outputs: output_json

    """
    # files

    # LoadData
    price_catalog_values, map_file_values = LoadandMap.extract_data()

    if price_catalog_values and map_file_values:
        mapping_val = LoadandMap.mapping(map_file_values)








Application = Main()
print(Application.price_catalog_values)

