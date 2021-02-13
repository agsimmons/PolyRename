from polyrename.transformation import (
    current_datetime,
    date_time,
    insert,
    music_tags,
    prefix,
    regex_replace,
    remove_range,
    replace,
    replace_extension,
    sequence,
    suffix,
    transformation,
)

# List of all available transformations
TRANSFORMATIONS = transformation.Transformation.__subclasses__()

TRANSFORMATIONS_BY_NAME = {t.schema["metadata"]["name"]: t for t in TRANSFORMATIONS}
