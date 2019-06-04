from polyrename.transformation import TRANSFORMATIONS


VALID_DATATYPES = [str, int, bool]


def test_schemas():
    """Validate that each transformation's schema complies with the schema specification"""

    for transformation in TRANSFORMATIONS:

        # Test that transformation has a schema
        schema = transformation.schema

        # Test metadata block
        assert 'metadata' in schema
        # Name
        assert 'name' in schema['metadata']
        assert isinstance(schema['metadata']['name'], str)
        assert schema['metadata']['name'] != ''
        # Description
        assert 'description' in schema['metadata']
        assert isinstance(schema['metadata']['description'], str)
        assert schema['metadata']['description'] != ''

        # Test options block
        assert 'options' in schema
        assert isinstance(schema['options'], list)
        # TODO: Make sure list isn't empty?
        for option in schema['options']:
            # Name
            assert 'name' in option
            assert isinstance(option['name'], str)
            assert option['name'] != ''
            # Description
            assert 'description' in option
            assert isinstance(option['description'], str)
            assert option['description'] != ''
            # Data Type
            assert 'datatype' in option
            assert option['datatype'] in VALID_DATATYPES
            # Required
            assert 'required' in option
            assert isinstance(option['required'], bool)


def test_unique_names():
    """Validate that names are unique among transformations"""

    names = []

    for transformation in TRANSFORMATIONS:
        names.append(transformation.schema['metadata']['name'])

    assert len(names) == len(set(names))
