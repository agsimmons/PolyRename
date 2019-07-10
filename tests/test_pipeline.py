from pathlib import Path

from polyrename.transformation import prefix, suffix, pipeline
from tests import TEST_SEQUENCE_01


def test_pipeline():
    """Ensures that pipelines successfully string together transformations"""
    prefix_transformation = prefix.PrefixTransformation('Hello_')
    suffix_transformation = suffix.SuffixTransformation('_World')

    prefix_suffix_pipeline = pipeline.Pipeline([prefix_transformation, suffix_transformation])

    assert prefix_suffix_pipeline.resolve(TEST_SEQUENCE_01) == [Path('/home/test/Hello_example_World.py'), Path('Hello_file_without_extension_World'), Path('Hello_relative_World.jpg'), Path('relative/path/Hello_extreme_extreme04.tar_World.gz')]
