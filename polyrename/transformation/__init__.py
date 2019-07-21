from polyrename.transformation import (
    transformation,
    date_time,
    prefix,
    suffix,
    sequence,
    current_datetime,
    insert,
    remove_range,
    replace_extension,
    replace,
    regex_replace,
    music_tags,
)


# List of all available transformations
TRANSFORMATIONS = transformation.Transformation.__subclasses__()

TRANSFORMATIONS_BY_NAME = {t.schema["metadata"]["name"]: t for t in TRANSFORMATIONS}
