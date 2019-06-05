def insert_text_before_extension(file, insert_text):
    """Inserts text before the extension of a path"""
    file_name = file.stem + insert_text + file.suffix
    file_path = file.parent / file_name
    return file_path
