# TODO : A UTILISER DANS UN ENVIRONNEMENT LEAPP
""" See description below """

__artifacts_v2__ = {
    "function_name": {  # This should match exactly the function name in the script
        "name": "Human-readable Artifact Name",
        "description": "Brief description of what the artifact does",
        "author": "@AuthorUsername",
        "creation_date": "2023-05-24",
        "last_update_date": "2024-12-17",
        "requirements": "none",
        "category": "Artifact Category",
        "notes": "",
        "paths": ('Path/to/artifact/files',),
        "output_types": "all",  # or "standard" or ["html", "tsv", "timeline", "kml", "lava"]
        "artifact_icon": "feather-icon-name"
    }
}


from scripts.ilapfuncs import artifact_processor, get_file_path, get_sqlite_db_records


@artifact_processor
def function_name(files_found, report_folder, seeker, wrap_text, timezone_offset):
    """ See artifact description """

    source_path = get_file_path(files_found, "database_filename.db")
    data_list = []

    query = '''
    '''

    data_headers = (('Column 1', 'datetime'), 'Column 2', 'Column 3')

    # if no conversion needed in particular columns
    data_list = get_sqlite_db_records(source_path, query)

    # If conversion needed (i.e: timestamps), use the following pattern
    db_records = get_sqlite_db_records(source_path, query)
    for record in db_records:
        data_list.append((
            record[0],
            record[1],
            record[2]
        ))

    return data_headers, data_list, source_path
