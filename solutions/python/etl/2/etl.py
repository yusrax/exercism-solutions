"""ETL"""
def transform(legacy_data):
    """Change legacy_data from 1-many to 1-1 mapping"""
    data = {}
    for key, value in legacy_data.items():
        for item in value:
            data[item.lower()] = key

    return data
    